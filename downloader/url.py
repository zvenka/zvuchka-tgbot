from urllib.parse import urlparse

def is_yt_url(link: str) -> bool:
    parsed = urlparse(link)

    return parsed.hostname in (
        "youtube.com",
        "www.youtube.com",
        "youtu.be",
    )
