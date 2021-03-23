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

def get_user_monkeys(userId):
    with MSSQL() as db:
        sql = """
            SELECT m.MonkeyName, m.MonkeyID
            FROM Monkeys m
                JOIN Accounts_Users au ON m.AccountID = au.AccountID
            WHERE au.UserID = ?
        """
        return db.query(sql, (userId,))

def get_monkey_positions(monkeyId, date):
    with MSSQL() as db:
        sql = """
            SELECT Symbol, Shares, OpenDate, OpenPrice, CloseDate, ClosePrice, isShort
            FROM Positions
            WHERE MonkeyId = ? AND CurrentDate = CAST(? AS DATE) 
        """
        return db.query(sql, (monkeyId, date))