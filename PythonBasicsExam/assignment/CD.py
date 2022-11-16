from Opera import Opera

class CD(Opera):
    #attributo di classe
    categoria="CD"

    #costruttore
    def __init__(self, titolo: str, numero_tracce: int, in_prestito=False,) -> None:
        super().__init__(titolo, in_prestito)
        self.numero_tracce = numero_tracce

    #getter
    def get_numero_tracce(self) -> int:
        return self.numero_tracce
    
    #setter
    def set_numero_tracce(self, numero_tracce: int) -> None:
        self.numero_tracce = numero_tracce

    #OVERRIDE del metodo produci_scheda ereditato da Opera
    def produci_scheda(self):
        print(f"Il {CD.categoria} {self.titolo} ({self.numero_tracce} tracce in totale) è concesso in prestito!")