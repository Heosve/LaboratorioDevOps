class Carro:
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
mi_carro = Carro(marca="Toyota", modelo="Corolla", color="Rojo")
print(f"Mi carro es un {mi_carro.marca} {mi_carro.modelo} de color {mi_carro.color}")

mi_carro.acelerar(20)
mi_carro.frenar(10)
mi_carro.acelerar(50)
mi_carro.frenar(70)