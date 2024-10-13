from apiv2.utils import decoding
from apiv2.utils import get_first_chapter
from typing import Dict
import apiv2


class HandleSeriesLinks:
    def handle_series_links(client: "apiv2.Client", url: str) -> Dict:
        series_seasons = client.series_seasons(url)
        links = []
        for season in series_seasons:
            link = season["link"] if season["link"] else None
            decrypt_link = decoding("decrypt", link)
            links.append(decrypt_link)
        return get_first_chapter(links)
