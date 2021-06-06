""" Modulo Ciclos
    Funciones para practicas con ciclos
    Yenifer Barco Castrillón
    junio 06-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def simulador_caida_libre(altura):
    """ 
    Parameters
    ----------
    altura:float
        valor de la altura en metros
    Return:
    -------
   
    """  
    distancia=0
    gravedad=9.8
    tiempo=0
    if altura>0:
        while distancia<=altura:
            distancia=(1/2)*gravedad*(tiempo**2)
            print("t=",tiempo,"seg","\td=",distancia,"m")
            tiempo+=1
        
def generador_generaciones(generacion):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"

def constructor_triangulos(pisos):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"

def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"