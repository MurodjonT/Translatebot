import sqlite3


class Sql:
	def __init__(self):
		self.connection = sqlite3.connect('bot.db')
		self.cursor = self.connection.cursor()
	


	def baza_create(self):
		self.cursor.execute("""CREATE TABLE IF not exists user(
        id integer,
        firstname varchar(24),
        username varchar(24),
        tel integer NULL
		)""")



	def user_add(self, idi, username, first_name):
		self.cursor.execute("INSERT INTO user VALUES ({}, '{}', '{}', NULL)".format(idi, username, first_name))
        return self.connection.commit()
    
    def user_check(self, user_id):
        self.cursor.execute(f"SELECT * FROM user WHERE id = {user_id}")
        data = self.cursor.fetchone()
        return data



