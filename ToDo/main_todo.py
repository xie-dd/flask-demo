from flask import Flask, render_template, request, jsonify, Response
import json


app = Flask(__name__)


def get_data_from_mysql():
    import pymysql
    conn = pymysql.connect(host="****", port=3306, user='todo', passwd="****", charset='utf8', db='todo')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from tb1;")
    data_list = cursor.fetchall()
    # print(data_list)
    A1=data_list[0]
    A2=data_list[1]
    A3=data_list[2]
    A4=data_list[3]
    A5=data_list[4]


    data = {
                "reminderText_A1": A1["reminderText"], "email_A1": A1["email"], "reminderTime_A1": A1["reminderTime"], "A1": A1["rbtn"],
                "reminderText_A2": A2["reminderText"], "email_A2": A2["email"], "reminderTime_A2": A2["reminderTime"], "A2": A2["rbtn"],
                "reminderText_A3": A3["reminderText"], "email_A3": A3["email"], "reminderTime_A3": A3["reminderTime"], "A3": A3["rbtn"],
                "reminderText_A4": A4["reminderText"], "email_A4": A4["email"], "reminderTime_A4": A4["reminderTime"], "A4": A4["rbtn"],
                "reminderText_A5": A5["reminderText"], "email_A5": A5["email"], "reminderTime_A5": A5["reminderTime"], "A5": A5["rbtn"],
            }
    # 3.关闭连接
    cursor.close()
    conn.close()

    return data


def updata_mysql(data):

    print(data)
    import pymysql
    conn = pymysql.connect(host="****", port=3306, user='todo', passwd="****", charset='utf8', db='todo')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute("UPDATE  tb1 SET reminderText=%s, email=%s, reminderTime=%s, rbtn=%s WHERE id=1", 
              [data["reminderText_A1"], data["email_A1"], data["reminderTime_A1"], data["A1"]])
    cursor.execute("UPDATE  tb1 SET reminderText=%s, email=%s, reminderTime=%s, rbtn=%s WHERE id=2", 
              [data["reminderText_A2"], data["email_A2"], data["reminderTime_A2"], data["A2"]])
    cursor.execute("UPDATE  tb1 SET reminderText=%s, email=%s, reminderTime=%s, rbtn=%s WHERE id=3", 
              [data["reminderText_A3"], data["email_A3"], data["reminderTime_A3"], data["A3"]])
    cursor.execute("UPDATE  tb1 SET reminderText=%s, email=%s, reminderTime=%s, rbtn=%s WHERE id=4", 
              [data["reminderText_A4"], data["email_A4"], data["reminderTime_A4"], data["A4"]])
    cursor.execute("UPDATE  tb1 SET reminderText=%s, email=%s, reminderTime=%s, rbtn=%s WHERE id=5", 
              [data["reminderText_A5"], data["email_A5"], data["reminderTime_A5"], data["A5"]])

    conn.commit()
    cursor.close()
    conn.close()



@app.route('/')
def index():
    try:
        data = get_data_from_mysql()

    except:
        print("error when run get_data_from_mysql")
        data = {
            "reminderText_A1": "", "email_A1": "", "reminderTime_A1": "", "A1": "A1_Once",
            "reminderText_A2": "", "email_A2": "", "reminderTime_A2": "", "A1": "A2_Once",
            "reminderText_A3": "", "email_A3": "", "reminderTime_A3": "", "A1": "A3_Once",
            "reminderText_A4": "", "email_A4": "", "reminderTime_A4": "", "A1": "A4_Once",
            "reminderText_A5": "", "email_A5": "", "reminderTime_A5": "", "A1": "A5_Once"
        }
    
    return render_template("index.html", data=data)


@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    updata_mysql(data)

    return jsonify({"message": "Data saved successfully!"})



if __name__ == '__main__':
    app.run(debug=True)
