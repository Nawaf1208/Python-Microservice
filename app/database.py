from pymongo import MongoClient
import sqlite3

# MongoDB
mongo_client = MongoClient("mongodb://mongo:27017")
mongo_db = mongo_client["users_db"]
users_collection = mongo_db["users"]

# SQLite (logs)
conn = sqlite3.connect("/logs/app.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT
)
""")

conn.commit()

