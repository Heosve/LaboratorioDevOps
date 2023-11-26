class Moto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El carro {self.marca} {self.modelo} acelera a {self.velocidad} km/h")

    def frenar(self, decremento):
        if self.velocidad - decremento < 0:
            self.velocidad = 0
        else:
            self.velocidad -= decremento
        print(f"El carro {self.marca} {self.modelo} frena a {self.velocidad} km/h")

# Uso de la clase Carro
mi_moto = Moto(marca="Royal enfield", modelo="Hymalyan", color="Negra")
print(f"Mi carro es un {mi_moto.marca} {mi_moto.modelo} de color {mi_moto.color}")

mi_carro.acelerar(20)
mi_carro.frenar(10)
mi_carro.acelerar(50)
mi_carro.frenar(70)