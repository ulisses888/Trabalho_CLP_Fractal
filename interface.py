import ctypes
import os
import sys
import numpy as np
import pygame

# Configurações da Janela
LARGURA, ALTURA = 800, 600
MAX_ITERACAO = 150

x_min, x_max = -2.0, 0.5
y_min, y_max = -1.2, 1.2

if sys.platform.startswith("win"):
    lib = ctypes.CDLL("./mandelbrot.dll")
else:
    lib = ctypes.CDLL("./libmandelbrot.so")

lib.calcular_mandelbrot.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_int32),
]

# Inicializa a Interface Grafca
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mandelbrot C + Python (Clique para dar Zoom)")


def renderizar_fractal():
    """Chama o código em C e desenha os pixels na tela do Pygame"""
    matriz_resultado = np.zeros(LARGURA * ALTURA, dtype=np.int32)
    ponteiro_c = matriz_resultado.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))

    lib.calcular_mandelbrot(
        LARGURA, ALTURA, MAX_ITERACAO, x_min, x_max, y_min, y_max, ponteiro_c
    )

    dados_finais = matriz_resultado.reshape((ALTURA, LARGURA))

    superficie = pygame.Surface((LARGURA, ALTURA))
    pixels = pygame.PixelArray(superficie)

    for y in range(ALTURA):
        for x in range(LARGURA):
            iteracao = dados_finais[y, x]
            if iteracao == MAX_ITERACAO:
                pixels[x, y] = (0, 0, 0)  # Dentro do conjunto (Preto)
            else:
                r = (iteracao * 7) % 256
                g = (iteracao * 5) % 256
                b = (iteracao * 11) % 256
                pixels[x, y] = (r, g, b)

    return superficie


rodando = True
precisa_recalcular = True
fractal_surface = None

while rodando:
    if precisa_recalcular:
        fractal_surface = renderizar_fractal()
        precisa_recalcular = False

    tela.blit(fractal_surface, (0, 0))
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            clique_cx = x_min + (mouse_x * (x_max - x_min) / LARGURA)
            clique_cy = y_min + (mouse_y * (y_max - y_min) / ALTURA)

            largura_atual = x_max - x_min
            altura_atual = y_max - y_min

            if evento.button == 1:
                x_min = clique_cx - largura_atual / 4
                x_max = clique_cx + largura_atual / 4
                y_min = clique_cy - altura_atual / 4
                y_max = clique_cy + altura_atual / 4
            elif evento.button == 3:
                x_min = clique_cx - largura_atual * 1
                x_max = clique_cx + largura_atual * 1
                y_min = clique_cy - altura_atual * 1
                y_max = clique_cy + altura_atual * 1

            precisa_recalcular = True

pygame.quit()
