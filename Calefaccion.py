class Calefaccion:
    def __init__(self, id, nombre, status,temperatura):
        self.id=id
        self.nombre=nombre
        self.status=status
        self.temperatura=temperatura
    def toString(self):
        s = "{},{}".format(self.id,self.nombre)
        return s