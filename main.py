class Laberinto:
    PARED = 'p'
    CAMINO = 'c'
    ENTRADA = 'E'
    SALIDA = 's'

    laberinto = [
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'c', 'c', 'c', 'c', 'c', 'p'],
        ['p', 'p', 'c', 'p', 'p', 'p', 'c', 'p'],
        ['p', 'p', 'c', 'c', 'c', 'p', 'c', 'p'],
        ['p', 'p', 'p', 'p', 'c', 'p', 'c', 's'],
        ['p', 'p', 'p', 'p', 'c', 'p', 'p', 'p'],
        ['p', 'p', 'c', 'c', 'c', 'c', 'p', 'p'],
        ['p', 'p', 'c', 'c', 'p', 'p', 'p', 'p'],
        ['p', 'p', 'E', 'p', 'p', 'p', 'p', 'p']
    ]

    camino = []
    direcciones = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    @classmethod
    def resolver_laberinto(cls, x, y):
        if not cls.es_valido(x, y) or cls.laberinto[x][y] == cls.PARED:
            return False
        cls.camino.append((x, y))

        if cls.laberinto[x][y] == cls.SALIDA:
            return True

        cls.laberinto[x][y] = cls.PARED
        for dir_x, dir_y in cls.direcciones:
            nuevo_x, nuevo_y = x + dir_x, y + dir_y
            if cls.resolver_laberinto(nuevo_x, nuevo_y):
                return True

        cls.laberinto[x][y] = cls.CAMINO
        cls.camino.pop()
        return False

    @classmethod
    def es_valido(cls, x, y):
        return 0 <= x < len(cls.laberinto) and 0 <= y < len(cls.laberinto[0])

    @classmethod
    def main(cls):
        inicio_x, inicio_y = 13, 2
        if cls.resolver_laberinto(inicio_x, inicio_y):
            print("Camino encontrado:")
            for paso in reversed(cls.camino):
                print(f"({paso[0]}, {paso[1]})")
        else:
            print("No se encontró camino.")

# Ejecutar el programa
Laberinto.main()
