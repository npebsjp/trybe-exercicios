def calculo_area_triangulo(lado1: float, lado2: float, lado3: float) -> str:
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            return f"O triangulo e equilatero com area de {((lado1 * lado2) /2)}m2"
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return f" O triangulo e isosceles com area de {((lado1 * lado2) /2)}m2"
        elif lado1 != lado2 != lado3:
            return f"O triangulo e escaleno com area de {((lado1 * lado2) /2)}m2"
    else:
        return f"Os dados informados nao formam um triangulo."
