import requests

def obtener_datos_api():
    url = "https://restcountries.com/v3.1/region/europe"
    respuesta = requests.get(url)
    datos_json = respuesta.json()
    return datos_json

datos_api = obtener_datos_api()
# print(datos_api)
nombres_paises = []
for pais in datos_api:
    nombres_paises.append(pais["name"]["common"])
# print(nombres_paises)

nombre_pais_usuario = input("Por favor digite el nombre del país:")
def buscar_pais_lineal(lista_datos):
    urls_encontradas = []
    for pais in lista_datos:
        if pais["name"]["common"] == nombre_pais_usuario:
            urls_encontradas.append(pais["maps"]["googleMaps"])
            return urls_encontradas
    return "No se encontró"

print(buscar_pais_lineal(datos_api))

# Búsqueda Binaria
nombres_paises.sort()
# print(nombres_paises)
def buscar_pais_binaria(lista_api, lista_nombres, pais_buscado):
    inicio = 0
    fin = len(lista_nombres) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_nombres[medio] == pais_buscado:
            # Cuando lo encuentra, recorro la API para sacar la URL
            for pais in lista_api:
                if pais["name"]["common"] == lista_nombres[medio]:
                    return pais["maps"]["googleMaps"]
        elif lista_nombres[medio] < pais_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return "No se encontró"

print(buscar_pais_binaria(datos_api, nombres_paises, nombre_pais_usuario))
