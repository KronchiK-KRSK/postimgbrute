import argparse
import random
import re
import string
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor


def random_id(length: int = 8) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def fetch_image(url: str):
<<<<<<< k7dm6z-codex/разработать-многопоточный-парсер-с-генерацией-ссылок
    """Fetch the page and return the main image URL if present."""
=======
>>>>>>> main
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status != 200:
                return None
            html = resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as exc:
<<<<<<< k7dm6z-codex/разработать-многопоточный-парсер-с-генерацией-ссылок
        if exc.code == 404:
            print(f"{url}: 404 not found")
        else:
=======
        if exc.code != 404:
>>>>>>> main
            print(f"{url}: HTTP {exc.code}")
        return None
    except Exception as exc:  # pragma: no cover - network errors
        print(f"{url}: {exc}")
        return None

    match = re.search(
        r'<img[^>]+id=["\']main-image["\'][^>]*src=["\']([^"\']+)', html
    )
    if match:
        return match.group(1)
    return None


def worker(_):
    code = random_id()
    page_url = f"https://postimg.cc/{code}"
<<<<<<< k7dm6z-codex/разработать-многопоточный-парсер-с-генерацией-ссылок
    print(f"Checking {page_url}")
=======
>>>>>>> main
    img = fetch_image(page_url)
    if img:
        print(f"Found image {img} on {page_url}")
        return page_url, img
<<<<<<< k7dm6z-codex/разработать-многопоточный-парсер-с-генерацией-ссылок
    print(f"No image found on {page_url}")
=======
>>>>>>> main
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Brute force postimg.cc pages"
    )
    parser.add_argument(
        "--count", type=int, default=10, help="Number of attempts"
    )
    parser.add_argument(
        "--threads", type=int, default=5, help="Number of threads"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional file to save found images",
    )
    args = parser.parse_args()

    results = []
    with ThreadPoolExecutor(max_workers=args.threads) as exe:
        for result in exe.map(worker, range(args.count)):
            if result:
                results.append(result)

    if args.output and results:
        with open(args.output, "w", encoding="utf-8") as f:
            for page, img in results:
                f.write(f"{page} {img}\n")


if __name__ == "__main__":
    main()
