
import random
import os
from datetime import datetime

#Lista de palavras
PALAVRAS = [
    ["CORINTHIANS",          "Nome do clube mais popular do Brasil, fundado em 1910",          "facil",   2],
    ["FIEL",                 "Como é chamada a torcida do Timão",                              "facil",   1],
    ["TIMAO",                "Apelido carinhoso do Corinthians",                               "facil",   1],
    ["RONALDO",              "O Fenômeno encerrou sua carreira no Timão em 2011",              "facil",   1],
    ["CASSIO",               "Goleiro ídolo que defendeu o Corinthians por mais de uma década","facil",   1],
    ["MUNDIAL",              "Título conquistado em 2000 e 2012 pelo Corinthians",             "facil",   1],
    ["TEVEZ",                "Apache argentino que encantou a Fiel nos anos 2000",             "facil",   1],
    ["SHEIK",                "Apelido do atacante Emerson, artilheiro do mundial de 2012",     "facil",   1],
    ["SOCRATES",             "Médico e filósofo, maior ídolo da história do Timão",            "medio",   2],
    ["LIBERTADORES",         "Taça sul-americana conquistada pelo Timão em 2012",              "medio",   2],
    ["BRASILEIRO",           "Campeonato nacional vencido pelo Corinthians 7 vezes",           "medio",   2],
    ["PAULISTAO",            "Campeonato estadual com mais de 30 títulos do Corinthians",      "medio",   2],
    ["ITAQUERA",             "Bairro de São Paulo onde fica a Neo Química Arena",              "medio",   2],
    ["VAMPETA",              "Volante raça pura, campeão mundial em 2000",                     "medio",   2],
    ["RIVELLINO",            "Craque dos anos 70, famoso pelo chute de trivela",               "medio",   2],
    ["WLADIMIR",             "Lateral histórico da Democracia Corinthiana",                    "medio",   2],
    ["GARRINCHA",            "Estádio histórico onde o Corinthians jogou por décadas",         "medio",   2],
    ["MOSQUETEIROS",         "Nome dos quatro fundadores do Corinthians em 1910",              "dificil", 2],
    ["ANDREOLI",             "Um dos fundadores do Corinthians em 1910",                       "dificil", 2],
    ["SCCP",                 "Sigla oficial do Sport Club Corinthians Paulista",               "dificil", 1],
    ["NEO QUIMICA ARENA",    "Estádio moderno inaugurado em 2014 em Itaquera",                 "dificil", 3],
    ["DEMOCRACIA CORINTHIANA","Movimento dos anos 80 onde jogadores decidiam o clube juntos",  "dificil", 4],
    ["PARQUE SAO JORGE",     "Sede social e administrativa do Corinthians",                    "dificil", 3],
    ["LOVE FIEL",            "Campanha icônica da torcida do Corinthians",                     "medio",   2],
    ["BIRO BIRO",            "Apelido do meia Guilherme Esteves, ídolo dos anos 80",           "medio",   2],
]

#Setando as pontuacoes das fases
TENTATIVAS = {"facil": 8,  "medio": 6,  "dificil": 5}
PTS_ACERTO = {"facil": 10, "medio": 15, "dificil": 25}
PTS_ERRO   = {"facil": -3, "medio": -5, "dificil": -10}

ARQUIVO_RESULTADO = "resultados.txt"



#Função para limpar a tela
def limpar_tela():
    os.system("clear")

#Função para exibir o cabeçalho
def cabecalho():
    print("===========================================================")
    print("       PALAVRA SECRETA DO TIMAO - SCCP")
    print("     Sport Club Corinthians Paulista")
    print("          Aqui e Fiel! Vai Timao!")
    print("===========================================================")

#Função para sortear a palavra
def sortear_palavra(nivel):
    
    opcoes = []
    for item in PALAVRAS:
        if item[2] == nivel:
            opcoes.append(item)
    if len(opcoes) == 0:
        opcoes = PALAVRAS
    return random.choice(opcoes)

#Funcão para montar o display
def montar_display(palavra, letras_reveladas):
    display = ""
    for letra in palavra:
        if letra == " ":
            display += "  "
        elif letra in letras_reveladas:
            display += letra + " "
        else:
            display += "_ "
    return display.strip()

#Funcao para revelar as letras iniciais
def revelar_iniciais(palavra, quantidade):
    reveladas = []
    for letra in palavra:
        if letra != " " and letra not in reveladas:
            reveladas.append(letra)
        if len(reveladas) == quantidade:
            break
    return reveladas

#Funcao para verificar se a palavra foi descoberta 
def palavra_completa(palavra, letras_reveladas):
    for letra in palavra:
        if letra != " " and letra not in letras_reveladas:
            return False
    return True

