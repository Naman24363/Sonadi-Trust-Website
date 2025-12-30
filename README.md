# Sonadi Charitable Trust Website

A Django-based website for Sonadi Animal Care Center - a non-profit organization dedicated to animal rescue, sterilization, and care in Delhi, India.

## Features

- **Home** - Organization overview with rescue statistics
- **About** - Mission, vision, and core values
- **Donate** - Razorpay payment integration for donations
- **Adopt a Dog** - Browse and submit adoption requests
- **Volunteer** - Sign-up form for volunteers
- **Testimonials** - Community stories and experiences
- **Activities** - Organization's ongoing initiatives
- **Gallery/Photos** - Image galleries
- **Contact** - Contact form with email notifications

## Tech Stack

- **Backend**: Django 5.1
- **Database**: PostgreSQL (Supabase) / SQLite (local)
- **Payments**: Razorpay
- **Static Files**: WhiteNoise
- **Deployment**: Render (Gunicorn)

## Project Structure

```
sonadi-project/
├── sonadi-backend/          # Django application
│   ├── backend/             # Project settings
│   ├── core/                # Main app (models, views, forms)
│   └── manage.py
├── templates/               # HTML templates
├── assets/                  # Source CSS/JS files
├── staticfiles/             # Collected static files
├── media/                   # User uploads
└── requirements.txt
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sonadi-project.git
cd sonadi-project
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file in `sonadi-backend/`

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional - uses SQLite by default)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Email
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
ADMIN_EMAIL=admin@example.com

# Razorpay (for donations)
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
```

### 5. Run migrations

```bash
cd sonadi-backend
python manage.py migrate
```

### 6. Create admin user

```bash
python manage.py createsuperuser
```

### 7. Collect static files

```bash
python manage.py collectstatic
```

### 8. Run development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Admin Panel

Access the admin panel at `/admin/` to manage:

- Testimonials (approve/reject submissions)
- Contact messages
- Volunteer sign-ups
- Adoption requests
- Homepage statistics

## Deployment

The project is configured for deployment on Render:

- **Procfile** - Gunicorn configuration
- **build.sh** - Build script for dependencies and migrations
- **WhiteNoise** - Static file serving in production

Set all environment variables in your hosting platform's dashboard.

## Environment Variables

| Variable              | Description                     |
| --------------------- | ------------------------------- |
| `SECRET_KEY`          | Django secret key               |
| `DEBUG`               | Set to `False` in production    |
| `ALLOWED_HOSTS`       | Comma-separated allowed domains |
| `DATABASE_URL`        | PostgreSQL connection string    |
| `EMAIL_HOST_USER`     | SMTP email address              |
| `EMAIL_HOST_PASSWORD` | SMTP password/app password      |
| `RAZORPAY_KEY_ID`     | Razorpay API key                |
| `RAZORPAY_KEY_SECRET` | Razorpay API secret             |

## License

This project is for Sonadi Charitable Trust.

## Contact

- **Email**: sonadicharitytrust@gmail.com
- **Phone**: +91 9212797696
- **Location**: Masudabad, Near Sai Baba Mandir, Najafgarh, Delhi - 110043
