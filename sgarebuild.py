import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm 
from colorama import Fore

"""""

codigos = [Rebuild(1), Rebuild(2), Rebuild(3)]

for codigo in codigos:
    print(Rebuild.get_codigo(codigos))

"""""
print(Fore.GREEN +"") 
print("================================ BEM VINDO ======================================")
print("================================ SGA REBUILD ====================================")
print("============================== VERSÃO 1.1.4 =====================================")
for i in tqdm (range (100),
                colour='CYAN',
               desc="Iniciando...",
               ascii=False, ncols=80):
               time.sleep(0.01)
print('\n')

class Rebuild:
    #GRV-EST06
    #Erro [ )] ou [9/041] no arquivo SAIDA      na rotina GRV-EST06
    def gvr_est06():
        codigo = 1
        print(" rebuild -d -e SGC016,TESTE \n rebuild -d -e TESTE,SGC016 \n rebuild -d -e SGC024,TESTE \n rebuild -d -e TESTE,SGC024")
        return codigo
    
    #Erro [ )] ou [9/041] no arquivo VENDITENS  na rotina GRV-ITENS 
    def grv_itens():
        codigo = 2
        print(" rebuild -d -e SGC065,TESTE \n rebuild -d -e TESTE,SGC065 \n rebuild -d -e SGC066,TESTE \n rebuild -d -e TESTE,SGC066 \n rebuild -d -e SGC067,TESTE \n rebuild -d -e TESTE,SGC06")

    #Erro [ )] ou [9/041] no arquivo ENTRADA    na rotina GRAVA.
    def grava():
        codigo = 3
        print(" rebuild -d -e SGC044,TESTE \n rebuild -d -e TESTE,SGC044 ")
    
    #Erro [ )] ou [9/041] no arquivo no arquivo QUITADO NA ROTINA GR
    def quitado():
        codigo = 4
        print(" rebuild -d -e SGC024,TESTE \n rebuild -d -e TESTE,SGC024 \n rebuild -d -e SGC025,TESTE \n rebuild -d -e TESTE,SGC025 \n rebuild -d -e SGC026,TESTE \n rebuild -d -e TESTE,SGC026 ")
    #===========================================================================================
    #Erro [ ) ] ou [9/041] no arquivo CCFISCAL na rotina LE-ARQRET .
    def ccfiscal():
        print(' rebuild -d -e SGC904,TESTE \n rebuild -d -e TESTE,SGC904')
        
    #Erro [ )] ou [9/041] no arquivo VENDDUP    na rotina CALCULO
    def venddup():
        print(' rebuild -d -e SGC065,TESTE \n rebuild -d -e TESTE,SGC065 \n rebuild -d -e SGC066,TESTE \n rebuild -d -e TESTE,SGC066 \n rebuild -d -e SGC067,TESTE \n rebuild -d -e TESTE,SGC067')
    
    #Erro [ )] ou [9/041] no arquivo SAIDA      na rotina TST-SAI01
    def saida_tstsai01():
        print(' rebuild -d -e SGC016,TESTE \n rebuild -d -e TESTE,SGC016')
    
    #Erro [ )] ou [9/041] no arquivo COMISSAO   na rotina GRV-COM02
    def comissao():
        print(' rebuild -d -e SGC018,TESTE \n rebuild -d -e TESTE,SGC018')
    
    #Erro [ )] ou [9/041] no arquivo RECIBO
    def recibo():
        print(' rebuild -d -e SGC025,TESTE \n rebuild -d -e TESTE,SGC025 \n rebuild -d -e SGC026,TESTE \n rebuild -d -e TESTE,SGC026')

    #Erro [ )] ou [9/041] no arquivo ENTRADA na rotina LE-ENT
    def entrada():
        print(' rebuild -d -e SGC039,TESTE \n rebuild -d -e TESTE,SGC039 \n rebuild -d -e SGC040,TESTE \n rebuild -d -e TESTE,SGC040 \n rebuild -d -e SGC044,TESTE \n rebuild -d -e TESTE,SGC044')
    
    #Erro [ )] ou [9/041] no arquivo BALANCO    na rotina MES-ANO
    def balanco():
        print(' rebuild -d -e SGC102,TESTE \n rebuild -d -e TESTE,SGC102')
        
    #Erro [ )] ou [9/041] no arquivo SAIDA      na rotina GRV-ITC
    def saida_grvitc():
        print(' rebuild -d -e SGC016,TESTE \n rebuild -d -e TESTE,SGC016')
    
    #Erro [ )] ou [9/041] no arquivo VENDDOC    na rotina GRV-DOC3
    def venddoc():
        print(' rebuild -d -e SGC065,TESTE \n rebuild -d -e TESTE,SGC065 \n rebuild -d -e SGC066,TESTE \n rebuild -d -e TESTE,SGC066 \n rebuild -d -e SGC067,TESTE \n rebuild -d -e TESTE,SGC067')
    
    #Erro [ )] ou [9/041] no arquivo ECF60M     na rotina INICIO
    def ecf60m():
        print(' rebuild -d -e SGC080,TESTE \n rebuild -d -e TESTE,SGC080 \n rebuild -d -e SGC081,TESTE \n rebuild -d -e TESTE,SGC081')
    
    #Erro [ )] ou [9/041] no arquivo MOVBCO na rotina GRV-MOVBCO
    def movbco():
        print(' rebuild -d -e SGC035,TESTE \n rebuild -d -e TESTE,SGC035 \n rebuild -d -e SGC036,TESTE \n rebuild -d -e TESTE,SGC036')
    
    #Erro [ )] ou [9/041] no arquivo NTFILES na rotina INI-VND
    def ntfiles():
        print(' rebuild -d -e SGC802,TESTE \n rebuild -d -e TESTE,SGC802')
    
    #Erro [ +] ou [9/043] no arquivo CICF       na rotina INICIO
    def cicf():
        print(' Remover os arquivos :\n SGC083BKP \n SGC083.idx')
            
