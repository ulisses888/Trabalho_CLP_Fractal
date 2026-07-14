# Variáveis de configuração
CC = gcc
CFLAGS = -shared -fPIC -O3 -Wall
C_SOURCE = mandelbrot.c
LIB_NAME = libmandelbrot.so
PY_SCRIPT = interface.py
PYTHON = python3

# Alvo padrão: instala dependências, compila e roda tudo automaticamente
all: deps $(LIB_NAME) run

# Verifica e instala as dependências do Python se necessário
deps:
	@$(PYTHON) -c "import pygame, numpy" 2>/dev/null || ( \
		echo "Instalando dependências do Python (pygame, numpy)..."; \
		$(PYTHON) -m pip install pygame numpy --break-system-packages 2>/dev/null || \
		$(PYTHON) -m pip install pygame numpy \
	)

# Regra para compilar a biblioteca compartilhada (.so) no Linux
$(LIB_NAME): $(C_SOURCE)
	$(CC) $(CFLAGS) -o $(LIB_NAME) $(C_SOURCE)

# Regra para rodar o script em Python
run:
	$(PYTHON) $(PY_SCRIPT)

# Limpa o arquivo compilado para forçar uma nova compilação
clean:
	rm -f $(LIB_NAME)

.PHONY: all deps run clean
