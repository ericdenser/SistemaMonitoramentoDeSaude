import time # Para utilizar a funcao time.sleep e ter um melhor feedback visual no terminal
import random # Frases motivacionais aleatorias


#----------------------------------------------------FRASES-MOTIVACIONAIS-----------------------------------------------------------#
def frase_motivacional(nome):
    frases = [
        f"{nome}, você é imparável! Continue dando tudo nos treinos! 🚀",
        f"Vamos lá, {nome}! Cada esforço te leva mais perto do seu objetivo! 💪",
        f"{nome}, sua dedicação é inspiradora! Mantenha o foco! 🔥",
        f"Você tá arrasando, {nome}! Persista e conquiste seus sonhos! 🏆",
        f"{nome}, cada gota de suor é um passo rumo à vitória! 💥",
        f"Força total, {nome}! Você tem o que precisa pra vencer! 👊",
        f"{nome}, sua energia é contagiante! Continue brilhando! 🌟",
        f"Não para agora, {nome}! Você tá no caminho certo! 🏋️‍♂️"
    ]
    return random.choice(frases)


#----------------------------------------------------CADASTRO-EXERCÍCIOS-----------------------------------------------------------#
def cadastro_exercicios(exercicios, calorias, nome):
    dias_semana = ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO']
    redirecionar = 1

    while redirecionar != 0:
        print('\n==============CADASTRANDO=================')
        print('Em que dia da semana foi realizado o exercício? \nSegunda (1)\nTerça (2)\nQuarta (3)\nQuinta (4)\nSexta (5\nSábado (6)\nDomingo (7) ')

        try: #VALIDANDO ENTRADA
            dia = int(input('Escolha uma opção para prosseguir (0 para voltar a página anterior): '))
        except ValueError:
            print('\n⚠️   Entrada inválida! Digite apenas números entre 0 e 7. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i}')
                time.sleep(1)
            continue


        if dia == 0:
            return exercicios, calorias
        if 1 <= dia <= 7:
            print(f'\n=================={dias_semana[dia-1]}======================')
            exercicio = input('Exercício realizado: ')
            tempo = float(input('Tempo gasto em minutos: ')) 
            caloriaqueimada = float(input('Calorias queimadas: '))
            calorias[dia-1] += caloriaqueimada # Armazena as calorias totais de cada dia em outra lista separada para melhor manuseio
            exercicios[dia-1].append([exercicio, tempo, caloriaqueimada]) # Armazena na lista principal em forma de sublistas, ex: [[Perna, 20, 150], [Peito, 10, 100]]

            print(f'\n{frase_motivacional(nome)}')
        else: #VALIDANDO DIA
            print('\n⚠️   DIA INVÁLIDO! Por favor, escolha um número de 1 a 7.⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i} ')
                time.sleep(1) 
            continue

        redirecionar = int(input('\nDeseja adicionar mais algum exercício? (1 para sim, 0 para voltar à página anterior): '))

    return exercicios, calorias # Retorna as novas listas



