from flask import Flask, request

app = Flask(__name__)
# 
@app.route("/")
def hello_world():
    return {
        "message": "Hello, World!",
        "status": "success",
        "code": 200,
        
}

@app.route("/save-user", methods=["POST"])
def graphql():
    name = request.json['name']
    save_user(name)
    return {
        "message": "Hello, World!",
        "status": "success",
        "code": 200,
        "name": name
    }
def save_user(data):
    # save user to database
    pass

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7600)
