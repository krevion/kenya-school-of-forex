# Kenya School of Forex

Django website for Kenya School of Forex.

## Deploy to Render

1. Push this project to a GitHub, GitLab, or Bitbucket repository.
2. In Render, choose **New > Blueprint**, connect the repository, and apply the `render.yaml` Blueprint.
3. Render installs the dependencies, collects static files, runs database migrations, and starts the Django application. The Blueprint generates a production `SECRET_KEY` and configures the `.onrender.com` host and HTTPS settings.
4. Once the service is live, open its `.onrender.com` URL. Render checks `/health/` to verify the service is running.

The Blueprint uses Render's free web-service plan and does not create a separately billed database. The site does not currently store visitor submissions; by default Django uses SQLite for its framework tables. If you add persistent data such as registrations, create a Render PostgreSQL database and set `DATABASE_URL` on the web service to its **internal** connection string. The next deploy runs migrations automatically. SQLite files on a free web service are not persistent across deploys or restarts.

If you connect a custom domain, add it to the `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` environment variables in Render.

## Local development

Python 3.12 is recommended. Create and activate a virtual environment, then install dependencies:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:DEBUG = "true"
python manage.py runserver
```

The local development secret is intentionally unsuitable for production. Set a private `SECRET_KEY` in your environment if you need to run locally with `DEBUG` disabled.

Run the tests and Django checks with:

```powershell
python manage.py test
python manage.py check
```
