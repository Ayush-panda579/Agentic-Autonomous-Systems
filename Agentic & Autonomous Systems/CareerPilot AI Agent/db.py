import sqlite3

DB_NAME = "careerpilot.db"


def get_conn():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn


def init_db():

    conn = get_conn()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()

    conn.close()


def create_user(
    username,
    email,
    password
):

    conn = get_conn()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (username, email, password)
        VALUES (?, ?, ?)
        """,
        (
            username,
            email,
            password
        )
    )

    conn.commit()

    conn.close()


def get_user(username):

    conn = get_conn()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


if __name__ == "__main__":

    init_db()

    print(
        "Database initialized successfully."
    )