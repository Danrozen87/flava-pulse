#!/usr/bin/env python3
"""
Render Flava Pulse newsletter as a 2x retina PDF.
All stories expanded, pixel-perfect, ready to attach to email.

Requires: playwright (pip install playwright && playwright install chromium)

Usage:
  python3 render-pdf.py --edition 20260325-01 --output-dir ./output
"""

import argparse
import asyncio
import os
import sys


async def render(edition, output_dir):
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("Installing playwright...")
        os.system("pip install playwright && playwright install chromium")
        from playwright.async_api import async_playwright

    html_path = os.path.join(output_dir, f"flava-pulse-{edition}.html")
    pdf_path = os.path.join(output_dir, f"flava-pulse-{edition}.pdf")

    if not os.path.exists(html_path):
        print(f"Error: {html_path} not found")
        sys.exit(1)

    abs_html = os.path.abspath(html_path)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            device_scale_factor=2,
            viewport={"width": 800, "height": 1200},
        )

        await page.goto(f"file://{abs_html}")
        await page.wait_for_load_state("networkidle")

        # Expand all stories
        await page.evaluate("""
            document.querySelectorAll('.story').forEach(s => {
                s.classList.add('open');
                s.setAttribute('aria-expanded', 'true');
            });
        """)

        # Hide share buttons and expand hints for clean print
        await page.evaluate("""
            document.querySelectorAll('.share-btn, .share-panel, .story-expand-hint').forEach(el => {
                el.style.display = 'none';
            });
            // Remove hover bg since all are expanded
            document.querySelectorAll('.story').forEach(s => {
                s.style.backgroundColor = 'transparent';
                s.style.cursor = 'default';
            });
        """)

        # Small pause for fonts to load
        await page.wait_for_timeout(1000)

        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "48px",
                "bottom": "48px",
                "left": "48px",
                "right": "48px",
            },
            scale=0.82,
        )

        await browser.close()

    file_size = os.path.getsize(pdf_path)
    print(f"PDF rendered: {pdf_path}")
    print(f"Size: {file_size / 1024:.0f} KB")
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render Flava Pulse as PDF")
    parser.add_argument("--edition", required=True)
    parser.add_argument("--output-dir", default="./output")
    args = parser.parse_args()
    asyncio.run(render(args.edition, args.output_dir))
