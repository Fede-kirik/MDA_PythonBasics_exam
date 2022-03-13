
class Studente:

    def __init__(self, nome: str, cognome:str) -> None:
        self.nome = nome
        self.cognome = cognome

    #get nome+cognome
    def get_nominativo(self) -> str:
        return f"{self.nome} " + self.cognome

    #set nome
    def set_nome(self, new_nome:str):
        self.nome = new_nome

    #set cognome
    def set_cognome(self, new_cognome:str):
        self.cognome = new_cognome

