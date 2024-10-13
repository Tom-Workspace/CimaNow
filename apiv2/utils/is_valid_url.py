from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    parsed_url = urlparse(url)
    return parsed_url.netloc not in [
        "securepubads.g.doubleclick.net",
        "ads.example.com",
    ]
