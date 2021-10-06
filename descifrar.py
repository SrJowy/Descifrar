import operator

mensaje = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""

"""con durruti moria el dirigente que, a su manera, mejor expresaba como combatir al fascismo desde un criterio de independencia
de clase, a diferencia del colaboracionismo frentepopulista de la direccion anarquista.

durruti fue un factor de primer orden en el papel de la clase obrera en catalunya en julio de 1936. pero durruti, como ocurre con
las personalidades en la historia, no cayo del cielo. personificaba la tradicion revolucionaria de la clase obrera. su enorme
popularidad entre la clase trabajadora, reflejada en el entierro multitudinario en barcelona el 22 de noviembre de 1936,
muestra esa identificacion. su muerte fue sin duda un golpe objetivo al proceso revolucionario en marcha. sin durruti quedo mas
libre el camino para que el estalinismo, con la complicidad del gobierno del frente popular y de la direccion anarquista,
terminara en mayo de 1937 la tarea de liquidar la revolucion, desmoralizando a la clase obrera y facilitando con ello el posterior
triunfo franquista.
"""

mn = list(mensaje)

frec= ['e','a']


def crearArrays(): #Genera un diccionario donde se almacenan todas las letras por cada clave
    a={}
    k=0
    for i in range(65,91,1):
        c = chr(i)
        a[c] = 0
    c= 'Ñ'
    a[c]=0    
    for i in range(97,123,1):
        c = chr(i)
        a[c] = 0
    c='ñ'
    a[c] = 0
    return a

def anadirFrec(a): #Se rellena el diccionario con las frecuencias de las letras del texto
    for k in mensaje:
        if k != ' ' and k.isdigit() == False and k != ',' and k != '.' and k != '\n':
            a[k] = a[k] + 1
    ordA = sorted(a.items(), key=operator.itemgetter(1))
    return ordA      

def traducir(a): #Se cambian las dos letras con más frecuencia por las del array a
    i=0
    k= len(a)-1
    b={}
    while (i<len(frec)):
        b[a[k][0]] = frec[i]
        i = i+1
        k = k-1
    return b

def cambiarTexto(a): #Se cambian las letras del mensaje que se encuentren en a
    i = 0
    for k in mn:
        if k in a:
            mn[i] = a.get(k)
        i = i+1

def recorrerDic(a):
    for k,v in a.items():
        print(k,v)

def recorrerArray(a):
    for i in a:
        print(i, end= ', ')

def imprimirMensaje(m):
    print(''.join(m))

def sustituirLetra(p1,p2):
    i = 0
    while (i < len(mn)):
        if (mn[i] == p1): mn[i] = p2
        i = i+1

def elegirPalabra():
    print("")
    imprimirMensaje(mn)
    pal = input("Elige una palabra -> ")
    mn_p = ''.join(mn)
    if (pal in mn_p):
        p1 = input("Elige la letra que quieres sustituir -> ")
        p2 = input("Elige la letra por la que la quieres sustituir -> ")
        frec.append(p2)
        print("\nHasta ahora has usado: \n")
        recorrerArray(frec)
        print("")
        sustituirLetra(p1,p2)



def main():
    salir = -1
    cambiarTexto(traducir(anadirFrec(crearArrays())))
    print("Se han sustituido las dos primeras letras del del texto con las primeras del array de frecuencias")
    print("")
    while (salir != '0'):
        print("1- Elige una palabra para sustituir letras")
        print("2- Imprimir mensaje")
        print("3- Imprimir mensaje original")
        print("4- Ver letras ya cambiadas")
        print("5- Sustituir palabras")
        print("0- Salir")
        salir = input()
        if (salir == '1'):
            print("")
            elegirPalabra()
        elif (salir == '2'):
            print("")
            imprimirMensaje(mn)
        elif (salir == '3'):
            print("")
            imprimirMensaje(mensaje)
        elif (salir == '4'):
            print("")
            recorrerArray(frec)
        elif (salir == '5'):
            print("")
            sustituirPalabras()
        print("")
    return
main()