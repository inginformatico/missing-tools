#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################
# Nombre de aplicación: Chrome History Forensic Missing
# Descripcion: Aplicacion para encontrar pruebas del 
# paradero desconocido de una persona desaparecida a traves
# del historial de Google Chrome.
#
# Actualizado a python for windows 3.7
# Añadida posibilidad de pasar nombre fichero History como parametro -f
#
# Autor: Jorge Coronado @JorgeWebsec
# Autor: Enmanuel Donminguez @Xegami
# Autor: Juan Torres Ibañez @inginformatico
# Version: 2.0
# Licencia GNU v3
##############################################################

import sqlite3, datetime, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Nombre de archivo History")
args = parser.parse_args()

nr, nc, nh = 0, 0, 0
historyFile = 'History'
if args.file:
    historyFile = args.file

citys = ["albacete","alicante", "alacant", "almeria", "araba", "alava", "asturias", "avila", "badajoz", "balears", "beleares", "barcelona", "cataluna", "bizkaia", "burgos", "caceres", "cadiz", "cantabria", "castellon", "castello", "ciudad real", "cordoba", "coruna", "cuenca", "gipuzkoa", "girona", "granada", "guadalajara", "huelva", "huesca", "jaen", "leon", "lleida", "lugo", "madrid", "malaga", "murcia", "navarra", "ourense", "palencia", "literal", "palmas", "pontevedra", "rioja", "salamanca", "santa cruz de tenerife", "segovia", "sevilla", "soria", "tarragona", "teruel", "toledo", "valencia", "valladolid", "zamora", "zaragoza", "ceuta", "melilla"]

connection = sqlite3.connect(historyFile,  timeout=10)
cursor=connection.cursor()

def sqlite_select_Travel_ES(data):
	global nh
	cursor.execute("SELECT * FROM urls WHERE title LIKE ?", ("%"+data+"%",))
	for row in cursor:
		nh += 1
		datas = row[1], row[2], row[5]
		print ("\n**[" + str(nh) + "]", "Hoteles/Viajes...")
		print ("**URL:", datas[0])
		print ("**TITLE:", datas[1].encode('utf-8'))
		print ("**DATE:", datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=datas[2]))

def sqlite_select_RRSS_ES(data):
	global nr
	cursor.execute("SELECT * FROM urls WHERE url LIKE ?", ("%"+data+"%",))
	for row in cursor:
		nr += 1
		datas = row[1], row[2], row[5]
		print ("\n[" + str(nr) + "]", "Redes Sociales...")
		print ("URL:", datas[0])
		print ("TITLE:", datas[1].encode('utf-8'))
		print ("DATE:", datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=datas[2]))

def sqlite_select_City_ES(data):
	global nc
	cursor.execute("SELECT * FROM urls WHERE title LIKE ?", ("%"+data+"%",))
	for row in cursor:
		nc += 1
		datas = row[1], row[2], row[5]
		print (datas)
		print ("\n[" + str(nc) + "]", "Ciudades...")
		print ("URL:", datas[0])
		print ("TITLE:", datas[1].encode('utf-8'))
		print ("DATE:", datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=datas[2]))

def get_info():
	sqlite_select_Travel_ES("hotel")
	sqlite_select_Travel_ES("viaj")
	sqlite_select_Travel_ES("autobus")
	sqlite_select_Travel_ES("pension")
	sqlite_select_Travel_ES("hostal")
	sqlite_select_Travel_ES("reserv")
	for c in citys:
		print (c)
		sqlite_select_City_ES(c)
	sqlite_select_RRSS_ES("facebook.com")
	sqlite_select_RRSS_ES("instagram.com")
	sqlite_select_RRSS_ES("blablacar.com")
	sqlite_select_RRSS_ES("twitter.com")
	cursor.close()

def main():
	get_info()
	print ("\n>>>\n\nTotal de redes sociales:", nr)
	print ("Total de ciudades:", nc)
	print ("Total de hoteles/viajes:", nh)

if __name__ == "__main__":
	main()
