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

            if distancia>altura:
                break
            else:
               print("t=",tiempo,"seg","\td=",distancia,"m")
            tiempo+=1
    else:
        print("Ingrese un valor mayor a cero para la altura")
        
def generador_generaciones(generacion):
    """ 
    Parameters
    ----------
    generacion:float
        valor de el numero de la generacion de la familia
    Return:
    -------
    total_personas:int
        valor total de las personas que han habido en la familia segun las generaciones
    """  
    generaciones=0 #numero de la generacion en la que va el ciclo
    personas=1 #numero de personas por generacion
    total_personas=1
    if generacion >=0:

        while generaciones<=generacion:
            if generaciones==0:
                personas=personas
            else:
                personas=personas*2
            
            #suma la cantidad de personas que va calculando
            total_personas=total_personas+personas
            print("generacion:",generaciones,"Personas:",personas)
            generaciones+=1
    else:
        print("Por favor ingrese desde la generacion 0 en adelante")
    return total_personas

def constructor_triangulos(pisos):
    """ 
    Parameters
    ----------
    pisos:int
        numero de pisos que tendra el triangulo
    Return:
    -------

    """
    numero_piso=1 #cuenta el numero del piso
    numero=0 #sumando los numeros
    salto=1 #cuenta en que punto debe hacer el salto

    if pisos >0:
        while numero_piso<=pisos:
            numero=numero+1
            print(numero,end=" ")#Imprime varios print en la misma linea
            
            #Compruena si el salto y el numero de pisos es diferente, ya que si son iguales se hace el sato de linea
            if salto!=numero_piso:
                salto+=1
            else:
                print("\n")
                salto=1
                numero_piso+=1
    else:
        print("Ingrese un valor mayor a cero")


def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"