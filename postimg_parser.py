import concurrent.futures
import random
import re
import string
import sys
from typing import Optional, Tuple

from urllib import request, error


ALPHABET = string.ascii_letters + string.digits


def random_slug(length: int = 8) -> str:
    """Return a random slug composed of ASCII letters and digits."""
    return ''.join(random.choice(ALPHABET) for _ in range(length))


def fetch_image(slug: str) -> Tuple[str, Optional[str]]:
    """Fetch postimg page by slug and return (slug, image url) if found."""
    url = f"https://postimg.cc/{slug}"
    try:
        with request.urlopen(url, timeout=10) as resp:
            if resp.status != 200:
                return slug, None
            html = resp.read().decode("utf-8", "ignore")
    except error.URLError:
        return slug, None

    pattern = r'<img[^>]*id=["\']main-image["\'][^>]*src=["\']([^"\']+)["\']'
    match = re.search(pattern, html)
    if match:
        return slug, match.group(1)
    return slug, None


def main(attempts: int = 100, workers: int = 10) -> None:
    """Generate random links and check them concurrently."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(fetch_image, random_slug()) for _ in range(attempts)]
        for future in concurrent.futures.as_completed(futures):
            slug, img_url = future.result()
            if img_url:
                print(f"Found {slug}: {img_url}")


if __name__ == "__main__":
    attempts = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    main(attempts, workers)
