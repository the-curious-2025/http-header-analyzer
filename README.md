# HTTP Header Analyzer

CLI tool for checking basic web security headers on a target URL.

It sends a request, follows redirects, and reports which recommended headers are missing.

## Requirements

- Python 3.8+
- `requests`

Install:

```bash
pip install -r requirements.txt
```

## Quick start

```bash
python header_analyzer.py example.com
```

## What it checks

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`

## Example output

```text
Analyzing headers for: https://example.com
Final URL: http://example.com/
Status Code: 200
[MISSING] Content-Security-Policy
...
Result: 6 recommended security headers are missing.
```

## Common issues

- **TLS verification failed**: the tool retries over HTTP and prints a warning.
- **Request timeout**: check connectivity or try another target.

## Notes

This is a passive check. It does not exploit or modify the target.

## License

MIT.
