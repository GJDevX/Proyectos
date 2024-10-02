#Codigo de ensayo para proyecto de venta de casas.
class Casas:
    def __init__(self,tamaño:str,color:str,ubicacion:str,ventanas:int,habitaciones:int,baños:int):
        #clase contructora para una casa.
        self.tamaño = tamaño
        self.color = color 
        self.ubicacion = ubicacion
        self.ventanas = ventanas
        self.habitaciones = habitaciones
        self.baños = baños
        self.puertas = False
        
    def descripcion(self):
        #Hacer una descripcion mas ampliada y ordenada sobre la casa.
        return(f"La casa es de tamaño {self.tamaño}, su color es {self.color}, está ubicada es {self.ubicacion} a la zona centrica, tiene {self.ventanas} ventanas.\nLa casa cuenta con {self.habitaciones} habitaciones y cuenta con {self.baños} baños.")
    
    def puertas_abiertas(self):
        #Funcion para abrir y cerrarpuertas.
        if not self.puertas:
            print("Las puertas estan abiertas")
            self.puertas = True
            
casa_1 = Casas("grande", "Blanco", "lejana", 5, 3, 2)
#Descrición puntual de la primera casa.

print(casa_1.descripcion())
print(casa_1.puertas_abiertas())