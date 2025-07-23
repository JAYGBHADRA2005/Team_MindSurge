# Virtual Try-On SaaS

This directory contains a minimal prototype for a virtual try-on service that can be embedded into e-commerce stores. It consists of:

- `backend/` – FastAPI service for processing selfie uploads and generating personalized videos.
- `widget/` – React component that stores can embed on product pages.
- `admin-dashboard/` – Skeleton React app for brands to manage settings and view analytics.

## Running Locally

1. **Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

2. **Widget**
   Bundle the React component using your choice of build tool (e.g., webpack or Vite). The bundled script can then be included on a store's page as shown in `widget/README.md`.

3. **Admin Dashboard**
   ```bash
   cd admin-dashboard
   npm install
   npm start
   ```

## Embedding Example

Include the compiled widget script and render the component:

```html
<div id="tryon"></div>
<script src="/static/TryOnWidget.js"></script>
<script>
  ReactDOM.render(
    React.createElement(TryOnWidget, { productId: 'shirt123', apiUrl: 'http://localhost:8000' }),
    document.getElementById('tryon')
  );
</script>
```

## Notes
- Replace the mocked AI API call in `backend/main.py` with a real call to HeyGen or RunwayML using your API key.
- Store uploaded files and generated videos on a persistent storage service like AWS S3 in production.
