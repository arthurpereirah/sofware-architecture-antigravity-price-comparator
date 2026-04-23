from abc import ABC, abstractmethod

class BasePlatform(ABC):
    @abstractmethod
    def get_search_urls(self) -> list:
        pass

    @abstractmethod
    def get_category(self, title: str) -> str:
        """Retorna 'Consoles', 'Controles' ou None se não pertencer."""
        pass

    @abstractmethod
    def normalize_variant(self, title: str, category: str) -> str:
        """Tenta normalizar a variante, retorna a string ou None."""
        pass
