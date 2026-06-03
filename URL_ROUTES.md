# Job Portal - URL Routes Reference

## Quick Navigation Guide

### Authentication Routes (Accounts App)

| URL                                        | Purpose                 | Method    | Auth Required | User Type  |
| ------------------------------------------ | ----------------------- | --------- | ------------- | ---------- |
| `/accounts/register/`                      | Register new account    | GET, POST | No            | All        |
| `/accounts/login/`                         | Login to account        | GET, POST | No            | All        |
| `/accounts/logout/`                        | Logout current user     | GET       | Yes           | All        |
| `/accounts/verify-email/<uidb64>/<token>/` | Verify email address    | GET       | No            | All        |
| `/accounts/profile/`                       | View user profile       | GET       | Yes           | All        |
| `/accounts/profile/edit/`                  | Edit user profile       | GET, POST | Yes           | All        |
| `/accounts/become-employer/`               | Request employer status | GET, POST | Yes           | Job Seeker |
| `/accounts/dashboard/`                     | View user dashboard     | GET       | Yes           | All        |

---

### Jobs Routes (Jobs App)

| URL                      | Purpose                      | Method    | Auth Required | User Type |
| ------------------------ | ---------------------------- | --------- | ------------- | --------- |
| `/` or `/jobs/`          | Browse all jobs (Homepage)   | GET       | No            | All       |
| `/jobs/job/<job_id>/`    | View job details             | GET       | No            | All       |
| `/jobs/post-job/`        | Create new job posting       | GET, POST | Yes           | Employer  |
| `/jobs/edit/<job_id>/`   | Edit job posting             | GET, POST | Yes           | Employer  |
| `/jobs/delete/<job_id>/` | Delete job posting           | POST      | Yes           | Employer  |
| `/my-jobs/`              | Manage my job postings       | GET       | Yes           | Employer  |
| `/jobs/search/`          | Search jobs (if implemented) | GET       | No            | All       |

---

### Applications Routes (Applications App)

| URL                                          | Purpose                   | Method    | Auth Required | User Type  |
| -------------------------------------------- | ------------------------- | --------- | ------------- | ---------- |
| `/applications/`                             | View my applications      | GET       | Yes           | Job Seeker |
| `/applications/apply/<job_id>/`              | Submit job application    | GET, POST | Yes           | Job Seeker |
| `/applications/resumes/`                     | Manage resumes            | GET       | Yes           | Job Seeker |
| `/applications/upload-resume/`               | Upload new resume         | GET, POST | Yes           | Job Seeker |
| `/applications/delete-resume/<resume_id>/`   | Delete resume             | POST      | Yes           | Job Seeker |
| `/applications/view-applicants/<job_id>/`    | View applicants for job   | GET       | Yes           | Employer   |
| `/applications/update-application/<app_id>/` | Update application status | POST      | Yes           | Employer   |
| `/applications/saved-jobs/`                  | View saved jobs           | GET       | Yes           | Job Seeker |
| `/applications/save-job/<job_id>/`           | Save/bookmark a job       | POST      | Yes           | Job Seeker |

---

### Blog Routes (Blog App)

| URL                         | Purpose               | Method    | Auth Required | User Type   |
| --------------------------- | --------------------- | --------- | ------------- | ----------- |
| `/blog/`                    | View all blog posts   | GET       | No            | All         |
| `/blog/post/<slug>/`        | View blog post detail | GET       | No            | All         |
| `/blog/post-create/`        | Create new blog post  | GET, POST | Yes           | Admin/Staff |
| `/blog/post-edit/<slug>/`   | Edit blog post        | GET, POST | Yes           | Admin/Staff |
| `/blog/post-delete/<slug>/` | Delete blog post      | POST      | Yes           | Admin/Staff |
| `/blog/comment/<post_id>/`  | Add comment to post   | POST      | Yes           | All         |

---

