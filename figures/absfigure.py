from abc import ABC, abstractmethod


class Figure(ABC):
    _name = 'Abstract figure'

    @abstractmethod
    def area(self):
        pass
