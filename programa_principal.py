# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:22:47 2026

@author: delfi
"""
import funciones_habitos

lista = funciones_habitos.registrar_habitos()

resultado = funciones_habitos.analizar_habitos(lista)

print("Resumen de actividades:")
print(resultado)