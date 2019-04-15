# -*- coding: utf-8 -*-

import socket, sys
from struct import *

email = raw_input('Informe o seu email: ')
endIp = raw_input('Informe seu endereço IP: ')
nomeArquivo = raw_input('Informe o nome do arquivo LOG.txt: ')
qntPacotes = input('Informe a quantidade de pacotes maximos: ')

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)  # type: socket

except socket.error, msg:
    print 'Socket não pode ser criado' + str(msg[0]) + ' mensagem ' + msg[1]
    sys.exit()

i = 0
pacote = 0
qntTCP = 0
while True:

    print "------***-------PACOTE ", i, "------***-------"
    i = i + 1


    if pacote == pacote:
        qntTCP = qntTCP + 1
    elif pacote == qntPacotes:
        pacote = 0

print 'quantidade de pacotes TCP', qntTCP
