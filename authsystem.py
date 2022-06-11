import sqlite3


class register_login:
    def register():
        username = input('Enter your user name: ')
        passwaord = input('Enter your password: ')
        # coonecting to database
        db = sqlite3.connect('login.db')
        # Create cursor
        cur = db.cursor()
        # insert data into database
        # cur.execute(
        #     "CREATE TABLE IF NOT EXISTS login(Username TEXT,Password TEXT)")
        cur.execute("INSERT INTO login VALUES (:Username, :Password)",
                    {
                        'Username': username,
                        'Password': passwaord,
                    })
        # commit changes
        db.commit()
        # closing db
        db.close()

    def access():
        user = input("Please enter your username> ")
        pas = input("Please enter your password> ")
        # connecting to db
        db = sqlite3.connect('Confidential\login.db')
        # Create cursor
        cur = db.cursor()
        # Fetching data from database
        cur.execute(
            "SELECT * FROM login WHERE Username=? AND Password=?", (user, pas))
        row = cur.fetchone()
        if row:
            print("loging success")
        else:
            print('lognin failed')

        db.commit()
        # close db
        db.close()


if __name__ == "__main__":
    register_login.register()
