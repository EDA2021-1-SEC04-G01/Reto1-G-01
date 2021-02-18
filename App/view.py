﻿"""
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

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga la informacion de los videos en la estructura de datos
    """
    controller.loadData(catalog)
def topVideos():
    pass

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
        print("Cargando información de los archivos ......")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories'])))
       

    elif int(inputs[0]) == 2:
        print("Cargando el top de los videos")
        topVideos()
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