import sqlite3

class Database:
    def __init__(self, db_path="data/knowledge_space.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            parent_id INTEGER,
            FOREIGN KEY(parent_id) REFERENCES notes(id)
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_note(self, title, content, parent_id=None):
        query = "INSERT INTO notes (title, content, parent_id) VALUES (?, ?, ?)"
        self.conn.execute(query, (title, content, parent_id))
        self.conn.commit()
    
    # Weitere Funktionen, wie Abruf von Notizen und Löschoperationen
