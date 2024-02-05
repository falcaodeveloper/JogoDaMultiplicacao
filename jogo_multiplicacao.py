from random import randint

#Desenvolvido por Ulisses F. Falcão em 26/01/2024
mensagemEntrada = 'Digite o resultado: '
sair = 'Você saiu do jogo com sucesso!'
valorInvalido = '''Você digitou um valor inválido.
Por ter digitado um valor "inválido" você perdeu 5 pontos e eu ganhei 1 ponto!\n
Se quiser sair do jogo, não digite nada e tecle ENTER.'''
usuario = computador = 0
PontosUsuario, PontosComputador, ResultadoSeErrado, msnAjuda = 'Usuário: {} pontos', 'Computador: {} pontos\n', 'O resultado é {} e não {}, PRESTE ATENÇÃO!', 'Para saber as regras do jogo, digite "s".'

desejaAjuda = input(msnAjuda).strip().lower()
match desejaAjuda:
    case 's':
        msnAjuda = open('ajuda/ajuda.txt')
        print(msnAjuda.read())
while True:
    a, b = randint(0, 10), randint(0, 10)
    print('\n{} x {} = ?' .format(a, b))
    resultado = input(mensagemEntrada)
    if resultado.isnumeric() == False:
        if resultado == '':
            print(sair)
            break
        else:
            print('**' * 30)
            print(valorInvalido)
            print('**' * 30)
            usuario -= 5
            computador += 1
            print(PontosUsuario.format(usuario))
            print(PontosComputador.format(computador))
    else:
        resultado = int(resultado)
        if resultado == a * b:
            usuario += 1
            print(PontosUsuario.format(usuario))
            print(PontosComputador.format(computador))
        else:
            computador += 1
            print(ResultadoSeErrado.format(a * b, resultado))
            print(PontosUsuario.format(usuario))
            print(PontosComputador.format(computador))