#----------------------------------------------------RELATÓRIO-----------------------------------------------------------#
def relatorio(exercicios, calorias, nome):
    dias_semana = ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO']
    redirecionar = 1

    while redirecionar != '0':
        print('\n==================RELATÓRIO======================')
        print('Qual dia da semana você quer consultar? \nSegunda (1)\nTerça (2)\nQuarta (3)\nQuinta (4)\nSexta (5)\nSábado (6)\nDomingo (7) ')

        try: #VALIDANDO ENTRADA
            dia = int(input('Escolha uma opção para prosseguir (0 para voltar ao menu): '))
        except ValueError:
            print('\n⚠️   Entrada inválida! Digite apenas números entre 0 e 7. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i}')
                time.sleep(1)
            continue


        if dia == 0: #RETORNA AO MENU
            return exercicios, calorias
        elif 1 <= dia <= 7: 
            print(f'\n=================={dias_semana[dia-1]}======================')
            if not exercicios[dia-1]: #CASO NAO EXISTA REGISTRO
                print('\nNenhum exercício registrado.')
                print(f'\n{frase_motivacional(nome)}')
            else:
                total_tempo = 0
                total_calorias = 0
                for indice in range(len(exercicios[dia-1])): # Percorre cada exercício do dia
                    exercicio = exercicios[dia-1][indice][0] # Nome do exercício
                    tempo = exercicios[dia-1][indice][1] # Tempo gasto no exercício
                    caloria = exercicios[dia-1][indice][2] # Calorias queimadas no exercício
                    print(f'\nExercício {indice + 1}: {exercicio} - Tempo: {tempo:.0f} minutos - Calorias Queimadas: {caloria}')  # Exibe os dados 
                    total_tempo += tempo # Total de tempo de exercícíos no dia
                    total_calorias += caloria # Total de calorias gastas no dia
                print(f'\nTotal no dia: {total_tempo:.0f} minutos, {total_calorias:.0f} calorias') # Exibe o total
        else:
            print('\n⚠️   DIA INVÁLIDO! Por favor, um dia de 1 a 7.⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i} ')
                time.sleep(1) 
            continue

        redirecionar = input('\nDeseja inspecionar mais algum dia? (Qualquer tecla para sim, 0 para voltar à página anterior): ')
        


#----------------------------------------------------CÁLCULO-IMC-----------------------------------------------------------#
def calculoimc(nome):
    redirecionar = 1
  
    while redirecionar != 0:
        print('\n==================CÁLCULO-IMC======================')
        print('Para calcular seu IMC, por favor informe seu peso e altura abaixo.')

        try: #VALIDANDO ENTRADA
            peso = float(input('Peso(kg): '))
            altura = float(input('Altura(m): '))
        except ValueError:
            print('\n⚠️   Entrada inválida! Digite apenas números. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i}')
                time.sleep(1)
            continue

        if peso == 0 or altura == 0: #VALIDANDO ENTRADA
            print('\nPor favor informe um peso e altura válidos. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i} ')
                time.sleep(1) 
            continue
        imc = peso / (altura ** 2)

        print(f'\nSeu IMC é: {imc:.2f}')

        if imc < 18.5:
            classificacao = 'Baixo peso'
            print(f'Classificação: {classificacao}\n')
            print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
        elif 18.5 <= imc < 25:
            classificacao = 'Peso normal'
            print(f'Classificação: {classificacao}\n')
            print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
        elif 25 <= imc < 30:
            classificacao = 'Sobrepeso'
            print(f'Classificação: {classificacao}\n')
            print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
        else:
            classificacao = 'Obesidade'
            print(f'Classificação: {classificacao}\n')
            print(f'\n{frase_motivacional(nome)}') # Frase Motivacional

    
        redirecionar = int(input('\nDeseja calcular outro IMC? (1 para sim, 0 para voltar à página anterior): '))



#----------------------------------------------------META-SEMANAL-----------------------------------------------------------#
def metasemanal(calorias, nome, metaatual):
    opcao = 1
    totalcalorias = sum(calorias) 

    while opcao != 0:
        print('\n ==================META-SEMANAL======================')
        print('Opção 1: Definir nova meta:\nOpção 2: Verificar meta atual: ')
    
        try: #VALIDANDO ENTRADA
             opcao = int(input('Escolha uma opção (0 para voltar a página anterior) : '))
        except ValueError:
            print('\n⚠️   Entrada inválida! Digite apenas números entre 0 e 2. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i}')
                time.sleep(1)
            continue

        if opcao == 0:
            break
        elif opcao == 1:
            meta = float(input('\nNova meta para bater(kcal): '))
            metaatual = meta
            print(f'\nBeleza {nome}! Sua nova meta de {metaatual:.0f}kcal foi definida 👊')
            print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
        elif opcao == 2:
            if metaatual <= 0:
                print('\nNenhuma meta definida! ⚠️')
                opcao = int(input('\nDeseja definir uma meta? (1 para sim, 0 para voltar à página anterior): ')) 
                continue
            if metaatual <= sum(calorias): # Meta atual menor ou igual as calorias queimadas = a meta foi batida
                print(f'\nFala {nome}! Você conseguiu queimar {totalcalorias}kcal e sua meta atual de {metaatual}kcal foi batida!! ')
                print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
            else:
               print(f'\nFala {nome}! Você conseguiu queimar {totalcalorias}kcal e infelizmente sua meta de {metaatual}kcal não foi batida ')
               print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
        else:
            print('\n⚠️   OPÇÃO INVÁLIDA! Por favor, escolha um número de 0 a 2.⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i} ')
                time.sleep(1) 
            continue

        opcao = int(input('\nDeseja definir nova/outra meta ou verificar atual? (1 para sim, 0 para voltar à página anterior): ')) 

    return metaatual

