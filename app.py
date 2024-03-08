from flask import Flask
import os
import pymysql

app = Flask(__name__)

# Function to check database connection
def check_db_connection():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'test')

    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        connection.close()
        return True
    except Exception as e:
        print("Failed to connect to database:", str(e))
        return False

@app.route('/')
def index():
    if check_db_connection():
        return 'Database Connection Status: Connected'
    else:
        return 'Database Connection Status: Disconnected'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
