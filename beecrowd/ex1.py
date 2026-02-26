# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
hora_inicial = int(input('Hora inicial: ')) 
minuto_inicial = int(input('Minuto inicial: '))
hora_final = int(input('Hora final: ')) 
minuto_final = int(input('Minuto final: '))

"""
1 hora = 60 min
24hora = 
"""

duracao_min = 1
duracao_maxima = 24

duracao_horas = hora_final - hora_inicial

if minuto_inicial > minuto_final:
    duracao_minutos = minuto_inicial - minuto_final
else:
    duracao_minutos = minuto_final - minuto_inicial
    
print(f'O jogo durou {duracao_horas} horas(s) e {duracao_minutos} minutos(s)')