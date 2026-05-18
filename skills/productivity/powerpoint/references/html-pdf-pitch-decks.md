# HTML-to-PDF pitch deck workflow

Use this when the user asks for a beautiful pitch deck and wants a PDF, especially when no PowerPoint template is provided.

## Pattern

1. Build the deck as a self-contained HTML file using one `<section class="slide">` per slide.
2. Set print sizing explicitly:
   - `@page { size: 16in 9in; margin: 0; }`
   - `.slide { width: 16in; height: 9in; page-break-after: always; overflow: hidden; }`
   - `body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }`
3. Use Playwright/Chromium to export the HTML to PDF with `print_background=True`, zero margins, and `prefer_css_page_size=True`.
4. Generate slide screenshots from the same HTML with Playwright (`locator('.slide').nth(i).screenshot(...)`) for visual QA when `pdftoppm`/Poppler is unavailable.
5. Create a contact sheet from screenshots and inspect it visually before delivery.
6. Run at least one fix-and-re-export loop if the first QA pass finds weak copy, cramped text, poor line breaks, or uneven composition.
7. Verify final PDF page count with available platform tooling (for example `mdls -name kMDItemNumberOfPages file.pdf` on macOS) and check file size.

## Playwright PDF export snippet

```python
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
html_path = ROOT / "deck.html"
pdf_path = ROOT / "Deck.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()  # or pass executable_path to an installed Chrome if bundled browser is missing
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.goto(html_path.as_uri(), wait_until="networkidle")
    page.pdf(
        path=str(pdf_path),
        width="16in",
        height="9in",
        print_background=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        prefer_css_page_size=True,
    )
    browser.close()
```

## Screenshot QA snippet

```python
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
html_path = ROOT / "deck.html"
out = ROOT / "deck_preview"
out.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.goto(html_path.as_uri(), wait_until="networkidle")
    slides = page.locator('.slide')
    for i in range(slides.count()):
        slides.nth(i).screenshot(path=str(out / f"slide-{i+1:02d}.png"))
    browser.close()
```

## QA checklist

- No blank pages or extra sections.
- No cropped/overlapping text.
- Body text remains readable on the contact sheet.
- Dark slides have enough contrast in body copy and footers.
- Headlines do not wrap into awkward single-word lines.
- Each slide has a clear visual element or layout device.
- Final PDF page count equals the intended slide count.
