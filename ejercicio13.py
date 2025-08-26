
# EJERCICIO 13:
while True:
    contraseña = input(f'Ingresa tu nueva contraseña: ')

    if any(letra.isupper() for letra in contraseña) and any(letra.islower() for letra in contraseña) and any(letra.isdigit() for letra in contraseña):

        confirmar_contraseña = input(f'Confirma tu contraseña: ')

        if confirmar_contraseña == contraseña:
            print(f'Contraseña creada con éxito.')
            break  
        else:
            print(f'Las contraseñas no coinciden. Por favor, inténtelo de nuevo.')
        
    else:
        
        print(f'La contraseña no es segura. Debe contener al menos una mayúscula, una minúscula y un número.')

