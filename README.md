# Postimg Brute Parser

This repository provides a small multithreaded parser that generates random
`postimg.cc` links and checks them for hosted images. Links have the format
`https://postimg.cc/********` where each `*` is an alphanumeric character.
If a page exists and contains an image with `id="main-image"`, the image URL is
printed.

## Usage

```
python postimg_parser.py [ATTEMPTS] [WORKERS]
```

- `ATTEMPTS` – how many random links to try (default: 100)
- `WORKERS` – number of worker threads (default: 10)

Example:

```
python postimg_parser.py 200 20
```

This will spawn 20 threads and check 200 random links.

