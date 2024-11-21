class SelectFromDB:
    @staticmethod
    def method2(conn):
        try:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS products1;")
            conn.commit()  
            cur.close()
            return {"status": "success", "data": "Dropped the table"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
