import os

os.system('cls' if os.name == 'nt' else 'clear') #LIMPAR TELA

#CRIAR CLASSE JOVEM
class Jovem:
    def __init__(self, nome, saldo, salario, despesas):
        self.nome = nome
        self.saldo = saldo
        self.salario = salario
        self.despesas = despesas
        self.lucro = salario - despesas
        self.dinheiro_disponivel = self.lucro + self.saldo
        self.pedidos = []
    #INICIAR INFORMAÇÕES OBTIDAS PELO USUARIO
    def __str__(self):
        return (f"\n{self.nome} - " 
                f"|SALDO: R${self.saldo:.2f}| "
                f"|SALÁRIO: R${self.salario:.2f}| "
                f"|DESPESAS: R${self.despesas:.2f}| "
                f"|DINHEIRO DISPONÍVEL: R${self.dinheiro_disponivel:.2f}|")
    #COMPRAR JOGOS
    def comprar_jogo(self, jogo):
        if jogo in self.pedidos: #SE O JOGO JÁ ESTIVER NOS PEDIDOS
          print(f"\n{self.nome} JÁ COMPROU O JOGO {jogo.nome} NOVAMENTE.")
          return False
        if self.dinheiro_disponivel >= jogo.preço:  #SE O DINHEIRO DISPONÍVEL FOR MAIOR OU IGURAL O PREÇO DO JOGO
            self.dinheiro_disponivel -= jogo.preço  #COMPRAR O JOGO
            self.pedidos.append(jogo)  # ADICIONAR O JOGO NA LISTA DE PEDIDOS,DEPOIS À COMPRA
            print(f"\n{self.nome} COMPROU O JOGO {jogo.nome} POR R${jogo.preço:.2f}")
            return True 
        else:
            print(f"{self.nome} NÃO TEM DINHEIRO SUFICIENTE PARA COMPRAR O JOGO. {jogo.nome}. "
            f"DINHEIRO NECESSÁRIO: R${jogo.preço - self.dinheiro_disponivel:.2f}")
        return False
    #VER CARRINHO
    def ver_pedidos(self):
        if not self.pedidos: #SE NÃO TIVER NENHUM PEDIDOS
            print("PEDIDOS VAZIO.")
        else:
            print("-------------------------")
            print("|        PEDIDOS:       |")
            print("-------------------------")
            print(f"{nome} - SALDO DISPONÍVEL: {self.lucro}\n")
            total = 0
            for jogo in self.pedidos:
                print(jogo)
                total += jogo.preço
            print("\n------------------------")
            print(f"|VALOR TOTAL: R${total:.2f} |")
            print("------------------------\n")
            print("1. CONFIRMAR")
            print("2. NÃO CONFIRMAR")
            confirmar = input("CONFIRMAR PEDIDOS?:")
            if confirmar == "1":
                print("PEDIDOS FECHADOS COM SUCESSO!")
                return True
            elif confirmar == "2":
                print("PEDIDOS NÃO FECHADOS.")
                return False
            print(jogo)
                
#CRIAR CLASSE JOGO
class Jogo:
    def __init__(self, nome, preço, tipo):
        self.nome = nome
        self.preço = preço
        self.tipo = tipo
    #INFORMAÇÕES DO JOGO
    def __str__(self): 
        return f"{self.nome} - R${self.preço:.2f} - {self.tipo}"
#CRIAR CLASSE LOJA DE JOGOS
class LojaDeJogos:
    def __init__(self):
        self.jogos = []
    #ADICIONAR JOGOS NA LISTA DE JOGOS
    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)
    #NUMERAÇÃO DE JOGOS (SEQUENCIA DE INDICES)
    def listar_jogos(self):
        if not self.jogos: #SE NÃO HOUVER JOGOS
            print("NENHUM JOGO DISPONÍVEL.")
        else:
            for i, jogo in enumerate(self.jogos): #JOGOS
                print(f"{i+1}. {jogo}")
    #VENDER JOGOS
    def vender_jogo(self, jovem, indice_jogo):
        if 0 <= indice_jogo < len(self.jogos):
            jogo = self.jogos[indice_jogo]
            return jovem.comprar_jogo(jogo)
        else:
            print("OPÇÃO DO JOGO INVÁLIDO.")
            return False

    #RECOMENDAR DE ACORDO COM O DINHEIRO DISPONÍVEL
    def recomendar_jogos(self, jovem):
        tipos_jogos_comprados = [jogo.tipo for jogo in jovem.pedidos]
        recomendacoes = []
        for jogo in self.jogos:
            if jogo not in jovem.pedidos and jogo.preço <= jovem.dinheiro_disponivel:
                if jogo.tipo in tipos_jogos_comprados:
                    recomendacoes.append(jogo)
                
    #RECOMENDAÇÕES DE JOGOS
        if recomendacoes:
            print("---------------------------------------------------------------")
            print("|RECOMENDAÇÕES DE JOGOS COM BASE NO SEU HISTÓRICO DE COMPRAS: |")  #TITULO DE RECOMENDAÇÕES
            print("---------------------------------------------------------------")
            for jogo in recomendacoes:
                print(jogo)
        else:
            print("\nNENHUM JOGO DISPONÍVEL DENTRO DO SEU ORÇAMENTO OU COM BASE NO SEU HISTÓRICO DE COMPRAS.")
           
