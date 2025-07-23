# Virtual Try-On Backend

This FastAPI service exposes an endpoint for receiving user selfies and product information. It then calls an external AI API to generate a personalized product video.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
uvicorn main:app --reload
```

3. Environment variables for external API keys (e.g., `HEYGEN_API_KEY`) should be defined in a `.env` file or environment.

## Endpoint

`POST /api/try-on`

Form fields:
- `product_id` – ID or slug of the product/video.
- `file` – uploaded image of the user.

Returns JSON containing a `video_url` pointing to the generated video.

The current implementation mocks the AI API call by copying a sample video. Replace the section marked `TODO` in `main.py` with real API calls to HeyGen or RunwayML.
