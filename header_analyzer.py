#!/usr/bin/env python3
"""
HTTP Header Analyzer
CLI tool that inspects HTTP response headers and flags missing security headers.
Checks for CSP, HSTS, X-Frame-Options.
"""

import argparse
import requests
import sys

def analyze_headers(url):
    """
    Analyze HTTP response headers for security headers.
    """
    try:
        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, timeout=10)
        
        headers = response.headers
        
        security_headers = {
            'Content-Security-Policy': 'CSP',
            'Strict-Transport-Security': 'HSTS', 
            'X-Frame-Options': 'X-Frame-Options'
        }
        
        print(f"Analyzing headers for: {url}")
        print("-" * 50)
        
        all_present = True
        for header, name in security_headers.items():
            if header in headers:
                print(f"{name}: Present")
                if header == 'Strict-Transport-Security' and not url.startswith('https://'):
                    print(f"   Warning: HSTS is present but URL is not HTTPS")
            else:
                print(f"{name}: Missing")
                all_present = False
        
        print("-" * 50)
        if all_present:
            print("All security headers are present!")
        else:
            print("Some security headers are missing. Consider adding them for better security.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='HTTP Header Analyzer - Check for missing security headers',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python header_analyzer.py https://example.com
  python header_analyzer.py example.com
        """
    )
    parser.add_argument('url', help='URL to analyze (with or without http/https)')
    
    args = parser.parse_args()
    analyze_headers(args.url)

if __name__ == '__main__':
    main()