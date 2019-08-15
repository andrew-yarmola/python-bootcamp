from datetime import datetime
from config import db, ma
from marshmallow import fields

class Employee(db.Model) :
    __tablename__ = "employee"
    employee_id = db.Column(db.Integer, primary_key=True, index = True)
    age = db.Column(db.Integer)
    salary = db.Column(db.Float)
    name = db.Column(db.String(100))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class EmployeeSchema(ma.ModelSchema) :
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta :
        model = Employee
        sqla_session = db.session
