
import re
intro= "TEXTO"
print (intro)


texto= """
Un videojuego es una aplicación interactiva orientada al entretenimiento que, 
a través de ciertos Mandos o controles, permite simular experiencias en la 
pantalla de un televisor, una computadora u otro dispositivo electrónico.
Los "videojuegos" se diferencian de otras formas de entretenimiento, 
en que deben ser interactivos; es decir, los "usuarios" deben involucrarse 
activamente con el contenido. Los Mandos que se usan son alambricos e inalambricos
los Modos de juego de cada plataforma son "Distintas" Mexico es el pais con mas 
"Usuarios de juegos"

El concepto de videojuego se utiliza para referirse a cualquier juego digital interactivo, 
independientemente de su "soporte físico".

Pueden ser muy distintos entre sí, tanto en complejidad como en calidad "gráfica"
y en "temática". Se dice que muchos juegos son de Multijugador. Se dice que MRpig 
es uno de los mejores jugadores.

Los numeros de telefono de los mejores jugadores son los siguientes y sus contactos:

651-828-1096
713-932-6867
188-771-0576
843-564-4222
984-387-9621
082-885-6485
205-553-8834
179-870-1801
205-073-8200
668-549-8870

Cada uno de estos jugadores hacen directos en plataformas como twich en los siguientes horarios.

11:00am
09:21am
07:29am
11:33am
14:40pm
18:12pm
19:55pm
22:10pm

y para mayores contactos se presentan sus direcciones en base a su codigo postal y correos

78134
41551
82820
43098
23625
73887
31497
25917
72381
43406

correos: 

umicipall-8714@yopmail.com 
illumahu-1499@hotmail.com
honysawic-5656@gmail.com
emmalatte-3459@yopmail.com
xogaddixiqa-4669@gmail.com


En cada juego se genera una ip de usuario que tendrian que se como por ejemplo
236.252.134.147
422.34.162.94
912.69.50.75
105.119.76.148
163.10.221.134
168.25.48.196
147.246.161.49

Estas direcciones son usadas para Mayor Privacidad De Los Usuarios y sus direcciones de 
pagina web

www.facebook.com/sharer/sharer.php?u=
www.facebook.com/sharer/sharer.php?
twitter.com/home?status=
pinterest.com/pin/create/button/?url


"""
print("_______________________________________")
print(texto)
print("_______________________________________")
print()
print()
print()

print("____________________________________________________________________")
print("Busqueda de palabras de 7 o mas letras")
print("____________________________________________________________________")

patron1 = r"(\w{7,})"

coincidencias1 = re.findall(patron1, texto)

for coincidencia1 in coincidencias1:
    print(coincidencia1)

print("____________________________________________________________________")
print("EXPRESIONES QUE FINALIZAN CON UNA VOCAL")
print("____________________________________________________________________")

patron2 = r"[a-zA-Záéíóú]{1,}[^aeiou\s\W]\b"

coincidencias2 = re.findall(patron2, texto)

for coincidencia2 in coincidencias2:
    print(coincidencia2)

print("____________________________________________________________________")
print("LAS PALABRAS QUE INICIAN CON “M” DONDE LA SEGUNDA LETRA NO SEA VOCAL")
print("____________________________________________________________________")

patron3 = r"[M][^aeiou]\w{1,}"

coincidencias3 = re.findall(patron3, texto)

for coincidencia3 in coincidencias3:
    print(coincidencia3)

print("____________________________________________________________________")
print("EXPRESIONES ENCERRADAS ENTRE COMILLAS")
print("____________________________________________________________________")

patron4 = r"\"(\w{1,})\""

coincidencias4 = re.findall(patron4, texto)

for coincidencia4 in coincidencias4:
    print(coincidencia4)

print("____________________________________________________________________")
print("DIRECCIONES IP")
print("____________________________________________________________________")

patron5 = r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}"

coincidencias5 = re.findall(patron5, texto)

for coincidencia5 in coincidencias5:
    print(coincidencia5)

print("____________________________________________________________________")
print("BUSQUEDA DE HORAS")
print("____________________________________________________________________")

patron6 = r"\d\d\:\d\d[a|p][m]"

coincidencias6 = re.findall(patron6, texto)

for coincidencia6 in coincidencias6:
    print(coincidencia6)

print("____________________________________________________________________")
print("BUSQUEDA DE TELEFONOS")
print("____________________________________________________________________")

patron7 = r"\d{3}-\d{3}-\d{4}"

coincidencias7 = re.findall(patron7, texto)

for coincidencia7 in coincidencias7:
    print(coincidencia7)

print("____________________________________________________________________")
print("BUSQUEDA DE CORREOS ELECTRONICOS")
print("____________________________________________________________________")

patron8 = r"[a-z0-9\.-_]+@[\w\d]+\.\w"

coincidencias8 = re.findall(patron8, texto)

for coincidencia8 in coincidencias8:
    print(coincidencia8)

print("____________________________________________________________________")
print("BUSQUEDA DE URL")
print("____________________________________________________________________")

patron9 = r"\w+.[\w\-\.]+\/"

coincidencias9 = re.findall(patron9, texto)

for coincidencia9 in coincidencias9:
    print(coincidencia9)

print("____________________________________________________________________")
print("BUSQUEDA DE CODIGO POSTAL")
print("____________________________________________________________________")

patron10 = r"\d{5}"

coincidencias10 = re.findall(patron10, texto)

for coincidencia10 in coincidencias10:
    print(coincidencia10)
