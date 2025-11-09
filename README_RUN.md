Run locally (quick)

1. Install Node.js (if you don't have it): https://nodejs.org/
2. From the project root open PowerShell and run one of the following (no install required):

```powershell
# serve with http-server via npx (recommended for quick local testing)
npx http-server . -p 5000 --cors

# or use the built-in serve package if you prefer
npx serve . -l 5000
```

3. Open your browser to http://localhost:5000/ and edit `Index.html` to replace the `YOUR_API_KEY_HERE` placeholder with your Google Vision API key (or implement a server-side proxy for production).

Security note: Do NOT embed secret API keys in client-side code for production. Use a server-side proxy or serverless function to keep keys private.

This file is a short companion that shows quick startup steps for local testing.

---

Python proxy (optional, recommended)

1. Create and activate a Python virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Set your Google Vision API key in an environment variable and start the proxy:

```powershell
$env:GOOGLE_VISION_API_KEY = "<your-key>"
python server.py
```

3. Start the static server (if not already running) and open http://localhost:5000/

Notes:
- The client JavaScript prefers the local proxy at `/vision` (see `src/js/app.js`).
- The proxy removes the need to embed the API key in the browser; do NOT commit your key.

