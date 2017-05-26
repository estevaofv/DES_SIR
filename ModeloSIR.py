#!/usr/bin/env python
# Implementacion del Modelo SIR
# Autor: Jorge Parrilla

import numpy as np
from pylab import *
import scipy.integrate as spi
from decimal import Decimal

class ModeloSIR:
    _S_Inicial  = 0
    _I_Inicial  = 0
    _R_Inicial  = 0
    _N          = 0
    _Beta       = 0
    _Gamma      = 0
    _intervalos = 0

    def set_poblacion_inicial(self, S, I, R):
        self._S_Inicial = S
        self._I_Inicial = I
        self._R_Inicial = R
        self._N         = S + I + R

    def set_parametros(self, Beta, Gamma):
        self._Beta      = Beta
        self._Gamma     = Gamma

    def set_intervalos(self, inicio, fin, steps):
        self._intervalos = np.arange(inicio, fin, steps)

    def get_poblacion_array(self):
        return (self._S_Inicial, self._I_Inicial, self._R_Inicial)

    def get_intervalos(self):
        return self._intervalos

    def get_ecuaciones_diferenciales(self, poblacion, t):
        e_dif      = np.zeros((3))
        e_dif[0]   = -self._Beta   * poblacion[0]  * poblacion[1]/self._N
        e_dif[1]   = self._Beta    * poblacion[0]  * poblacion[1]/self._N - (self._Gamma * poblacion[1])
        e_dif[2]   = self._Gamma   * poblacion[1]
        return e_dif
