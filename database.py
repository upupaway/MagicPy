# Importing Important Libraries

import sqlite3
import bcrypt


class Database:
    '''
        Database Class for sqlite3
        :params conn - sqlite3Connection
        :params curr - cursor
    '''
    def __init__(self):
        try:
            self.conn = sqlite3.connect("users.db")
            self.curr = self.conn.cursor()
        except:
            print("Failed")

    def createTable(self):

        '''
            Method for Creating Table in Database
        '''

        create_table = '''
            CREATE TABLE IF NOT EXISTS cred(
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                salt TEXT NOT NULL
            );
        '''

        self.curr.execute(create_table)
        self.conn.commit()

    def insertData(self, data):

        '''
            Method for Inserting Data in Table in Database
        '''

        insert_data = """
            INSERT INTO cred(username, password, salt)
            VALUES(?, ?, ?);
        """
        val=(data[0],data[1], data[2])
        self.curr.execute(insert_data, val)
        self.conn.commit()

    def searchData(self, data):

        '''
            Method for Searching Data in Table in Database
        '''

        search_data = '''
            SELECT * FROM cred WHERE username = (?);
        '''

        self.curr.execute(search_data, data)

        rows = self.curr.fetchall()

        if rows == []:
            return 1
        return 0

    def validateData(self, data, inputData):

        '''
            Method for Validating Data Table in Database
        '''

        validate_data = """
            SELECT * FROM cred WHERE username = (?);
        """

        self.curr.execute(validate_data, data)
        row = self.curr.fetchall()
        if row[0][0] == inputData[0]:
            return row[0][1] == bcrypt.hashpw(str(inputData[1].encode()), row[0][2])