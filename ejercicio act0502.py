
def verificar(user, password):
    if user.upper() == "PEDRO" and password=="12345":
        print("Bienvenido")
        exit()
    elif user.upper() == "FERNANDA" and password == "4321":
        print("Bienvenido")
        exit() 
    else:
        print("Usuario incorrecto")
        return


while True:
    print("Desea ingresar S/N")
    respuesta =input(": ")
    if respuesta.upper() == "S" or respuesta.upper() == "SI":        
        print("Ingrese nombre de usuario")
        user=input(": ")
        print("Ingrese contraseña")
        password=input(": ")
        verificar(user,password)
    else:
        break

        
        
