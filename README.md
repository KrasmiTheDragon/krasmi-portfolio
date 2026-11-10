# krasmi.wyrmscalesyndicate.com
1. `python3 fetch-assets.py` (downloads project images into assets/p1-p3.jpg); check the order is Curse of Trespassing, Smolrors, Colorbox.
2. Push to a GitHub repo, Settings > Pages > Deploy from branch `main` / root. `CNAME` sets the domain; tick Enforce HTTPS.
3. Cloudflare DNS: CNAME `krasmi` -> `krasmithedragon.github.io`, **DNS only** until HTTPS is issued.
4. Text lives in `assets/data.js` (EN/FI side by side). Media kits: replace `assets/media-kit-en.pdf` and `assets/media-kit-fi.pdf` to update them (the four numbers on the Content page are keys s1-s4 in data.js).

5. Partner logos: drop WebP/PNG-converted logos into `assets/partners/` (see that folder's README.txt). Contact form opens the visitor's email app; to send directly instead, create a free Formspree (or similar) form and paste its URL into `D.FORM` at the end of `assets/data.js`. Phone number: set `D.PHONE` (empty = hidden).

6. Logos: drop any PNG/JPG into `assets/partners/` named like the card (see README.txt there); the site shows `.webp` if present, else `.png`. For small, cropped WebP versions run `python3 scripts/optimize-logos.py`.
7. Share previews (Open Graph) use `assets/og-home.jpg`, `og-game.jpg`, `og-content.jpg` (1200x630). After publishing, refresh caches with the Facebook Sharing Debugger / LinkedIn Post Inspector; Discord and X cache for a while too.

8. CV PDFs: `assets/Micke-Krasila-CV-en.pdf` / `-fi.pdf` are generated from the CV page. After you change CV text in `assets/data.js`, run `python3 scripts/make-cv-pdf.py` and commit the new PDFs.
9. Status ("open to work"): edit or switch off `D.STATUS` in `assets/data.js`. Analytics: fill in `D.ANALYTICS` (provider + id) in the same file; leave empty to keep it off.
10. Case studies: edit the `cs` sections of the project entries in `assets/data.js`; add photos/video via `media:[{src,a:{en,fi}}]` or `v:"YouTubeID"`. Missing images are skipped automatically.
