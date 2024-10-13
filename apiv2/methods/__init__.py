from .get_pages import GetItem, GetPagesLinks, ScrapePage
from .search import (
    SeriesSeasons,
    GetSeriesEpisodes,
    GetSeriesSeasons,
    HandleSeriesLinks,
)
from .watching import GetIframeButtons, RemoveAds

from .download_links import QualityInformation


class Methods(
    GetItem,
    GetPagesLinks,
    ScrapePage,
    SeriesSeasons,
    GetSeriesEpisodes,
    GetSeriesSeasons,
    HandleSeriesLinks,
    GetIframeButtons,
    RemoveAds,
):
    pass
