import pygame
from pygame.locals import *
import random
from sys import exit
import os

class BlackjackPygame:
    def __init__(self):
        pygame.init()

        musica_de_fundo = pygame.mixer.music.load('Fortune Tiger - Official Game Soundtrack & Effects.mp3')
        pygame.mixer.music.play(-1)

        # Configurações da janela
        self.largura = 1400
        self.altura = 780
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("BlackMonkeyJack")

        # Fonte e cores
        self.fonte = pygame.font.SysFont('CHEQUE', 50, True, True)
        self.cor_fundo = "dark green"
        self.cor_botao = (0, 0, 0)
        self.cor_texto_botao = (255, 255, 255)

        # Fundo
        self.img_mesa = pygame.image.load(os.path.join("Fundo", "Fundo.jpeg"))
        self.img_mesa = pygame.transform.scale(self.img_mesa, (self.largura, self.altura))

        # Botões
        self.ret_pedir_carta = pygame.Rect(60, 650, 250, 65)
        self.ret_parar = pygame.Rect(350, 650, 200, 65)
        self.ret_apostar = pygame.Rect(570, 650, 200, 65)
        # Mensagem para se perdeu ou venceu
        self.mensagem_final = ""

        # Carregar imagens de cartas e fichas
        self.cartas = self.carregar_cartas()
        self.fichas = self.carregar_fichas()
        self.ret_fichas = self.criar_clicavel_fichas()

        # Inicializar variáveis de jogo
        self.baralho = self.criar_baralho() # cria o baralho
        random.shuffle(self.baralho) # shuffle embaralha o baralho
        self.cartas_jogador = []
        self.cartas_bot = []
        self.pontos_jogador = 0
        self.pontos_bot = 0
        self.saldo = 200
        self.aposta = 0
        self.jogo_em_andamento = False
    #Função para carregar as cartas
    def carregar_cartas(self):
        naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']
        #lista de cartas
        cartas = {
            #Cartas de Copas
            "AsCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\As_Copas.jfif"), (80, 120)),
            "DoisCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\2_Copas.jfif"), (80, 120)),
            "TresCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\3_Copas.jfif"), (80, 120)),
            "QuatroCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\4_Copas.jfif"), (80, 120)),
            "CincoCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\5_Copas.jfif"), (80, 120)),
            "SeisCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\6_Copas.jfif"), (80, 120)),
            "SeteCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\7_Copas.jfif"), (80, 120)),
            "OitoCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\8_Copas.jfif"), (80, 120)),
            "NoveCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\9_Copas.jfif"), (80, 120)),
            "DezCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\10_Copas.jfif"), (80, 120)),
            "RainhaCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\Rainha_Copas.jfif"), (80, 120)),
            "ValeteCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\Valete_Copas.jfif"), (80, 120)),
            "ReiCopas": pygame.transform.scale(pygame.image.load(".\\Copas\\Rei_Copas.jfif"), (80, 120)),
            #Cartas de Espadas
            "AsEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\As_Espadas.jfif"), (80, 120)),
            "DoisEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\2_Espadas.jfif"), (80, 120)),
            "TresEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\3_Espadas.jfif"), (80, 120)),
            "QuatroEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\4_Espadas.jfif"), (80, 120)),
            "CincoEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\5_Espadas.jfif"), (80, 120)),
            "SeisEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\6_Espadas.jfif"), (80, 120)),
            "SeteEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\7_Espadas.jfif"), (80, 120)),
            "OitoEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\8_Espadas.jfif"), (80, 120)),
            "NoveEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\9_Espadas.jfif"), (80, 120)),
            "DezEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\10_Espadas.jfif"), (80, 120)),
            "RainhaEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\Rainha_Espadas.jfif"), (80, 120)),
            "ValeteEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\Valete_Espadas.jfif"), (80, 120)),
            "ReiEspadas": pygame.transform.scale(pygame.image.load(".\\Espadas\\Rei_Espadas.jfif"), (80, 120)),

            #Cartas de Ouros
            "AsOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\As_Ouros.jfif"), (80, 120)),
            "DoisOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\2_Ouros.jfif"), (80, 120)),
            "TresOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\3_Ouros.jfif"), (80, 120)),
            "QuatroOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\4_Ouros.jfif"), (80, 120)),
            "CincoOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\5_Ouros.jfif"), (80, 120)),
            "SeisOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\6_Ouros.jfif"), (80, 120)),
            "SeteOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\7_Ouros.jfif"), (80, 120)),
            "OitoOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\8_Ouros.jfif"), (80, 120)),
            "NoveOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\9_Ouros.jfif"), (80, 120)),
            "DezOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\10_Ouros.jfif"), (80, 120)),
            "RainhaOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\Rainha_Ouros.jfif"), (80, 120)),
            "ValeteOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\Valete_Ouros.jfif"), (80, 120)),
            "ReiOuros": pygame.transform.scale(pygame.image.load(".\\Ouros\\Rei_Ouros.jfif"), (80, 120)),

            #Cartas de Paus
            "AsPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\As_Paus.jfif"), (80, 120)),
            "DoisPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\2_Paus.jfif"), (80, 120)),
            "TresPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\3_Paus.jfif"), (80, 120)),
            "QuatroPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\4_Paus.jfif"), (80, 120)),
            "CincoPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\5_Paus.jfif"), (80, 120)),
            "SeisPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\6_Paus.jfif"), (80, 120)),
            "SetePaus": pygame.transform.scale(pygame.image.load(".\\Paus\\7_Paus.jfif"), (80, 120)),
            "OitoPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\8_Paus.jfif"), (80, 120)),
            "NovePaus": pygame.transform.scale(pygame.image.load(".\\Paus\\9_Paus.jfif"), (80, 120)),
            "DezPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\10_Paus.jfif"), (80, 120)),
            "RainhaPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\Rainha_Paus.jfif"), (80, 120)),
            "ValetePaus": pygame.transform.scale(pygame.image.load(".\\Paus\\Valete_Paus.jfif"), (80, 120)),
            "ReiPaus": pygame.transform.scale(pygame.image.load(".\\Paus\\Rei_Paus.jfif"), (80, 120)),
        }
        for naipe in naipes:
            for valor in valores:
                chave_carta = (valor, naipe)
                caminho_imagem = os.path.join(naipe, f"{valor}_{naipe}.jfif")
                cartas[chave_carta] = pygame.transform.scale(pygame.image.load(caminho_imagem), (80, 120))
        return cartas
    #função para carregar as imagens das fichas
    def carregar_fichas(self):
        return {
            "1": pygame.transform.scale(pygame.image.load(os.path.join("Fichas", "Ficha_1.png")), (60, 60)),
            "5": pygame.transform.scale(pygame.image.load(os.path.join("Fichas", "Ficha_5.png")), (60, 60)),
            "25": pygame.transform.scale(pygame.image.load(os.path.join("Fichas", "Ficha_25.png")), (60, 60)),
            "100": pygame.transform.scale(pygame.image.load(os.path.join("Fichas", "Ficha_100.png")), (60, 60)),
        }
    #cria a area clicavel das fichas
    def criar_clicavel_fichas(self):
        return {
            "1": pygame.Rect(50, 500, 60, 60),
            "5": pygame.Rect(100, 500, 60, 60),
            "25": pygame.Rect(150, 500, 60, 60),
            "100": pygame.Rect(200, 500, 60, 60),
        }
    #cria a tela de tutorial
    def tela_tutorial(self):
        fundo_imagem = pygame.image.load('./Fundo/Fundo.jpeg')  # Adicione uma imagem de fundo para o tutorial
        fundo_imagem = pygame.transform.scale(fundo_imagem, (self.largura, self.altura))  # Ajustar ao tamanho da tela

        while True:
            self.tela.blit(fundo_imagem, (0, 0))  # Desenhar a imagem de fundo

            # Adicionar texto com as regras
            titulo = self.fonte.render("Regras do Blackjack", True, (255, 255, 255))
            regras = [
                "1. O objetivo é somar 21 pontos ou o mais próximo possível sem ultrapassar.",
                "2. Valetes, Rainhas e Reis valem 10 pontos.",
                "3. Ases podem valer 1 ou 11 pontos, dependendo da sua mão",
                "(Sem ela for menor que 21 vale 1).",
                "4. Você pode pedir mais cartas ou parar quando quiser.",
                "5. Se você ultrapassar 21 pontos, você perde automaticamente.",
                "6. O dealer joga após você parar, devendo somar pelo menos 17 pontos.",
                "7. Empate ocasiona em derrota",
                "",
                "A GANÂNCIA QUE MOVE O HOMEM É A MESMA QUE MATA",
                "(NÃO APOSTE TUDO O QUE VC TEM!)"
            ]

            # Posicionar o título e as regras
            self.tela.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, 50))
            y_offset = 150
            for regra in regras:
                texto_regra = self.fonte.render(regra, True, (255, 255, 255))
                self.tela.blit(texto_regra, (50, y_offset))
                y_offset += 50

            # Instruções para voltar ao menu 
            voltar_menu = self.fonte.render("Pressione ESC para voltar ao menu", True, (255, 255, 255))

            self.tela.blit(voltar_menu, (50, self.altura - 80))
            #atualiza a tela
            pygame.display.update()
            #cria os eventos para sair 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # Voltar ao menu principal
                        return

    # cria a tela de menu
    def menu(self):
        # Carregar a imagem de fundo
        fundo_imagem = pygame.image.load('./Fundo/Menu.jpeg') 
        fundo_imagem = pygame.transform.scale(fundo_imagem, (self.largura, self.altura))  

        while True:
            self.fonte_pixelada = pygame.font.Font('./FontePixel/PressStart2P-Regular.ttf', 20) # fonte 
            self.fonte_pixelada1 = pygame.font.Font('./FontePixel/PressStart2P-Regular.ttf', 40)
            self.tela.blit(fundo_imagem, (0, 0))  # Desenhar a imagem de fundo
            titulo = self.fonte_pixelada1.render("TIGRINHO JACK", True, (255, 255, 255))
            opcao_jogar = self.fonte_pixelada.render("Pressione ENTER para Jogar", True, (255, 255, 255)) # Instruções para iniciar o jogo
            opcao_sair = self.fonte_pixelada.render("Pressione ESC para Sair", True, (255, 255, 255)) # Instruções para sair
            opcao_tutorial = self.fonte_pixelada.render("Pressione T para Tutorial", True, (255, 255, 255)) # Instruções para ver tutorial

            self.tela.blit(opcao_tutorial, (self.largura // 2.5 - opcao_tutorial.get_width() // 2, self.altura // 2 + 200))
            self.tela.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, self.altura // 3 - 200))
            self.tela.blit(opcao_jogar, (self.largura // 2.5 - opcao_jogar.get_width() // 2, self.altura // 2))
            self.tela.blit(opcao_sair, (self.largura // 2.5 - opcao_sair.get_width() // 2, self.altura // 2 + 100))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:  # Enter
                        return  # Sair do menu e iniciar o jogo
                    elif event.key == K_ESCAPE:  # Escape
                        pygame.quit()
                        exit()
                    elif event.key == K_t:  # T para abrir o tutorial
                        self.tela_tutorial()

    #função para criar o baralho
    def criar_baralho(self):
        naipes = ['Copas', 'Espadas', 'Paus', 'Ouros']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']
        return [(valor, naipe) for naipe in naipes for valor in valores]

    #Função para dar valor as cartas sem pontuação como o rei
    def carta_valor(self, carta, pontuacao_atual=0):
        if carta[0] in ['Valete', 'Rainha', 'Rei']:
            return 10
        elif carta[0] == 'As': # o As pode valer tanto 11 quanto 1 dependendo dos valores das outras cartas
            return 11 if pontuacao_atual + 11 <= 21 else 1
        else:
            return int(carta[0])

    # Métodos para lógica de jogo: pedir_carta, parar, apostar, etc.
    def pedir_carta(self):
        if self.jogo_em_andamento:
            # Verificar se o baralho está vazio
            if not self.baralho:
                print("Baralho vazio! Recriando e embaralhando...")
                self.baralho = self.criar_baralho()
                random.shuffle(self.baralho)

            # Remover a carta do topo do baralho
            carta = self.baralho.pop()
            self.cartas_jogador.append(carta)
            self.pontos_jogador += self.carta_valor(carta, self.pontos_jogador)
            
            if self.pontos_jogador == 21:
                self.mensagem_final = "Jackpot! Você ganhou!"
                self.jogo_em_andamento = False
                if self.saldo == 0:
                    self.reiniciar_jogo()
                else:
                    # Reiniciar aposta para nova rodada
                    self.aposta = 0
                    print("Aposta reiniciada para nova rodada.")
            elif self.pontos_jogador > 21:
                self.mensagem_final = "Você perdeu!"
                self.jogo_em_andamento = False
                if self.saldo == 0:
                    self.reiniciar_jogo()
                else:
                    # Reiniciar aposta para nova rodada
                    self.aposta = 0
                    print("Aposta reiniciada para nova rodada.")
    # Retira uma carta do baralho, recriando-o se estiver vazio.
    def retirar_carta(self):
        if not self.baralho:
            print("Baralho vazio! Recriando e embaralhando...")
            self.baralho = self.criar_baralho()
            random.shuffle(self.baralho)
        return self.baralho.pop()
    #Função para parar a rodada
    def parar(self):
        if self.jogo_em_andamento:
            print(f"Você parou com {self.pontos_jogador} pontos.")
            self.jogo_em_andamento = False
            self.jogar_bot()
    #Função para apostar
    def apostar(self):
        if not self.jogo_em_andamento:
            if self.aposta > 0:
                self.mensagem_final = ""
                print(f"Aposta confirmada: {self.aposta}")
                self.jogo_em_andamento = True

                # Resetar variáveis de jogo
                self.cartas_jogador = []
                self.cartas_bot = []
                self.pontos_jogador = 0
                self.pontos_bot = 0

                # Distribuir cartas iniciais
                self.adicionar_carta_jogador()
                self.adicionar_carta_jogador()
                self.adicionar_carta_bot()
                self.adicionar_carta_bot()
            else:
                print("Por favor, aposte um valor válido antes de começar.")
        else:
            print("O jogo já está em andamento. Termine a rodada antes de apostar novamente.")
    #função que reinicia a rodada
    def reiniciar_jogo(self):
        if self.saldo == 0:
            self.mensagem_final = "FIM DE JOGO! Saldo reiniciado."
            self.saldo = 200  # Reiniciar saldo se acabou
        self.aposta = 0  # Reiniciar a aposta para nova rodada
        self.cartas_jogador = []
        self.cartas_bot = []
        self.pontos_jogador = 0
        self.pontos_bot = 0
        self.jogo_em_andamento = False
        print("Pronto para uma nova rodada!")
        
    #função para adicionar carta ambas as duas
    def adicionar_carta_jogador(self):
        carta = self.retirar_carta()
        self.cartas_jogador.append(carta)
        self.pontos_jogador += self.carta_valor(carta, self.pontos_jogador)

    def adicionar_carta_bot(self):
        carta = self.retirar_carta()
        self.cartas_bot.append(carta)
        self.pontos_bot += self.carta_valor(carta, self.pontos_bot)

    #Funcionalidade do bot
    def jogar_bot(self):
        while self.pontos_bot < 17:
            self.adicionar_carta_bot()

        if self.pontos_bot > 21 or self.pontos_jogador > self.pontos_bot:
            self.mensagem_final = "Você ganhou!"
            self.saldo += self.aposta * 2  # O jogador ganha o dobro da aposta
        else:
            self.mensagem_final = "O bot ganhou!"

        self.jogo_em_andamento = False

        # Verificar se o saldo acabou
        if self.saldo == 0:
            self.reiniciar_jogo()
        else:
            # Reiniciar aposta para nova rodada
            self.aposta = 0
            print("Aposta reiniciada para nova rodada.")


    def desenhar_tela(self):
        self.tela.fill(self.cor_fundo)
        self.tela.blit(self.img_mesa, (0, 0))

        # Exibir saldo e aposta
        texto_saldo = self.fonte.render(f"Saldo: {self.saldo}", True, (255, 255, 255))
        texto_aposta = self.fonte.render(f"Aposta: {self.aposta}", True, (255, 255, 255))
        self.tela.blit(texto_saldo, (50, 30))
        self.tela.blit(texto_aposta, (50, 100))

        # Exibir fichas
        for valor, img in self.fichas.items():
            self.tela.blit(img, (self.ret_fichas[valor].x, self.ret_fichas[valor].y))

        # Exibir cartas na mesa
        x_cartas = 400
        for carta in self.cartas_jogador:
            self.tela.blit(self.cartas[(carta[0], carta[1])], (x_cartas, 500))
            x_cartas += 100

        # Exibir cartas do bot (uma virada para baixo se o jogo está em andamento)
        x_cartas = 400
        for i, carta in enumerate(self.cartas_bot):
            if i == 0 and self.jogo_em_andamento:
                carta_virada = pygame.transform.scale(pygame.image.load(".\\Costa Baralho\\Costas_Baralho.png"), (80, 120))
                self.tela.blit(carta_virada, (x_cartas, 300))
            else:
                self.tela.blit(self.cartas[carta], (x_cartas, 300))
            x_cartas += 100

        # Desenhar botões
        pygame.draw.rect(self.tela, self.cor_botao, self.ret_pedir_carta)
        pygame.draw.rect(self.tela, self.cor_botao, self.ret_parar)
        pygame.draw.rect(self.tela, self.cor_botao, self.ret_apostar)

        texto_pedir_carta = self.fonte.render("Pedir Carta", True, self.cor_texto_botao)
        texto_parar = self.fonte.render("Parar", True, self.cor_texto_botao)
        texto_apostar = self.fonte.render("Apostar", True, self.cor_texto_botao)

        self.tela.blit(texto_pedir_carta, (self.ret_pedir_carta.x + 10, self.ret_pedir_carta.y + 5))
        self.tela.blit(texto_parar, (self.ret_parar.x + 50, self.ret_parar.y + 5))
        self.tela.blit(texto_apostar, (self.ret_apostar.x + 20, self.ret_apostar.y + 5))
        
        if self.mensagem_final:
            texto_mensagem = self.fonte.render(self.mensagem_final, True, (255, 0, 0))
            self.tela.blit(texto_mensagem, ((self.largura - texto_mensagem.get_width()) // 2, self.altura // 2 + 75))

    def rodar(self):
        """Controla o fluxo principal do jogo."""
        self.menu()  # Exibir o menu antes do jogo começar
        while True:
            self.desenhar_tela()
            voltar_menu = self.fonte.render("Pressione ESC para voltar ao menu", True, (255, 255, 255))
            self.tela.blit(voltar_menu, (750, self.altura - 750))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # Voltar ao menu principal
                        self.menu()
                if event.type == MOUSEBUTTONDOWN:
                    if self.ret_pedir_carta.collidepoint(event.pos): # pede carta
                        self.pedir_carta()

                    elif self.ret_parar.collidepoint(event.pos): # parar
                        self.parar()

                    elif self.ret_apostar.collidepoint(event.pos): # apostar
                        self.apostar()
                    # crescentar valor das fichas
                    for valor, rect in self.ret_fichas.items():
                        if rect.collidepoint(event.pos):
                            valor_ficha = int(valor)
                            if self.saldo >= valor_ficha:
                                self.aposta += valor_ficha
                                self.saldo -= valor_ficha
                                print(f"Saldo atual: {self.saldo}, Aposta: {self.aposta}")

                                # Verificar se o saldo acabou
                                if self.saldo == 0:
                                    self.reiniciar_jogo()
            pygame.display.update()

#roda o jogo
if __name__ == "__main__":
    jogo = BlackjackPygame()
    jogo.rodar()