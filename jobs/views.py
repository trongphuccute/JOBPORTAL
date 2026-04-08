from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator


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