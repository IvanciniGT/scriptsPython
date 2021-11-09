Documentar un código:
    Explicar lo que hace el código
Comentar un código:
    Explicar CÓMO LO HACE
    
    
nombre=sinput("Como se llama el servidor que quieres reiniciar? ",3 , "localhost")

    >>> Como se llama el servidor que quieres reiniciar [localhost]?  ENTER
    valor: localhost

servicio=sinput("Que servicio desea reiniciar? ",3 )

    Que servicio dsea reiniciar? ENTER
        Oye, pringao! que no me has dado nombre del servicio... 
    Que servicio dsea reiniciar? ENTER
    Que servicio dsea reiniciar? 

if condicion1:
    HAGO UNA COSA
    if condicion2:
        HAGO OTRA COSA    
else:
    HAGO OTRA COSA DIFERENTE
    
    
if condicion1:
    HAGO UNA COSA
else if CONDICION2:
    HAGO OTRA COSA
else: 
    HAGO OTRA COSA DIFERENTE



Complejidad ciclomática? Número de caminos diferentes de mi codigo: 3
Complejidad cognitiva?   Cómo de dificil o fácil es entender un código por un ser humano

REFACTORIZAR:
    Tarea que hacemos después de tener un programa en funcionamiento...
    Le dedicamos un ratito a ver si puedo reescribir aquello de forma que quede más DECENTE
    
    
Estás seguro que quieres reiniciar el servidor (si|no) [si]? 

Si recibo otra cosa... Le avisaré que la respues no es válida... y pregunto de nuevo


------------------------------------
REGEX
-------------------------------------

#edad?  Numero entero
#email? No... tiene que ser un email valido
#ip?    No.. tiene que se tener un formato de IP
#nombre de un servidor? Sin caracteres especiales

#Validación sobre la respuesta del usuario

# respuesta es si|no    Dentro de unos valores permitidos
# Edad email ip. No puedo enumerarlos todos... son infinitos
# Expresiones regulares. Patrones

# Python permite usar regex según sintaxis PERL

TEXTO                           PATRON                      LO CUMPLE?       EN QUE POSICION?
Hola amigo                      Contiene la letra a            √                  4, 6
                                Empieza por la a               x
                                Acaba por la o                 √                  10
                                Contiene dos vocales seguidas  x
                                Contiene dos vocales           √                  4-6
                                separadas por un espacio 
                                en blanco

SECUENCIAS DE CARACTERES     -     NUMERO DE OCURRENCIAS
a                                             (1)                  Contiene la letra a en una posicion, la que sea
amigo                                             
[amigo]                                                            Contiene alguno de los caracteres de esa lista
[a-z]                                                               Cualquier caracter de la "a" a la "z"
[A-Z]
[0-9]                                                               Cualquier digito
[5-9]                                                               Cualquier digito
[0-9a-zA-ZñÑáÁ]                             ?                   0-1           La secuencia anterior puede aparecer o no
                                            +                   1-infinito    La secuencia anterior debe aparecer al menos una vez
                                            *                   0-infinito    La secuencia anterior puede aparecer todas las veces que quiera o no hacerlo
.                                                                   Cualquier caracter
[.]
MODIFICADORES ADICIONALES                                            
^ COMIENZO
$ FIN


Hola amigo amigo               amigo+        
Adios compañero                amigo*

^      (([1-9][0-9])|[1-9])        $
EMPIEZA                             ACABA
(antes que no haya nada)            (despues que no haya nada más)

 ([1-9][0-9])        |           [1-9]
 o aparece esto      o              aparece esto otro
                                un digito del 1 al 9                   Edad: 1,2,3,4,5,6,7,8,9
Primero un digito del 1 al 9 y luego otro del 0 al 9                   Edad: 87
    --> 10-99
    
^[a-z0-9_-]+@[a-z]+.[a-z]+$

1.1.1.1
0-255
198
-----------------
1
8
12
98
167
250
255
---
256
300
987
1298


[0-9]       Numeros del 0 al 9
[1-9][0-9]  Numeros 10 al 99
1[0-9]{2}   Numeros del 100 al 199         
2[0-4][0-9] Numeros del 200 al 249
25[0-5]     Numeros del 250-255

^((([0-9])|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5]))[.]){3}(([0-9])|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5]))$

PATRON_IP=^((([0-9])|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5]))[.]){3}((([0-9])|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5])))$


^([0-9]{1,3}[.]?){4}$