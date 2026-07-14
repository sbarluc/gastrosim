class Reloj():

    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora = hora if self._hora_en_rango(hora) else 0
        self.minuto = minuto if self._minuto_en_rango(minuto) else 0
        self.segundo = segundo if self._minuto_en_rango(segundo) else 0

    def avanzar(self):
        self.segundo += 1
        if not self._segundo_en_rango(self.segundo):
            self.segundo = 0
            self.minuto += 1
            if not self._minuto_en_rango(self.minuto):
                self.minuto = 0
                self.hora += 1 if self._hora_en_rango(self.hora + 1) else -23

    def _hora_en_rango(self, hora):
        return (hora <= 23 and hora >= 0)

    def _minuto_en_rango(self, minuto):
        return (minuto <= 59 and minuto >= 0)
    
    def _segundo_en_rango(self, segundo):
        return (segundo <= 59 and segundo >= 0)

    
    def __repr__(self):
        return (
            f"{0 if self.hora<10 else ''}{self.hora}:" + \
            f"{0 if self.minuto<10 else ''}{self.minuto}:" + \
            f"{0 if self.segundo<10 else ''}{self.segundo}"
        )