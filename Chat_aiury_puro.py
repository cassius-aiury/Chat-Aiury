while True: # loop infinito até o usuário decidir sair
    inicio = input('Se quiser começar a conversar, digite "Vamos conversar": ').strip().lower()

    if inicio != 'vamos conversar':
        print('Ok, até mais')
        break

    print("Olá, eu sou o Chat Aiury, vamos conversar!")
    nome = input("Seu nome: ")

    print(f"Olá ", {nome}, ' qual sua idade?')

    idade = int(input('Idade: '))

    if idade < 18:
        print('Hmmm, sinto muito, não podemos prosseguir com essa chat, você é muito novo, volte depois de alguns anos')
        break
    else:
        print("Excelete, podemos prosseguir com nossa conversa, ainda bem!")

    resposta = input('Você deseja prosseguir com a nossa conversa?')

    if resposta.lower() == " sim":
        cor = input('Tudo bem, me fale mais sobre você, qual sua cor favorita?')
        print(f"Legal! {cor} é uma cor muito bonita.")
    elif resposta.lower() == " não":
        print('Ok, terminamos por aqui então. Até a próxima! Caso deseje recomeçar o chat, digite "Vamos conversar".')
    else:
        print('Não entendi sua resposta, digite novamente "sim" ou "não" por favor')
    



