from typing import List, Dict
import apiv2


class SeriesSeasons:
    def series_seasons(client: "apiv2.Client", url: str) -> List[Dict]:
        results_inf = client.get_item(url, 15)
        series_link = []

        for index, item in enumerate(results_inf, start=1):
            link_item = item.get("item_link", "")


            if not link_item.startswith("https://bs.cimanow.cc/selary/"):
                continue
            series_link.append(
                {
                    "id": index,
                    "title": item.get("name", ""),
                    "year": item.get("year", ""),
                    "link": link_item,
                }
            )

        return series_link