### AI Assistant Routes (AI Assistant App)

| URL                    | Purpose                 | Method | Auth Required | User Type  |
| ---------------------- | ----------------------- | ------ | ------------- | ---------- |
| `/ai/`                 | AI Assistant interface  | GET    | Yes           | Job Seeker |
| `/ai/chat/`            | Send message to AI      | POST   | Yes           | Job Seeker |
| `/ai/recommendations/` | Get job recommendations | GET    | Yes           | Job Seeker |

---

### Admin Routes

| URL                                | Purpose                   | Access         |
| ---------------------------------- | ------------------------- | -------------- |
| `/admin/`                          | Django Admin Dashboard    | SuperUser only |
| `/admin/accounts/user/`            | Manage users              | SuperUser      |
| `/admin/accounts/profile/`         | Manage profiles           | SuperUser      |
| `/admin/accounts/employerrequest/` | Approve employer requests | SuperUser      |
| `/admin/accounts/notification/`    | View notifications        | SuperUser      |
| `/admin/jobs/job/`                 | Manage all jobs           | SuperUser      |
| `/admin/jobs/company/`             | Manage companies          | SuperUser      |
| `/admin/applications/application/` | View all applications     | SuperUser      |
| `/admin/applications/resume/`      | View all resumes          | SuperUser      |
| `/admin/blog/blogpost/`            | Manage blog posts         | SuperUser      |

---

## Common URL Patterns

### Query Parameters

```
# Search jobs
/jobs/?search=python&job_type=remote

# Filter by type
/jobs/?job_type=fulltime

# Pagination
/applications/?page=2

# Sort
/jobs/?sort=recent&order=desc
```

---

## User Flow by URL Navigation

### Job Seeker Journey

```
1. / (Home)
   ↓
2. /accounts/register/ (Sign up)
   ↓
3. /accounts/verify-email/ (Verify email)
   ↓
4. /accounts/login/ (Login)
   ↓
5. /jobs/ (Browse jobs)
   ↓
6. /jobs/job/<id>/ (View job details)
   ↓
7. /applications/upload-resume/ (Upload resume if needed)
   ↓
8. /applications/apply/<job_id>/ (Apply for job)
   ↓
9. /applications/ (View my applications)
   ↓
10. /applications/saved-jobs/ (View saved jobs)
```

### Employer Journey

```
1. / (Home)
   ↓
2. /accounts/register/ (Sign up as job seeker)
   ↓
3. /accounts/become-employer/ (Request employer status)
   ↓ (Wait for admin approval)
   ↓
4. /accounts/login/ (Login - now as employer)
   ↓
5. /jobs/post-job/ (Post new job)
   ↓
6. /my-jobs/ (Manage job postings)
   ↓
7. /applications/view-applicants/<job_id>/ (Review applications)
   ↓
8. /applications/update-application/<app_id>/ (Update status)
```

### Admin Journey

```
1. /admin/ (Access admin panel)
   ↓
2. /admin/accounts/employerrequest/ (Review employer requests)
   ↓
3. /admin/accounts/user/ (Manage users)
   ↓
4. /admin/jobs/job/ (Monitor all jobs)
   ↓
5. /admin/applications/application/ (Review applications)
```

---

## API Response Codes (HTTP Status)

| Code | Meaning            | Scenario                                    |
| ---- | ------------------ | ------------------------------------------- |
| 200  | OK                 | Successful GET/POST request                 |
| 201  | Created            | Resource successfully created               |
| 302  | Found (Redirect)   | Redirect to another page (login, dashboard) |
| 400  | Bad Request        | Form validation error                       |
| 401  | Unauthorized       | User not logged in                          |
| 403  | Forbidden          | User doesn't have permission                |
| 404  | Not Found          | Resource doesn't exist                      |
| 405  | Method Not Allowed | Wrong HTTP method                           |
| 500  | Server Error       | Unexpected error                            |

