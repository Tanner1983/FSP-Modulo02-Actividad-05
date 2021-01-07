nombre1 = input("Ingrese nombre: ") 
puntaje1= input("Ingrese puntaje: ")
print("=======================")

nombre2 = input("Ingrese nombre: ") 
puntaje2= input("Ingrese puntaje: ")
print("=======================")

nombre3 = input("Ingrese nombre: ") 
puntaje3= input("Ingrese puntaje: ")
print("=======================")

if puntaje1 > puntaje2 and puntaje1 > puntaje3:
    primerLugar = nombre1
    primerPuntaje = puntaje1
    if puntaje2 > puntaje3:
        segundoLugar = nombre2
        segundoPuntaje = puntaje2
        tercerLugar = nombre3
        tercerPuntaje = puntaje3
    else:
        segundoLugar = nombre3
        segundoPuntaje = puntaje3
        tercerLugar = nombre2
        tercerPuntaje = puntaje2
elif puntaje2 > puntaje1 and puntaje2 > puntaje3:
    primerLugar = nombre2
    primerPuntaje = puntaje2
    if puntaje1 > puntaje3:
        segundoLugar = nombre1
        segundoPuntaje = puntaje1
        tercerLugar = nombre3
        tercerPuntaje = puntaje3
    else:
        segundoLugar = nombre3
        segundoPuntaje = puntaje3
        tercerLugar = nombre1
        tercerPuntaje = puntaje1
elif puntaje3 > puntaje1 and puntaje3> puntaje2:
    primerLugar = nombre3
    primerPuntaje = puntaje3
    if puntaje2 > puntaje1:
        segundoLugar = nombre2
        segundoPuntaje = puntaje2
        tercerLugar = nombre1
        tercerPuntaje = puntaje1
    else:
        segundoLugar = nombre1
        segundoPuntaje = puntaje1
        tercerLugar = nombre2
        tercerPuntaje = puntaje2


    

print(primerLugar, primerPuntaje)
print(segundoLugar, segundoPuntaje)
print(tercerLugar, tercerPuntaje)
