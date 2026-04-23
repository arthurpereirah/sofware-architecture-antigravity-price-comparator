from .base_mapping import BasePlatform

class GenericPlatform(BasePlatform):
    def get_search_urls(self) -> list:
        return []

    def get_category(self, title: str) -> str:
        if any(x in title for x in ["volante", "pedais", "driving force", "g923", "g29"]):
            return "Volantes"
        elif any(x in title for x in ["headset", "fone", "áudio"]):
            return "Headsets & Áudio"
        elif any(x in title for x in ["jogo", "spider-man", "gran turismo", "ghost of", "resident evil", "pragmata", "mega man", "collection", "game", "ea sports"]):
            return "Jogos"
        elif any(x in title for x in ["cabo", "cable", "usb", "suporte", "base", "carregamento", "ssd", "macbook", "notebook"]):
            if "macbook" in title or "notebook" in title:
                return "Consoles"
            return "Acessórios & Hardware"
        elif any(x in title for x in ["controle", "controller", "mando", "joystick"]):
            return "Controles"
        return None

    def normalize_variant(self, title: str, category: str) -> str:
        if category == "Volantes":
            if "g29" in title:
                return "Volante Logitech G29"
            elif "g923" in title:
                return "Volante Logitech G923"
            elif "direct drive" in title or "g pro" in title or "pro wheel" in title:
                return "Volante Logitech G PRO Direct Drive"
            return "Volante Genérico"

        elif category == "Headsets & Áudio":
            if "g pro x 2" in title:
                return "Headset Logitech G PRO X 2"
            elif "g435" in title:
                return "Headset Logitech G435"
            return "Headset/Fones Diversos"

        elif category == "Controles":
            if "hori" in title or "luta" in title:
                return "Controle Fightpad Hori ALPHA"
            return "Controle Genérico"

        elif category == "Jogos":
            if "spider-man" in title:
                return "Jogo: Marvel's Spider-Man 2"
            elif "gran turismo" in title:
                return "Jogo: Gran Turismo 7"
            elif "ghost of" in title:
                return "Jogo: Ghost of Tsushima/Yōtei"
            elif "resident evil" in title:
                return "Jogo: Resident Evil"
            elif "pragmata" in title:
                return "Jogo: Pragmata"
            elif "mega man" in title:
                return "Jogo: Mega Man Collection"
            elif "ea sports" in title or "fc" in title:
                return "Jogo: EA Sports FC"
            return "Jogo Genérico"

        elif category == "Acessórios & Hardware":
            if "cabo" in title or "cable" in title:
                return "Cabo HDMI / USB"
            elif "ssd" in title or "firecuda" in title:
                return "SSD Interno M.2"
            elif "suporte" in title:
                return "Suporte Vertical Console"
            return "Acessório Genérico"
            
        elif category == "Consoles":
            if "macbook" in title:
                return "Macbook"
        
        return None
