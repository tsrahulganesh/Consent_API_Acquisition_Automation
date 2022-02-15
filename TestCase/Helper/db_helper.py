import psycopg2

conn = psycopg2.connect(
    host="tbscinldtstwsp2psql1.postgres.database.azure.com",
    database="tanlaconfigdb",
    user="postgresadmin@tbscinldtstwsp2psql1",
    password="postgres@Tanla")


def test_db():
    # create a cursor
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute("SELECT *From public.account Where id=67")
    dn_poll_sub = cur.fetchone()
    print(dn_poll_sub)
