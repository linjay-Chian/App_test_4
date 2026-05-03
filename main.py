import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Cloud Run Success</title></head>
<body style="text-align: center; margin-top: 50px; font-family: sans-serif;">
    <h1 style="color: #4285F4;">Your App is Live!</h1>
    <p>The root path (/) is routing correctly.</p>
</body>
</html>
"""

@app.route('/')
def home():
    """Serves the main HTML page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/<path:invalid_path>')
def catch_all(invalid_path):
    """This catches any 404 error and prints exactly what the browser asked for."""
    return f"""
    <h1 style="color: red;">Debugging 404</h1>
    <p>Flask is running perfectly on Cloud Run!</p>
    <p>However, your browser requested the path: <strong>/{invalid_path}</strong></p>
    <p>To fix this, go back to the base URL without anything at the end.</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)