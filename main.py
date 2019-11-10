# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:36:29 2019
Assignment 2 - Ingenieria de software II
@author: Daniel Perez - Manuel Bejarano.
"""
class Matematicas():

    def operation(self, x, y) -> str:
        pass


class Default(Matematicas):

    def operation(self, x, y) -> int:
        aux = x + y
        return f"Suma = {aux}"


class Decorator(Matematicas):

    _componente: Matematicas = None

    def __init__(self, componente: Matematicas) -> None:
        self._componente = componente

    @property
    def componente(self) -> str:
        return self._componente

    def operation(self, x, y) -> str:
        self._componente.operation(x, y)


class Multiplicacion(Decorator):

    def operation(self, x, y) -> str:
        aux = x * y        
        return f"Multiplicacion = {aux}, {self.componente.operation(x, y)}"


class Resta(Decorator):
    
    def operation(self, x, y) -> str:
        aux = x - y
        return f"Resta = {aux}, {self.componente.operation(x, y)}"

class Division(Decorator):

    def operation(self, x, y) -> str:

        if y != 0:
            aux = x / y
            return f"Division = {aux}, {self.componente.operation(x, y)}"
        else:    
            return f"Division = No es posible dividir entre 0, {self.componente.operation(x, y)}"

def Verificar() -> int:

    aux = True

    while(aux):
        try:
            x = int(input())
            aux = False
        except:
            print("Digite un numero valido:")
    return x
        

def client_code(componente: Matematicas, x, y) -> None:    
    print(f"{componente.operation(x, y)}", end = "")

    
if __name__ == "__main__":
    
    print("Digite un numero:")
    x=Verificar()

    print("Digite otro numero:")
    y=Verificar()
    
    simple = Default()
    print("Simple operacion")
    
    client_code(simple, x, y)
    print("\n")

    decorator1 = Multiplicacion(simple)
    decorator2 = Resta(decorator1)
    decorator3 = Division(decorator2)
    
    print("Varias operaciones")
    client_code(decorator3, x, y)
