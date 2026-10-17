

from flask import Flask, render_template_string  # type: ignore[import-not-found]

app = Flask(__name__)

@app.route("/")

def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        
        <head>
            <title>My Flask App</title>
        </head>
        <body>
            <h1>Welcome to Flask!</h1>
            <p>Your Python web application is running.</p>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
