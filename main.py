""" Modulo Ciclos
    Funciones para practicas con ciclos
    Yenifer Barco Castrillón
    junio 06-2021 """

#---------------- Zona librerias------------
import funciones_ciclos as fc

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#Llamado de la funcion de caida libre
altura = float(input("Por favor ingrese la altura:"))
fc.simulador_caida_libre(altura)

#Llamado de la fncion de generador de generaciones
generacion= int(input("\nIngrese el numero de la generación:"))
total_personas=fc.generador_generaciones(generacion)
print("Total de personas en la familia hasta ahora:",total_personas)

#Llamado de la fncion de constructor de triangilos
pisos = int(input("\nPor favor ingrese el número de pisos:"))
fc.constructor_triangulos(pisos)

#Llamado de la fncion de constructor de tableros
longitud=int(input("\nIngrese la longitud del tablero:"))
fc.constructor_tableros(longitud)

