"""Simple Flask proxy to forward Google Vision requests server-side.

Usage (PowerShell):
  $env:GOOGLE_VISION_API_KEY = "<your-key>"
  python server.py

The client app can call POST /vision with the same body it would send to
the Google Vision API and this proxy will attach the API key and forward it.
"""
from flask import Flask, request, jsonify, Response
import os
import requests

app = Flask(__name__)

GOOGLE_VISION_API_KEY = os.environ.get('GOOGLE_VISION_API_KEY')
GOOGLE_VISION_URL = 'https://vision.googleapis.com/v1/images:annotate'


@app.route('/vision', methods=['POST'])
def vision_proxy():
    """Forward the incoming JSON body to Google Vision with server-side key."""
    if not GOOGLE_VISION_API_KEY:
        return jsonify({"error": "Server missing GOOGLE_VISION_API_KEY environment variable"}), 500

    try:
        # Forward the JSON body as-is
        resp = requests.post(
            f"{GOOGLE_VISION_URL}?key={GOOGLE_VISION_API_KEY}",
            json=request.get_json(force=True),
            timeout=30
        )

        # Return the raw response content and status code
        return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type', 'application/json'))

    except requests.RequestException as exc:
        return jsonify({"error": "Failed to reach Google Vision API", "details": str(exc)}), 502


if __name__ == '__main__':
    # For local testing only. In production use a proper WSGI server and HTTPS.
    app.run(host='0.0.0.0', port=8000, debug=True)
