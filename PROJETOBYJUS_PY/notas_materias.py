#criação da lista
result = ["Matemática", 90, "Inglês", 80, "História", 75, "Artes",85]

#utilização da técnica slicing para exibição
materias = result[::2]
print("Matérias:", materias)

notas = result[1::2]
print("Notas:", notas)