#----------------------------------------------------MÉDIA-CALORIAS-----------------------------------------------------------#
def mediacalorias(exercicios, calorias, nome):
    totalexercicios = sum(len(dia) for dia in exercicios) # Acha o total de exercicios, já que cada entrada representa um exercício completo
    totalcalorias = sum(calorias)
    redirecionar = 1

    if totalexercicios <= 0 or totalcalorias <= 0:
        print('\nNão foi possível calcular a média (exercício ou calorias não registrado)⚠️')
        for i in range(3, 0, -1):
            print(f'Voltando em {i} ')
            time.sleep(1)
    else:
        while redirecionar != 0:
            media = totalcalorias / totalexercicios
            print('\n==================MÉDIA-DE-CALORIAS-GASTAS======================')
            print(f'\n{nome} sua média de calorias gastas por exercício realizado foi de {media:.2f}kcal.')
            if media < 100:
                print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
            elif 100 <= media < 250:
                print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
            elif 250 <= media < 400:
                print(f'\n{frase_motivacional(nome)}') # Frase Motivacional
            else:
                print(f'\n{frase_motivacional(nome)}') # Frase Motivacional

            redirecionar = input('\nDigite qualquer tecla para voltar: ')
            break


#----------------------------------------------------GRÁFICOS-----------------------------------------------------------#
def graficocalorias(calorias, nome):
    dias_semana = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM'] 
    maxcal = max(calorias) # Acha qual o dia que mais consumiu calorias
    escala = 20  
    redirecionamento = 1
    while redirecionamento != '0':
        print('\n==================GRÁFICO-DE-CALORIAS======================\n')
        print(f'\n{nome} como você deseja visualizar seu gráfico? \nHorizontal(1)\nVertical(2)')
        try: #VALIDANDO ENTRADA
            opcao = int(input('Escolha uma opção (0 para voltar): '))
        except ValueError:
            print('\n⚠️   Entrada inválida! Digite apenas números entre 0 e 2. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i}')
                time.sleep(1)
            continue
        #-------VERIFICAÇÃO DE INVALIDEZ-------#
        if opcao == 0: #Retorna ao menu
            return
        elif opcao != 1 and opcao != 2: # Verifica se a opcao é valida
            print('\nNão foi possível gerar o gráfico (opcão inválida)')
            for i in range(3, 0, -1):
                print(f'Voltando em {i} ')
                time.sleep(1) 
                continue
        elif sum(calorias) <= 0: # Verifica se há calorias registradas
            print('\nNão foi possível gerar o gráfico (nenhuma caloria registrada)')
            for i in range(3, 0, -1):
                print(f'Voltando em {i} ')
                time.sleep(1) 
                continue

        #-------CONSTRUÇÃO DOS GRÁFICOS-------#       
        else: 
            if opcao == 1: # Horizontal
                print(f'\nSegue abaixo as calorias queimadas que você queimou até agora nessa semana!!\n')
                print(f'\nGRÁFICO TIPO HORIZONTAL: \n')

                for i in range(len(calorias)): # Percorre cada dia da semana
                    barras = '█' * int(calorias[i] // escala) # Constrói a barra do gráfico apartir da divisao inteira das calorias do dia pela escala
                    print(f'{dias_semana[i]:>3} | {barras:<20} {calorias[i]:>5.0f} kcal') #Constrói o gráfico: Dia | Barra, Caloria
            
                print(f'\nCada █ representa exatamente {escala} kcal.')
                redirecionamento = input('\nDigite qualquer tecla para ver outro gráfico (0 volta ao menu): ')
            else: # Vertical
                print(f'\nSegue abaixo as calorias queimadas que você queimou até agora nessa semana!!\n')
                print(f'\nGRÁFICO TIPO VERTICAL: \n')
                altura = int((maxcal + escala) // escala) # Monta a altura do gráfico
                for i in reversed(range(1, altura + 1)): # Comeca o grafico por cima 
                    linha = '' # Define a váriavel linha dentro do for para reiniciar sempre que abaixar a altura
                    for caloria in calorias:
                        if caloria >= i * escala: # Verifica se tal caloria é compativel com a altura atual da escala 
                            linha += '  █  ' # se for, registra 
                        else:
                            linha += '     ' #se nao, deixa em branco

                    print(f'{i * escala:>4} |{linha}') # Printa o valor da escala na altura atual e depois a linha contendo █ ou branco
                    
                print('     ' + '-----' * len(dias_semana))  # Base do gráfico, ajustando a largura
                print('       ' + '  '.join(dias_semana))# Rótulos dos dias alinhados 
                print(f'\nCada nível representa exatamente 20 kcal.')
                redirecionamento = input('\nDigite qualquer tecla para ver outro gráfico (0 volta ao menu): ')

def menu_principal(exercicios, calorias, metaatual):
    nome = input('Por favor, informe-nos seu nome: ')
    while True:
        print('\n==================MENU-PRINCIPAL======================')
        print('\nSeja Bem-Vindo à Academia Mackenzie!!')
        print(f'\nFala {nome}! O que te traz aqui?')
        print('\n Opção 1: Cadastro de Exercícios \n Opção 2: Relatório Diário \n Opção 3: Cálculo de IMC \n ' \
        'Opção 4: Meta Semanal \n Opção 5: Média de Calorias por Exercício\n Opção 6: Gráfico de Calorias')

        try: #VALIDAÇÃO
            direcionamento = int(input('\nEscolha uma opção para prosseguir (0 para sair): '))
            if direcionamento < 0 or direcionamento > 6:
                print('\n⚠️   Opção inválida! Digite um número entre 0 e 6. ⚠️')
                for i in range(3, 0, -1):
                    print(f'Voltando em {i}')
                    time.sleep(1)
                continue
        except ValueError:
            print('\n⚠️   Entrada inválida! Digite apenas números inteiros. ⚠️')
            for i in range(3, 0, -1):
                print(f'Voltando em {i}')
                time.sleep(1)
            continue

        if direcionamento == 0:
            return print ('Programa encerrado')
        elif direcionamento == 1:
            exercicios, calorias = cadastro_exercicios(exercicios, calorias, nome)
        elif direcionamento == 2:
            relatorio(exercicios, calorias, nome)
        elif direcionamento == 3:
            calculoimc(nome)
        elif direcionamento == 4:
             metaatual = metasemanal(calorias, nome, metaatual)
        elif direcionamento == 5:
            mediacalorias(exercicios, calorias, nome)
        else: 
            graficocalorias(calorias, nome)
        
      

#-----VARIÁVEIS-GLOBAIS---------#
metaatual = 0
exercicios = [[] for _ in range(7)]  # 7 listas, uma para cada dia
calorias = [0 for _ in range(7)] # 7 calorias, uma para cada dia
menu_principal(exercicios, calorias, metaatual) # Volta ao menu novamente sempre que uma funcao é encerrada (0)