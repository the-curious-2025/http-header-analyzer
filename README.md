# HTTP Header Analyzer

A simple CLI tool that analyzes HTTP response headers and flags missing security headers like CSP, HSTS, and X-Frame-Options.

## Installation

1. Make sure you have Python 3 installed
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Make the file executable:
   ```
   chmod +x header_analyzer.py
   ```

## Usage

```
./header_analyzer.py https://example.com
```

or

```
python header_analyzer.py example.com
```

The tool checks for the following headers:
- Content-Security-Policy (CSP)
- Strict-Transport-Security (HSTS)
- X-Frame-Options

## Example Output

```
Analyzing headers for: https://example.com
--------------------------------------------------
CSP: Present
HSTS: Missing
X-Frame-Options: Present
--------------------------------------------------
Some security headers are missing. Consider adding them for better security.
```

## Notes

- The tool automatically adds https:// if no protocol is specified
- It checks only basic security headers
- For Linux usage