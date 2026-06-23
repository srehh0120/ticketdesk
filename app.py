from flask import Flask,render_template,request,url_for,redirect
from ai_utils import analyze_ticket
from database import mysql
from config import Config
from databasesetup import setup_database
from MySQLdb.cursors import DictCursor
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
        INSERT into tickets(ticket_text,summary,resolution,category,impact,urgency,priority,team) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (ticket,result['summary'],result['resolution'],result['category'],result['impact'],result['urgency'],result['priority'],result['team']
        ))
    mysql.connection.commit()
    cur.close()
def get_all_tickets():
    cur=mysql.connection.cursor(DictCursor)
    cur.execute("""SELECT * from tickets ORDER BY created_at DESC """)
    tickets=cur.fetchall()
    cur.close()
    return tickets
def get_ticket_by_id(id):
    cur=mysql.connection.cursor(DictCursor)
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
    open_count=sum(1 for t in tickets if t['status']=='Open')
    team_counts={}
    for t in tickets:
        team=t['team']
        if team not in team_counts:
            team_counts[team]=0
        team_counts[team]+=1
    print(team_counts)
    teams = sorted(set(t['team'] for t in tickets))
    return render_template('dashboard.html',tickets=tickets,open_count=open_count,team_counts=team_counts,teams=teams)
@app.route('/ticket/<int:ticket_id>')
def ticket_details(ticket_id):
    ticket=get_ticket_by_id(ticket_id)
    return render_template('ticket_details.html',ticket=ticket)
@app.route('/update_status/<int:ticket_id>',methods=['POST'])
def update_status(ticket_id):
    status=request.form['status']
    cur=mysql.connection.cursor()
    cur.execute("""UPDATE tickets SET status=%s WHERE id = %s """,(status,ticket_id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('ticket_details',ticket_id=ticket_id))
@app.route('/team/<team>')
def team_dashboard(team):
    cur=mysql.connection.cursor()
    cur.execute("""Select * from tickets WHERE team =%s ORDER BY created_at DESC""",(team,))
    ticket=cur.fetchall()
    cur.close()
    return render_template('team_dashboard.html',ticket=ticket,team=team)

if __name__=='__main__':
    app.run(debug=True)

