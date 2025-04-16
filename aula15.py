import os

class Calcular:
    
    def operacao(self, numero1, numero2, conta):
        while True:
            if conta == 'Somar':
                resultado = numero1 + numero2
                limpar_tela()
                print(f'O resultado de {numero1} + {numero2} é: {resultado}')
                break
                
            elif conta == 'Subtrair':
                resultado = numero1 - numero2
                print(f'O resultado de {numero1} - {numero2} é: {resultado}')
                break
            elif conta == 'Dividir':
                resultado = numero1 / numero2
                print(f'O resultado de {numero1} / {numero2} é: {resultado:.2}')
                break
            elif conta == 'Multiplicar':
                resultado = numero1 * numero2
                print(f'O resultado de {numero1} * {numero2} é: {resultado}')
                break
            elif conta == 'Sair':
                 quit()
            else:
                limpar_tela()
                print('Escolha uma opção válida')
                conta = input('Você deseja: Somar, Subtrair, Dividir ou Multiplicar? ')
    

def limpar_tela():
                os.system('cls' if os.name == 'nt' else 'clear')


nome = input('Qual o seu nome? ')
print('Hello', nome)
input('\nPressione Enter para continuar...')
limpar_tela()

calc = Calcular()

while True:

    input('Preparado pra começar? (Aperte enter!)')
    limpar_tela()
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    conta = input('Você deseja: Somar, Subtrair, Dividir, Multiplicar ou Sair? ')


    calc.operacao(numero1, numero2, conta)