#SOLICITAR DADOS DO USUÁRIO
nome = input("DIGITE O SEU NOME: ")
saldo = float(input("DIGITE O SEU SALDO ATUAL:"))
salario = float(input("DIGITE O SEU SALÁRIO: R$"))
despesas = float(input("DIGITE QUANTO VOCÊ GASTOU ESSE MÊS: R$"))
#MOSTRAR OS DADOS DO USUÁRIO
jovem = Jovem(nome, saldo, salario, despesas)
print(jovem)

#LOJA DE JOGOS E ADICIONAR JOGOS
loja = LojaDeJogos()
#CRIAR UMA LISTA DE JOGOS
jogos = [
    Jogo("FC 24", 350, "\033[91mESPORTE\033[0m"),
    Jogo("BATTLEFIELD V", 250, "\033[94mTIRO\033[0m"), 
    Jogo("IT TAKES TWO", 200, "\033[93mAVENTURA\033[0m"), 
    Jogo("MORTAL KOMBAT", 150, "\033[95mLUTA\033[0m"), 
    Jogo("ASSASSIN'S CREED VALHALLA", 300, "\033[93mAVENTURA\033[0m"), 
    Jogo("CYBERPUNK 2077", 250, "\033[92mRPG\033[0m"), 
    Jogo("THE WITCHER 3", 150, "\033[92mRPG\033[0m"),  
    Jogo("CALL OF DUTY: MODERN WARFARE", 220, "\033[94mTIRO\033[0m"), 
    Jogo("BATTLERITE", 100, "\033[95mLUTA\033[0m"),
    Jogo("EFOOTBALL™ 2024", 200, "\033[91mESPORTE\033[0m"), 
    Jogo("COUNTER STRIKE", 150, "\033[94mTIRO\033[0m"),
    Jogo("ROCKET LEAGUE", 80, "\033[91mESPORTE\033[0m"),
    Jogo("BRAWHALLA", 100, "\033[95mLUTA\033[0m"),
    Jogo("NARUTO SHIPPUDEN", 70, "\033[93mAVENTURA\033[0m"),
    Jogo("DIABLO IV", 140, "\033[92mRPG\033[0m"),
    Jogo("F1 2024", 300, "\033[91mESPORTE\033[0m"),
    Jogo("APEX LEGENDS", 130, "\033[94mTIRO\033[0m"),
    Jogo("LIMBO", 100, "\033[93mAVENTURA\033[0m"),
    Jogo("INJUSTICE 2", 90, "\033[95mLUTA\033[0m"),
    Jogo("GENSHIN IMPACT", 150, "\033[92mRPG\033[0m")
]
#ADICIONAR JOGOS À LOJA
for jogo in jogos:  
    loja.adicionar_jogo(jogo)

while True:
    print("---------------------------------------------------------")
    print("|                   LOJA DE JOGOS:                      |")  #TITULO DA LOJA
    print("---------------------------------------------------------")

    loja.listar_jogos()
    print("21. VER PEDIDOS") 
    print("22. PARA SAIR")
    #DIGITAR A OPÇÃO 
    opcao = int(input("\nDIGITE A OPÇÃO DESEJADA: "))
    os.system('cls' if os.name == 'nt' else 'clear')
#OPÇÃO DESEJADO ENTRE 1 E 21
    if 1 <= opcao <= len(loja.jogos):
            if loja.vender_jogo(jovem, opcao - 1):  #PASSAR ÍNDICE DO JOGO NA LISTA
                print(jovem)
                loja.recomendar_jogos(jovem)  # MOSTRAR RECOMENDAÇÕES APÓS A COMPRA
#21 PARA VER PEDIDOS
    elif opcao == 21: 
        jovem.ver_pedidos()
#PARAR 22 PARA SAIR
    elif opcao == 22:
        break
#SE DIGITAR A OPÇÃO ERRADA
    else:
        print("OPÇÃO INVÁLIDA, DIGITE A OPÇÃO CORRETA!")
print("VOLTE SEMPRE")