#Funcao para salvar os resultados dos jogadores
def salvar_resultado(nome, pontuacao, tentativas, acertos, erros, palavra, nivel, venceu):
    arquivo_novo = not os.path.exists(ARQUIVO_RESULTADO)

    arquivo = open(ARQUIVO_RESULTADO, "a", encoding="utf-8")

    if arquivo_novo:
        arquivo.write("===========================================================\n")
        arquivo.write("  PALAVRA SECRETA DO TIMAO - REGISTRO DE PARTIDAS\n")
        arquivo.write("===========================================================\n\n")

    arquivo.write("-" * 55 + "\n")
    arquivo.write("DATA        : " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    arquivo.write("JOGADOR     : " + nome + "\n")
    arquivo.write("PALAVRA     : " + palavra + "\n")
    arquivo.write("NIVEL       : " + nivel.upper() + "\n")
    arquivo.write("PONTUACAO   : " + str(pontuacao) + " pts\n")
    arquivo.write("TENTATIVAS  : " + str(tentativas) + "\n")
    arquivo.write("ACERTOS     : " + str(acertos) + "\n")
    arquivo.write("ERROS       : " + str(erros) + "\n")

    if venceu:
        arquivo.write("RESULTADO   : VENCEU!\n")
    else:
        arquivo.write("RESULTADO   : PERDEU!\n")

    arquivo.write("-------------------------------------------\n\n")
    arquivo.close()

#Funcao para exibir o historico de jogos 
def exibir_historico():
    if not os.path.exists(ARQUIVO_RESULTADO):
        print("\n  Nenhuma partida registrada ainda!")
        return

    arquivo = open(ARQUIVO_RESULTADO, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    print("\n" + "=" * 55)
    print("            HALL DA FAMA - TIMAO")
    print("=" * 55)

    partidas = []
    partida = {}

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith("DATA        :"):
            partida["data"] = linha.replace("DATA        : ", "")
        elif linha.startswith("JOGADOR     :"):
            partida["jogador"] = linha.replace("JOGADOR     : ", "")
        elif linha.startswith("PALAVRA     :"):
            partida["palavra"] = linha.replace("PALAVRA     : ", "")
        elif linha.startswith("NIVEL       :"):
            partida["nivel"] = linha.replace("NIVEL       : ", "")
        elif linha.startswith("PONTUACAO   :"):
            partida["pontos"] = linha.replace("PONTUACAO   : ", "").replace(" pts", "")
        elif linha.startswith("TENTATIVAS  :"):
            partida["tentativas"] = linha.replace("TENTATIVAS  : ", "")
        elif linha.startswith("RESULTADO   :"):
            partida["resultado"] = linha.replace("RESULTADO   : ", "")
            partidas.append(partida)
            partida = {}

    if len(partidas) == 0:
        print("  Nenhuma partida encontrada.")
        return
    

    for i in range(len(partidas)):
        for j in range(i + 1, len(partidas)):
            if int(partidas[i]["pontos"]) < int(partidas[j]["pontos"]):
                partidas[i], partidas[j] = partidas[j], partidas[i]

    print(f"  {'JOGADOR':<15} {'PONTOS':>6}  {'NIVEL':<8}  RESULTADO")
    print("  " + "----------------------------------------------------------")


    total = len(partidas)
    if total > 10:
        total = 10

    for i in range(total):
        p = partidas[i]
        print(f"  {p['jogador']:<15} {p['pontos']:>6}  {p['nivel']:<8}  {p['resultado']}")

    print("===========================================================\n")

#Funcao para exibir as regras do jogo
def exibir_regras():
    limpar_tela()
    cabecalho()
    print()
    print("  REGRAS DO JOGO")
    print("  " + "-" * 45)
    print()
    print("  1. Uma palavra secreta do Corinthians")
    print("     sera sorteada com uma dica.")
    print()
    print("  2. Algumas letras ja aparecem reveladas.")
    print()
    print("  3. Digite UMA letra por vez.")
    print()
    print("  4. Letra certa  --> voce ganha pontos!")
    print("  5. Letra errada --> voce perde pontos")
    print("                  e uma tentativa.")
    print()
    print("  6. Descubra a palavra antes de acabar")
    print("     as tentativas!")
    print()
    print("  PONTUACAO:")
    print("  Facil  : +10 pts acerto | -3  pts erro | 8 tent.")
    print("  Medio  : +15 pts acerto | -5  pts erro | 6 tent.")
    print("  Dificil: +25 pts acerto | -10 pts erro | 5 tent.")
    print()
    print("  BONUS: +5 pts por tentativa nao usada ao vencer!")
    print()


#A Funcao do Jogo 
def jogar(nome, nivel):
    # Sorteia a palavra
    item         = sortear_palavra(nivel)
    palavra      = item[0]
    dica         = item[1]
    letras_ini   = item[3]

    total_tent   = TENTATIVAS[nivel]
    restantes    = total_tent
    pontuacao    = 0
    acertos      = 0
    erros        = 0

    reveladas    = revelar_iniciais(palavra, letras_ini)
    ja_tentadas  = list(reveladas)  
    mensagem     = ""

    while restantes > 0:
        limpar_tela()
        cabecalho()
        print()
        print("  Jogador : " + nome)
        print("  Nivel   : " + nivel.upper())
        print("  Dica    : " + dica)
        print()

        qtd = 0
        for c in palavra:
            if c != " ":
                qtd += 1
        print("  Letras na palavra: " + str(qtd))
        print()
        print("  " + montar_display(palavra, reveladas))
        print()

        erradas_str = ""
        for letra in ja_tentadas:
            if letra not in palavra:
                erradas_str += letra + " "
        if erradas_str == "":
            erradas_str = "nenhuma"
        print("  Letras erradas : " + erradas_str)
        print()
        print("  Tentativas restantes : " + str(restantes) + "/" + str(total_tent))
        print("  Acertos: " + str(acertos) + "  |  Erros: " + str(erros) + "  |  Pontos: " + str(pontuacao))
        print()

        if mensagem != "":
            print("  " + mensagem)
            print()
            mensagem = ""

        if palavra_completa(palavra, reveladas):
            break

        entrada = input("  Digite uma letra: ").strip().upper()

        if len(entrada) == 0:
            mensagem = "AVISO: Digite uma letra!"
            continue

        if len(entrada) != 1:
            mensagem = "AVISO: Digite apenas UMA letra por vez."
            continue

        if not entrada.isalpha():
            mensagem = "AVISO: Apenas letras sao validas."
            continue

        if entrada in ja_tentadas:
            mensagem = "AVISO: Voce ja tentou a letra '" + entrada + "'."
            continue

        ja_tentadas.append(entrada)

        if entrada in palavra:
            ocorrencias = palavra.count(entrada)
            reveladas.append(entrada)
            ganhou = ocorrencias * PTS_ACERTO[nivel]
            pontuacao += ganhou
            acertos += ocorrencias
            mensagem = "CERTO! A letra '" + entrada + "' esta na palavra! +" + str(ganhou) + " pontos"
        else:
            pontuacao += PTS_ERRO[nivel]
            erros += 1
            restantes -= 1
            mensagem = "ERRADO! A letra '" + entrada + "' nao esta na palavra! " + str(PTS_ERRO[nivel]) + " pontos"

    venceu = palavra_completa(palavra, reveladas)
    tentativas_usadas = total_tent - restantes

    if venceu:
        if restantes > 0:
            bonus = restantes * 5
            pontuacao += bonus

        limpar_tela()
        cabecalho()
        print()
        print("  PARABENS! VOCE E FIEL DEMAIS!")
        print()
        print("  A palavra era : " + palavra)
        print("  Pontuacao     : " + str(pontuacao) + " pts")
        print("  Tentativas    : " + str(tentativas_usadas) + " usadas")
        print()
        print("  Vai Corinthians!")
    else:
        limpar_tela()
        cabecalho()
        print()
        print("  SUAS TENTATIVAS ACABARAM!")
        print()
        print("  A palavra era : " + palavra)
        print("  Pontuacao     : " + str(pontuacao) + " pts")
        print()
        print("  Nao desanima! Tente Novamente!")

    print()
    input("  Pressione ENTER para continuar...")

    salvar_resultado(nome, pontuacao, tentativas_usadas, acertos, erros, palavra, nivel, venceu)

    return pontuacao, tentativas_usadas, acertos, erros, venceu

#Funcao do menu interativo para escolher o nivel
def menu_nivel():
    limpar_tela()
    cabecalho()
    print()
    print("  Escolha o nivel de dificuldade:")
    print()
    print("  [1]  Facil   - 8 tentativas | +10/-3  pts")
    print("  [2]  Medio   - 6 tentativas | +15/-5  pts")
    print("  [3]  Dificil - 5 tentativas | +25/-10 pts")
    print("  [4]  Aleatorio (todos os niveis)")
    print()

    while True:
        opcao = input("  Sua escolha [1-4]: ").strip()

        if opcao == "1":
            return "facil"
        elif opcao == "2":
            return "medio"
        elif opcao == "3":
            return "dificil"
        elif opcao == "4":
            niveis = ["facil", "medio", "dificil"]
            return random.choice(niveis)
        else:
            print("  Opcao invalida. Tente novamente.")

#Funcao do menu interativo, mostrando as opcoes
def menu_principal(nome):
    while True:
        limpar_tela()
        cabecalho()
        print()
        print("  Bem-vindo(a), " + nome + "!")
        print("  Pronto(a) para provar que e Fiel?")
        print()
        print("  [1]  Nova Partida")
        print("  [2]  Hall da Fama")
        print("  [3]  Regras do Jogo")
        print("  [4]  Sair")
        print()

        opcao = input("  Escolha [1-4]: ").strip()

        if opcao == "1":
            nivel = menu_nivel()
            jogar(nome, nivel)

        elif opcao == "2":
            limpar_tela()
            cabecalho()
            exibir_historico()
            input("  Pressione ENTER para voltar...")

        elif opcao == "3":
            exibir_regras()
            input("  Pressione ENTER para voltar...")

        elif opcao == "4":
            limpar_tela()
            cabecalho()
            print()
            print("  Ate logo! Vai Corinthians!")
            print("  Aqui e Fiel, sempre foi e sempre sera!")
            print()
            break

        else:
            pass


limpar_tela()
cabecalho()
print()
print("  Antes de comecar, qual e o seu nome, Fiel?")
print()

nome = ""
while nome == "":
    nome = input("  Seu nome: ").strip()
    if nome == "":
        print("  Por favor, informe seu nome.")

menu_principal(nome)