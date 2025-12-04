# Barber Shop MVP

A modern barber shop website with a React frontend and Django REST API backend.

## Tech Stack

- **Frontend**: React + Vite + Tailwind CSS → Netlify
- **Backend**: Django REST Framework → Fly.io
- **Database**: Supabase PostgreSQL
- **Booking**: Fresha integration (external link/widget)

## Project Structure

```
Barber/
├── frontend/          # React application
│   ├── src/
│   │   ├── api/       # API hooks and config
│   │   ├── components/ # Reusable components
│   │   └── pages/     # Page components
│   └── ...
├── backend/           # Django REST API
│   ├── api/           # API app (models, views, serializers)
│   ├── barbershop/    # Django project settings
│   └── ...
└── README.md
```

## Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env   # Edit with your settings
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env   # Edit with your API URL
npm run dev
```

## Deployment

See individual README files in `frontend/` and `backend/` directories for detailed deployment instructions.

### Quick Deploy Checklist

1. **Supabase**: Create project → Copy connection string
2. **Fly.io**: Deploy backend with `fly deploy`
3. **Netlify**: Connect GitHub repo → Set `VITE_API_URL` env var

## Features

- Services listing with categories and pricing
- Barber profiles with specialties
- Image gallery with lightbox
- Contact page with Google Maps
- Fresha booking integration
- Responsive mobile-friendly design
- Django Admin for content management
