from abc import ABC, abstractmethod
class Identifizierbar(ABC):

    @abstractmethod
    def __init__(self, id):
        self.id = id

