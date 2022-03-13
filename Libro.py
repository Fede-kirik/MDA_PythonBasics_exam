from Opera import Opera

class Libro(Opera):
    #attributo di classe
    categoria = "Libro"

    #costruttore
    def __init__(self, titolo: str, numero_pagine: int, in_prestito=False) -> None:
        super().__init__(titolo, in_prestito)
        self.numero_pagine = numero_pagine

    #getter
    def get_numero_pagine(self) -> int:
        return self.numero_pagine

    #setter
    def set_numero_pagine(self, numero_pagine) -> None:
        self.numero_pagine = numero_pagine

    #OVERRIDE del metodo produci_scheda ereditato da Opera
    def produci_scheda(self):
        print(f"Il {Libro.categoria} {self.titolo} ({self.numero_pagine} pagine in totale) è concesso in prestito!")
        
