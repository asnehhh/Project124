from flask import Flask,jsonify, request

appPro = Flask(__name__)

tasks = [
    {
        'Contact': '9986754423',
        'Name': u'Raju',
        'done': False, 
        'id': 1
    },
    {
        'Contact': '919008435',
        'Name': u'Rahul',
        'done': False, 
        'id': 2
    }
]

@appPro.route("/")
def hello_world():
    return "Hello World!"

@appPro.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'Contact': request.json['Contact'],
        'Name': request.json['Name'],
        'done': False,
        'id': tasks[-1]['id'] + 1
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@appPro.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    appPro.run(debug=True)
