from urllib.parse import unquote
from typing import List


def get_first_chapter(chapters: List[str], unquoted: bool = True) -> List[str]:
    grouped_chapters = {}

    for chapter_url in chapters:
        chapter_url = chapter_url if unquoted else unquote(chapter_url)
        splited_chapter_url = chapter_url.split("-")
        chapter_idx = None
        chapter_slice_idx = None
        chapter_slice = None

        for slice in splited_chapter_url:
            if len(slice) == 2 and slice.startswith("ج") and slice[1].isdigit():
                chapter_idx = int(slice[1])
                chapter_slice_idx = chapter_url.index(slice)
                chapter_slice = slice
                break

        base_url = "-".join(
            [slice for slice in splited_chapter_url if slice != chapter_slice]
        )

        if base_url not in grouped_chapters:
            grouped_chapters[base_url] = {
                "least_chapter": chapter_idx,
                "least_chapter_slice_idx": chapter_slice_idx,
                "original_url": chapter_url,
            }
        else:
            if chapter_idx < grouped_chapters[base_url]["least_chapter"]:
                grouped_chapters[base_url]["least_chapter"] = chapter_idx
                grouped_chapters[base_url][
                    "least_chapter_slice_idx"
                ] = chapter_slice_idx
                grouped_chapters[base_url]["original_url"] = chapter_url

    result = []
    for base_url, data in grouped_chapters.items():
        original_url = data["original_url"]
        least_chapter_slice_idx = data["least_chapter_slice_idx"]
        least_chapter = data["least_chapter"]

        if least_chapter_slice_idx is not None:
            url = (
                original_url[:least_chapter_slice_idx]
                + f"ج{least_chapter}"
                + original_url[least_chapter_slice_idx + 2 :]
            )
            result.append(url)
        else:
            result.append(original_url)

    return result
