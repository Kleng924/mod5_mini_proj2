from db import get_connection

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name, biography) VALUES (%s, %s)", (self.name, self.biography))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return authors