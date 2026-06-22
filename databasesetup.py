import MySQLdb
from config import Config
def setup_database():
    conn=MySQLdb.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD
    )
    cur=conn.cursor()
    cur.execute(f"""CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}""")
    cur.execute(f"""USE {Config.MYSQL_DB}""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets(
            id INT AUTO_INCREMENT PRIMARY KEY,
            ticket_text TEXT NOT NULL,
            summary TEXT,
            resolution TEXT,
            category VARCHAR(100),
            impact VARCHAR(20),
            urgency VARCHAR(20),
            priority VARCHAR(20),
            team VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()

    cur.close()
    conn.close()