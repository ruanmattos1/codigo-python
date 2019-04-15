# -*- coding: utf-8 -*-

import socket, sys, smtplib
from struct import *

myEmail = raw_input('Informe o seu email: ')
quant_max = input('Informe a quantidade maxima de pacotes por sessão: ')

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error, msg:
    print 'Socket não pode ser criado' + str(msg[0]) + ' Mensagem ' + msg[1]
    sys.exit()

i = 0
quant_sessao = 0

while True:
    print "------***PACOTE", i, "------***-------"
    i = i + 1
    quant_sessao = quant_sessao + 1
    if quant_sessao == quant_max:
        email = 'ruanmatossilva@gmail.com'
        senha = '16202428trucado'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, senha)
        mensagem = 'Foram processados ' + str(i) + 'Pacotes TCP'
        server.sendmail(email, myEmail, mensagem)
        server.quit()
        for cont in range(1, 2):
            meuSocket = socket.socket()
            meuHost = socket.gethostname()
            minhaPorta = 12345

            meuSocket.connect((meuHost, minhaPorta))
            print meuSocket.recv(1024)
            meuSocket.close
        quant_sessao = 0
    pacote = s.recvfrom(65565)





