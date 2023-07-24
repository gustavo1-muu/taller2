import cx_Oracle
from conexion import Conexion
from tiquet import Tiquet
class TiquetDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def crear_tiquet(self, tiquet):
        query = '''
        INSERT INTO Tiquet (ID_UsuarioCreador, 
                            ID_UsuarioAsignado, 
                            ID_ClienteAsignado, 
                            ID_TipoTiquet,
                            ID_Criticidad, 
                            ID_AreaDestino, 
                            DetalleServicio, 
                            DetalleProblema, 
                            Estado,
                            Observacion 
                            )
        
        
        VALUES (:id_usuario_creador, 
                :id_usuario_asignado, 
                :id_cliente_asignado, 
                :id_tipo_tiquet,
                :id_criticidad, 
                :id_area_destino, 
                :detalle_servicio, 
                :detalle_problema, 
                :estado,
                :observacion)
        '''

        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query, tiquet.__dict__)
            self.conexion.getConexion().commit()
            print("Tiquet creado exitosamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al crear el tiquet: {e}")

    def ver_todos_los_tiquets(self):
        query = '''
            SELECT * FROM Tiquet
        '''
        
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            tiquets = []

            for row in cursor:
                tiquet = Tiquet(id_tiquet=row[0],
                                id_usuario_creador=row[1],
                                id_usuario_asignado=row[2],
                                id_cliente_asignado=row[3],
                                id_tipo_tiquet=row[4],
                                id_criticidad=row[5],
                                id_area_destino=row[6],
                                detalle_servicio=row[7],
                                detalle_problema=row[8],
                                estado=row[9],
                                observacion=row[10])
                tiquets.append(tiquet)

            return tiquets
        except cx_Oracle.DatabaseError as e:
            print(f"Error al ver los tiquets: {e}")
