from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

# Routes
# GET /actors and /movies
# DELETE /actors/ and /movies/
# POST /actors and /movies and
# PATCH /actors/ and /movies/


if __name__ == '__main__':
    app.run(debug=True)
