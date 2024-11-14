#!usr/Scriptenv python

""""BLOCO DE NOTAS

$notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
'''
'''
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print("Invalid command {argument[0]}")

if arguments[0] == "read":
    #leitura das notas

if arguments[0] == "new":
    titulo = arguments [1]  #TODO: tratar exception
    #criação da nota