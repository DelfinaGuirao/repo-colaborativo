def analizar_habitos (lista): 
    dicc_final={}
    for actividad in lista: 
     if actividad in dicc_final:
            dicc_final[actividad] += 1
     else:
            dicc_final[actividad] = 1
    return dicc_final 