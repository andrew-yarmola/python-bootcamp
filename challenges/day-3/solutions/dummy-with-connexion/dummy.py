from flask import Flask, Blueprint, request, json

api = Blueprint('api', __name__, url_prefix='/api/v1')
app = Flask(__name__)

EMPLOYEES = {}
FREE_ID = 0
with open('employees.json','r') as fp :
    EMPLOYEES_LIST = json.loads(fp.read())
    for e in EMPLOYEES_LIST :
        eid = int(e['id'])
        EMPLOYEES[eid] = e
        FREE_ID = max(FREE_ID, eid)
    del EMPLOYEES_LIST

@api.route('/employee')
def employees():
    return EMPLOYEES

@api.route('/employee/<int:eid>')
def get_employee(eid) :
    return EMPLOYEES.get(eid,{}) 

@api.route('/create', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    if not new_employee :
        return { "failed" : { "text" : "bad employee format" }  }    
    global FREE_ID
    new_id = FREE_ID
    FREE_ID += 1
    new_employee['id'] = new_id
    EMPLOYEES[new_id] = new_employee
    return new_employee

@api.route('/update/<int:eid>', methods=['PUT'])
def update_employee(eid):
    if eid not in EMPLOYEES :
        return { "failed" : { "text" : "no such employee" } }
    update_data = request.get_json()
    if not update_data :
        return { "failed" : { "text" : "bad update format" } }
    employee = EMPLOYEES[eid]
    employee.update(update_data)
    return employee 

@api.route('/delete/<int:eid>', methods=['DELETE'])
def delete_employee(eid):
    if eid not in EMPLOYEES :
        return { "failed" : { "text" : "no such employee" } }
    else :
        del EMPLOYEES[eid]
        return { "success" : { "text" : "succesfully deleted employee" } }

app.register_blueprint(api)
