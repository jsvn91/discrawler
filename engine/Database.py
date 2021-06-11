import mysql.connector
from mysql.connector import Error

class Database():

   __instance = None

   @staticmethod
   def getInstance(self):
      """ Static access method. """
      if Database.__instance == None:
         Database()
      return Database.__instance

   def __init__(self):

      self.conn,self.curr = self.connect()

      """ Virtually private constructor. """
      # if Database.__instance != None:
      #    raise Exception("This class is a singleton!")
      # else:
      #    Database.__instance = self

   def connect(self):
      """ Connect to MySQL database """

      conn = None
      try:
         conn = mysql.connector.connect(host='localhost',
                                        database='db_discrawler',
                                        user='root',
                                        password='2410')
         cur = conn.cursor()
         if conn.is_connected():
            print('Connected to MySQL database')

      except Error as e:
         print(e)
         return None

      return conn,cur

