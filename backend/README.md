# Barber Shop Backend

Django REST API for the Barber Shop website.

## Local Development

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your settings:
- `DJANGO_SECRET_KEY`: Generate a secure key
- `DATABASE_URL`: Your Supabase PostgreSQL URL (or leave empty for SQLite)
- `CORS_ALLOWED_ORIGINS`: Your frontend URLs

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

### 6. Start Development Server

```bash
python manage.py runserver
```

API available at: `http://localhost:8000/api/`
Admin panel at: `http://localhost:8000/admin/`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/services/` | GET | List all services |
| `/api/services/?category=Haircuts` | GET | Filter by category |
| `/api/barbers/` | GET | List all barbers |
| `/api/gallery/` | GET | List gallery images |
| `/api/gallery/?category=fades` | GET | Filter by category |
| `/api/shop-info/` | GET | Get shop information |
| `/api/health/` | GET | Health check |

## Deploy to Fly.io

### 1. Install Fly CLI

```bash
# Windows (PowerShell)
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

### 2. Login to Fly

```bash
fly auth login
```

### 3. Create App

```bash
fly launch --no-deploy
```

### 4. Set Secrets

```bash
fly secrets set DJANGO_SECRET_KEY="your-secret-key"
fly secrets set DATABASE_URL="postgres://user:pass@host:5432/db"
fly secrets set ALLOWED_HOSTS="your-app.fly.dev"
fly secrets set CORS_ALLOWED_ORIGINS="https://your-site.netlify.app"
```

### 5. Deploy

```bash
fly deploy
```

### 6. Run Migrations (if needed)

```bash
fly ssh console -C "python manage.py migrate"
```

### 7. Create Admin User on Fly

```bash
fly ssh console -C "python manage.py createsuperuser"
```

## Supabase Setup

1. Create a new project at [supabase.com](https://supabase.com)
2. Go to **Settings → Database**
3. Copy the **Connection string (URI)**
4. Replace `[YOUR-PASSWORD]` with your database password
5. Use this as your `DATABASE_URL`

### Example Connection String

```
postgres://postgres:yourpassword@db.abcdefgh.supabase.co:5432/postgres
```

## Image Storage (Supabase Storage)

1. In Supabase, go to **Storage**
2. Create a new bucket called `barbershop`
3. Set bucket to **Public**
4. Upload images via the Supabase dashboard
5. Copy the public URL and paste into Django Admin

### Getting Image URLs

After uploading, the URL format is:
```
https://yourproject.supabase.co/storage/v1/object/public/barbershop/image-name.jpg
```
