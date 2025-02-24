from db import get_connection

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)", (self.name, self.library_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users