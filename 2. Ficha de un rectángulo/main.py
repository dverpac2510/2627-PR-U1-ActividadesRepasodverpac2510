def calcular_medidas(base: float, altura: float) -> tuple[float, float]:

    """
    Calcula las medidas de area y perimetro

    :param base: el numero de la base introducido por el usuario
    :param altura: el numero de la altura introducido por el usuario
    :return: devuelve una tupla de el area del rectangulo y su perimetro
    """

    area: float = base * altura
    perimetro: float = (base + altura) * 2

    return area, perimetro


def determinar_forma(base: float, altura: float) -> str:

    """
    Determina la forma del rectángulo viendo las 

    :param base: el numero de la base introducido por el usuario
    :param altura: el numero de la altura introducido por el usuario
    :return: Devuelve la forma 
    """


    
    if base == altura:
        return "cuadrado"

    if base > altura:
        return "horizontal"
    
    if base < altura:
        return "vertical"




def main():
    """Función principal"""

    base: float = float(input("Escribe la base de un rectángulo: "))
    altura: float = float(input("Escribe la altura de un rectángulo: "))

    conversión: tuple[float, float] = calcular_medidas(base, altura)

    if base == 0 or altura == 0:
        print("No puede ser 0")

    else:
        print(f"Forma: {determinar_forma(base, altura)}")
        print (f"Área: {conversión[0]:.2f}")
        print (f"Perímetro: {conversión[1]:.2f}")
               
               

if __name__ == "__main__":
    main()