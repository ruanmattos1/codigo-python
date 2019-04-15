# -*- coding: utf-8 -*-

import socket, sys
import smtplib
from struct import *
myEmail = raw_input('Informe o seu email: ')
quant_max = input('Informe a quantidade de pacotes maximos: ')
endIp = raw_input('Informe o seu endereço Ip: ')
log = raw_input('Informe o arquivo de log.txt: ')

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)  # type: socket

except socket.error, msg:
    print 'Socket não pode ser criado' + str(msg[0]) + ' mensagem ' + msg[1]
    sys.exit()

i = 0
quant_sessao = 0

while True:
    print "------***-------PACOTES TCP DA DISNEY ", i, "------***-------"
    i = i + 1
    quant_sessao = quant_sessao + 1
    if (quant_sessao == quant_max):
        #ENVIAR EMAIL
        email = 'ruanmatossilva@gmail.com'
        senha = '16202428trucado'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, senha)
        mensagem = 'Foram processados ' + str(i) + ' Pacotes TCP\n'
        server.sendmail(email, myEmail, mensagem)
        server.quit()
        #CRIAÇÃO DO ARQUIVO DE LOG/ ESCRITA/ LEITURA
        arquivo = open(log, 'a')

        arquivo.write(str(mensagem))
        arquivo.close()

        arquivo = open(log, 'r')
        print arquivo.read()
        #PARTE DO CLIENTE
        for cont in range(1, quant_sessao):
            meuSocket = socket.socket()
            meuHost = socket.gethostname()
            minhaPorta = 12345

            meuSocket.connect((meuHost, minhaPorta))
            print meuSocket.recv(1024)
            meuSocket.close
        quant_sessao = 0
    pacote = s.recvfrom(65565)

