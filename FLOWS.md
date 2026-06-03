# Job Portal - Processing Flows & Workflows

## Overview

The Job Portal has three main user roles with distinct workflows:

1. **Job Seekers** - Browse and apply for jobs
2. **Employers** - Post jobs and manage applications
3. **Administrators** - Oversee the entire system

---

## 1. User Registration & Authentication Flow

### Job Seeker Registration

```
┌─────────────────────────────────────────────────────────────┐
│ User navigates to /accounts/register                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────┐
        │ User fills registration form:   │
        │ - Username                      │
        │ - Email                         │
        │ - Password                      │
        │ - Confirm Password              │
        └──────────────┬──────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────┐
        │ Validation checks:              │
        │ - Passwords match?              │
        │ - Username unique?              │
        │ - Email valid?                  │
        └──────────────┬──────────────────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
        ✗ Invalid         ✓ Valid
        Show error        Create User
        Return to form    (is_active=False)
                          │
                          ▼
        ┌─────────────────────────────────┐
        │ Generate verification token &   │
        │ email verification link         │
        └──────────────┬──────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────┐
        │ Send verification email to user │
        │ Link: /accounts/verify-email/   │
        │       ?uidb64=...&token=...     │
        └──────────────┬──────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────┐
        │ User clicks email verification  │
        │ link                            │
        └──────────────┬──────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────┐
        │ Token validation & user marked  │
        │ as verified (is_verified=True)  │
        │ User redirected to login        │
        └─────────────────────────────────┘
```

### Employer Registration Process

```
┌────────────────────────────────────┐
│ Job Seeker registers as normal     │
│ role = 'job_seeker'                │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│ After verification, user can:      │
│ Navigate to /accounts/become-      │
│ employer                           │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│ Fill Employer Request form:        │
│ - Company Name                     │
│ - Company Location                 │
│ - Website (optional)               │
│ - Company Description              │
│ - Company Logo                     │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│ Create EmployerRequest object      │
│ Status: 'pending'                  │
│ Admin notification sent            │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│ Admin reviews request via Django   │
│ Admin dashboard                    │
└────────────┬──────────────────────┘
             │
        ┌────┴────────┐
        │             │
        ▼             ▼
    ✓ Approved   ✗ Rejected
    user.role =  Status changed
    'employer'   to 'rejected'
    Company      Notification
    created      sent to user
    Notification
    sent
```

---

## 2. Job Seeker Workflow

### Browse & Search Jobs

```
┌──────────────────────────────────────┐
│ Job Seeker visits /jobs/             │
│ (Job listings homepage)              │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Display all jobs with:               │
│ - Job title                          │
│ - Company name                       │
│ - Job type (Full-time, Part-time, .. │
│ - Location                           │
│ - Salary (if available)              │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ User can apply filters:              │
│ - Job type                           │
│ - Location                           │
│ - Search keyword                     │
│ - Salary range (if implemented)      │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Database query filters jobs based    │
│ on selected criteria                 │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Display filtered results             │
└──────────────────────────────────────┘
```

### Save Job for Later

```
┌──────────────────────────────────────┐
│ User clicks "Save Job" button        │
│ on job detail page                   │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Check if already saved:              │
│ SavedJob.objects.filter(             │
│   user=request.user,                 │
│   job=job_id                         │
│ ).exists()                           │
└────────┬──────────────────────────────┘
         │
    ┌────┴────────┐
    │             │
    ▼             ▼
Already      Not saved yet
saved        │
│            ▼
│        Create SavedJob record
│        (user, job)
│            │
│            ▼
│        Redirect to /my-saved-jobs/
│        Display success message
▼
Redirect to /my-saved-jobs/
Display already saved message
```

### Apply for a Job

```
┌──────────────────────────────────────┐
│ User clicks "Apply Now" on job       │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Check if user is logged in           │
└────────┬─────────────────────────────┘
         │
    ┌────┴─────────┐
    │              │
    ▼              ▼
Not logged   Logged in
in           │
│            ▼
│    ┌──────────────────────┐
│    │ Load user's resumes  │
│    │ Resume.objects.filter│
│    │ (user=request.user)  │
│    └──────────┬───────────┘
│              │
│              ▼
│    ┌──────────────────────┐
│    │ Verify not already   │
│    │ applied:             │
│    │ Application.objects..│
│    │ filter(user, job)    │
│    │ .exists()            │
│    └──────────┬───────────┘
│              │
│         ┌────┴────────┐
│         │             │
│         ▼             ▼
│    ✓ Can apply  ✗ Already applied
│    │             Error message
│    ▼
│    Display resume selection
│    form with user's resumes
│    │
│    ▼
│    User selects resume
│    │
│    ▼
│    Create Application record:
│    - user
│    - job
│    - resume
│    - status='pending'
│    │
│    ▼
│    Redirect to /applications/
│    Success message shown
│    │
│    ▼
│    Employer receives notification
│    Application appears in
│    employer's dashboard
│
▼
Redirect to login page
```

