#!/usr/bin/env python3
"""
Test script to find the correct Canvas LMS URL for Georgetown.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from canvas_api import _get_canvas_token
from canvasapi import Canvas


# Possible Canvas URLs for Georgetown
POSSIBLE_URLS = [
    "https://canvas.georgetown.edu",
    "https://georgetown.instructure.com",
    "https://georgetownuniversity.instructure.com",
]


def test_canvas_url(url: str, token: str) -> bool:
    """
    Test if a Canvas URL is valid.

    Args:
        url: Canvas URL to test
        token: Canvas API token

    Returns:
        True if URL works, False otherwise
    """
    print(f"\nTesting: {url}")
    try:
        canvas = Canvas(url, token)
        user = canvas.get_current_user()
        print(f"  ✓ Success! User: {user.name}")
        print(f"  ✓ User ID: {user.id}")
        print(f"  ✓ Correct URL: {url}")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:100]}")
        return False


def main():
    """Main function to test Canvas URLs."""
    print("Testing Canvas API URLs for Georgetown...")

    token = _get_canvas_token()
    print(f"Token loaded: {token[:10]}...")

    for url in POSSIBLE_URLS:
        if test_canvas_url(url, token):
            print(f"\n{'='*60}")
            print(f"CORRECT CANVAS URL: {url}")
            print(f"{'='*60}")
            return

    print("\n❌ None of the tested URLs worked.")
    print("Please check your Canvas API token or contact Georgetown IT support.")


if __name__ == "__main__":
    main()
