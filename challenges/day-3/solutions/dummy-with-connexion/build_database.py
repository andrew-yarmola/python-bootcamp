import os
import re
from datetime import datetime
from config import db
from models import Employee
from flask import json

ISWORDS = re.compile(r'^[a-zA-Z\s]+$')

# Create the database
db.create_all()

with open('employees.json', 'r') as fp :
    try :
        data = json.loads(fp.read())
        for eid, e_dict in data.items() : 
            name = e_dict['employee_name']
            name = name[ : min(len(name), 100)]
            if ISWORDS.match(name) and len(name) > 0 :
                e = Employee(employee_id = eid,
                             age = e_dict['employee_age'],
                             salary = e_dict['employee_salary'],
                             name = name) 
                db.session.add(e)
            db.session.commit()
    except :
        pass
        db.app.logger.error('Failed to build database')
