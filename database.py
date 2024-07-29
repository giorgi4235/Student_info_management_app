import sqlite3

def create_connection():
    conn=sqlite3.connect('student_information.db')
    return conn

def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS studs(
        student_id PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        email TEXT NOT NULL,
        phone INTEGER NOT NULL,
        address TEXT NOT NULL
        )''')
    conn.commit()
    conn.close()

def add_student(student_id, firstname, lastname, email, phone, address):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO studs (student_id, firstname, lastname, email, phone, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id,firstname, lastname, email, phone, address)
        )
        conn.commit()
    except sqlite3.Error as error:
        print(f"database error: {error}")
    finally:
        conn.close()

def update_student(student_id, firstname, lastname, email, phone, address):
    try:
        conn = create_connection()
        cur = conn.cursor()
        print("Executing update query")
        cur.execute("""
        UPDATE studs 
        SET firstname = ?, lastname = ?, email = ?, phone = ?, address = ?
        WHERE student_id = ?
        """, (firstname, lastname, email, phone, address, student_id))
        conn.commit()
        print("Updated student successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def delete_student(student_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM studs WHERE student_id = ?""", (student_id,)
    )
    conn.commit()
    conn.close()


def get_all_students():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM studs""")
    students = cur.fetchall()
    conn.close()
    return students

def check_student_id(student_id):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute('''SELECT 1 FROM studs WHERE student_id = ?''', (student_id,))
        result = cur.fetchone()
        return result is None # if True its empty, if false it isn't
    except Exception as e:
        print(f"An error occurred while checking student ID: {e}")
        return False
    finally:
        conn.close()

