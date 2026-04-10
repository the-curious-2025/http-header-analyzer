# HTTP Header Analyzer

A CLI tool that inspects HTTP response headers and flags missing security headers like CSP, HSTS, and X-Frame-Options.

## Features

- Checks for essential security headers
- Simple CLI interface
- Supports HTTP and HTTPS URLs

## Usage

```bash
python header_analyzer.py <url>
```

### Examples

```bash
python header_analyzer.py https://example.com
python header_analyzer.py example.com  # Automatically adds https://
```

## Requirements

- Python 3.x
- requests library (`pip install requests`)

## License

MIT