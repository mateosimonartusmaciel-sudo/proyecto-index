import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Juego: Atrapar Cosas")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Jugador (canasta)
jugador_ancho = 80
jugador_alto = 20
jugador_x = ANCHO // 2 - jugador_ancho // 2
jugador_y = ALTO - 40
velocidad_jugador = 7

# Objeto que cae
objeto_ancho = 20
objeto_alto = 20
objeto_x = random.randint(0, ANCHO - objeto_ancho)
objeto_y = -20
velocidad_objeto = 5

# Puntuación
puntos = 0
fuente = pygame.font.SysFont("Arial", 24)

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_ancho:
        jugador_x += velocidad_jugador

    # Movimiento del objeto
    objeto_y += velocidad_objeto
    if objeto_y > ALTO:
        objeto_y = -20
        objeto_x = random.randint(0, ANCHO - objeto_ancho)

    # Colisión
    if (jugador_x < objeto_x + objeto_ancho and
        jugador_x + jugador_ancho > objeto_x and
        jugador_y < objeto_y + objeto_alto and
        jugador_y + jugador_alto > objeto_y):
        puntos += 1
        objeto_y = -20
        objeto_x = random.randint(0, ANCHO - objeto_ancho)

    # Dibujar
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, AZUL, (jugador_x, jugador_y, jugador_ancho, jugador_alto))
    pygame.draw.rect(pantalla, ROJO, (objeto_x, objeto_y, objeto_ancho, objeto_alto))

    texto = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)