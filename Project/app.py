from flask import Flask,request,render_template
import pymysql
app=Flask(__name__)
def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Notbiju2005',
        database='flaskdb',
        cursorclass=pymysql.cursors.DictCursor
    )
@app.route('/')
def home():
    return render_template("event.html")
@app.route('/submit',methods=['POST'])
def submit():
    name=request.form["peru"]
    email=request.form["mail"]
    contact=request.form["phone"]
    conn=connection()
    cursor=conn.cursor()
    sql="INSERT INTO users(name,email,contact) VALUES (%s,%s,%s)"
    cursor.execute(sql,(name,email,contact))
    conn.commit()
    conn.close()
    return "Data stored successfully!"
if __name__=="__main__":
    app.run(debug=True)