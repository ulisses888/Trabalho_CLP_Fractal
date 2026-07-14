#include <stdint.h>

void calcular_mandelbrot(int largura, int altura, int max_iteracao,
                         double x_min, double x_max, double y_min, double y_max,
                         int32_t *resultado) {
    
    for (int tela_y = 0; tela_y < altura; tela_y++) {
        for (int tela_x = 0; tela_x < largura; tela_x++) {
            
            double cx = x_min + (tela_x * (x_max - x_min) / largura);
            double cy = y_min + (tela_y * (y_max - y_min) / altura);

            double x = 0.0;
            double y = 0.0;
            int iteracao = 0;

            while (x*x + y*y <= 4.0 && iteracao < max_iteracao) {
                double x_novo = x*x - y*y + cx;
                y = 2.0 * x * y + cy;
                x = x_novo;
                iteracao++;
            }

            resultado[tela_y * largura + tela_x] = iteracao;
        }
    }
}
