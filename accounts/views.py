import json

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import EmployerRequest
from jobs.models import Job
from applications.models import Application, SavedJob
from django.db.models import Count
from django.utils.timezone import now
from datetime import timedelta, datetime
from .forms import RegisterForm, LoginForm, User
from jobs.models import Company
from django.utils.timezone import now
from .models import Profile

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # kiểm tra password
        if password != confirm_password:
            messages.error(request, "Mật khẩu không khớp")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username đã tồn tại")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Đăng ký thành công!")
        return redirect('login')

    return render(request, 'auth/register.html')


def user_login(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')

    return render(request, "auth/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/accounts/login/')


@login_required
def dashboard(request):

    role = request.user.role

    # =========================

    # EMPLOYER DASHBOARD

    # =========================

    if role == 'employer':

        # lấy company của employer

        company = Company.objects.filter(user=request.user).first()
        if not company:
            messages.warning(
                request,
                'Bạn chưa có công ty nào. Vui lòng tạo công ty để đăng tin tuyển dụng.'
            )
            return redirect('request_employer')

        # jobs của employer

        jobs = Job.objects.filter(company=company)

        # applications apply vào jobs đó

        applications = Application.objects.filter(

            job__in=jobs

        ).order_by('-applied_at')

        total_jobs = jobs.count()

        total_applications = applications.count()

        pending_count = applications.filter(

            status='pending'

        ).count()

        accepted_count = applications.filter(

            status='accepted'

        ).count()

        rejected_count = applications.filter(

            status='rejected'

        ).count()

        context = {

            'total_jobs': total_jobs,

            'total_applications': total_applications,

            'pending_count': pending_count,

            'accepted_count': accepted_count,

            'rejected_count': rejected_count,

            'applications': applications[:10],

        }

        return render(

            request,

            'accounts/employer_dashboard.html',

            context

        )

    # =========================

    # USER DASHBOARD

    # =========================

    else:

        applications = Application.objects.filter(

            user=request.user

        ).order_by('-applied_at')

        saved_jobs = SavedJob.objects.filter(

            user=request.user

        )

        total_apply = applications.count()

        total_saved = saved_jobs.count()

        pending = applications.filter(

            status='pending'

        ).count()

        accepted = applications.filter(

            status='accepted'

        ).count()

        rejected = applications.filter(

            status='rejected'

        ).count()

        # chart

        labels = []

        data = []

        for i in range(6, -1, -1):

            day = now().date() - timedelta(days=i)

            count = applications.filter(

                applied_at__date=day

            ).count()

            labels.append(day.strftime("%d/%m"))

            data.append(count)

        context = {

            'applications': applications[:5],

            'saved_jobs': saved_jobs[:5],

            'total_apply': total_apply,

            'total_saved': total_saved,

            'pending': pending,

            'accepted': accepted,

            'rejected': rejected,

            'chart_labels': json.dumps(labels),

            'chart_data': json.dumps(data),

        }

        return render(

            request,

            'accounts/user_dashboard.html',

            context

        )


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})


@login_required
def request_employer(request):

    # nếu đã là employer
    if request.user.role == 'employer':
        return redirect('dashboard')

    # nếu đã gửi request rồi
    if EmployerRequest.objects.filter(user=request.user).exists():

        messages.warning(
            request,
            'Bạn đã gửi yêu cầu rồi.'
        )

        return redirect('dashboard')

    # submit form
    if request.method == 'POST':

        EmployerRequest.objects.create(
            user=request.user,
            company_name=request.POST.get('company_name'),
            description=request.POST.get('description'),
        )

        messages.success(
            request,
            'Đã gửi yêu cầu cho admin.'
        )

        return redirect('dashboard')

    return render(
        request,
        'accounts/request_employer.html'
    )


def user_dashboard(request):
    user = request.user

    applications = Application.objects.filter(user=user)
    saved_jobs = SavedJob.objects.filter(user=user)

    # 🔥 STATS
    total_apply = applications.count()
    total_saved = saved_jobs.count()
    pending = applications.filter(status="pending").count()
    accepted = applications.filter(status="accepted").count()

    # 🔥 CHART DATA
    labels = []
    data = []
    info = []  # 👈 dùng cho hover nâng cao

    for i in range(6, -1, -1):
        day = now().date() - timedelta(days=i)

        apps_in_day = applications.filter(created_at__date=day)
        count = apps_in_day.count()

        labels.append(day.strftime("%d/%m"))
        data.append(count)

        # 🔥 info chi tiết
        info.append({
            "date": day.strftime("%d/%m/%Y"),
            "total": count,
            "jobs": [app.job.title for app in apps_in_day[:3]]
        })

    context = {
        "applications": applications.order_by("-created_at")[:5],
        "saved_jobs": saved_jobs[:5],

        "total_apply": total_apply,
        "total_saved": total_saved,
        "pending": pending,
        "accepted": accepted,

        "chart_labels": json.dumps(labels),
        "chart_data": json.dumps(data),
        "chart_info": json.dumps(info),  # 👈 mới
    }

    return render(request, "accounts/user_dashboard.html", context)

@login_required
def employer_dashboard(request):
    # 🔥 JOBS CỦA EMPLOYER
    jobs = Job.objects.filter(
        company__user=request.user
    )
    # 🔥 APPLICATIONS APPLY VÀO JOB CỦA EMPLOYER
    applications = Application.objects.filter(
        job__company__user=request.user
    ).select_related(
        'user',
        'job',
        'resume'
    ).order_by('-created_at')
    # 🔥 STATS
    total_jobs = jobs.count()
    total_applications = applications.count()
    pending_count = applications.filter(
        status='pending'
    ).count()
    accepted_count = applications.filter(
        status='accepted'
    ).count()
    rejected_count = applications.filter(
        status='rejected'
    ).count()
    context = {
        'jobs': jobs,
        'applications': applications,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'pending_count': pending_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
    }
    return render(
        request,
        'accounts/employer_dashboard.html',
        context
    )

@login_required

def profile(request):

    profile = request.user.profile

    if request.method == 'POST':

        request.user.username = request.POST.get('username')

        profile.full_name = request.POST.get('full_name')

        profile.phone = request.POST.get('phone')

        profile.address = request.POST.get('address')

        if request.FILES.get('avatar'):

            request.user.avatar = request.FILES.get('avatar')

        request.user.save()

        profile.save()

    return render(request, 'accounts/profile.html', {

        'profile': profile

    })