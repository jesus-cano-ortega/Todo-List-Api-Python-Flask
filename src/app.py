from flask import Flask
from flask import jsonify
from flask import request
from flask import json

app = Flask(__name__)

#Variable global
todos = [
    {"label": "Sample", "done": True},
    {"label": "My second task", "done": True},
    {"label": "My third task", "done": True}
]

# Endpoint GET
@app.route('/todos', methods=['GET'])
def hello_world():  
    return jsonify(todos)

# Endpoint POST
@app.route('/todos', methods=['POST'])
def add_new_todo(): 
    request_body = json.loads(request.data)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

#Endpoint DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)


# Código de ejecución: $ pipenv run python src/app.py
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3245, debug=True)