JobPortal: Enterprise Recruitment Management SystemJobPortal is a comprehensive, full-stack recruitment platform designed to bridge the gap between talent and opportunity. It features specialized workflows for Job Seekers, Employers, and Administrators.🔗 Live Application: View on Render🛠 Technical SpecificationsCategoryTechnologyBackendDjango 5.x (Python)DatabasePostgreSQLFrontendHTML5, CSS3, JavaScript, BootstrapAuthDjango Contrib AuthDeploymentRender (PaaS)✨ Key Features👤 Job SeekerAccount Management: Secure registration, login, and profile customization.Discovery: Advanced browsing and filtering of active job listings.Engagement: One-click application submission and a "Saved Jobs" tracking system.🏢 EmployerVerified Access: Multi-step onboarding via an Employer Request system.Corporate Identity: Management of dedicated Company Profiles.Recruitment Tools: Full CRUD capabilities for job postings and applicant management.🛡 System AdministratorGovernance: Oversight of the Employer approval workflow.Data Integrity: Global management of users, companies, and job listings via the Django Admin Suite.📂 Project StructurePlaintextjobportal/
├── accounts/      # Auth, Profiles, and EmployerRequest logic
├── jobs/          # Job listing and filtering management
├── applications/  # Application processing & "Save Job" logic
├── templates/     # Centralized UI components and layouts
├── static/        # Assets (CSS, JS, Images)
├── media/         # User-uploaded content
└── manage.py      # Django CLI
⚙️ Installation & Local Development1. Clone the RepositoryBashgit clone https://github.com/trongphuccute/JOBPORTAL.git
cd JOBPORTAL
2. Environment SetupWindows:Bashpython -m venv venv
venv\Scripts\activate
macOS/Linux:Bashpython3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Database & Admin SetupBashpython manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
5. Run ServerBashpython manage.py runserver
🌐 Deployment ConfigurationFor production environments, ensure these variables are set:VariableDescriptionSECRET_KEYUnique Django secret key.DEBUGSet to False in production.DATABASE_URLPostgreSQL connection string.DJANGO_SUPERUSER_PASSWORDAdmin password for automated deployment.🗺 Development Roadmap[ ] Persistent Storage: Migrate media assets to Cloudinary or AWS S3.[ ] Enhanced Search: Implement full-text search and advanced filtering.[ ] Notifications: Real-time application status updates.[ ] Analytics: Employer dashboard for tracking application metrics.✍️ AuthorHuỳnh Trọng Phúc Lead Developer📄 LicenseThis project is licensed under the MIT License. See the LICENSE file for details.
