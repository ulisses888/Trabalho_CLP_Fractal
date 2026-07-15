Trabalho da disciplina Conceitos de Linguagens de Programação
Nome: Ulisses Gilioli Francescatto Junior
Turma: T1

 Implementar uma aplicação gráfica com apoio de duas linguagens de programação, a escolha. O desafio consiste em realizar o uso conjunto de duas linguagens de programação, sendo o desafio especificamente, realizar o uso conjunto das linguagens. Uma das linguagens deve ser utilizado para oferecer uma interface com o usuário e apresentar a imagem gerada. A outra deve ser utilizada para implementar o serviço de cálculo desejado.

Implementado um Fractal de Mandelbrot utilizando linguagem C  e Python

 Arquivos do repositório

 - mandelbrot.c - 1ª Parte do trabalho onde é realizado o calculo do Fractal de Mandelbrot escrito em C.
 - interface.py - 2ª Parte do trabalho onde é criada a interface gráfica e importa o libmandelbrot.so (1ª parte compilada) via ctypes.
 - Makefile - Automatiza a instalação de dependências, compilação da biblioteca e execução do programa.
 - README.md - Este arquivo.
 - documentacao.pdf - Documentação da implementação.

Dependências:
- gcc
- Python 3
- Pacotes Python: pygame e numpy

Os pacotes python são instaladas no Makefile, para compilar tudo é so colocar no terminal make e para rodar o programa make run, o programa foi testado somente no Linux não é garantido que vai funcionar da mesma forma no Windows.

Para compilar e executar no terminal coloque: (Ele ja executa no primeiro make, posteriormente só usar o make run para não precisar compilar novamente)
- make
- make run

Controles:
- Clique esquerdo: zoom in na região clicada
- Clique direito: zoom out
