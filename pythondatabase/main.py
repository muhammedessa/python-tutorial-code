import sqlite3 
from employee import Employee

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('emplyees.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS
                employees (
                first text,
                last text,
                salary integer
                )""")

 
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :salary)", {'first': emp.first, 'last': emp.last, 'salary': emp.salary})


def get_emps_by_name(first):
    c.execute("SELECT * FROM employees WHERE first=:first", {'first': first})
    return c.fetchall()


def update_salary(emp, salary):
    with conn:
         c.execute("""UPDATE employees SET salary = :salary
               WHERE first = :first AND last = :last""",
          {'first': emp.first, 'last': emp.last, 'salary': salary})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


def get_all_emps():
    c.execute("SELECT * FROM employees")
    return c.fetchall()


emp_1 = Employee('Muhammed', 'Essa', 2000)
emp_2 = Employee('Ahmed', 'Essa', 3000)
emp_3 = Employee('Osama', 'Essa', 5000)
emp_4 = Employee('Ali', 'Essa', 6000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)

print("--------allemps before-------")
allemps = get_all_emps()
print(allemps)

print("-----get_emps------")
emps = get_emps_by_name('Muhammed')
print(emps)

update_salary(emp_2, 9500)
remove_emp(emp_4)

print("------get_emps_by_name-------")
emps = get_emps_by_name('Ahmed')
print(emps)


print("---------------")

allemps = get_all_emps()
print(allemps)

conn.close()
