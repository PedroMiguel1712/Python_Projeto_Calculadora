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
                limpar_tela()
                print(f'O resultado de {numero1} - {numero2} é: {resultado}')
                break
            elif conta == 'Dividir':
                resultado = numero1 / numero2
                limpar_tela()
                print(f'O resultado de {numero1} / {numero2} é: {resultado:.2}')
                break
            elif conta == 'Multiplicar':
                resultado = numero1 * numero2
                limpar_tela()
                print(f'O resultado de {numero1} * {numero2} é: {resultado}')
                break
            elif conta == 'Sair':
                 limpar_tela()
                 quit()
            else:
                limpar_tela()
                print('Escolha uma opção válida')
                conta = input('Você deseja: Somar, Subtrair, Dividir ou Multiplicar? ')
    

def limpar_tela():
                os.system('cls' if os.name == 'nt' else 'clear')

calc = Calcular()

while True:

    start = input('Preparado pra começar? (Aperte enter!) | Caso não, digite "Sair" ')
    if start == 'Sair':
     quit()
    
    limpar_tela()
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    limpar_tela()
    conta = input('Você deseja: Somar, Subtrair, Dividir, Multiplicar ou Sair? ')


    calc.operacao(numero1, numero2, conta)



