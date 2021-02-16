"""
    Database calls
"""

from app.util.mssql import MSSQL

def get_user_etrade_params(userId):
    with MSSQL() as db:
        sql = """
            SELECT *
            FROM dbo.Users_Etrade_Session
            WHERE UserID = ?
        """
        result = db.query_one(sql, (userId,))
        if result:
            return result
        else:
            sql = """
                INSERT INTO dbo.Users_Etrade_Session (UserId)
                Values (?)
            """
            db.execute(sql, (userId,))

def save_auth_request(token, secret, userId):
    with MSSQL() as db:
        sql = """
            UPDATE dbo.Users_Etrade_Session
            SET RequestToken = ?,
                RequestSecret = ?
            WHERE UserID = ?
        """
        return db.execute(sql, (token, secret, userId))

def save_session(token, secret, userId):
    with MSSQL() as db:
        sql = f"""
            UPDATE dbo.Users_Etrade_Session
            SET AccessToken = ?,
                AccessSecret = ?,
                CreateDateTime = GETDATE()
            WHERE UserID = ?
        """
        return db.execute(sql, (token, secret, userId))
