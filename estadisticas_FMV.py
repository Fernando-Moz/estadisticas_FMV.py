# Estadísticas de una lista de notas

notas = [7.5, 4.0, 9.0, 5.5, 3.0, 8.0, 6.5]

# min, max, sum, len --> nota más alta, más baja y nota media
nota_maxima = max(notas)
nota_minima = min(notas)
nota_media = sum(notas) / len(notas)

print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
print(f"Nota media: {nota_media:.2f}")

# all, any --> ¿hay algún suspenso? ¿hay algún cero?
hay_suspenso = any(nota < 5 for nota in notas)
no_hay_ceros = all(nota != 0 for nota in notas)

print(f"¿Hay algún suspenso? {'Sí' if hay_suspenso else 'No'}")
print(f"¿No hay ningún cero? {'Sí' if no_hay_ceros else 'No'}")