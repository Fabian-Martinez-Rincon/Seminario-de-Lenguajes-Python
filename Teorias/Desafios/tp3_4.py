tipo_Usuarios = list[tuple[str,str,int]]
def ordeno3(usuarios:tipo_Usuarios):
    return sorted(usuarios, key=lambda usuario: usuario[1])
usuarios = [
    ('JonY BoY', 'Nivel3', 15),
    ('1962', 'Nivel1', 12),
    ('caike', 'Nivel2', 1020),
    ('Straka^', 'Nivel2', 1020),
]
print(type(usuarios))
print(ordeno3(usuarios))