#a = [ Rebuild.gvr_est06, Rebuild.grv_itens ,Rebuild.grava ,Rebuild.quitado]
#0123
print(Fore.GREEN +"")

def menu():
    print('==================== MENU ===================')
    print('Comando para reogarnizar os arquivos de saída')
    print('|===========================================|')
    print("|        Escolha a Opção                    |")
    print('|  SAIDA                                    |')
    print('|  VENDITENS                                |')
    print('|  GRAVA                                    |')
    print('|  QUITADO                                  |')
    print('|  CCFISCAL                                 |')
    print('|  VENDDUP                                  |')
    print('|  SAIDATSTSAI01                            |')
    print('|  COMISSAO                                 |')
    print('|  RECIBO                                   |')
    print('|  ENTRADA                                  |')
    print('|  BALANCO                                  |')
    print('|  SAIDA-GRV-ITC                            |')
    print('|  VENDDOC                                  |')
    print('|  ECF60M                                   |')
    print('|  MOVBCO                                   |')
    print('|  NTFILES                                  |')
    print('|  CICF                                     |')
    print("|  SAIR                                     |")
    print("============================================|")
menu()    
p  = str(input(' Digite a opção do Menu  : '))


def pesquisa():
   if p == 'SAIDA':
        print(' Erro [ )] ou [9/041] no arquivo SAIDA      na rotina GRV-EST06')
        Rebuild.gvr_est06()
   elif p == 'VENDITENS':
        print(' Erro [ )] ou [9/041] no arquivo VENDITENS  na rotina GRV-ITENS ')
        Rebuild.grv_itens()
   elif p == 'GRAVA':
       print(' Erro [ )] ou [9/041] no arquivo ENTRADA    na rotina GRAVA')
       Rebuild.grava()

   elif p == 'QUITADO':
       print(' Erro [ )] ou [9/041] no arquivo no arquivo QUITADO NA ROTINA GR')
       Rebuild.quitado()
       
   elif p == 'CCFISCAL':
       print(' Erro [ ) ] ou [9/041] no arquivo CCFISCAL na rotina LE-ARQRET')
       Rebuild.ccfiscal()

   elif p == 'VENDDUP':
        print(' Erro [ )] ou [9/041] no arquivo VENDDUP    na rotina CALCULO')
        Rebuild.venddup()

   elif p == 'SAIDATSTSAI01':
        print(' Erro [ )] ou [9/041] no arquivo SAIDA      na rotina TST-SAI01')
        Rebuild.saida_tstsai01()

   elif p == 'COMISSAO':
        print(' Erro [ )] ou [9/041] no arquivo COMISSAO   na rotina GRV-COM02')
        Rebuild.comissao()

   elif p == 'RECIBO':
        print(' Erro [ )] ou [9/041] no arquivo RECIBO')
        Rebuild.recibo()

   elif p == 'ENTRADA':
        print(' Erro [ )] ou [9/041] no arquivo ENTRADA na rotina LE-ENT')
        Rebuild.entrada()

   elif p == 'BALANCO':
        print(' Erro [ )] ou [9/041] no arquivo BALANCO    na rotina MES-ANO')
        Rebuild.balanco()

   elif p == 'SAIDA-GRV-ITC':
        print(' Erro [ )] ou [9/041] no arquivo SAIDA      na rotina GRV-ITC')
        Rebuild.saida_grvitc()

   elif p == 'VENDDOC':
        print(' Erro [ )] ou [9/041] no arquivo VENDDOC    na rotina GRV-DOC3')
        Rebuild.venddoc()

   elif p == 'ECF60M':
        print(' Erro [ )] ou [9/041] no arquivo ECF60M     na rotina INICIO')
        Rebuild.ecf60m()

   elif p == 'MOVBCO':
        print(' Erro [ )] ou [9/041] no arquivo MOVBCO na rotina GRV-MOVBCO')
        Rebuild.movbco()

   elif p == 'NTFILES':
        print(' Erro [ )] ou [9/041] no arquivo NTFILES na rotina INI-VND')
        Rebuild.ntfiles()

   elif p == 'CICF':
        print(' Erro [ +] ou [9/043] no arquivo CICF       na rotina INICIO')
        Rebuild.cicf()
