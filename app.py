from flask import Flask,render_template,request
from ai_utils import analyze_ticket
from database import mysql
from config import Config
from databasesetup import setup_database
setup_database()
app=Flask(__name__)
app.config['MYSQL_HOST']=Config.MYSQL_HOST
app.config['MYSQL_USER']=Config.MYSQL_USER
app.config['MYSQL_PASSWORD']=Config.MYSQL_PASSWORD
app.config['MYSQL_DB']=Config.MYSQL_DB
mysql.init_app(app)
def save_ticket(ticket,result):
    print("SAVE FUNCTION CALLED")
    cur=mysql.connection.cursor()
    cur.execute("""
        INSERT into tickets(ticket_text,summary,category,impact,urgency,priority,team) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (ticket,result['summary'],result['category'],result['impact'],result['urgency'],result['priority'],result['team']
        ))
    mysql.connection.commit()
    cur.close()
def get_all_tickets():
    cur=mysql.connection.cursor()
    cur.execute("""SELECT * from tickets ORDER BY created_at DESC """)
    tickets=cur.fetchall()
    cur.close()
    return tickets
def get_ticket_by_id(id):
    cur=mysql.connection.cursor()
    cur.execute("""SELECT * from tickets where id = %s """,(id,))
    ticket=cur.fetchone()
    cur.close()
    return ticket
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/analyze',methods=['POST'])
def analyze():
    ticket=request.form.get('ticket')
    result=analyze_ticket(ticket)
    save_ticket(ticket,result)
    return render_template('result.html',ticket=ticket,result=result)
@app.route('/dashboard')
def dashboard():
    tickets=get_all_tickets()
    return render_template('dashboard.html',tickets=tickets)
@app.route('/ticket/<int:ticket_id>')
def ticket_details(ticket_id):
    ticket=get_ticket_by_id(ticket_id)
    return render_template('ticket_details.html',ticket=ticket)


if __name__=='__main__':
    app.run(debug=True)

