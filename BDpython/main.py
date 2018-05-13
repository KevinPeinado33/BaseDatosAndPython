# -*- coding: utf-8 -*-
__author__ = 'dbquebin'
import cx_Oracle

from util import util

db = util()

"""

"""
def registrarUsuario():#metodo para el regitro de usuarios nuevos
	print("\nRegistro de nuevo Usuario: ")
	pregunta=str(input("\n¿Desea registarse con facebook? "))
	if pregunta == "si":
		#aqui entrara la API de facebook
		print("hola")
	elif pregunta == "no":
		print("\nRellene sus datos personales: ")
		nombres = str(input("\nNombre: "))
		apellidos = str(input("Apellidos: "))
		edad = int(input("edad:"))
		if edad > 18:
			correo = str(input("correo electronico: "))
			contraseña = str(input("Contraseña: "))
			sexo = str(input("Sexo: */masculino ó femenino/* "))
			telefono = str(input("Numero Telefono: "))
			#insertamos los datos a la bd
			QUERY = 'insert into persona (nombres, apellidos, edad, sexo, telefono, id_persona) values (:nombres, :apellidos, :edad, :sexo, :telefono, :id_persona)'
			res = db.query_otro(QUERY, (nombres, apellidos, edad, sexo, telefono, 'null'))

			#QUERYK = 'insert into usuario (correo, contraseña, id_usuario, persona_id_persona) values(:correo, :contraseña, :id_usuario, :persona_id_persona)'
			#resk = db.query_otro2(QUERYK, (correo, contraseña, 'null', 'null'))

		elif edad < 18:
			print("Usted no puede crear una cuenta por temas de politica")

def iniciarSesion():#metodo para logearse desde cualquier usuario
	print("\nBienvenido")
	usu = str(input("\tCorreo: "))
	cont = str(input("\tContraseña: "))
	#consulta sql para el incio de sesion
	if usu == 'bd' and cont == 'bd':
		print("correcto")
	else:
		print("Incorrecto")

def informacionEmpresa():#info de la empresa
	print("Informacion de la empresa Derechos reservados")


def menuPrincipal():
	print("""

		**************************************************
		* 1) Ver lista de amigos
		* 2) Publicar Nuevo Envento
		* 3) otra funcion
		* 4) Salir
		**************************************************
		""")


def menuIncio():#menu de incio
	print("""
		***************************************************
		*  1) Crear Cuenta
		*  2) Inciar Sesion
		*  3) Informacion de la Red Social
		*  4) Salir
		***************************************************
		""")
	opcion = int(input("Ingrese su opcion: "))
	while opcion > 4:
		opcion = int(input("Ingrese su opcion: "))
		if opcion == 1:
			registrarUsuario()
		elif opcion == 2:
			iniciarSesion()
		elif opcion == 3:
			informacionEmpresa()
		elif opcion == 4:
			print("\tUsted salio :'(")

#ejecucion del main principal
if __name__ == '__main__':#con esto ejecuto el main principal

	menuIncio()
	
