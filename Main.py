# importe los datos necesarios
from Date import vegetales, products
"""
#-------------------------------------------------

# 1) recorra 'vegetales' usando un 'for':
# muestra en mayúsculas aquellos que comienzan 
# con la letra 'p'

def vegetales_P():
    vegetales_p = []
    for vegetal in vegetales:
        if vegetal[0] == "p":
            x = vegetal.upper()
            vegetales_p += [x]
    print(vegetales_p)
vegetales_P()

#-------------------------------------------------

# 2) recorra 'vegetales' usando un 'for':
# muestra aquellos cuyo nombre incluya
# una tilde

def tildes():
    vegetales_tildes = []
    for vegetal in vegetales:
        if "á" in vegetal or "é" in vegetal or "í" in vegetal or "ó" in vegetal or "ú" in vegetal:
            vegetales_tildes += [vegetal]
    print(vegetales_tildes)
tildes()

#---------------------------------------------------
"""
# 3) recorre 'vegetales' usando un 'for' y enumarate():
# muestra los que tengan el nombre más largo
# y el nombre mas corto

def vegetal_l():
    vegetal_largo = ""
    lista_vegetales_largos = []
    for vegetal in vegetales:
        if len(vegetal) > len(vegetal_largo):
            vegetal_largo = vegetal
    for vegetal in vegetales:
        if len(vegetal) == len(vegetal_largo):
            vegetal_largo = vegetal
            lista_vegetales_largos.append(vegetal_largo)
    return lista_vegetales_largos

def vegetal_p():
    vegetal_pequeño = vegetal_l()
    vegetal_pequeño = vegetal_pequeño[-1]
    lista_vegetales_pequeños = []
    for vegetal in vegetales:
        if len(vegetal) < len(vegetal_pequeño):
            vegetal_pequeño = vegetal
    for vegetal in vegetales:
        if len(vegetal) == len(vegetal_pequeño):
            vegetal_pequeño = vegetal
            lista_vegetales_pequeños.append(vegetal_pequeño)
    return lista_vegetales_pequeños
print(vegetal_l(), vegetal_p())

#---------------------------------------------------
"""
# 4) con 'products'
# para cada producto mostrar el nombre, la descripción y el código de barras

def nombre():

    for x in products:
        nombre = x.get("name")
        descripcion = x.get("description")
        codigo = x.get("code")
        print("El producto " + nombre + "con su descripción " + descripcion + "y codigo de barras " + codigo)     
nombre()

#---------------------------------------------------

# 5) con 'products'
# Si un cliente Silver compra 4 productos con 
# código 'LADHJFLAKSH'
# cuál es el valor a pagar?
# nota: tenga en cuenta el impuesto

def requisitos():
    #Digite los requisitos
    numero_productos = 4
    cliente = "Silver Client Price"
    code = 'LADHJFLAKSH'
    return numero_productos, cliente, code

def calculo():
    cantidad, cliente, code = requisitos()
    for x in products:
        if x.get("code") == code:
            taxe = x.get("taxes")[0]
            taxe_number = taxe.get("percentage")
            price = x.get("prices")[0]
            for y in price.get("price_list"):
                if y.get("name") == cliente:
                    precio_sin_impuestos = y.get("value") * cantidad
                    precio_con_impuestos = precio_sin_impuestos + (precio_sin_impuestos * (taxe_number/100))
    return precio_con_impuestos
print(calculo())    
"""








