from usuarios import Usuario
from clientes import Clientes
from tipotiquet import TipoTiquet
from criticidad import Criticidad
from areas import Areas

class Tiquet:
    def __init__(self, id_tiquet, id_usuario_creador, id_usuario_asignado, id_cliente_asignado,
                 id_tipo_tiquet, id_criticidad, id_area_destino, detalle_servicio, detalle_problema,
                 estado, observacion):
        
        self.id_tiquet = id_tiquet
        self.id_usuario_creador = id_usuario_creador
        self.id_usuario_asignado = id_usuario_asignado
        self.id_cliente_asignado = id_cliente_asignado
        self.id_tipo_tiquet = id_tipo_tiquet
        self.id_criticidad = id_criticidad
        self.id_area_destino = id_area_destino
        self.detalle_servicio = detalle_servicio
        self.detalle_problema = detalle_problema
        self.estado = estado
        self.observacion = observacion
       
