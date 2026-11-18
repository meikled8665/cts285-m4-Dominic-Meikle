import sqlite3
import problems
from pathlib import Path

folder = Path(__file__).resolve().parent
bank = folder / "bank.db"

def bankAdd(id):
    conn = sqlite3.connect(bank)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO bank (id, problem) VALUES (?, ?)", (id, problems.loadProb(id)))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Could Not Add item: {e}")

    conn.close()

def bankRemove(num):
    conn = sqlite3.connect(bank)
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM bank WHERE num = ?", (num,))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Could not remove: {e}")
    
    conn.close()

def loadBank():
    conn = sqlite3.connect(bank)
    cursor = conn.cursor()
    cursor.execute("SELECT num, problem, id FROM bank")
    bankDat = cursor.fetchall()
    conn.close()
    return bankDat

def createBank():
    with sqlite3.connect(bank) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank(
                num INTEGER PRIMARY KEY,
                problem VARCHAR(50),
                id TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS block_over_10
            BEFORE INSERT ON bank
            BEGIN
                SELECT RAISE(ABORT, 'Table Is Full: 10 Items Max')
                WHERE (SELECT COUNT(*) FROM bank) >= 10;
            END;
        """)