import cx_Oracle

class Conexion:

    def __init__(self):

       # cx_Oracle.init_oracle_client(lib_dir=r"c:\instantclient_21_10") 

        self.__connection = cx_Oracle.connect(user="gustavo", password=".Inacap2023.", dsn="dbtaller_high")

        self.__cursor = self.__connection.cursor()



    def getConexion(self):

        return self.__connection



    def getCursor(self):

        return self.__cursor



    def cerrarConexion(self):
      if self.__cursor is not None:
          self.__cursor.close()
      if self.__connection is not None:
            self.__connection.close()
