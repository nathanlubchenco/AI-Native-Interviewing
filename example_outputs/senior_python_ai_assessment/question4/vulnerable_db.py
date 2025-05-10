import psycopg2

def get_user_orders(cursor, user_id):
    # Vulnerable to SQL injection
    query = f"SELECT * FROM orders WHERE user_id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

def search_products(cursor, keyword):
    # Vulnerable to SQL injection and may have performance issues
    query = "SELECT id, name, price FROM products WHERE name LIKE '%{}%'".format(keyword)
    cursor.execute(query)
    return cursor.fetchall()

def bulk_insert_logs(cursor, logs):
    # Unsafe batching of inserts
    values = ",".join(f"('{log['id']}', '{log['message']}')" for log in logs)
    query = f"INSERT INTO logs (id, message) VALUES {values}"
    cursor.execute(query)