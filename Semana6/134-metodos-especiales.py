class Libro:
    def __init__(self, autor, titulo, paginas):
        self.autor = autor
        self.titulo = titulo
        self.pagina = paginas

    def __str__(self):

        return f"Titulo '{self.titulo}'\nEscrito por: {self.autor}'"

    def __len__(self):
        return self.pagina

libro_1 = Libro("Stepehen King", "Cujo", 1074)
print(str(libro_1))
print(len(libro_1))