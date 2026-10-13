import os


class Database:
    """PARENT CLASS: creates the connection between Python and MySQL.
    PortfolioManager extends this class (INHERITANCE)."""

    def __init__(self):
        self._host = os.getenv("PORTFOLIO_DB_HOST", "localhost")
        self._user = os.getenv("PORTFOLIO_DB_USER", "root")
        self._password = os.getenv("PORTFOLIO_DB_PASSWORD", "")
        self._database = os.getenv("PORTFOLIO_DB_NAME", "portfolio_flask")

    def get_connection(self):
        # Imported here so the app can show a clear message if the driver is missing.
        import mysql.connector
        return mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database,
        )
