# import sqlite3


# class Sql:
# 	def __init__(self):
# 		self.connection = sqlite3.connect('bot.db')
# 		self.cursor = self.connection.cursor()
	


# 	def baza_create(self):
# 		self.cursor.execute("""CREATE TABLE IF not exists user(
#         id integer,
#         firstname varchar(24),
#         username varchar(24),
#         tel integer NULL
# 		)""")



# 	def user_add(self, idi, username, first_name):
# 		self.cursor.execute("INSERT INTO user VALUES ({}, '{}', '{}', NULL)".format(idi, username, first_name))
#         return self.connection.commit()
    
#     def user_check(self, user_id):
#         self.cursor.execute(f"SELECT * FROM user WHERE id = {user_id}")
#         data = self.cursor.fetchone()
#         return data



import sqlite3

class Translate():
    def __init__(self):
        self.connection = sqlite3.connect('bot.db')
        self.cursor = self.connection.cursor()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id integer,
            first_name varchar(65),
            user_name varchar(65)
        )""")
    def add_user(self,user_id,firstname, username):
        self.cursor.execute("INSERT INTO users VALUES ({},'{}','{}')".format(user_id, firstname, username))
        self.connection.commit()
    def user_exist(self, userid):
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_id = {userid}")
        data = self.cursor.fetchone()
        return data



