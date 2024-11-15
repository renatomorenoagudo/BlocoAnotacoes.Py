#!usr/Scriptenv python

""""BLOCO DE NOTAS

$notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read tech
'''
'''
"""
__version__ = "0.1.0"

import os
import sys
cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage"),
    print(f"you mus specify subcomand")
    sys.exit(1)


if arguments[0] not in cmds:
    print("Invalid command {argument[0]}")

if arguments[0] == "read":
    #leitura das notas
    pass
    #for line open(filepath):
      #  title, tag, text = line.split("\t")
       # if tag.lower()  == 

if arguments[0] == "new":
    titulo = arguments [1]  #TODO: tratar exception
    text = [
        f"{titulo}",
        input ("tag:").strip(), 
        input ("text:\n").strip(),
    ]
    # \t - tsv
    with open (filepath, "a") as file_:
        file_.write("\t".join(text))
