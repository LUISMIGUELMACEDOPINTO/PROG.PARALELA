#include <iostream>
#include <omp.h>

int main() {
    // Variables para almacenar los números a sumar y el resultado
    int num1 = 5, num2 = 7, resultado = 0;

    // Inicio de la región paralela
    #pragma omp parallel
    {
        // Cada hilo suma los números
        #pragma omp single
        std::cout << "Sumando números en paralelo...\n";

        // Sección crítica para evitar condiciones de carrera
        #pragma omp atomic
        resultado += num1 - num2;
    } // Fin de la región paralela

    // Imprimir el resultado
    std::cout << "La suma de " << num1 << " y " << num2 << " es: " << resultado << std::endl;

    return 0;
}
