from .base_mapping import BasePlatform

class XboxPlatform(BasePlatform):
    def get_search_urls(self) -> list:
        return ["https://www.amazon.com.br/s?k=xbox+one"]

    def get_category(self, title: str) -> str:
        if "xbox one" in title or "xbox series" in title or "xbox 360" in title:
            if "controle" in title or "controller" in title:
                return "Controles"
            if "para xbox" not in title and not any(x in title for x in ["cabo", "case", "suporte"]):
                return "Consoles"
        return None

    def normalize_variant(self, title: str, category: str) -> str:
        if category == "Consoles" and "xbox" in title:
            if "series x" in title:
                return "Console Xbox Series X"
            elif "series s" in title:
                return "Console Xbox Series S"
            elif "xbox one" in title:
                return "Console Xbox One"
            elif "xbox 360" in title:
                return "Console Xbox 360"
            return "Console Xbox"

        elif category == "Controles" and ("xbox" in title or "controller" in title):
            if "elite" in title:
                return "Controle Xbox Elite"
            return "Controle Xbox One"
        return None
