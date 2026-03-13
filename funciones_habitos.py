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
        



def analizar_habitos (lista): 
    dicc_final={}
    for actividad in lista: 
     if actividad in dicc_final:
            dicc_final[actividad] += 1
     else:
            dicc_final[actividad] = 1

    return dicc_final 
 

