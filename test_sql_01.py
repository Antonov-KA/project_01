import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL PRIMARY KEY, 
# Student_Name TEXT NOT NULL, 
# School_Id INTEGER NOT NULL
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# ('201', 'Иван', 1),
# ('202', 'Петр', 2),
# ('203', 'Анастасия', 3),
# ('204', 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close
        
def get_schoolname(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """
        SELECT Students.student_id, School.school_name
        FROM Students 
        JOIN School ON Students.school_id = School.School_Id
        WHERE student_id = ?;"""
        cursor.execute(select_query, (student_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, sqlite3.Error) as error:
        print("Ошибка получения данных", error)

def get_student(student_id):
    try:
        schoolname = get_schoolname(student_id)
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM Students WHERE Student_Id = ?"""
        cursor.execute(select_query, (student_id,))
        records = cursor.fetchall()
        print("Данные стулента ")
        for raw in records:
            print("ID студента ", raw[0])
            print("Имя студента ", raw[1])
            print("ID школы ", raw[2])
            print("Название школы ", schoolname)
        close_connection(connection)
    
    except (Exception, sqlite3.Error) as error:
        print("Ошибка получения данных", error)


print("Задача №7 Студенты \n")
get_student(204)
