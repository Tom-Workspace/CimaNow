import base64
from typing import Dict, List
from bs4 import BeautifulSoup as bs
import requests
from urllib.parse import unquote


def fetch_page_content(url: str) -> str:
    response = requests.get(url)
    response.encoding = "utf-8"
    return response.text


def clean_html_content(content: str) -> str:
    lines = content.split("\n")
    if (
        len(lines) > 3
        and lines[0].startswith("<script")
        and lines[1].startswith("var")
        and lines[2].startswith("var")
    ):
        lines = lines[3:]
    end_marker = "var _0x0dd0"
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].startswith(end_marker):
            lines = lines[:i]
            break
    cleaned_content = "\n".join(lines)
    if cleaned_content and cleaned_content[-1] == ";":
        cleaned_content = cleaned_content[:-1].replace("+", "")
    return cleaned_content


def decode_base64_content(content: str) -> str:
    encoded_parts = content.split(".")
    decoded_parts = []

    for part in encoded_parts:
        while len(part) % 4 != 0:
            part += "="
        try:
            decoded_part = base64.b64decode(part).decode("utf-8")
            numeric_value = "".join(filter(str.isdigit, decoded_part))
            decoded_parts.append(numeric_value)
        except (base64.binascii.Error, UnicodeDecodeError):
            print(f"خطأ في فك التشفير للجزء: {part}")
            continue

    decoded_chars = [chr(int(part)) for part in decoded_parts if part.isdigit()]
    return "".join(decoded_chars)


def extract_download_links(decoded_text: str) -> List[Dict]:
    soup = bs(decoded_text, "lxml")
    lists = soup.find_all("ul", {"id": "download"})

    download_links = [
        {"quality": unquote(link.text.strip()), "link": link.get("href", None)}
        for ul in lists
        for link in ul.find_all("a")
    ]

    return download_links


def QualityInformation(url: str) -> List[Dict]:
    content = fetch_page_content(url)
    cleaned_content = clean_html_content(content)
    # decoded_text = decode_base64_content(cleaned_content)
    links = extract_download_links(cleaned_content)
    return links


