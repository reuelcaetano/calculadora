class Calculadora:
    
    def somar(self, a, b):
        return (a+b)

    def subtrair(self, a, b):
        return (a-b)
    
    def dividir(self, a, b):
        try:
            return (a/b)
        except ZeroDivisionError:
            return "Erro de divisão por zero"
    
    def multiplicar(self, a, b):
        return (a*b)

calc = Calculadora()
print(calc.somar(1,2))
print(calc.subtrair(5,2))
print(calc.dividir(4,2))
print(calc.multiplicar(3,3))