import pygame
from pygame.locals import *
from sys import exit
import random
import os  
import variaveis


pygame.init()
pygame.mixer.init()

# exportando as pastas

pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'imagens')
pasta_sons = os.path.join(pasta_principal, 'sons')

# fps do jogo
relogio = pygame.time.Clock()

# configuração da tela

tela = pygame.display.set_mode((variaveis.largura, variaveis.altura))
pygame.display.set_caption(variaveis.nome_do_jogo)



aleatoriedade = random.choice(variaveis.npc)
# configuração da musica de fundo

musica = pygame.mixer.music.load(os.path.join(pasta_sons, variaveis.musica_fundo))
pygame.mixer.music.play(-1)



# carregando a imagem da sprite
spriteSheet = pygame.image.load(os.path.join(pasta_imagens, 'pacman_sprite.png')).convert_alpha()



# gerando o piso do jogo


class Piso(pygame.sprite.Sprite):
    def __init__(self, posiçãox):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((11 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*4, 32*4 ))
        self.rect = self.image.get_rect()
        self.rect.y = variaveis.altura - 128
        self.rect.x = posiçãox * 128



    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = variaveis.largura
        self.rect.x -= variaveis.velocidade


# criando o pacman

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_pacman = []  # lista de sprite do pacman
        for i in range(3):
            img = spriteSheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_pacman.append(img)
  
        self.i_lista = 0
        self.image = self.imagens_pacman[self.i_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.y_inicial = variaveis.altura - 60 - 96//2
        self.x_inicial = variaveis.largura - 600
        self.rect.center = (100, variaveis.altura - 60)
        self.pulo = False

    # metodo pular

    def pular(self):
        self.pulo = True

    # metodo de atualização do pacman
    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
           # self.rect.x += 2
           
        else:
            if self.rect.y < self.y_inicial:
                self.rect.y += 20
               # self.rect.x -= 1
        
            else:
                self.rect.y = self.y_inicial
               # self.rect.x = self.x_inicial+1

        if self.i_lista > 2:
            self.i_lista = 0
        self.i_lista += 0.25
        self.image = self.imagens_pacman[int(self.i_lista)]
 



# criando as moedas
class Moedas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((12 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.aleatorio = aleatoriedade
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (variaveis.largura, variaveis.altura-60)
        self.rect.x = variaveis.largura

  # fazer a moeda reiniciar na tela
    def update(self):
        if self.aleatorio == "moedinha":
            if self.rect.topright[0] < 0:
                self.rect.x = variaveis.largura
            self.rect.x -= variaveis.velocidade




#criando  moeda dos pontos
class Moeda_parada(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((12 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.center = (490, 45)




# inimigo vermelho
class Inimigo_vermelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_vermelho = []
        for i in range(3, 5):
            img = spriteSheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2.9, 32*2.9))
            self.imagens_vermelho.append(img)

        self.i_lista = 0
        self.image = self.imagens_vermelho[self.i_lista]
        self.rect = self.image.get_rect()
        self.aleatorio = aleatoriedade
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (variaveis.largura, variaveis.altura-49)
        self.rect.x = variaveis.largura
        

    def update(self):
        if self.aleatorio == "vermelho":
            if self.rect.topright[0] < 0:
                self.rect.x = variaveis.largura
            self.rect.x -= variaveis.velocidade

            if self.i_lista > 1:
                self.i_lista = 0
            self.i_lista += 0.09
            self.image = self.imagens_vermelho[int(self.i_lista)]




# inimigo rosa
class Inimigo_rosa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_rosa = []
        for i in range(5, 7):
            img = spriteSheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2.9, 32*2.9))
            self.imagens_rosa.append(img)

        self.i_lista = 0
        self.image = self.imagens_rosa[self.i_lista]
        self.rect = self.image.get_rect()
        self.aleatorio = aleatoriedade
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (variaveis.largura, variaveis.altura-49)
        self.rect.x = variaveis.largura
        

    def update(self):
        if self.aleatorio == "rosa":
            if self.rect.topright[0] < 0:
                self.rect.x = variaveis.largura
            self.rect.x -= variaveis.velocidade

    
            if self.i_lista > 1:
                self.i_lista = 0
            self.i_lista += 0.09
            self.image = self.imagens_rosa[int(self.i_lista)]



# inimigo amarelo
class Inimigo_amarelo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_amarelo = []
        for i in range(7, 9):
            img = spriteSheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2.9, 32*2.9))
            self.imagens_amarelo.append(img)

        self.i_lista = 0
        self.image = self.imagens_amarelo[self.i_lista]
        self.aleatorio = aleatoriedade
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (variaveis.largura, variaveis.altura-49)
        self.rect.x = variaveis.largura
        self.aleatorio = aleatoriedade


    def update(self):
        if self.aleatorio == "amarelo":
            if self.rect.topright[0] < 0:
                self.rect.x = variaveis.largura
            self.rect.x -= variaveis.velocidade

    
            if self.i_lista > 1:
                self.i_lista = 0
            self.i_lista += 0.09
            self.image = self.imagens_amarelo[int(self.i_lista)]



