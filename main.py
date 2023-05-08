from ClaseConjunto import Conjunto# This is a sample Python script.




if __name__ == '__main__':
    # Cracion de 2 conjuntos
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 6, 9])

    # Muestra los conjuntos
    print("Conjunto A:", A.elementos)
    print("Conjunto B:", B.elementos)

    op = 0
    while (op != 4):
        print("____Menú____")
        print("ingrese Opción")
        print("1-La unión de dos conjuntos")
        print("2-La diferencia de dos conjuntos")
        print("3-Verificar si dos conjuntos son iguales")
        print("4-Salir")
        op = int(input(""))
        if (op == 1):

            # genera la de dos conjuntos
            C = A + B
            print("Unión de A y B:", C.elementos)
        elif (op == 2):

            # genera la diferencia de los conjuntos
            D = A - B
            print("Diferencia de A y B:", D.elementos)
        elif (op == 3):

            # Compara los conjuntos
            E = Conjunto([1, 2, 3, 4])
            print("El conjunto A es igual al conjunto E:", A == E)
            print("El conjunto B es igual al conjunto E:", B == E)









