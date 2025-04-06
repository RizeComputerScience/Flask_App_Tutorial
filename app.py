from flask import Flask, render_template
from routes.movie_routes import movie_bp

app = Flask(__name__, template_folder="templates")

# Register blueprint
app.register_blueprint(movie_bp)

# Home route remains in app.py
@app.route("/")
def home():
    return "Welcome to the home page!"

if __name__ == "__main__":
    app.run(debug=True)