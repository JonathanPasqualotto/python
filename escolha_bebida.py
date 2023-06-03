print("Escolha uma Bebida: ")
print("""
    MENU    

1 - COCA-COLA R$ 5,00
2 - GUARANÁ   R$ 4,50
3 - ÁGUA      R$ 2,00
""")
opcao = int(input("Opção: "))
if opcao == 1:
    print('VOCÊ ESCOLHEU COCA-COLA')
elif opcao == 2:
    print('VOCÊ ESCOLHEU GUARANÁ')
elif opcao == 3:
    print('VOCÊ ESCOLHEU ÁGUA')
  
else:
    print("NAO TEMOS ESTA OPCAO, FAVOR PRESTAR ATENCAO NO MENU")
print("OBRIGADO A PREFERENCIA")