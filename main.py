from flask import Flask, render_template, request
from add_entry import *
import os
app = Flask(__name__)

database = "lims.sqlite"
db_path = os.getcwd() + "\\database\\" + database
#db_path = r"c:\python\lims\database\lims1.sqlite"


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        seat_num = request.form["seat_num"]
        if len(seat_num) < 2:
            reenter = "Please enter a seat num and then click Submit"
            return render_template("home.html", message = reenter)
        else:
            try:
                conn, cursor = conn_db(db_path)
                row = get_seat(cursor, seat_num)
                if row != None:
                    seat_id = row[0]
                    row = get_key_details(cursor, seat_id)
                    if row != None:
                        return render_template("seat_info.html", emp_id=row[0],
                        first_name=row[1], middle_name=row[2],last_name=row[3],
                        project_id=row[4],key_num=row[5],key_status=row[6],eff_date=row[7],
                        return_date=row[8],key_return_ind=row[9],seat_num=row[10])
                    else:
                        seat_not_found = "Deatils not found! Please try again with a valid Seat number"
                        return render_template("home.html", message=seat_not_found)
                else:
                    seat_not_found = "Seat Number not found! Please try again with a valid Seat number"
                    return render_template("home.html", message=seat_not_found)
            except Exception as e:
                return render_template("505.html", e = e)
    else:
        return render_template("home.html", message = " ")


if __name__ == "__main__":
    app.run(debug=True)


