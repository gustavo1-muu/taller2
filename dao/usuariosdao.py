import cx_Oracle
from conexion import Conexion
from usuarios import Usuario

class UsuarioDAO:
    def __init__(self):
        self.conexion = Conexion()

    def insertar_usuario(self, usuario):
        query = '''
            INSERT INTO usuarios (id_usuario, nombre, contrasena, tipo_usuario)
            VALUES (:id_usuario, :nombre, :contrasena, :tipo_usuario)
        '''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query, usuario.__dict__)
            self.conexion.getConexion().commit()
            print("Usuario insertado exitosamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al insertar usuario: {e}")


    def eliminar_usuario(self, id_usuario):
        query = '''
            DELETE FROM usuarios WHERE id_usuario = :id_usuario
        '''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query, {"id_usuario": id_usuario})
            self.conexion.getConexion().commit()
            print("Usuario eliminado exitosamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al eliminar usuario: {e}")


    def editar_usuario(self, usuario):
        query = '''
            UPDATE usuarios 
            SET nombre = :nombre, contrasena = :contrasena, tipo_usuario = :tipo_usuario
            WHERE id_usuario = :id_usuario
        '''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query, usuario.__dict__)
            self.conexion.getConexion().commit()
            print("Usuario editado exitosamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al editar usuario: {e}")         


    def mostrar_usuarios(self):
        query = '''
            SELECT * FROM usuarios
        '''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Contraseña: {usuario[2]}, Tipo de Usuario: {usuario[3]}")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar usuarios: {e}")         

     
    def verificar_usuario(self, nombre, contrasena):
        query = '''
            SELECT * FROM usuarios WHERE nombre = :nombre AND Contraseña = :contrasena
        '''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query, {"nombre": nombre, "contrasena": contrasena})
            usuario = cursor.fetchone()
            if usuario:
                usuario_obj = Usuario(id_usuario=usuario[0], nombre=usuario[1], contrasena=usuario[2], tipo_usuario=usuario[3])
                if usuario_obj.tipo_usuario == 'administrador':
                    print("\n¡Usuario válido!")
                    return 1
                elif usuario_obj.tipo_usuario == 'usuario':
                    print("\n¡Usuario válido!")
                    return 2
                else:
                    return 3
            else:
                print("Nombre de usuario o contraseña incorrectos.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al verificar el usuario: {e}")