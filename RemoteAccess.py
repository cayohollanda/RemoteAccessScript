#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Created by: @cayohollanda
#github.com/cayohollanda

import os
import ConfigParser
from os.path import expanduser

#Abrindo arquivo
home = expanduser("~")
config = ConfigParser.ConfigParser()
config.read("%s/RemoteAccess/Remoto.ini"%(home))

#Verificando credenciais e guardando em variaveis (se nao existir o Remoto, caira no except)
try:
	usuario = config.get("Config", "USUARIO")
	senha = config.get("Config", "SENHA")
	resolucao = config.get("Config", "RESOLUCAO")
	ip = config.get("Config", "IP")
	fullscreen = config.get("Config", "FULLSCREEN")
except:
	print("Erro ao achar sessão Config no arquivo Remoto.ini");
	exit(0)

#Verificando se o Remoto.ini ainda esta com as configuracoes padroes
if usuario == "" or senha == "" or resolucao == "" or ip == "":
	print("Verifique se as informações foram informadas no arquivo Remoto.ini");
	exit(0)

#Verificando se e pra ser fullscreen e executando
if fullscreen == "1":
	conexao = os.system("rdesktop -u %s -p %s -f -T Acesso\ Remoto %s" %(usuario, senha, ip))
elif fullscreen == "0":
	conexao = os.system("rdesktop -u %s -p %s -g %s -T Acesso\ Remoto %s" %(usuario, senha, resolucao,  ip))
else:
	print("Informação de Fullscreen não foi informada");
	exit(0)

#Se essa condicao for verdadeira, e porque o endereco do RDP foi informado incorretamente ou está sem internet
if conexao == 19456:
	print("Endereço incorreto.");
