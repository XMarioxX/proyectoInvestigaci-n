from openai import OpenAI
from sympy import *
import random

client = OpenAI(
    api_key="sk-proj-ocnwoBekmwVjap177e9KT3BlbkFJXHuFaVf9lBxJo5bhHpHZ"
)   

while True:
    métodoIn = input("Ingresa 1 si deseas derivadas o 2 si quieres integrales (exit para terminar): ")

    # Derivadas---------------------------------------------------------------------------------------------
    def genFuncion(nivel_dificultad):
        x = sp.symbols('x')
        grado = random.randint(1, 5)
        
        if nivel_dificultad < 10:
            coeficientes_permitidos = list(range(-5, 6))
        else:
            coeficientes_permitidos = list(range(-15, -5)) + list(range(6, 15))
        
        coeficientes = []
        while len(coeficientes) < grado:
            coef = random.choice(coeficientes_permitidos)
            if all(coef % p != 0 for p in coeficientes):
                coeficientes.append(coef)
        
        funcion = sum(coeficientes[i] * x**i for i in range(grado))
        return funcion
    def genDerivada(nivel_dificultad):
        funcion = genFuncion(nivel_dificultad)
        derivada = sp.diff(funcion, sp.symbols('x'))
        return derivada
    # ------------------------------------------------------------------------------------------------------
    # Integrales--------------------------------------------------------------------------------------------
    def genIntegral(nivel_dificultad):
        x = sp.symbols('x')
        
        if nivel_dificultad < 10:
            funciones = [
                sp.sin(x), 
                sp.cos(x), 
                sp.exp(x),
                sp.log(x + 1),
                x**2,
                x**3
            ]
        else:
            funciones = [
                sp.sin(x) * sp.cos(x), 
                sp.exp(sp.sin(x**2)),
                sp.sqrt(x**3 + 1),
                sp.log(sp.exp(x) + sp.cos(x)),
                sp.tan(x),
                sp.sin(x**2)
            ]
        
        funcion = random.choice(funciones)
        
        a = random.randint(-10, 10)
        b = random.randint(a + 1, 10)
        
        integral = sp.integrate(funcion, (x, a, b))
        return integral
    # ------------------------------------------------------------------------------------------------------

    if métodoIn == "exit" :
        break
    elif métodoIn == "1":
        try:
            easy_int = int(25)
            if easy_int > 0:
                # derivada = "ln(root((4x ^ 2 - 7x) ^ 3, 5))"
                # derivada = "ln[(root(x, 3) * e ^ (3x) * sqrt(x ^ 2 + 1))/(root(5x + 2, 3))]"
                # derivada = genDerivada(50)
                derivada = "y = 8 * acot((sqrt(16 - x ^ 2))/x) - (x * sqrt(16 - x ^ 2))/2"
                print(derivada)

                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": "Dame la resolución paso a paso obligatoriamente de la siguiente derivada ademas dame la forma mas simplificada posible no escatimes en pasos, simplifica todo lo posible de la exprecion aunque tengas que hacer 100 pasos dame cada movimiento que hiciste y explica el por que: " + str(derivada)}
                    ],
                    max_tokens=1000,
                )

                print(completion.choices[0].message.content)
            else:
                print("Dificultad no valida ingrese solo números mayores a 0")
        except ValueError:
            print("Dificultad no válida. Ingresa solo números.")
    elif métodoIn == "2":
        easy = input("Ingresa la dificultad de la integral (1+): ")
        try:
            easy_int = int(easy)
            if easy_int > 0:
                integral = genIntegral(int(easy))
                print(integral)

                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": "Dame la resolución paso a paso obligatoriamente de la siguiente integral: " + str(integral)}
                    ],
                    max_tokens=1000,
                )

                print(completion.choices[0].message.content)
            else:
                print("Dificultad no valida ingrese solo números mayores a 0")
        except ValueError:
            print("Dificultad no válida. Ingresa solo números.")
    elif métodoIn != "1" or métodoIn != "2":
        print("Método incorrecto seleccione solo 1 o 2")