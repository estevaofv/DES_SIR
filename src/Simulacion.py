#!/usr/bin/env python
# Implementacion del Modelo SIR
# Autor: Jorge Parrilla

# Externas
from pylab import *
import scipy.integrate as spi
from decimal import Decimal

# Propias
from Graficar import Graficar
from ModeloSIR import ModeloSIR

modelo  = ModeloSIR()
grafica = Graficar()

modelo.set_poblacion_inicial(99900, 100, 0)
modelo.set_parametros(0.50, 0.10)
modelo.set_intervalos(1, 100, .02)

poblacion_inicial   = modelo.get_poblacion_array()
intervalos          = modelo.get_intervalos()

modelo_SIR = spi.odeint(modelo.get_ecuaciones_diferenciales, poblacion_inicial, intervalos)

S   = (modelo_SIR[:,0])
I   = (modelo_SIR[:,1])
R   = (modelo_SIR[:,2])

x = arange(len(modelo_SIR),dtype=float)

for i in x:
    x[i]=(x[i]*.02)

datos_SIR = vstack([S,I,R,x])

grafica.generar_grafica(datos_SIR)
