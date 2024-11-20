from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

# Generate a random color and timestamp when the app starts
random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

# HTML template with dynamic content
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pod Start</title>
</head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 20%;">
    <div style="display: flex; justify-content: center; align-items: center;">
        <div style="width: 20px; height: 20px; background-color: {{ color }}; margin-right: 10px;"></div>
        <p style="margin: 0;">This Pod started at {{ timestamp }}.</p>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_template, color=random_color, timestamp=start_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0")