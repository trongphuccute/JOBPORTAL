from django.shortcuts import redirect, render, get_object_or_404
from jobs.form import JobForm
from .models import Job
from django.core.paginator import Paginator
from accounts.decorators import employer_required
from django.contrib.auth.decorators import login_required
from .form import JobForm, CompanyForm
from .models import JobImage
from jobs.models import Company
from django.contrib import messages
from applications.models import Application, SavedJob
from django.db.models import Q
from .utils import get_recommended_jobs

def job_list(request):
    jobs = Job.objects.select_related('company').all().order_by('-created_at')

    # SEARCH
    query = request.GET.get('q')
    if query:
        jobs = jobs.filter(title__icontains=query)

    #  FILTER
    location = request.GET.get('location')
    if location:
        jobs = jobs.filter(location__icontains=location)

    job_type = request.GET.get('type')
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    #  PAGINATION
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs
    })
def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedJob.objects.filter(user=request.user, job=job).exists()
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'user': request.user,
        'is_saved': is_saved
    })
@login_required
@employer_required
def create_job(request):
    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        requirements = request.POST.get("requirements")
        about_company = request.POST.get("about_company")
        location = request.POST.get("location")
        job_type = request.POST.get("job_type")
        salary = request.POST.get("salary")

        # 🔥 MULTIPLE IMAGES
        images = request.FILES.getlist("images")

        # 🔥 FILTER EMPTY FILES
        valid_images = []

        for img in images:
            if img and hasattr(img, "size") and img.size > 0:
                valid_images.append(img)

        # 🔥 MAIN IMAGE
        main_image = valid_images[0] if valid_images else None

        # 🔥 COMPANY
        company = Company.objects.filter(user=request.user).first()

        if not company:
            return redirect('request_employer')

        # ✅ CREATE JOB
        job = Job.objects.create(
            title=title,
            description=description,
            requirements=requirements,
            about_company=about_company,
            location=location,
            job_type=job_type,
            salary=salary if salary else None,
            company=company,
            image=main_image
        )

        # ✅ SAVE GALLERY IMAGES
        for img in valid_images:
            try:
                JobImage.objects.create(job=job, image=img)
            except Exception as e:
                print("UPLOAD ERROR:", e)

        return redirect("jobs:job_list")

    return render(request, "jobs/create_job.html")
def edit_job(request, id):
    company = Company.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, id=id, company=company)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_detail', id=job.id)
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form})
def delete_job(request, id):
    company = Company.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, id=id, company=company)

    job.delete()
    return redirect('jobs:my_jobs')
def home(request):

    jobs = Job.objects.all().order_by('-created_at')[:6]

    recommended_jobs = []

    if request.user.is_authenticated:

        saved_types = SavedJob.objects.filter(

            user=request.user

        ).values_list(

            'job__job_type',

            flat=True

        )

        applied_types = Application.objects.filter(

            user=request.user

        ).values_list(

            'job__job_type',

            flat=True

        )

        liked_types = list(saved_types) + list(applied_types)

        if liked_types:

            recommended_jobs = Job.objects.filter(

                job_type__in=liked_types

            ).exclude(

                id__in=SavedJob.objects.filter(

                    user=request.user

                ).values_list('job_id', flat=True)

            ).distinct()[:6]

    return render(request, 'base/home.html', {

        'jobs': jobs,

        'recommended_jobs': recommended_jobs

    })
@login_required
def my_jobs(request):
    company = Company.objects.filter(user=request.user).first()

    if not company:
        return redirect('request_employer')

    jobs = Job.objects.filter(company=company).order_by('-created_at')

    return render(request, 'jobs/my_jobs.html', {
        'jobs': jobs
    })

def update_company(request):
    company = request.user.company_profile

    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'accounts/company_form.html', {'form': form})

def company_profile(request, id):

    company = get_object_or_404(Company, id=id)

    jobs = Job.objects.filter(
        company=company
    ).order_by('-created_at')

    total_jobs = jobs.count()

    return render(
        request,
        'jobs/company_profile.html',
        {
            'company': company,
            'jobs': jobs,
            'total_jobs': total_jobs,
        }
    )