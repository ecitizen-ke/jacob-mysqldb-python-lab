import mysql.connector

class Connection:
    """This class provides connection to our database"""

    def __init__(self):
        self.host = "localhost"
        self.db = "US_States"
        self.user = "root"
        self.password = "password"

        # Create a db connection
        self.conn = mysql.connector.connect(
            host=self.host, database=self.db, user=self.user, password=self.password
        )

        # Create cursor
        self.cursor = self.conn.cursor()
