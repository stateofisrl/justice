# VS Code Workspace Configuration

## Project: Cyber Intelligence Website

A comprehensive Django application for assisting fraud victims with recovery services and awareness education.

## Getting Started

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database:**
   ```bash
   python manage.py migrate
   ```

3. **Seed Sample Content:**
   ```bash
   python manage.py seed_blog
   ```

4. **Create Admin User:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

## Project Structure


## Features


 # Copilot Instructions for Cyber Intelligence Django Project

 ## Architecture Overview

 - **Monolithic Django app** with three main domains:
    - `apps/core`: Homepage and main site logic
    - `apps/blog`: Blog system (categories, rich text, comment moderation)
    - `apps/support`: Support ticketing (priority, status, threaded replies)
 - **config/**: Central Django settings, URLs, and WSGI entrypoint
 - **templates/**: Organized by app, all use TailwindCSS and a shared `base.html`
 - **static/**: CSS/JS assets; Tailwind is loaded via CDN in templates
 - **Database**: SQLite by default (`db.sqlite3`), easily swappable

 ## Key Workflows

 ### Setup & Development
 1. Install dependencies:
      `pip install -r requirements.txt`
 2. Migrate DB:
      `python manage.py migrate`
 3. Seed blog & admin user:
      `python manage.py seed_blog`
      - Creates sample posts and admin user (`admin`/`admin123`)
 4. Create superuser (optional):
      `python manage.py createsuperuser`
 5. Run server:
      `python manage.py runserver`

 ### Testing & Content
 - No explicit test suite; validate by running server and using UI
 - Blog posts/comments/tickets can be managed via admin (`/admin/`)
 - Email notifications use console backend for dev; see `send_notification_email()` in `apps/support/views.py`

 ## Conventions & Patterns

 - **Models**: Use explicit choices for status/priority (see `SupportTicket`), and slug fields for SEO
 - **Blog**: Rich text via `django-summernote`, tags as comma-separated string
 - **Support**: Replies distinguish staff/user via `is_staff_reply`; status updates via POST
 - **Templates**: Extend `base.html`, use Tailwind utility classes, navy/cyan/gray color scheme
 - **Forms**: Use Django ModelForms with custom widgets for styling
 - **Management Commands**: Seeders in `apps/blog/management/commands/`

 ## Integration Points

 - **Email**: Console backend for dev; switch to SMTP in `config/settings.py` for production
 - **Static/Media**: Static files in `static/`, media uploads (blog images) in `/media/`
 - **Admin**: `/admin/` (default user: `admin`/`admin123` after seeding)

 ## URLs

 - Homepage: `/`
 - Blog: `/blog/` (list), `/blog/<slug>/` (detail)
 - Support: `/support/ticket/new/`, `/support/ticket/<id>/`
 - Admin: `/admin/`

 ## Security & Production Notes

 - Change all default credentials and `SECRET_KEY` before deploying
 - Set `DEBUG = False` and configure `ALLOWED_HOSTS`
 - Use HTTPS and environment variables for secrets

 ## Examples & References

 - See `apps/blog/models.py` and `apps/support/models.py` for model patterns
 - See `apps/blog/views.py` and `apps/support/views.py` for class-based view usage
 - See `apps/blog/management/commands/seed_blog.py` for seeding logic and admin creation
 - See `templates/base.html` for layout and Tailwind usage

 ---
 For questions, contact support@cyberintelligence.com

After seeding the database:
- Admin URL: http://localhost:8000/admin/
- Default User: admin
- Default Password: admin123
- ⚠️ **Change these credentials!**

## URLs

- Homepage: http://localhost:8000/
- Blog: http://localhost:8000/blog/
- New Support Ticket: http://localhost:8000/support/ticket/new/
- Admin: http://localhost:8000/admin/

## Configuration Notes

- Database: SQLite (db.sqlite3)
- Email: Console backend (development)
- Debug: True (change for production)
- Static files: Configured for development
