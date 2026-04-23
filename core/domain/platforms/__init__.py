from .playstation import PlayStationPlatform
from .xbox import XboxPlatform
from .generic import GenericPlatform

class PlatformRegistry:
    def __init__(self):
        self.platforms = [
            PlayStationPlatform(),
            XboxPlatform(),
            GenericPlatform()
        ]

    def get_all_search_urls(self) -> list:
        urls = []
        for p in self.platforms:
            urls.extend(p.get_search_urls())
        return urls

    def categorize(self, title: str) -> str:
        t = title.lower()
        for p in self.platforms:
            cat = p.get_category(t)
            if cat:
                return cat
        return "Outros"

    def normalize_variant(self, title: str, category: str) -> str:
        t = title.lower()
        for p in self.platforms:
            var = p.normalize_variant(t, category)
            if var:
                return var
        return f"Outros: {title[:30]}"
