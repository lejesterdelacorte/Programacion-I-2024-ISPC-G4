'''Hacer un archivo python llamado test_aritmetica.py que
utilice el módulo aritmetica.py y contenga una funcion test por cada funcion
del modulo aritmetica, es decir, test_sumar, test_restar, …. con al menos 3
assert cada función '''

from modules.aritmetica.sumar import sumar
from modules.aritmetica.sumar_n import sumar_n
from modules.aritmetica.restar import restar
from modules.aritmetica.dividir import dividir
from modules.aritmetica.multiplicar import multiplicar
from modules.aritmetica.promedio_n import promedio_n

def test_sumar():
    resultado = sumar(2.00, 3.00)    
    assert resultado == 5
    assert resultado > 0
    assert isinstance(resultado, float)
    assert resultado is not None
    

def test_restar():  
    resultado = restar(-15.00, 16)    
    assert resultado == -31
    assert resultado < 0
    assert isinstance (resultado, float)
    assert resultado is not None
   


def test_multiplicar(): 
    resultado = multiplicar(5.00, -7)    
    assert resultado == -35
    assert resultado < 0
    assert isinstance (resultado, float)
    assert resultado is not None
    

def test_dividir():  
    resultado = dividir(10.00, 2.00)    
    assert resultado == 5
    assert resultado > 0
    assert isinstance (resultado, float)
    assert resultado is not None    

def test_sumar_n():
    resultado = sumar_n([2.00, 8.00, 4.00])
    assert resultado == 14.00
    assert resultado > 0
    assert isinstance (resultado, float)
    assert resultado is not None

def test_promedio_n():
    resultado = promedio_n([6.00, 3.00, 3.00])
    assert resultado == 4.00
    assert resultado > 0
    assert isinstance (resultado, float)
    assert resultado is not None


if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_multiplicar()
    test_dividir()
    test_sumar_n()
    test_promedio_n()


    