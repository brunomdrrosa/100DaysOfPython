# Recursos do Café
agua = 300
leite = 200
gramas_cafe = 100
caixa = 0

# Função do café Expresso
def expresso():
    global agua
    global gramas_cafe
    if agua >= 50:
        if gramas_cafe >= 18:
            print("O café expresso custa R$ 3,00")
            print("Por favor, insira o dinheiro.")
            cinco_cents = int(input("Quantas moedas de 5 centavos você tem? "))
            dez_cents = int(input("Quantas moedas de 10 centavos você tem? "))
            vinte_cinco_cents = int(input("Quantas moedas de 25 centavos você tem? "))
            cinquenta_cents = int(input("Quantas moedas de 50 centavos você tem? "))
            um_real = int(input("Quantas moedas de 1 real você tem? "))
            dinheiro = (cinco_cents * 0.05 + dez_cents * 0.1 + vinte_cinco_cents * 0.25 + cinquenta_cents * 0.5 + um_real)
            if dinheiro >= 3.00:
                global caixa
                agua -= 50
                gramas_cafe -= 18
                troco = dinheiro - 3.00
                caixa += dinheiro - troco
                print(f"Aqui está R$ {troco:.2f} de troco")
                print("Aqui está o seu café expresso")
                menu()
            else:
                print(f"Desculpe, isso não é suficiente para comprar o café, ele custa R$ 3,00 e você pagou R$ {dinheiro:.2f}\nDinheiro reembolsado")
                menu()
        else:
            print("Desculpe, não temos grãos de café suficiente para fazer o café")
            menu()
    else:
        print("Desculpe, não temos água suficiente para fazer o café")
        menu()

# Função do café Latte
def latte():
    global agua
    global leite
    global gramas_cafe
    if agua >= 200:
        if leite >= 150:
            if gramas_cafe >= 24:
                print("O café Latte custa R$ 4,00")
                print("Por favor, insira o dinheiro.")
                cinco_cents = int(input("Quantas moedas de 5 centavos você tem? "))
                dez_cents = int(input("Quantas moedas de 10 centavos você tem? "))
                vinte_cinco_cents = int(input("Quantas moedas de 25 centavos você tem? "))
                cinquenta_cents = int(input("Quantas moedas de 50 centavos você tem? "))
                um_real = int(input("Quantas moedas de 1 real você tem? "))
                dinheiro = (cinco_cents * 0.05 + dez_cents * 0.1 + vinte_cinco_cents * 0.25 + cinquenta_cents * 0.5 + um_real)
                if dinheiro >= 4.00:
                    global caixa
                    agua -= 200
                    leite -= 150
                    gramas_cafe -= 24
                    troco = dinheiro - 4.00
                    caixa += dinheiro - troco
                    print(f"Aqui está R$ {troco:.2f} de troco")
                    print("Aqui está o seu café Latte")
                    menu()
                else:
                    print(f"Desculpe, isso não é suficiente para comprar o café, ele custa R$ 4,00 e você pagou R$ {dinheiro:.2f}\nDinheiro reembolsado")
                    menu()
            else:
                print("Desculpe, não temos grãos de café suficiente para fazer o café")
                menu()
        else:
            print("Desculpe, não temos leite suficiente para fazer o café")
            menu()
    else:
        print("Desculpe, não temos água suficiente para fazer o café")
        menu()

# Função do café Cappuccino
def cappuccino():
    global agua
    global leite
    global gramas_cafe
    if agua >= 250:
        if leite >= 100:
            if gramas_cafe >= 24:
                print("O café Cappuccino custa R$ 5,00")
                print("Por favor, insira o dinheiro.")
                cinco_cents = int(input("Quantas moedas de 5 centavos você tem? "))
                dez_cents = int(input("Quantas moedas de 10 centavos você tem? "))
                vinte_cinco_cents = int(input("Quantas moedas de 25 centavos você tem? "))
                cinquenta_cents = int(input("Quantas moedas de 50 centavos você tem? "))
                um_real = int(input("Quantas moedas de 1 real você tem? "))
                dinheiro = (cinco_cents * 0.05 + dez_cents * 0.1 + vinte_cinco_cents * 0.25 + cinquenta_cents * 0.5 + um_real)
                if dinheiro >= 5.00:
                    global caixa
                    agua -= 250
                    leite -= 100
                    gramas_cafe -= 24
                    troco = dinheiro - 5.00
                    caixa += dinheiro - troco
                    print(f"Aqui está R$ {troco:.2f} de troco")
                    print("Aqui está o seu café Cappuccino")
                    menu()
                else:
                    print(f"Desculpe, isso não é suficiente para comprar o café, ele custa R$ 4,00 e você pagou R$ {dinheiro:.2f}\nDinheiro reembolsado")
                    menu()
            else:
                print("Desculpe, não temos grãos de café suficiente para fazer o café")
                menu()
        else:
            print("Desculpe, não temos leite suficiente para fazer o café")
            menu()
    else:
        print("Desculpe, não temos água suficiente para fazer o café")
        menu()

# Menu da máquina
def menu():
    print()
    global cafe
    cafe = input("O que você gostaria de tomar?\nDigite '1' para Expresso\nDigite '2' para Latte\nDigite '3' para Cappuccino\n")

    if cafe == "1":
        expresso()
    elif cafe == "2":
        latte()
    elif cafe == "3":
        cappuccino()
    elif cafe == "relatorio":
        print(f"Água: {agua}ml")
        print(f"Leite: {leite}ml")
        print(f"Café: {gramas_cafe}g")
        print(f"Dinheiro: R$ {caixa}")
        menu()
    elif cafe == "desligar":
        exit()

menu()