import re
cadena = "aaaaaaaaaa@!"
cumple = (len(cadena)>=10) & bool(re.search(r'@', cadena)) & bool(re.search(r'!', cadena))
if cumple:
    print("Contra Correcta")
#falta esto :( print("Ingresaste alguno de estos símbolos: @ o !" )
#count