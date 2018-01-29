#!/usr/bin/python
# -*- coding: utf-8 -*-

#Created by: @cayohollanda
#github.com/cayohollanda

#API's utilizadas
import os
import ConfigParser
from os.path import expanduser

#Coletando informacoes
os.system("clear")
print("[ ==== REMOTE ACCESS ==== ]")
usuarioLocal = raw_input("[?] Digite o usuário que se conectará -> ")
senhaLocal = raw_input("[?] Digite a senha do usuário -> ")
resolucaoLocal = raw_input("[?] Digite a resolução a ser usada -> ")
ipLocal = raw_input("[?] Digite o endereço de acesso -> ")
fullscreenLocal = raw_input("[?] Fullscreen? (0=N/1=S) -> ")

#Definindo o /home para pegar a pasta RemoteAccess
home = expanduser("~")

#Abrindo Remoto.ini para setar variaveis
config = ConfigParser.ConfigParser()
config.read("%s/RemoteAccess/Remoto.ini"%(home))

#Abrindo open para aplicar as alteracoes apos setar
cfgfile = open("%s/RemoteAccess/Remoto.ini"%(home), "w")

#Setando as variaveis
config.set("Config", "USUARIO", usuarioLocal)
config.set("Config", "SENHA", senhaLocal)
config.set("Config", "RESOLUCAO", resolucaoLocal)
config.set("Config", "IP", ipLocal)
config.set("Config", "FULLSCREEN", fullscreenLocal)
#Escrevendo
config.write(cfgfile)

#Chamando o .Atalho.py para poupar tempo de quem estiver instalando
os.system("clear")
print("[?] Por favor, insira a senha do usuário abaixo...")
os.system("sudo python .Atalho.py %s"%(home))

