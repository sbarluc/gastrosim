class Reloj():

    def __init__(self, hora=0, minuto=0):
        self.hora = hora if self._hora_en_rango(hora) else 0
        self.minuto = minuto if self._minuto_en_rango(minuto) else 0

    def avanzar(self):
        self.minuto += 1
        if not self._minuto_en_rango(self.minuto):
            self.minuto = 0
            self.hora += 1 if self._hora_en_rango(self.hora + 1) else -23

    def _hora_en_rango(self, hora):
        return (hora <= 23 and hora >= 0)

    def _minuto_en_rango(self, minuto):
        return (minuto <= 59 and minuto >= 0)