'''
Hacer un archivo python llamado test_aritmetica.py que
utilice el módulo aritmetica.py y contenga una funcion test por cada funcion
del modulo aritmetica, es decir, test_sumar, test_restar, …. con al menos 3
assert cada función. 
'''

from aritmetica import (sumar, restar, multiplicar, dividir, sumar_n)

def test_sumar():
    num1 = 2.00
    num2 = 3.00
    resultado = sumar(num1, num2)    
    assert resultado == 5
    assert resultado > 0
    assert isinstance(resultado, float)
    assert resultado is not None
    assert resultado >= num1

def test_restar():    
    num1 = -15.00
    num2 = 16    
    resultado = restar(num1, num2)    
    assert resultado == -31
    assert resultado < 0
    assert isinstance (resultado, float)
    assert resultado is not None
    assert resultado < num1


def test_multiplicar():    
    num1 = 5.00
    num2 = -7    
    resultado = multiplicar(num1, num2)    
    assert resultado == -35
    assert resultado < 0
    assert isinstance (resultado, float)
    assert resultado is not None
    assert resultado < num1   

def test_dividir():
    num1 = 10
    num2 = 2    
    resultado = dividir(num1, num2)    
    assert resultado == 5
    assert resultado > 0
    assert isinstance (resultado, float)
    assert resultado is not None
    assert resultado < num1 
    assert resultado != 7
    assert num2 != 0

def test_sumar_n():
    numlist= [1.00, 5.00, 8.00]
    resultado = sumar_n(numlist)
    assert resultado == 14.00


if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_multiplicar()
    test_dividir()
    test_sumar_n()


    