class Usuario:
    def __init__(self, nome: str, id_usuario: str):
        self.nome = nome
        self.id_usuario = id_usuario  

    def __str__(self):
        return f"{self.nome} (id: {self.id_usuario})"
