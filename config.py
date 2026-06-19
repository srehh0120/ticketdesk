from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
    GROQ_API_KEY=os.getenv('GROQ_API_KEY')

    MYSQL_HOST=os.getenv('MYSQL_HOST')
    MYSQL_USER=os.getenv('MYSQL_USER')
    MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
    MYSQL_DB=os.getenv('MYSQL_DB')
