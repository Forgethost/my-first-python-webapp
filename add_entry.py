from db_calls import *

#insert key
def add_entry_key_table(cursor):
    insert_key(cursor, 1022)


def get_seat_info(cursor, seat_num):
    row = get_key_details(cursor, seat_num)
    return row