### Manage Resumes

```
┌──────────────────────────────────────┐
│ User navigates to /applications/     │
│ resumes/                             │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Display user's uploaded resumes      │
│ - Resume title                       │
│ - Upload date                        │
│ - Download link                      │
│ - Delete button                      │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ User can upload new resume:          │
│ - Fill resume title                  │
│ - Select file (PDF/DOC)              │
│ - Click upload                       │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ File validation & storage            │
│ Save to media/resumes/               │
│ Create Resume model instance         │
└──────────────────────────────────────┘
```

---

## 3. Employer Workflow

### Post a New Job

```
┌──────────────────────────────────────┐
│ Employer navigates to /jobs/         │
│ post-job/                            │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Check employer status:               │
│ - user.role == 'employer'?           │
│ - Company profile exists?            │
└────────┬─────────────────────────────┘
         │
    ┌────┴─────────┐
    │              │
    ▼              ▼
Not verified   Verified
employer       employer
│              │
Redirect to    ▼
employer    Display job form:
request     - Title
form        - Description
            - Job type
            - Location
            - Salary
            - Requirements
            - About company
            - Job image
            │
            ▼
        Form validation
        & submission
            │
            ▼
        Create Job record:
        - company=user.company_profile
        - status='active' (default)
        │
        ▼
        Job listed on platform
        Emails sent to matching
        job seekers (if implemented)
        │
        ▼
        Redirect to /my-jobs/
```

### Manage Job Postings

```
┌──────────────────────────────────────┐
│ Employer visits /my-jobs/            │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Display all company's active jobs    │
│ - Job title                          │
│ - Applications count                 │
│ - Posted date                        │
│ - Edit button                        │
│ - Delete button                      │
│ - View applicants button             │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Employer can:                        │
│ - Click "Edit" to modify job         │
│ - Click "View Applicants" to see     │
│   list of applications               │
│ - Click "Delete" to remove job       │
└──────────────────────────────────────┘
```

### Review & Manage Applications

```
┌──────────────────────────────────────┐
│ Employer clicks "View Applicants"    │
│ on a job posting                     │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Fetch all applications for job:      │
│ Application.objects.filter(          │
│   job=job_id                         │
│ )                                    │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Display applicant list with:         │
│ - Applicant name                     │
│ - Application date                   │
│ - Current status (pending, ...)      │
│ - Resume download button             │
│ - Status change dropdown             │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Employer selects new status:         │
│ - pending                            │
│ - accepted                           │
│ - rejected                           │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Update Application.status            │
│ Save to database                     │
│ Create notification for applicant    │
│ Email sent to applicant              │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Redirect to applicants list          │
│ Updated status displayed             │
└──────────────────────────────────────┘
```

---

## 4. Administrator Workflow

### Approve Employer Requests

```
┌──────────────────────────────────────┐
│ Admin accesses Django Admin:         │
│ /admin/                              │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Navigate to Employer Requests        │
│ (accounts > EmployerRequest)         │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Display all pending requests:        │
│ - Company name                       │
│ - User email                         │
│ - Status (pending/approved/rejected) │
│ - Request details                    │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Admin selects request to review      │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ View full request details            │
└────────┬─────────────────────────────┘
         │
    ┌────┴──────────┐
    │               │
    ▼               ▼
Approve         Reject
│               │
▼               ▼
Set status  Set status
to          to
'approved'  'rejected'
│           │
▼           ▼
user.role   Notification
= 'employer' sent
Company     user to
created     reapply
Notification
sent
```

### Monitor System

```
┌──────────────────────────────────────┐
│ Admin can manage via Django Admin:   │
│ - Users                              │
│ - Companies                          │
│ - Jobs                               │
│ - Applications                       │
│ - Resumes                            │
│ - Blog posts                         │
│ - Notifications                      │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ Actions available:                   │
│ - View all records                   │
│ - Filter by status/date/user         │
│ - Edit/Delete records                │
│ - Bulk actions                       │
│ - Search functionality               │
└──────────────────────────────────────┘
```

---

## 5. Notification Flow

```
┌──────────────────────────────────────────────┐
│ Event triggers notification creation:        │
│ - User registers (verification email)        │
│ - Employer request status changes            │
│ - Job application status changes             │
│ - New job posted (matching skills)           │
│ - Job seeker saves a job                     │
└──────────┬───────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────┐
│ Create Notification record:                  │
│ - user (FK to User)                          │
│ - message (notification text)                │
│ - is_read (default: False)                   │
│ - created_at (timestamp)                     │
└──────────┬───────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────┐
│ Email notification sent (if configured):     │
│ - Subject: [Portal] Notification             │
│ - Body: notification message                 │
│ - Link to action if applicable               │
└──────────┬───────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────┐
│ User receives notification:                  │
│ - In-app notification displayed              │
│ - Email received                             │
│ - User can mark as read                      │
└──────────────────────────────────────────────┘
```

