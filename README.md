# Simple Chat Agent

A simple Flask-based chat agent designed to be hosted on [Render](https://render.com).

## Deployment to Render

1.  Create a Render account.
2.  Click **New +** and select **Web Service**.
3.  Connect your GitHub repository.
4.  Render will automatically detect the `render.yaml` file or you can configure it manually:
    *   **Runtime**: Python
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `gunicorn app:app`
5.  Deploy!

## Local Development

1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the app: `python app.py`
3.  Open `http://127.0.0.1:5000` in your browser.