#==============================================================================

print("                                             PROGRAMA DE REBUILD")
print(" ===============================================================================================================================|")
print(" =================================================== ATENÇÃO ===================================================================|")
print("              FAZER O BACKUP ANTES PRIMEITO PASSO MATAR TODOS OS PROCESSOS.  ( killall -9 rts32 ")
print(" E RENOMEAR ( mv sgauser.gnt sgauser.old | USAR NO FINAL PRA VOLTAR A ROTINA DE ACESSO AO SISTEMA : mv sgauser.old sgauser.gnt )")
print(' -------------------------------------------------------------------------------------------------------------------------------|')



pesquisa()

while p != 'SAIR':
    p  = str(input(' Digite a opção do Menu  : '))
    menu()
    pesquisa()
else:
    p =='SAIR'

print(' Sistema Será Finalizado !')
hora =[
    
]
now = datetime.datetime.now() 
print(f' Gerando Relatorio...: {now}')
time.sleep(2)
for i in tqdm (range (100),
                colour='#5F9EA0',
               desc=" Gerando Relatorio...",
               ascii=False, ncols=90):
               time.sleep(0.01)

""""
l = "N"
print('Deseja sair do sistema ? S/N')
while l == 'N':
    menu()
    pesquisa()
        
    if l == 'S':
        s  = str(input('Digite a opção do Menu  : '))
    break 
    
p  = str(input('Digite a opção do Menu  : '))
print('Deseja sair do sistema ? S/N')
while p == 'N':
    pesquisa()
    if p == 'S':
        break
"""  
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='SAIDA')  # Plot some data on the (implicit) axes.
plt.plot(x, x**5, label='VENDDUP')  # etc.
plt.plot(x, x*9, label='RECIBO')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()

fig, ax = plt.subplots(figsize=(5, 2.2), layout='constrained')
categories = ['SAIDA', 'VENDITENS', 'GRAVA', 'QUITADO ', 'CCFISCAL', 'VENDDUP', 'CICF', 'COMISSAO', 'RECIBO', 'ENTRADA', 'BALANCO', 'MOVBCO' ]
ax.bar(categories, np.random.rand(len(categories)))

plt.show()
