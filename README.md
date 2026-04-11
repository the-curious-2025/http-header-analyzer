# HTTP Header Analyzer (Python)

Simple CLI tool to check whether a target site returns baseline defensive security headers.

## Features

- Accepts URLs with or without scheme
- Follows redirects and prints final URL + status code
- Reports missing headers:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
- Prints server banner when exposed

## Requirements

- Python 3.8+
- `requests` (from `requirements.txt`)

## Usage

```bash
python header_analyzer.py example.com
python header_analyzer.py https://example.com
```

## Notes

This tool is passive and does not attempt exploitation.

## License

MIT (see `LICENSE`).
