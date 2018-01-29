#!/usr/bin/python
# -*- coding: utf-8 -*-

#Created by: @cayohollanda
#github.com/cayohollanda

import os
import sys

os.system("clear")

if sys.argv < 1:
	print("[-] Erro na sintaxe de execução, por favor, use a sintaxe: python .Atalho.py [nomeDoUsuário]")
	exit(0)

home = sys.argv[1]

#Criando (ou sobrescrevendo) o atalho
print("[!] Configurando atalho...")
atalho = open("/usr/share/applications/remoteaccess.desktop", "w")
atalho.write("[Desktop Entry]\nName=Remote Access\nComment=Abrir o Acesso\nExec=%s/RemoteAccess/RemoteAccess\nIcon=%s/RemoteAccess/icone.bmp\nType=Application"%(home, home))
atalho.close()
print("[+] Atalho criado com sucesso!")

#Enviando o atalho p/ area de trabalho
print("[!] Enviando atalho para área de trabalho...")
try:
	os.system("cp /usr/share/applications/remoteaccess.desktop /%s/Desktop/remoteaccess.desktop || cp /usr/share/applications/remoteaccess.desktop /%s/Área\ de\ trabalho/remoteaccess.desktop || cp /usr/share/applications/remoteaccess.desktop /%s/Área\ de\ Trabalho/remoteaccess.desktop"%(home, home, home))
	print("[!] Apesar do erro acima, verifique se o ícone chegou na área de trabalho, caso não tenha chegado, envie-o manualmente.")
except:
	print("[-] Ocorreu um erro ao enviar o atalho para a área de trabalho, por favor, envie manualmente.")

os.system("clear")
os.system("sudo apt-get install rdesktop")

os.system("clear")
print("[+] Instalação concluída com sucesso! Verifique a Área de Trabalho.")
print("[+] @cayohollanda - github.com/cayohollanda")
