from kustos import Kustos, Karta
from typing import Optional

class Terminal(Kustos):

    
    def __init__(self) -> None:
        self._zaznamenane_karty : dict[str, str] = {}
    
    
    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        self.gjmen = jmeno
        self.gprimeni = prijmeni

        self.jmeno_držitele = (jmeno + " " + prijmeni)

        self._zaznamenane_karty.update({id_karty : self.jmeno_držitele})
        # print(self.zaznamenane_karty)

        return print(Karta(id_karty, jmeno, prijmeni))

    
    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        # print("Karta odebrána")
        jmeno = self.gjmen
        prijmeni = self.gprimeni
        self._zaznamenane_karty.pop(id_karty, None)

        return print(Karta(id_karty, jmeno, prijmeni))

    
    def muze_vstoupit(self, id_karty: str) -> bool:
        return self._zaznamenane_karty.get(id_karty) is not None

        
t = Terminal()
t.pridej_kartu("1", "Šimon", "Klíma")
print(t.muze_vstoupit("1"))
t.odeber_kartu("1")
print(t.muze_vstoupit("1"))
