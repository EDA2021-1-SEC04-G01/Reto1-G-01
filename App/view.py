"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar Top x de videos mas vistos en un pais en una categoria")
    print("3- Buscar video con mas dias en trending por pais")
    print("4- Buscar video con mas dias en trending por categoria")
    print("5- Buscar videos con mas likes con un tag especifico")
    print("0- Salir")

def initCatalog(dtEstructure):
    """
    Inicializa el catalogo de videos
    """
<<<<<<< HEAD
    return controller.initCatalog(dtEstructure)
=======
    print("1- Arreglo")
    print("2- Lista encadenada")
    type_list=int(input('Seleccione una representación de lista para continuar\n'))
    return controller.initCatalog(type_list)
>>>>>>> 2c6481b63c3fab74ccb7ba8b54c1c794b625cbd9


def loadData(catalog):
    """
    Carga la informacion de los videos en la estructura de datos
    """
    controller.loadData(catalog)
def topVideos(catalog, topAmount, country):
    controller.topVideos(catalog, topAmount, country)

def trendingCountry():
    pass

def trendingCategory():
    pass

def mostLiked():
    pass


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
<<<<<<< HEAD
        print("Seleccione la estructura de datos que deseea escoger: ")
        dtEstructure= int(input("Para Array escriba 0, Para Single-Linked escriba 1: "))
        print("Cargando información de los archivos ......")
        catalog = initCatalog(dtEstructure)
=======
        print("Cargando información de los archivos ......")      
        catalog = initCatalog()
>>>>>>> 2c6481b63c3fab74ccb7ba8b54c1c794b625cbd9
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories'])))
        print(catalog['categories'])
       
        

    elif int(inputs[0]) == 2:
        print("Seleccione el tipo de algoritmo de ordenamiento\n Shell= 0\n Insertion = 1\n Selection = 2")
        sorting = int(input("Ingrese el numero: "))
        countryname= input("Ingrese el pais del que desea consultar el top: ")
        topAmount= int(input("Escoga la cantidad de videos que desea ver en el top: "))
        category= input("Ingrese la categoria de los videos: ")
        print("Cargando el top de los videos")
        sortVideos(catalog, sorting)
        topVideos(catalog,topAmount,countryname, category)
    elif int(inputs[0]) == 3:
        print("El video mas trending en este pais es: ")
        trendingCountry()
    elif int(inputs[0]) == 4:
        print("El video mas trending en esta categoria es: ")
        trendingCategory()
    elif int(inputs[0]) == 5:
        print("Cargando los videos con mas likes que tienen este tag...")
        mostLiked()
    else:
        sys.exit(0)
sys.exit(0)