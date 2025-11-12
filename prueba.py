def saludo(nombre: str) -> str:
    return f"Hola, {nombre}! Bienvenido a Git, otra vez, desde git. Ahora desde la rama"

if __name__ == "__main__":
    nombre = input("¿Tu nombre? ")
    print(saludo(nombre))
