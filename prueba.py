def saludo(nombre: str) -> str:
    return f"Hola, {nombre}! Bienvenido a Git, otra vez, desde git. Ahora desde la rama.prueba dos y tres"

if __name__ == "__main__":
    nombre = input("¿Tu nombre? ")
    print(saludo(nombre))