# inimigo azul
class Inimigo_azul(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_azul = []
        for i in range(9, 11):
            img = spriteSheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2.9, 32*2.9 ))
            self.imagens_azul.append(img)

        self.i_lista = 0
        self.image = self.imagens_azul[self.i_lista]
        self.aleatorio = aleatoriedade
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (variaveis.largura, variaveis.altura-49)
        self.rect.x = variaveis.largura
        

    
    def update(self):
        if self.aleatorio == "azul":
            if self.rect.topright[0] < 0:
                self.rect.x = variaveis.largura
            self.rect.x -= variaveis.velocidade

 
            if self.i_lista > 1:
                self.i_lista = 0   
            self.i_lista += 0.09
            self.image = self.imagens_azul[int(self.i_lista)]





#grupos
grupo_imagens = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
pontinhos = pygame.sprite.Group()




#atualizar a aleatoriedade dos inimigos e da moeda
def ale():
    moeda = Moedas()
    grupo_imagens.add(moeda)
    pontinhos.add(moeda)
    aleatoriedade = random.choice(variaveis.npc)
    moeda.rect.x = variaveis.largura  
    moeda.aleatorio = aleatoriedade
    inimigo_vermelho.rect.x = variaveis.largura
    inimigo_vermelho.aleatorio = aleatoriedade
    inimigo_azul.rect.x = variaveis.largura
    inimigo_azul.aleatorio = aleatoriedade
    inimigo_rosa.rect.x = variaveis.largura
    inimigo_rosa.aleatorio = aleatoriedade
    inimigo_amarelo.rect.x = variaveis.largura
    inimigo_amarelo.aleatorio = aleatoriedade


#retornar o jogo
def retorna():
    variaveis.pontos = 0 
    variaveis.velocidade = 8
    variaveis.teste = False
    pygame.mixer.music.play(-1)
    pacman.y_inicial = variaveis.altura - 60 - 96//2
    ale()



#textos 
def textinho_tela(pontuação, tamanho, cor):
    fonte_jogo = pygame.font.SysFont("arial", tamanho, True, False)
    mensagem_tela = f"{pontuação}"
    pontos_forma = fonte_jogo.render(mensagem_tela, True, cor)
    return pontos_forma






#gerando o pacman
pacman = Pacman()
grupo_imagens.add(pacman)

# gerando moedas
moeda = Moedas()
grupo_imagens.add(moeda)
pontinhos.add(moeda)

moeda_parada = Moeda_parada()
grupo_imagens.add(moeda_parada)

# gerando inimigo vermelho  
inimigo_vermelho = Inimigo_vermelho()
grupo_imagens.add(inimigo_vermelho)
inimigos.add(inimigo_vermelho)

#gerando inimigo rosa 
inimigo_rosa = Inimigo_rosa()
grupo_imagens.add(inimigo_rosa)
inimigos.add(inimigo_rosa)

#gerando inimigo amarelo 
inimigo_amarelo = Inimigo_amarelo()
grupo_imagens.add(inimigo_amarelo)
inimigos.add(inimigo_amarelo)

#gerando inimigo azul
inimigo_azul = Inimigo_azul()
grupo_imagens.add(inimigo_azul)
inimigos.add(inimigo_azul)

# gerando o piso e quantos pisos cabem na tela
for i in range(variaveis.largura):
    piso = Piso(i)
    grupo_imagens.add(piso)



# loop principal do jogo
while True:
    relogio.tick(variaveis.fps)
    tela.fill(variaveis.preto)  
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                if pacman.rect.y != pacman.y_inicial:
                    pass
                else:
                    pacman.pular()
            
            if evento.key == K_LSHIFT and variaveis.teste == True or evento.key == K_RSHIFT and variaveis.teste == True:
                retorna() 

    
    #colisões 
    colidindo = pygame.sprite.spritecollide(pacman, inimigos, False, pygame.sprite.collide_mask)
    colidindo_moeda = pygame.sprite.spritecollide(pacman, pontinhos, True, pygame.sprite.collide_mask)
    
    #texto
    texto = textinho_tela(variaveis.pontos, 45, variaveis.branco) 
    tela.blit(texto, (520,30))


    #colisão da moeda 
    if colidindo_moeda:
        variaveis.pontos += 1
        ale()     
    if inimigo_amarelo.rect.topright[0] <= 0:
        ale() 
    elif inimigo_azul.rect.topright[0] <= 0 : 
        ale()
    elif inimigo_rosa.rect.topright[0] <= 0 :
        ale()
    elif inimigo_vermelho.rect.topright[0] <= 0:   
        ale()
    elif moeda.rect.topright[0]<= 0:
        ale()
         
    
        
    
    # adcionar sprite na tela
    grupo_imagens.draw(tela)
    
    #colidindo com o inimigo 
    if colidindo: 
        mensagem_perdeu = textinho_tela("PERDEU AMIGO", 35, variaveis.branco)
        tela.blit(mensagem_perdeu,(180,100))
        mensagem_voltar = textinho_tela("Aperte SHIFT para reiniciar", 20, variaveis.branco)
        tela.blit(mensagem_voltar,(183,150)) 
        mensagem_pontos = textinho_tela(f"Seus pontos {variaveis.pontos}", 20, variaveis.branco)
        tela.blit(mensagem_pontos,(183,180)) 
        variaveis.teste = True
        pygame.mixer.music.stop()

        
        
    else:   
        grupo_imagens.update()
        variaveis.pontos_total += 1

    #velocidade do jogo 
    if variaveis.pontos_total % 120 == 0:
        variaveis.velocidade += 1
     

    # atualizar a tela
    pygame.display.flip()
 