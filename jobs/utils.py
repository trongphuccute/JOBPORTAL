from django.db.models import Q
from .models import Job, Company, JobImage
from .form import JobForm, CompanyForm
from applications.models import Application, SavedJob

def get_recommended_jobs(user):

    saved_jobs = SavedJob.objects.filter(

        user=user

    ).select_related('job')

    applied_jobs = Application.objects.filter(

        user=user

    ).select_related('job')

    keywords = []

    # Lấy keywords từ saved jobs

    for item in saved_jobs:

        keywords += item.job.title.lower().split()

    # Lấy keywords từ applied jobs

    for item in applied_jobs:

        keywords += item.job.title.lower().split()

    keywords = list(set(keywords))

    recommended = Job.objects.none()

    for word in keywords:

        recommended |= Job.objects.filter(

            Q(title__icontains=word) |

            Q(description__icontains=word)

        )

    recommended = recommended.distinct()

    return recommended[:6]