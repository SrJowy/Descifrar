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
    mn = mensaje
    lm= list(mn)
    for k in mn:
        if k in a:
            lm[i] = a.get(k)
        i = i+1
    b = ''.join(lm)
    print(b)

def recorrerDic(a):
    for k,v in a.items():
        print(k,v)
    return None

def recorrerArray(a):
    for i in a:
        print(i)
    return None

#def main():
    

recorrerDic(traducir(anadirFrec(crearArrays())))
cambiarTexto(traducir(anadirFrec(crearArrays())))