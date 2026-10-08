import csv

with open('data/employee.csv', newline='') as file:
    data = csv.DictReader(file)

    for row_number, row in enumerate(data, start=2):
            empoyee_id = row['id']
            salary = row['salary']

            if not empoyee_id:
                 raise ValueError('employee_id is missing at row ', row_number)

            if float(salary) < 0:
                raise ValueError("salary is negative", row_number)

    print("load into target system")