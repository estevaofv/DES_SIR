#!/usr/bin/env python
# Implementacion del Modelo SIR
# Autor: Jorge Parrilla

from pylab import *

class Graficar:
    figura = figure()
    def generar_grafica(self, datos):
        eje_x = self.figura.add_subplot(111)
        plot(datos[3], datos[0], 'g--', datos[3], datos[1], 'r-', datos[3], datos[2], '-.b', linewidth=3)
        xlabel("Tiempo (Dias)")
        ylabel("Poblacion")
        title("Modelo SIR")
        grid(False)
        legend(("Susceptibles", "Infectados", "Recuperados"), shadow=True, fancybox=True)
        show()
