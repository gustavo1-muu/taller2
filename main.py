import cx_Oracle
from beautifultable import BeautifulTable
from conexion import Conexion
from dao.usuariosdao import UsuarioDAO
from dao.tiquetdao import TiquetDAO
from tiquet import Tiquet


def main():
    usuario_dao = UsuarioDAO()
    tiquet_dao = TiquetDAO(Conexion())

    print("\n\nBienvenido al sistema de usuarios")
    nombre_usuario = input("Nombre de usuario: ")
    contrasena_usuario = input("Contrasena: ")


    if usuario_dao.verificar_usuario(nombre_usuario, contrasena_usuario) == 1:
        print("\n¡Bienvenido Administrador!\n")
        
        opcion =""
        while opcion not in ["1", "2", "3", "4"]:
            
            print("1. Crear Tiquet")
            print("2. Ver Tiquets")
            print("3. Ver Empleados")
            print("4. Salir")
            opcion = input("\n\n¿Que quieres hacer?\n\n\n")

            if opcion == "1":
               usuarioAsignado = int(input("Escribe el ID al usuario que le quieres asignar este tiquet: \n"))
               clienteAsignado = int(input("Escribe el ID al cliente que le quieres asignar este tiquet: \n"))
               TipoTiquet = int(input("¿Que tipo de tiquet quieres crear?:\n1. Felicitación\n2. Consulta\n3. Reclamo\n4. Problema\n"))
               Criticidad = int(input("¿Que criticidad le quieres asignar?\n1. Baja\n2. Media\n3. Alta\n4. Crítica\n"))
               Area = int(input("¿Que área de destino le quieres asignar?\n1. Soporte Técnico\n2. Atención Al Cliente\n3. Gestión de Incidencias\n4. Servicio de consultas\n"))
               Detalle = str(input("Escribe el detalle del servicio: \n"))
               DetalleProblemas = str(input("Escribe el detalle del problema: \n"))
               Observacion = str(input("Escribe la observación: \n")) 
               

               tiquet = Tiquet(
                id_tiquet=None,
                id_usuario_creador=1,
                id_usuario_asignado=usuarioAsignado,
                id_cliente_asignado=clienteAsignado,
                id_tipo_tiquet=TipoTiquet,
                id_criticidad=Criticidad,
                id_area_destino=Area,
                detalle_servicio=Detalle,
                detalle_problema=DetalleProblemas,
                estado=1,
                observacion=Observacion,
                )
               tiquet_dao.crear_tiquet(tiquet)

            elif opcion == "2":
                tiquets = tiquet_dao.ver_todos_los_tiquets()
                for tiquet in tiquets:
                    print(f"ID Tiquet: {tiquet.id_tiquet}")
                    print(f"ID Usuario Creador: {tiquet.id_usuario_creador}")
                    print(f"ID Usuario Asignado: {tiquet.id_usuario_asignado}")
                    print(f"ID Cliente Asignado: {tiquet.id_cliente_asignado}")
                    print(f"ID Tipo Tiquet: {tiquet.id_tipo_tiquet}")
                    print(f"ID Criticidad: {tiquet.id_criticidad}")
                    print(f"ID Área Destino: {tiquet.id_area_destino}")
                    print(f"Detalle de Servicio: {tiquet.detalle_servicio}")
                    print(f"Detalle de Problema: {tiquet.detalle_problema}")
                    print(f"Estado: {tiquet.estado}")
                    print(f"Observación: {tiquet.observacion}")
                    print("-------------------------------------")
            elif opcion == "3":
               usuario_dao.mostrar_usuarios()
            elif opcion == 4:
               break 
        

    elif usuario_dao.verificar_usuario(nombre_usuario, contrasena_usuario) == 2:
        print("\n¡Bienvenido Usuario!")

        opcion =""
        while opcion not in ["1", "2", "3"]:
            print("\n\n¿Que quieres hacer?")
            print("1. Crear Tiquet")
            print("2. Ver Mis Tiquets")
            print("3. Salir")
            opcion = input("\n\n¿Que quieres hacer?\n\n\n")

            if opcion == "1":
               pass
            elif opcion == "2":
                tiquets = tiquet_dao.ver_todos_los_tiquets()
                for tiquet in tiquets:
                    print(f"ID Tiquet: {tiquet.id_tiquet}")
                    print(f"ID Usuario Creador: {tiquet.id_usuario_creador}")
                    print(f"ID Usuario Asignado: {tiquet.id_usuario_asignado}")
                    print(f"ID Cliente Asignado: {tiquet.id_cliente_asignado}")
                    print(f"ID Tipo Tiquet: {tiquet.id_tipo_tiquet}")
                    print(f"ID Criticidad: {tiquet.id_criticidad}")
                    print(f"ID Área Destino: {tiquet.id_area_destino}")
                    print(f"Detalle de Servicio: {tiquet.detalle_servicio}")
                    print(f"Detalle de Problema: {tiquet.detalle_problema}")
                    print(f"Estado: {tiquet.estado}")
                    print(f"Observación: {tiquet.observacion}")
                    print("-------------------------------------")
                    
            elif opcion == "3":
               break

    elif usuario_dao.verificar_usuario(nombre_usuario, contrasena_usuario) == 3:
        print("¡Usuario no válido!")    
if __name__ == "__main__":
    main()