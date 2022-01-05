import sqlite3
import sys


def create_tables_if_not_exist():
    con = None

    try:
        con = sqlite3.connect('crunchbase.db')
        cur = con.cursor()

        # Organizations
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS organizations(id INTEGER PRIMARY KEY AUTOINCREMENT, name STR, inserted_at DATETIME, total_amount INT, n_round INT, lead_investors INT, investors INT);
            """)
        cur.executescript("""
            CREATE UNIQUE INDEX IF NOT EXISTS organizations_idx ON organizations(name, inserted_at);
            """)

        # Organization People
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS organization_people(id INTEGER PRIMARY KEY AUTOINCREMENT, full_name STR,  inserted_at DATETIME, startup_name STR, company_position STR);
            """)
        cur.executescript("""
            CREATE UNIQUE INDEX IF NOT EXISTS organization_people_idx ON organization_people(full_name, inserted_at, startup_name);
            """)

        # Investment Firms
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS investment_firms(id INTEGER PRIMARY KEY AUTOINCREMENT, name STR, inserted_at DATETIME, investments INT, lead_investments INT, diversity_investments INT, exits INT);
            """)
        cur.executescript("""
            CREATE UNIQUE INDEX IF NOT EXISTS investment_firms_idx ON investment_firms(name, inserted_at);
            """)

        # Rounds
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS rounds(id INTEGER PRIMARY KEY AUTOINCREMENT, round_name STR, round_date DATETIME, inserted_at DATETIME, startup_name STR, investment_firm_name STR);
            """)
        cur.executescript("""
            CREATE UNIQUE INDEX IF NOT EXISTS rounds_idx ON rounds(round_name, inserted_at);
            """)

        con.commit()

    except sqlite3.Error as e:
        if con:
            con.rollback()
        print(f"Error {e.args[0]}")
        sys.exit(1)

    finally:
        if con:
            con.close()


if __name__ == '__main__':
    create_tables_if_not_exist()
