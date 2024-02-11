from app import app


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/homepage", methods=["GET"])
def index():
    return "Welcome Abhishek Khajuria! You are authenticated to use the API.”  "