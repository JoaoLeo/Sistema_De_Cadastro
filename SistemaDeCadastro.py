lista = []
print("="*30)
print("SISTEMA DE CADASTRO DE PESSOAS")
print("="*30)
nome = str(input("Nome: "))
lista.append(nome)
idade = int(input("Idade: "))
lista.append(idade)
email = str(input("Email: "))
lista.append(email)
while True: 
    print("""Digite
    [1]Para acessar o nome
    [2]Para acessar a idade
    [3]Para acessar o email
    [4]Para mostrar os dados do cadastrado
    [5]Para fechar o programa
    """)
    resp = int(input("Sua opção: "))
    if resp == 5:
        break
    elif resp == 1:
        print(f"O nome cadastrado foi {nome}")
        continuar = str(input("Deseja acessar algo a mais? [S]/[N]")).strip()
        if continuar in "Nn":
            break
    elif resp ==2:
        print(f"A idade da pessoa cadastrada é {idade} anos")
        continuar = str(input("Deseja acessar algo a mais? [S]/[N]")).strip()
        if continuar in "Nn":
            break
    elif resp == 3:
        print(f"O email cadastrado foi {email}")
        continuar = str(input("Deseja acessar algo a mais? [S]/[N]")).strip()
        if continuar in "Nn":
            break
    elif resp ==4:
        print(f"Os dados cadastrados foram {lista}")
        continuar = str(input("Deseja acessar algo a mais? [S]/[N]")).strip()
        if continuar in "Nn":
            break 
    else:
        print("Por favor digite uma opção válida")   

print("Programa finalizado")
print("Volte sempre!!!")