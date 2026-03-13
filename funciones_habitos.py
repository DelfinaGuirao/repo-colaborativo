"""
def registrar_habitos(lista):

    Recorrer los ingresos del usuario y crear una lista con las actividades ingresadas.
   
    Args:
        No recibe parametros
    
    Returns:
        lista_habitos(list): una lista con las actividades ingresadas por el usuario
    """    

def registrar_habitos():
   lista_habitos=[]
   actividades = input("Ingrese las actividades: ")
   lista_habitos.append(actividades)
  
   while True:
        actividades_agregadas = input("Desea seguir agregando?: ")
      
        if actividades_agregadas == "si":
          actividades = input("Ingrese las actividades: ") 
          lista_habitos.append(actividades)
    
        elif actividades_agregadas == "no":
             break 
   return lista_habitos
        


"""

def analizar_habitos (lista):

   Recorrer una lista con actividades y crear un diccionario donde cada clave sea cada actividad y cada valor las veces que aparece esa actividad en la lista
   
   Args:
       lista(list): es una lista con actividades a clasificar
      
    Returns:
        dicc_final(diccionario): un diccionario con la actividad como clave y la cantidad de veces que aparece en la lista como valor

    """

def analizar_habitos (lista): 
    dicc_final={}
    for actividad in lista: 
     if actividad in dicc_final:
            dicc_final[actividad] += 1
     else:
            dicc_final[actividad] = 1

    return dicc_final 
 

