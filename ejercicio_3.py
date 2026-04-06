
from ejercicio_2 import Punto

class Linea:
    def __init__(self, _punto_a, _punto_b):
        self.punto_a = _punto_a
        self.punto_b = _punto_b
    def mueve_derecha(self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia
    def mueve_izquierda(self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia
    def mueve_arriba(self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia
    def mueve_abajo(self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia
    