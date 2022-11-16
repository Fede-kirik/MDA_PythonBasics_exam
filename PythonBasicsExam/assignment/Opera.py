
class Opera():

    #costruttore
    def __init__(self, titolo: str, in_prestito = False) -> None:
        self.titolo = titolo
        self.in_prestito = in_prestito

    def colloca_in_prestito(self) -> None:
        self.in_prestito = True
    
    def restituzione_dal_prestito(self) -> None:
        self.in_prestito = False
    
    #getter
    def get_titolo(self) -> str:
        return self.titolo

    #setter
    def set_titolo(self, new_titolo: str):
        self.titolo = new_titolo

    #definisco come rappresentare l'oggetto Opera quando viene passato ad un print
    def __repr__(self) -> str:
        if self.in_prestito: 
            print("Attualmente in prestito!")
        else:
            print("Non in prestito!")

    #dichiaro il metodo produci_scheda che poi implemento nelle classi figlie  
    def produci_scheda(self):
        pass