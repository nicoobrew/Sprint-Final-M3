import random
import string

nombres_usuarios = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5',
                    'user_6', 'user_7', 'user_8', 'user_9', 'user_10']

cuentas_usuarios = {}

def generar_contrasena():
    '''
    Genera una contraseña aleatoria y que contiene al menos un numero,
    una letra mayúscula y una letra minúscula.
    Retorna: La contraseña generada como un string. 
    '''
    cantidad_numeros = random.randint(1, 4)
    cantidad_mayusculas = random.randint(1, 4)
    cantidad_minusculas = 10 - cantidad_numeros - cantidad_mayusculas

    caracteres = []

    for _ in range(cantidad_numeros):
        caracteres.append(random.choice(string.digits))

    for _ in range(cantidad_mayusculas):
        caracteres.append(random.choice(string.ascii_uppercase))

    for _ in range(cantidad_minusculas):
        caracteres.append(random.choice(string.ascii_lowercase))
    
    # Los caracteres están agrupados en orden asi que usamos shuffle()
    # para desordenarlos antes de retornar la contraseña.
    random.shuffle(caracteres)
    return ''.join(caracteres)

#Funcion que crea a todos los usuarios una cuenta automáticamente
def creacion_cuenta(nombre_usuario):
    contraseña = generar_contrasena()
    cuentas_usuarios[nombre_usuario] = {'contraseña': contraseña, 'num_telefonico': ''}
    
#Funcion para validar que el telefono ingresado corresponda a solo numeros y tenga 8 digitos
def validar_numero_telefonico(numero):
    if len(numero) == 8 and numero.isdigit():
        return True
    else:
        return False
#funcion que asigna los numeros telefonicos a los usuarios 
def asignar_numeros_telefonicos():
    usuarios_sin_numero = nombres_usuarios.copy()
    while usuarios_sin_numero:
        for usuario in usuarios_sin_numero:
            numero_telefonico = input(f"Ingrese el número telefónico para el usuario {usuario}: ")
            if validar_numero_telefonico(numero_telefonico):
                cuentas_usuarios[usuario]['num_telefonico'] = numero_telefonico
                usuarios_sin_numero.remove(usuario)
            else:
                print("Debe ingresar un número de teléfono válido con 8 dígitos.")

for usuario in nombres_usuarios:
    creacion_cuenta(usuario)

asignar_numeros_telefonicos()

#String que permite guardar en formato de cadena del diccionario cuentas_usuarios 
#en la variable datos_usuarios utilizando la función
datos_usuarios = str(cuentas_usuarios)
print(datos_usuarios)