from .base_mapping import BasePlatform

class PlayStationPlatform(BasePlatform):
    def get_search_urls(self) -> list:
        return ["https://www.amazon.com.br/s?k=playstation+5"]

    def get_category(self, title: str) -> str:
        if any(x in title for x in ["playstation 5", "playstation®5", "ps5", "pro"]):
            if "para console" not in title and not any(x in title for x in ["cabo", "case", "suporte", "base", "vr2", "portal"]):
                return "Consoles"
        if any(x in title for x in ["console ", "pacote ", "bundle", "edição digital", "digital edition", "disc edition", "disc console"]) and ("playstation" in title or "ps5" in title):
            return "Consoles"
        if "dualsense" in title or ("controle" in title and ("ps5" in title or "playstation" in title)):
            return "Controles"
        if any(x in title for x in ["vr2", "portal", "leitor de disco", "carregamento dualsense", "unidade de disco"]):
            return "Acessórios & Hardware"
        return None

    def normalize_variant(self, title: str, category: str) -> str:
        if category == "Consoles":
            if "pro" in title:
                return "Console PlayStation 5 PRO"
            elif "slim" in title:
                if "digital" in title or "edição digital" in title or ("disk" not in title and "disco" not in title):
                    if "digital" in title or "edição digital" in title:
                        return "Console PlayStation 5 Slim Digital"
                return "Console PlayStation 5 Slim Standard (Disco)"
            elif "digital" in title or "edição digital" in title:
                return "Console PlayStation 5 Base Digital"
            elif "ps5" in title or "playstation" in title:
                return "Console PlayStation 5 Standard (Base/Fat)"
                
        elif category == "Controles":
            if "edge" in title or "pro " in title:
                return "Controle DualSense Edge (Pro)"
            elif "dualsense" in title or ("controle" in title and ("ps5" in title or "playstation" in title)):
                return "Controle DualSense Padrão"
                
        elif category == "Acessórios & Hardware":
            if "portal" in title:
                return "PlayStation Portal"
            elif "vr2" in title:
                return "PlayStation VR2"
            elif "unidade de disco" in title or ("drive" in title and "direct drive" not in title):
                return "Leitor de Disco Avulso PS5"
            elif "base de carregamento" in title or "carregador" in title:
                return "Base de Carregamento DualSense"
        return None
