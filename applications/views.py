from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Notification
from jobs.models import Job
from .models import Application, Resume, SavedJob
from accounts.decorators import employer_required
from django.contrib import messages

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # 🔥 chặn employer
    if request.user.role != 'job_seeker':
        messages.error(request, "Chỉ ứng viên mới được apply")
        return redirect('dashboard')

    # 🔥 check đã apply
    if Application.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, "Bạn đã apply job này rồi")
        return redirect('jobs:job_detail', id=job.id)

    if request.method == 'POST':
        file = request.FILES.get('file')

        if not file:
            messages.error(request, "Vui lòng upload CV")
            return redirect('applications:apply_job', job_id=job.id)

        resume = Resume.objects.create(
            user=request.user,
            title=f"CV - {request.user.username}",
            file=file
        )

        Application.objects.create(
            user=request.user,
            job=job,
            resume=resume,
            status='pending'
        )
        from accounts.models import Notification
        Notification.objects.create(
            user=job.company.user,
            message=f"{request.user.username} đã apply vào {job.title}"
        )

        messages.success(request, "Apply thành công!")
        return redirect('jobs:job_detail', id=job.id)

    return render(request, 'applications/apply.html', {'job': job})

@login_required
def save_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    saved_job, created = SavedJob.objects.get_or_create(
        user=request.user,
        job=job
    )

    if not created:
        saved_job.delete()
        messages.warning(request, "Removed from saved jobs")
    else:
        messages.success(request, "Saved job successfully")

    return redirect('jobs:job_detail', id=job.id)
@login_required
def applicants_list(request, job_id):
    job = get_object_or_404(Job, id=job_id, company=request.user)

    applications = Application.objects.filter(job=job).select_related('user', 'resume')

    return render(request, 'applications/applicants.html', {
        'job': job,
        'applications': applications
    })
@login_required
def update_application_status(request, app_id, status):

    application = get_object_or_404(Application, id=app_id)

    # update status

    if status == 'accepted':

        application.status = 'accepted'

    elif status == 'rejected':
        application.status = 'rejected'
    else:
        application.status = 'pending'
    application.save()
    return redirect('dashboard')

@login_required
def saved_jobs(request):

    saved_jobs = SavedJob.objects.filter(
        user=request.user
    ).select_related('job', 'job__company')

    return render(request, 'applications/saved_jobs.html', {
        'saved_jobs': saved_jobs
    })
@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user).select_related('job')

    return render(request, 'applications/my_applications.html', {
        'applications': applications
    })
@login_required
def update_status(request, app_id, status):

    application = get_object_or_404(
        Application,
        id=app_id
    )

    # 🔥 chỉ employer của job đó mới được sửa
    if application.job.company.user != request.user:
        messages.error(request, "Không có quyền")
        return redirect('home')

    application.status = status
    application.save()

    messages.success(
        request,
        f"Application {status}"
    )
    Notification.objects.create(
        user=application.user,  
        message=f"Ứng dụng của bạn vào {application.job.title} đã được {status}"
    )

    return redirect('employer_dashboard')
