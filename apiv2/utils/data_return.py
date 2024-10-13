from typing import Dict


def data_return(self, index: int, src: str, *li: str) -> Dict:
    return {
        "id": f"iframe_embed_{index}",
        "name": li.text or f"Unnamed_{index}",
        "src": src,
    }