---

## 6. Email Notification Templates

### Verification Email (Registration)

```
Subject: [JobPortal] Email Verification Required
Body:
Hello [USERNAME],

Thank you for registering at JobPortal!

Please verify your email address by clicking the link below:
[VERIFICATION_LINK]

This link expires in 24 hours.

Best regards,
JobPortal Team
```

### Application Status Change Email

```
Subject: [JobPortal] Application Status Update
Body:
Hello [APPLICANT_NAME],

Your application for the position of [JOB_TITLE] at [COMPANY_NAME]
has been updated to: [STATUS]

View your application: [APPLICATION_LINK]

Best regards,
JobPortal Team
```

### Employer Request Status Email

```
Subject: [JobPortal] Employer Request Status
Body:
Hello [USER_NAME],

Your employer request has been [APPROVED/REJECTED].

[If approved:]
You can now post jobs and manage applications.
Visit your dashboard: [DASHBOARD_LINK]

[If rejected:]
Please review our requirements and resubmit.
Contact support for assistance.

Best regards,
JobPortal Team
```

---

## 7. Key Database Relationships

```
User (1) ←──────→ (1) Profile
  ↓
  ├─→ (1) Company (Employer only)
  │     ↓
  │     ├─→ (M) Job
  │     │     ↓
  │     │     ├─→ (M) JobImage
  │     │     ├─→ (M) Application
  │     │     └─→ (M) SavedJob
  │     │
  │     └─→ (1) Logo
  │
  ├─→ (1) EmployerRequest
  ├─→ (1) Avatar
  ├─→ (M) Notification
  ├─→ (M) Resume
  │     ↓
  │     └─→ (M) Application
  └─→ (M) SavedJob
```

---

## 8. Data Flow Diagram (High Level)

```
┌─────────────────┐       ┌─────────────────┐
│   Job Seeker    │       │   Employer      │
└────────┬────────┘       └────────┬────────┘
         │                         │
         │ Register/Login          │ Register/Login
         │                         │ Submit Employer
         │                         │ Request
         │                         │
         ▼                         ▼
    ┌─────────────────────────────────────┐
    │         Authentication Flow         │
    │  (Django Auth + Email Verification) │
    └────────────┬────────────────────────┘
                 │
         ┌───────┴────────┐
         │                │
         ▼                ▼
    Job Seeker      Employer (After
    Dashboard       Admin Approval)
    │               │
    ├─Browse Jobs   ├─Post Jobs
    ├─Search/Filter ├─Manage Jobs
    ├─Save Jobs     ├─View Applications
    ├─Apply         ├─Change App Status
    ├─Manage Resume └─Send Notifications
    └─View Notifications
         │                │
         └────────┬───────┘
                  │
         ┌────────▼────────┐
         │  Django Admin   │
         │  (SuperUser)    │
         ├─Manage Users    │
         ├─Approve Requests│
         ├─Monitor System  │
         └─Manage Content  │
```

---

## 9. Error Handling & Edge Cases

### Application Submission Error Scenarios

| Scenario              | Handler                   | Result                       |
| --------------------- | ------------------------- | ---------------------------- |
| User not logged in    | `@login_required`         | Redirect to login            |
| No resumes uploaded   | Check Resume.objects      | Show error message           |
| Already applied       | Check Application.objects | Show already applied message |
| Job posting closed    | Check job.is_active       | Show job unavailable message |
| Resume file corrupted | File validation           | Show upload error            |

### Employer Request Error Scenarios

| Scenario              | Handler               | Result                        |
| --------------------- | --------------------- | ----------------------------- |
| User already employer | Check user.role       | Show already employer message |
| Missing company info  | Form validation       | Show validation errors        |
| Invalid website URL   | URLField validation   | Show URL format error         |
| Duplicate request     | Check EmployerRequest | Show pending request message  |

---

## 10. Performance Considerations

### Optimization Strategies

- **Database Indexing**: Foreign keys, status fields, user fields
- **Query Optimization**: Use `select_related()` and `prefetch_related()`
- **Caching**: Cache job listings, company profiles
- **Pagination**: List views implement pagination (20 items per page)
- **Static Files**: Served via CDN (Cloudinary)

### Query Examples

```python
# Good: Avoids N+1 queries
jobs = Job.objects.select_related('company').all()

# Good: Fetch related applications with count
applications = Application.objects.filter(job=job).select_related('user', 'resume')

# Good: Paginate large result sets
from django.core.paginator import Paginator
paginator = Paginator(jobs, 20)
page_jobs = paginator.get_page(page_number)
```

---

## Conclusion

This document provides a comprehensive overview of the Job Portal's workflows and processes. For implementation details, refer to the corresponding views.py, models.py, and forms.py files in each Django app.
