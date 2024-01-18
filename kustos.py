from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class Karta:
    id: str
    jmeno: str
    prijmeni: str


class Kustos(ABC):

    @abstractmethod
    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        ...

    @abstractmethod
    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        ...

    @abstractmethod
    def muze_vstoupit(self, id_karty: str) -> bool:
        ...
