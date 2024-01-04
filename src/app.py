from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    global todos
    if not todos:
        todos = [
            { "label": "Sample", "done": True }
        ]
    for todo in todos:
        if not isinstance(todo, dict) or "label" not in todo or "done" not in todo:
            return "Invalid todo format", 500
        if not isinstance(todo["label"], str):
            return "Todo label must be a string", 500
        if not isinstance(todo["done"], bool):
            return "Todo done must be a boolean", 500
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    if position < 0 or position >= len(todos):
        return "Todo not found", 404
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

