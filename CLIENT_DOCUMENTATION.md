# Feedback System - Client Documentation

## 1. Project Overview

This project is a Django-based feedback system for collecting user opinions about their visit.
It includes:
- user registration and login
- emotional feedback selection (Happy, Unhappy, Sad)
- optional remarks with each feedback
- score calculation based on emotion
- a dashboard for users to review their submissions
- profile view for user details
- admin panel for managing users and feedback

## 2. How It Works

### 2.1 User Authentication

Users can create a new account using their email and password.
During signup, the system also captures optional details such as first name, last name, phone, and city.
Each user has a `UserProfile` linked to Django's built-in `User` model.

### 2.2 Feedback Submission

After login, users land on the feedback page where they answer:
- "How was your visit today?"

They choose one of three emotions:
- 😊 Happy → 100%
- 😐 Unhappy → 50%
- 😢 Sad → 0%

Users can also add optional remarks about their visit.

### 2.3 Daily Submission Rule

The system allows each user to submit only one feedback per day.
If a user tries to submit again on the same day, they are redirected to the dashboard with a warning.

### 2.4 Feedback Storage

Each feedback record stores:
- user reference
- selected emotion
- calculated score
- optional remarks
- creation timestamp

## 3. User Flow

### 3.1 Signup

1. Visit `/signup/`
2. Enter email, password, and optional details
3. Submit the form
4. The user is automatically logged in and redirected to the feedback page

### 3.2 Login

1. Visit `/login/`
2. Enter registered email and password
3. Submit to access the feedback page

### 3.3 Submit Feedback

1. Choose one emotional response
2. Enter remarks if desired
3. Click "Submit Feedback"
4. View the thank-you page with score details

### 3.4 Dashboard

The dashboard shows:
- total feedback count
- average score
- emotion breakdown
- feedback history with remarks

### 3.5 Profile

The profile page displays:
- email and username
- name and contact details
- account creation date
- total submitted feedbacks

## 4. Admin Flow

The admin panel is available at `/admin/`.
Only superusers can log in here.

From the admin panel, the administrator can:
- manage users
- view all feedback submissions
- inspect user profiles
- search and filter feedback by emotion and date

## 5. Technical Details

### 5.1 Main Components

- `feedback_project/settings.py`: Django project configuration
- `feedback_project/urls.py`: global URL routing
- `feedback_project/wsgi.py`: WSGI application for deployment

- `feedback_app/models.py`: defines `UserProfile` and `Feedback`
- `feedback_app/forms.py`: defines registration and feedback forms
- `feedback_app/views.py`: contains authentication and business logic
- `feedback_app/urls.py`: app-specific routes
- `feedback_app/admin.py`: admin registration and display settings

- `templates/`: HTML templates for pages
- `static/`: static assets for CSS and JavaScript

### 5.2 Database

The current configuration uses SQLite by default for local development.
For production, it is recommended to use PostgreSQL or another production-ready database.

### 5.3 Production Settings

The project uses environment variables defined in `.env`.
Key settings include:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG` (should be `False` in production)
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_SESSION_COOKIE_SECURE`
- `DJANGO_CSRF_COOKIE_SECURE`
- `DJANGO_SECURE_SSL_REDIRECT`

## 6. Deployment Instructions

### 6.1 Create a fresh database and migrations

If the client wants a fresh database before deployment:
1. Delete `db.sqlite3`
2. Delete `feedback_app/migrations/` if it must be reset
3. Run:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 6.2 Run the app locally

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in the browser.

### 6.3 Production deployment

Use the existing `Procfile` and production packages:
- `gunicorn`
- `whitenoise`
- `python-dotenv`

Collect static files:
```bash
python manage.py collectstatic --noinput
```

Run the app with Gunicorn:
```bash
gunicorn feedback_project.wsgi --bind 0.0.0.0:8000
```

## 7. How to Use the App (Client Summary)

This project is designed to let users provide quick feedback in the form of emotion + remarks.
The admin can monitor submissions, and users can see their own feedback history.

Key benefits for the client:
- simple and polished user interface
- one feedback per user per day enforcement
- optional comments for richer data
- dashboard analytics for quick insights

## 8. Notes for the Client

- Make sure `.env` is not pushed to GitHub.
- Use a strong secret key for production.
- Keep `DEBUG=False` when launching live.
- Do not commit `db.sqlite3` if you want a fresh database on deployment.
- Use `requirements.txt` to install the exact package versions.

---

Thank you! This document explains how the feedback project works, how users interact with it, and how it should be deployed and maintained.