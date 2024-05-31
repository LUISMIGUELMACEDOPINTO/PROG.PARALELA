#include <iostream>
#include <omp.h>

int main() {
    // Variables para almacenar los n�meros a sumar y el resultado
    int num1 = 5, num2 = 7, resultado = 0;

    // Inicio de la regi�n paralela
    #pragma omp parallel
    {
        // Cada hilo suma los n�meros
        #pragma omp single
        std::cout << "Sumando n�meros en paralelo...\n";

        // Secci�n cr�tica para evitar condiciones de carrera
        #pragma omp atomic
        resultado += num1 - num2;
    } // Fin de la regi�n paralela

    // Imprimir el resultado
    std::cout << "La suma de " << num1 << " y " << num2 << " es: " << resultado << std::endl;

    return 0;
}
