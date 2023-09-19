#from Rebuild import menu, pesquisa

l = "N"
print('Deseja sair do sistema ? S/N')
while l == 'N':
    menu()
    s  = str(input('Digite a opção do Menu  : '))
    pesquisa()
    
    
    if l == 'S':
        s  = str(input('Digite a opção do Menu  : '))
    break