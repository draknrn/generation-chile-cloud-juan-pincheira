def mensaje_bienvenida():
    print("Bienvenido a nuestro programa!")

def saludo(nombre):
    dias_totales = calculo_dias_por_edad(int(input("Ingrese su edad: ")))
    print(f"Hola, {nombre}, has vivido aproximadamente {dias_totales} días.")

def calculo_dias_por_edad(edad):
    return edad * 365

mensaje_bienvenida()
saludo(input("Ingrese su nombre: "))