---

## URL Building Examples

### In Templates (Django Template Language)

```django
<!-- Navigate to home -->
<a href="{% url 'home' %}">Home</a>

<!-- View job details -->
<a href="{% url 'job_detail' job.id %}">{{ job.title }}</a>

<!-- Edit job -->
<a href="{% url 'job_edit' job.id %}">Edit</a>

<!-- Apply for job -->
<form action="{% url 'apply_job' job.id %}" method="POST">
    {% csrf_token %}
    <button type="submit">Apply Now</button>
</form>

<!-- View applications -->
<a href="{% url 'my_applications' %}">My Applications</a>

<!-- Access admin -->
<a href="{% url 'admin:index' %}">Admin Panel</a>
```

### In Python Views

```python
from django.urls import reverse

# Generate URL
profile_url = reverse('user_profile', kwargs={'user_id': request.user.id})

# Redirect to URL
from django.shortcuts import redirect
return redirect(reverse('my_applications'))

# Full URL (for emails)
absolute_url = request.build_absolute_uri(reverse('job_detail', args=[job.id]))
```

---

## Error Pages

| Status | Page              | Route                 |
| ------ | ----------------- | --------------------- |
| 404    | Not Found         | `/templates/404.html` |
| 403    | Permission Denied | `/templates/403.html` |
| 500    | Server Error      | `/templates/500.html` |

---

## Cache & Static Files

- **Static Files**: `/static/` (CSS, JavaScript, images)
- **User Uploads**: `/media/`
  - `/media/avatars/` - User profile pictures
  - `/media/job_images/` - Job listing images
  - `/media/resumes/` - User resumes
  - `/media/company/` - Company logos
- **Cloudinary CDN**: Image optimization and storage

---

## Testing URLs (Local Development)

Start development server:

```bash
python manage.py runserver
```

Access application:

- **Main Site**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **Django Shell**: `python manage.py shell`

Test URLs in browser:

```
http://localhost:8000/jobs/
http://localhost:8000/accounts/register/
http://localhost:8000/admin/
http://localhost:8000/applications/
```

---

## URL Name Reference (for code)

### Accounts App

- `'home'` - Homepage
- `'register'` - Registration
- `'login'` - Login page
- `'logout'` - Logout
- `'verify_email'` - Email verification
- `'user_profile'` - User profile page
- `'edit_profile'` - Edit profile
- `'become_employer'` - Employer request form
- `'dashboard'` - User dashboard

### Jobs App

- `'job_list'` - All jobs
- `'job_detail'` - Job detail page
- `'post_job'` - Create job
- `'edit_job'` - Edit job
- `'delete_job'` - Delete job
- `'my_jobs'` - Employer's job list

### Applications App

- `'my_applications'` - My applications list
- `'apply_job'` - Apply for job
- `'resumes'` - Resume management
- `'upload_resume'` - Upload resume
- `'view_applicants'` - View job applicants
- `'update_application'` - Update app status
- `'saved_jobs'` - Saved jobs list
- `'save_job'` - Save a job

### Admin

- `'admin:index'` - Admin dashboard
- `'admin:accounts_user_changelist'` - User list
- `'admin:accounts_employerrequest_changelist'` - Employer requests

---

## Advanced: URL Patterns Structure

```
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),
    path('my-jobs/', my_jobs, name='my_jobs'),

    # Apps
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
    path('blog/', include('blog.urls')),
    path('ai/', include('ai_assistant.urls')),
]

# Media files (development only)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Useful Django URL Commands

```bash
# Show all URL patterns
python manage.py show_urls

# Test URL resolution
python manage.py shell
>>> from django.urls import reverse
>>> reverse('job_detail', args=[1])
'/jobs/job/1/'

# Check reverse resolution
>>> from django.urls import resolve
>>> resolve('/jobs/job/1/')
ResolverMatch(func=views.job_detail, ...)
```
