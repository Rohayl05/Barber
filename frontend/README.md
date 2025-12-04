# Barber Shop Frontend

React frontend for the Barber Shop website.

## Local Development

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:
```env
VITE_API_URL=http://localhost:8000/api
```

### 3. Start Development Server

```bash
npm run dev
```

Frontend available at: `http://localhost:5173`

## Build for Production

```bash
npm run build
```

Output is in the `dist/` folder.

## Deploy to Netlify

### Option 1: Netlify CLI

```bash
npm install -g netlify-cli
netlify login
netlify init
netlify deploy --prod
```

### Option 2: GitHub Integration (Recommended)

1. Push code to GitHub
2. Log in to [Netlify](https://netlify.com)
3. Click **Add new site → Import an existing project**
4. Select your GitHub repo
5. Configure:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
6. Add Environment Variable:
   - `VITE_API_URL`: `https://your-api.fly.dev/api`
7. Click **Deploy**

### Environment Variables on Netlify

Go to **Site settings → Environment variables** and add:

| Variable | Value |
|----------|-------|
| `VITE_API_URL` | `https://your-barbershop-api.fly.dev/api` |
| `VITE_FRESHA_URL` | `https://www.fresha.com/a/your-shop-id` (optional) |

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home page with hero, services preview, gallery preview |
| `/services` | Full services list with category filter |
| `/barbers` | Barber profiles |
| `/gallery` | Image gallery with lightbox |
| `/contact` | Contact info, hours, Google Maps |

## Fresha Integration

The "Book Now" buttons link to Fresha. Configure the URL in:
1. Django Admin → Shop Information → Fresha URL
2. Or via `VITE_FRESHA_URL` environment variable

### For Embedded Widget (Optional)

Add to any component:
```jsx
<div>
  <script src="https://assets.fresha.com/website/online-booking/bundle.js"></script>
  <fresha-booking-widget shop-id="YOUR-SHOP-ID"></fresha-booking-widget>
</div>
```

## Customization

### Colors

Edit `tailwind.config.js`:
```js
colors: {
  accent: {
    DEFAULT: '#c9a96e',  // Gold accent color
    dark: '#b8963f',
  }
}
```

### Fonts

Fonts are loaded from Google Fonts in `index.html`:
- **Display**: Playfair Display (headings)
- **Body**: Inter (body text)
