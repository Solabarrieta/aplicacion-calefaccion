class Radiador:
    def __init__(self, id, nombre, status,temperatura):
        self.id=id
        self.nombre=nombre
        self.status=status
        self.temperatura=temperatura
    def toString(self):
        s = "{},{}".format(self.id,self.nombre.encode('utf8'))
        return s
    # Metodo para simular que no se puede acceder al objeto.
    def connect(self):
        return True;