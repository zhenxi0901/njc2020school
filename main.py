
from flask import *
import sqlite3
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    data = request.form
    school = data["school"]
    department = data["department"]
    connection = sqlite3.connect(
        "task1(NJC exercise).db")
    cursor = connection.execute(
        "SELECT * From staff WHERE Department = ?", (department,))
    rows = cursor.fetchall()
    lst = []
    for item in rows:
        schoolcode, name, department1, contact = item
        cursor2 = connection.execute(
            "SELECT Name,Address From school WHERE SchoolCode= ?", (schoolcode,))
        cursor2 = cursor2.fetchall()[0]
        connection.commit()
        schoolname, schooladdress = cursor2
        if school in schoolname:
            lst.append((schoolname, name, department1, contact, schooladdress))
    return render_template("teacher.html", lst=lst)
    connection.close()

if __name__ == '__main__':
    app.run(debug=True , use_reloader = True)
