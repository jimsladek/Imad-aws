from flask import Flask,request,jsonify
import mysql.connector
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)

employees = [
    {"id": 1, "firstName": "raouf", "lastName": "cherfa","emailId": "123"},
    {"id": 2, "firstName": "islam", "lastName": "eladly","emailId": "256"},
    {"id": 3, "firstName": "sofiane", "lastName": "idk","emailId": "758"}
    ]
# Creating connection object
db = mysql.connector.connect(
    host='172.50.0.3',
    port=3306,
    user='root',
    password='password',
    database='products_db'
)
cursor = db.cursor()
#cursor.execute("CREATE TABLE employee (id MEDIUMINT NOT NULL AUTO_INCREMENT,firstName CHAR(30) NOT NULL,lastName CHAR(30) ,emailId int ,PRIMARY KEY (id))")
@app.route('/')
def default():
    return "Jim SLADEK"

@app.route('/api/v1/employees/', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'GET':
        cursor.execute("select id, firstName, lastName, emailId from employees")
        result=cursor.fetchall()
        employees = []
        for row in result:
            employee = {'id': row[0], 'firstName': row[1], 'lastName': row[2], 'emailId': row[3]}
            employees.append(employee)
        return jsonify(employees)

    if request.method == 'POST':
        firstName=request.json['firstName']
        lastName=request.json['lastName']
        emailIf=request.json['emailId']
        print(firstName, lastName, emailId)
        cursor.execute("INSERT INTO employees (firstName, lastName, emailId) VALUES (%s, %s, %s)", (firstName, lastName, emailId))
        db.commit()
        return jsonify({'employee added'}), 201

@app.route('/api/v1/employees/<int:id>', methods=['GET'])   
def get_employee(id):
    cursor.execute("select id, firstName, lastName, emailId from employees where employees.id=%s",[id])
    result = cursor.fetchall()
    if result == []:
        return jsonify({'error': 'Employee not found'}), 404
    row = result[0]
    employee = {'id': row[2], 'firstName': row[1], 'lastName': row[3], 'emailId': row[0]}
    return jsonify(employee)

@app.route('/api/v1/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    cursor.execute("delete from employees where employees.id=%s",[id])
    db.commit()
    # Return a success message if the employee was deleted
    if cursor.rowcount > 0:
        return jsonify({"message": "employee deleted"}),201
    # Return an error message if the employee is not found
    else:
        return jsonify({'error': 'Employee not found'}), 404
    

@app.route('/api/v1/employees/<int:id>', methods=['PUT'])
def update_employees(id):
    firstName=request.json['firstName']
    lastName=request.json['lastName']
    emailId=request.json['emailId']
    cursor.execute("select * from employees where employees.id=%s",[id])
    if cursor.fetchall() == []:
        return jsonify({'error': 'Employee not found'}), 404
    command="UPDATE employees set firstName = %s, lastName = %s, emailId = %s WHERE id= %s"
    cursor.execute(command,(firstName,lastName,emailId,id))
    print(cursor.fetchwarnings())
    db.commit()
    #employee = [employee for employee in employees if employee['id'] == id]
    #if len(employee) == 0:
    #    return {"message": "employee not found"}
    #employee[0]['First Name'] = request.json.get('First Name', employee[0]['First Name'])
    #employee[0]['Last Name'] = request.json.get('Last Name', employee[0]['Last Name'])
    #employee[0]['emailId'] = request.json.get('emailId', employee[0]['emailId'])

    return jsonify({"message": "employee updated"}),201


if __name__ == '__main__':
    app.run(debug=True,port=8081)
