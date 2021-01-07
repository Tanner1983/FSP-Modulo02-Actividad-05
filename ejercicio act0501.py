print("Ingrese su edad")
edad = int(input(": "))

if edad < 2:
    print("Es un Bebé")
elif edad < 12:
    print("Es un Niño")
elif edad < 18:
    print("Es un Adolescente")
elif edad < 65:
    print("Es un Adulto")
elif edad > 65:
    print("Es de 3ra Edad")
