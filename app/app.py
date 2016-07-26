from flask import Flask, Response, request, jsonify

app = Flask(__name__)

# In-memory data store
names = [
    'Patricio López',
]


@app.route("/")
def hello():
    response = {"status": "on"}
    return jsonify(**response)


@app.route('/names', methods=['GET', 'POST'])
def resource_names():
    if request.method == 'GET':
        # Return current values
        return jsonify(names=names)

    elif request.method == 'POST':
        # Obtain JSON from request body
        content = request.get_json(silent=True)  # Do not throw exception

        if 'name' in content:
            names.append(content['name'])
            # 201 CREATED | https://httpstatuses.com/201
            return jsonify(name=content['name']), 201
        else:
            # 406 NOT ACCEPTABLE | https://httpstatuses.com/406
            return Response(status=406)

    else:
        # 501 NOT IMPLEMENTED | https://httpstatuses.com/501
        return Response(status=501)
