import sqlite3
from sqlite3 import DatabaseError


def conn_db(databasefile):
    conn = sqlite3.connect(databasefile)
    cursor = conn.cursor()
    return conn, cursor


def get_seat(cursor, seat_num):
    """This function inserts data in Key Table
       Parameters: Cursor object
       Return: Status"""
    seat_num = seat_num.upper()
    seat_num = seat_num.rstrip()
    seat_num = str(seat_num)
    sqlstmt = """SELECT SEAT_ID FROM SEAT
                 WHERE SEAT_NUM = ?"""
    cursor.execute(sqlstmt, (seat_num,))
    row = cursor.fetchone()
    return row

def get_key_details(cursor, seat_num):
    sqlstmt = """SELECT EMPLOYEE_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME, COG_PROJECT_ID,
                 KEY_NUM, key_status, EFF_DATE, RETURN_DATE, KEY_RETURN_IND, seat_num
                 FROM EMPLOYEE
				 INNER JOIN SEAT ON EMPLOYEE.SEAT_ID = SEAT.SEAT_ID
                 INNER JOIN KEY ON EMPLOYEE.KEY_ID = KEY.KEY_ID
               INNER JOIN PROJECT ON EMPLOYEE.PROJECT_ID = PROJECT.PROJECT_ID
               INNER JOIN  key_status ON EMPLOYEE.KEY_STATUS_ID = KEY_STATUS.KEY_STATUS_ID               
               WHERE SEAT.SEAT_ID = ?
               ORDER BY EFF_DATE DESC"""
    cursor.execute(sqlstmt, (seat_num,))
    row = cursor.fetchone()
    return row





def insert_key(cursor, key_num):
    """This function inserts data in Key Table
       Parameters: Cursor object
       Return: Status"""
    sqlstmt = """INSERT INTO KEY(KEY_NUM)
                 VALUES(?)"""
    cursor.execute(sqlstmt, (key_num,))

#exception handling



