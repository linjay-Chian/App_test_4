import os
from flask import Flask, render_template_string

app = Flask(__name__)

# This is your HTML directly inside Python!
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Success!</title></head>
<body>
    <h1>My Cloud Run App is Live!</h1>
</body>
</html>
"""

@app.route('/')
def home():
    """Serves the main HTML page."""
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)