while True:  # Loop que mantém o chat rodando
    inicio = input('Se quiser começar a conversar, digite "Vamos conversar": ').strip().lower()

    if inicio != 'vamos conversar':
        print('Ok, até mais!\n')
        break  # Sai do chat de vez

    print("Olá, eu sou o Chat Aiury, vamos conversar!")
    nome = input("Seu nome: ")

    print(f"Olá {nome}, qual sua idade?")

    try:
        idade = int(input('Idade: '))
    except ValueError:
        print("Por favor, digite um número válido para a idade.\n")
        continue  # Volta para o começo, caso a idade seja inválida

    if idade < 18:
        print('Hmmm, sinto muito, não podemos prosseguir com essa conversa. Você é muito novo, volte depois de alguns anos.')
        print('Caso deseje voltar a conversar, digite "Vamos conversar".\n')
        continue  # Volta para o início oferecendo a opção
    else:
        print("Excelente, podemos prosseguir com nossa conversa, ainda bem!")

    resposta = input('Você deseja prosseguir com a nossa conversa? (sim/não): ').strip().lower()

    if resposta == "sim":
        cor = input('Tudo bem, me fale mais sobre você, qual sua cor favorita? ')
        print(f"Legal! {cor} é uma cor muito bonita.\n")
        print('Terminamos nossa conversa por aqui. Caso deseje voltar a conversar, digite "Vamos conversar".\n')
    elif resposta == "não":
        print('Ok, terminamos por aqui então. Até a próxima!')
        print('Caso deseje voltar a conversar, digite "Vamos conversar".\n')
    else:
        print('Não entendi sua resposta. Digite "sim" ou "não", por favor.\n')
        print('Caso deseje voltar a conversar, digite "Vamos conversar".\n')

    # Volta automaticamente para o início perguntando "Vamos conversar"
