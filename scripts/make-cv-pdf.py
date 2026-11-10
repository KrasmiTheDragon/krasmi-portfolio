# Regenerates the compact CVs (Micke-Krasila-CV-en/fi.pdf) and the full ones (Micke-Krasila-CV-full-en/fi.pdf) from cv.html using the print stylesheet.
# Needs: pip install playwright && playwright install chromium     Run from the repo root:  python3 scripts/make-cv-pdf.py
import pathlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    for lang in('en','fi'):
        for full in(False,True):
            pg.goto((root/'cv.html').as_uri()+'?lang='+lang+('&full=1' if full else ''));pg.wait_for_timeout(600)
            pg.emulate_media(media='print')
            pg.pdf(path=str(root/'assets'/f'Micke-Krasila-CV-{"full-" if full else ""}{lang}.pdf'),format='A4',print_background=True,prefer_css_page_size=True)
            print('saved',lang,'full' if full else 'compact')
    b.close()
