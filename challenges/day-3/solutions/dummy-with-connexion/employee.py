"""
This is the employee module and supports all the REST actions for the
employee data
"""

from flask import make_response, abort
from config import db
from models import Employee, EmployeeSchema

def read_all():
    """
    This function responds to a request for /api/employee
    with the complete lists of employee

    :return:        json string of list of employee
    """
    # Create the list of employee from our data
    employee = Employee.query.order_by(Employee.employee_id).all()

    # Serialize the data for the response
    employee_schema = EmployeeSchema(many=True)
    data = employee_schema.dump(employee).data
    return data


def read_one(employee_id):
    """
    This function responds to a request for /api/employee/{employee_id}
    with one matching employee from employee

    :param employee_id:   Id of employee to find
    :return:            employee matching id
    """
    # Build the initial query
    employee = Employee.query.filter(Employee.employee_id == employee_id).one_or_none()

    # Did we find a employee?
    if employee is not None:

        # Serialize the data for the response
        employee_schema = EmployeeSchema()
        data = employee_schema.dump(employee).data
        return data

    # Otherwise, nope, didn't find that employee
    else:
        abort(404, f"Employee not found for id: {employee_id}")


def create(employee):
    """
    This function creates a new employee in the employee structure
    based on the passed in employee data

    :param employee:  employee to create in employee structure
    :return:        201 on success, 406 on employee exists
    """
    name = employee.get("name")

    existing_employee = Employee.query.filter(Employee.name == name).one_or_none()

    # Can we insert this employee?
    if existing_employee is None:

        # Create a employee instance using the schema and the passed in employee
        schema = EmployeeSchema()
        new_employee = schema.load(employee, session=db.session).data

        # Add the employee to the database
        db.session.add(new_employee)
        db.session.commit()

        # Serialize and return the newly created employee in the response
        data = schema.dump(new_employee).data

        return data, 201

    # Otherwise, nope, employee exists already
    else:
        abort(409, f"Employee {fname} {lname} exists already")


def update(employee_id, employee):
    """
    This function updates an existing employee in the employee structure

    :param employee_id:   Id of the employee to update in the employee structure
    :param employee:      employee to update
    :return:            updated employee structure
    """
    # Get the employee requested from the db into session
    update_employee = Employee.query.filter(
        Employee.employee_id == employee_id
    ).one_or_none()

    # Did we find an existing employee?
    if update_employee is not None:

        # turn the passed in employee into a db object
        schema = EmployeeSchema()
        update = schema.load(employee, session=db.session).data

        # Set the id to the employee we want to update
        update.employee_id = update_employee.employee_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated employee in the response
        data = schema.dump(update_employee).data

        return data, 200

    # Otherwise, nope, didn't find that employee
    else:
        abort(404, f"Employee not found for Id: {employee_id}")


def delete(employee_id):
    """
    This function deletes a employee from the employee structure

    :param employee_id:   Id of the employee to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the employee requested
    employee = Employee.query.filter(Employee.employee_id == employee_id).one_or_none()

    # Did we find a employee?
    if employee is not None:
        db.session.delete(employee)
        db.session.commit()
        return make_response(f"Employee {employee_id} deleted", 200)

    # Otherwise, nope, didn't find that employee
    else:
        abort(404, f"Employee not found for Id: {employee_id}")
