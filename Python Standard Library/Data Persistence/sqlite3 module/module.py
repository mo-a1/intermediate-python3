import sqlite3

# https://www.youtube.com/watch?v=pd-0G0MigUA&ab_channel=CoreySchafer

con = sqlite3.connect("students.db", check_same_thread=True)
c = con.cursor()

c.execute("DROP TABLE students")

with con:
    c.execute("""CREATE TABLE IF NOT EXISTS students (
                                                    fname TEXT,
                                                    lname TEXT,
                                                    degree INTEGER
                                                    )""")


def add_student(fname, lname, degree):
    with con:
        c.execute("INSERT INTO students (fname, lname, degree) VALUES (?, ?, ?)", (fname, lname, degree))


def show_students():
    c.execute("SELECT * FROM students")
    print(c.fetchall())


add_student("ahmed", "ali", 95)
add_student("mazen", "khaled", 70)
show_students()

with con:
    c.execute("UPDATE students SET degree = 99 WHERE fname = 'ahmed'")
    c.execute("SELECT * FROM students")
    print(c.fetchall())
    c.execute("SELECT count(fname) FROM students")
    print(c.fetchone())
    c.execute("SELECT avg(degree) FROM students")
    print(c.fetchone())
    c.execute("SELECT fname, lname FROM students WHERE fname LIKE 'm_%'")
    print(c.fetchone())
