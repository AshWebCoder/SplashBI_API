class InsertInDB:
    @staticmethod
    def method1(conn):
        try:
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS products1 (id SERIAL PRIMARY KEY, name VARCHAR(100), price FLOAT);'''
            )
            cur.execute('''INSERT INTO products1 (name, price) VALUES ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59); '''
            )
            conn.commit()
            cur.close()
            return {"status": "success", "message": "Data inserted successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}