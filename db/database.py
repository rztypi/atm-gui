import sqlite3


class Database:
    """A class for handling the app's database-related functions.

    Attributes:
        conn (sqlite3.Connection): The database connection.
    """

    def __init__(self, db_path):
        """Initializes a database connection to db_path.

        Parameters:
            db_path (str): The path of the database.
        """
        self.conn = sqlite3.connect(db_path)

    def close(self):
        """Closes the database connection."""
        self.conn.close()

    def login_account(self, username, password):
        """Checks if username and password arguments exist in the database.

        Parameters:
            username (str): The username entry from the login form.
            password (str): The password entry from the login form.

        Returns:
            bool: True if login is successful, False if not.
        """
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT username, password
            FROM accounts
            WHERE username = ?
            AND password = ?
            """,
            (username, password),
        )

        login_found = cursor.fetchone()

        cursor.close()

        return True if login_found else False

    def register_account(self, username, password, phone_number):
        """Inserts the account details from the registration form to the database.

        Parameters:
            username (str): The username entry from the register form.
            password (str): The password entry from the register form.
            phone_number (str): The phone_number entry from the register form.

        Returns:
            bool: True if registration is successful, False if not.
        """
        cursor = self.conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO accounts VALUES
                    (?, ?, ?)
                """,
                (username, password, phone_number),
            )
        except sqlite3.IntegrityError:
            register_status = False
        else:
            self.conn.commit()

            register_status = True

        cursor.close()

        return register_status