from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET', 'PUT'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
    elif request.method == 'PUT':
        if username in USERS:
            USERS.update({username: {'name': request.form['name']}})
            return jsonify(USERS.get(username)), 201
        else:
            return Response(status=404)

@app.route("/users", methods=['POST'])
def users():
    if request.method == 'POST':
        if request.form['username'] not in USERS:
            USERS.update({request.form['username']: {'name': request.form['name']}})
            return Response(status=201)
        else:
            return Response(status=404)

if __name__ == "__main__":
    app.run()
