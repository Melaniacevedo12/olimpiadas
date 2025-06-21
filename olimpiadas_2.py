
print("---------------------------------------------------------------------------------------------------")

# Listas iniciales
libros = ["Cien años de soledad", "El principito", "1984"]
autores = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell"]

print("Libros actuales:", libros)
print("Autores actuales:", autores)

print("------------------------------------------------------------------------------------------------")

# 1. Agregar Fahrenheit 451 si está 1984
if "1984" in libros:
    respuesta = input("¿Agregar 'Fahrenheit 451'? (si/no): ")
    if respuesta == "si":
        libros.append("Fahrenheit 451")
        print("'Fahrenheit 451' fue añadido.")
    else:
        print("No se añadió 'Fahrenheit 451'.")

print("-------------------------------------------------------------------------------------------------------")

# 2. Agregar Ray Bradbury si está George Orwell
if "George Orwell" in autores:
    respuesta = input("¿Agregar 'Ray Bradbury'? (si/no): ")
    if respuesta == "si":
        autores.append("Ray Bradbury")
        print("'Ray Bradbury' fue añadido.")
    else:
        print("No se añadió 'Ray Bradbury'.")

print("-------------------------------------------------------------------------------------------------------")

# 3. Eliminar El principito si está
if "El principito" in libros:
    respuesta = input("¿Eliminar 'El principito'? (si/no): ")
    if respuesta == "si":
        libros.remove("El principito")
        print("'El principito' fue eliminado.")
    else:
        print("Se mantuvo 'El principito'.")

print("-------------------------------------------------------------------------------------------------------")

# 4. Eliminar primer autor si hay más de 3
if len(autores) > 3:
    respuesta = input(f"¿Eliminar el primer autor '{autores[0]}'? (si/no): ")
    if respuesta == "si":
        eliminado = autores.pop(0)                 #pop es para eliminar un valor 
        print(f"'{eliminado}' fue eliminado.")
    else:
        print("No se eliminó ningún autor.")

print("-------------------------------------------------------------------------------------------------------")

# 5. Reemplazar Cien años de soledad
if "Cien años de soledad" in libros:
    respuesta = input("¿Reemplazar 'Cien años de soledad' por 'Crónica de una muerte anunciada'? (s/n): ")
    if respuesta == "s":
        libros.remove("Cien años de soledad")
        libros.append("Crónica de una muerte anunciada")
        print("Reemplazo realizado.")
    else:
        print("No se hizo ningún reemplazo.")

print("-------------------------------------------------------------------------------------------------------")

# 6. Crear destacados con los dos primeros libros
destacados = libros[:2]
print("Destacados:", destacados)

print("-------------------------------------------------------------------------------------------------------")

# 7. Autores vivos: los dos últimos autores
autores_vivos = autores[-2:]
print("Autores vivos:", autores_vivos)

print("-------------------------------------------------------------------------------------------------------")

# 8. Crear tupla libro destacado
libro_destacado = ()
if "Ray Bradbury" in autores:
    libro_destacado = ("Fahrenheit 451", "Ray Bradbury")
    print("Libro destacado:", libro_destacado)
else:
    print("Ray Bradbury no está en la lista, no se creó libro destacado.")

print("-------------------------------------------------------------------------------------------------------")

# 9. Añadir Premio Nobel
if "Crónica de una muerte anunciada" in destacados:
    respuesta = input("¿Agregar 'Premio Nobel' a destacados? (si/no): ")
    if respuesta == "si":
        destacados.append("Premio Nobel")
        print("'Premio Nobel' fue añadido.")
    else:
        print("No se añadió 'Premio Nobel'.")

print("-------------------------------------------------------------------------------------------------------")

# 10. Crear diccionario registro
registro = {}
if "Premio Nobel" in destacados:
    registro = {
        "titulo": "Crónica de una muerte anunciada",
        "autor": "Gabriel García Márquez",
        "disponible": True
    }
    print("Registro creado:", registro)
else:
    print("No se creó el registro porque no está 'Premio Nobel'.")

print("-------------------------------------------------------------------------------------------------------")

# 11. Agregar ubicación
if registro:
    respuesta = input("¿Agregar ubicación 'Estantería A3'? (si/no): ")
    if respuesta == "si":
        registro["ubicación"] = "Estantería A3"
        print("Ubicación añadida.")
    else:
        print("No se añadió ubicación.")


print("-------------------------------------------------------------------------------------------------------")

# 12. Agregar Don Quijote
if "Don Quijote" not in libros:
    respuesta = input("¿Agregar 'Don Quijote'? (si/no): ")
    if respuesta == "si":
        libros.append("Don Quijote")
        print("'Don Quijote' fue añadido.")
    else:
        print("No se añadió 'Don Quijote'.")

print("-------------------------------------------------------------------------------------------------------")

# 13. Agregar El principito
if "El principito" not in libros:
    respuesta = input("¿Agregar 'El principito'? (si/no): ")
    if respuesta == "si":
        libros.append("El principito")
        print("'El principito' fue añadido.")
    else:
        print("No se añadió 'El principito'.")


print("-------------------------------------------------------------------------------------------------------")

# 14. Mostrar todo
print("\n=== RESULTADO FINAL ===")
print("Libros:", libros)
print("Autores:", autores)
print("Destacados:", destacados)
print("Autores vivos:", autores_vivos)
print("Libro destacado:", libro_destacado)
print("Registro:", registro)

print("-------------------------------------------------------------------------------------------------------")
