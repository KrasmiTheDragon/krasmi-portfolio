# Regenerates assets/media-kit-en.pdf and assets/media-kit-fi.pdf (A4) in the site's look.
# Edit the numbers in STATS / PLATFORMS below, then run from the repo root:  python3 scripts/make-media-kit.py
# Needs: pip install playwright && playwright install chromium
import pathlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parent.parent
ASOF={'en':'as of 15 Oct 2026','fi':'15.10.2026 tilanne'}
# platform, handle, followers, views  (None = not available)
PLATFORMS=[("Twitch","twitch.tv/krasmi",841,1574),("YouTube","@krasmi",199,1900),("YouTube","@lifeofkrasmi",43,92),("YouTube Clips","Krasmi Clips",6,10219),
("TikTok","@krasmithedragon",192,19621),("Instagram","@krasmithedragon",84,18700),("Instagram","@krasilamicke",212,396),("X","@krasmithedragon",233,None),("Kick","@krasmithedragon",44,69),("Bluesky","@wyrmscalesyndicate.com",76,None)]
FOLLOWERS=sum(p[2] or 0 for p in PLATFORMS);VIEWS=sum(p[3] or 0 for p in PLATFORMS)
FEAT=[('ALIEN OVERLORD VS. CULT OF THE DRAGON | DBD Full Match Edit','youtu.be/0HYiU5MpMXA'),('Twitch Marker Tutorial (Finnish)','youtu.be/A_NDatUwPUE'),('Stream Highlights #8, edited for Sha77etv','youtu.be/xR0NCuSIImg')]
BRANDS=["strafe","gamerbulk","yvolve","allkeyshop","soulmate","pitaka","dakota-irish","kamk-gg","fel","igda-finland","finnish-game-jam","northern-game-summit"]
T={'en':dict(lang='en',kit='CONTENT CREATOR MEDIA KIT',sub='Variety Gaming & Tech Creator · Twitch Affiliate · Multi-platform',
 bio='A Finnish variety-gaming streamer and dragon-themed VTuber persona, blending tech tutorials, live commentary and community-first streaming across Twitch, YouTube, TikTok, X, Instagram and Kick. Behind the persona: a game producer and A/V professional with live-broadcast credits for KAMK.GG, the Finnish Esport League and IGDA Finland.',
 reach='Reach',fol='Followers, all platforms',vw='Views, all platforms',mo='Views per month, all platforms',rk='Finnish Twitch channel (top 1.52%)',hr='Hours streamed, recent months',vd='YouTube videos published',
 feat='Featured edits',plat='Platforms',pl='Platform',hd='Account',fo='Followers',vi='Views',why='Why partner with Krasmi',
 w=[('Bilingual','Native Finnish, fluent English: content and callouts work for Nordic and international audiences.'),('Production quality built in','Professional editing (DaVinci Resolve) and OBS/Streamer.bot workflows, so sponsor integrations look and sound polished, not bolted on.'),('Rooted in the Finnish games and esports scene','Active ties to IGDA Finland, KAMK.GG and the Finnish Game Jam: real reach into a niche, engaged audience.'),('Steady, growing channel','Regular stream and upload cadence and an actively growing Twitch community.')],
 pil='Content pillars',pills=['Variety gaming','Tech tutorials','Stream-tool guides','VTuber / dragon lore','Community events'],fit='Past brand fit',fits='Gaming peripherals & PC hardware · streaming software & overlays · energy drinks · Nordic gaming events · creator-economy tools',
 wk='Worked with',cta="Let's work together",ctat='Sponsored streams, product reviews, affiliate partnerships and video edits. Rates on request.',foot='Content Creator Kit · November 2026'),
'fi':dict(lang='fi',kit='SISÄLLÖNTUOTTAJAN MEDIAKORTTI',sub='Variety Gaming & Tech -sisällöntuottaja · Twitch Affiliate · Monikanavainen',
 bio='Suomalainen variety-gaming-striimaaja ja lohikäärmeteemainen VTuber-persoona, jonka sisältö yhdistää tekniikkatutoriaaleja, livekommentointia ja yhteisölähtöistä striimaamista Twitchissä, YouTubessa, TikTokissa, X:ssä, Instagramissa ja Kickissä. Persoonan takana on pelituottaja ja A/V-ammattilainen, jolla on lähetystuotantoreferenssejä KAMK.GG:ltä, Finnish Esport Leaguelta ja IGDA Finlandilta.',
 reach='Tavoittavuus',fol='Seuraajat, kaikki alustat',vw='Katselut, kaikki alustat',mo='Katselukertaa kuukaudessa, kaikki alustat',rk='Suomen Twitch-kanavista (top 1,52 %)',hr='Striimattuja tunteja viime kuukausina',vd='Julkaistua YouTube-videota',
 feat='Valitut editoinnit',plat='Alustat',pl='Alusta',hd='Tili',fo='Seuraajat',vi='Katselut',why='Miksi tehdä yhteistyötä Krasmin kanssa',
 w=[('Kaksikielinen','Äidinkielenä suomi, sujuva englanti: sisältö ja nostot toimivat sekä pohjoismaiselle että kansainväliselle yleisölle.'),('Tuotantolaatu sisäänrakennettuna','Ammattimainen editointi (DaVinci Resolve) ja OBS/Streamer.bot-työnkulut: yhteistyöt näyttävät ja kuulostavat viimeistellyiltä.'),('Osa Suomen peli- ja esports-kenttää','Yhteydet IGDA Finlandiin, KAMK.GG:hen ja Finnish Game Jamiin: aitoa tavoittavuutta sitoutuneelle kapealle yleisölle.'),('Tasainen, kasvava kanava','Säännöllinen striimaus- ja julkaisutahti sekä aktiivisesti kasvava Twitch-yhteisö.')],
 pil='Sisältöpilarit',pills=['Variety gaming','Tekniikkatutoriaalit','Striimaustyökalut','VTuber / lohikäärmetarusto','Yhteisötapahtumat'],fit='Aiempi brändisopivuus',fits='Pelilaitteet ja tietokonekomponentit · striimausohjelmistot ja overlayt · energiajuomat · pohjoismaiset pelitapahtumat · sisällöntuottajien työkalut',
 wk='Yhteistyössä mukana',cta='Tehdään yhteistyötä',ctat='Sponsoroidut striimit, tuotearvostelut, affiliate-yhteistyöt ja videoeditoinnit. Hinnat pyynnöstä.',foot='Sisällöntuottajan mediakortti · marraskuu 2026')}
def fmt(n,l):return (f"{n:,}".replace(',',' ' if l=='fi' else ',')) if n is not None else '–'
def html(l):
    t=T[l];nb=lambda s:s.replace(' ','\u00a0')
    rows=''.join(f"<tr><td><b>{p[0]}</b></td><td>{p[1]}</td><td class=n>{fmt(p[2],l)}</td><td class=n>{fmt(p[3],l)}</td></tr>" for p in PLATFORMS)
    tiles=[(fmt(FOLLOWERS,l),t['fol']+' ('+ASOF[l]+')'),(fmt(VIEWS,l),t['vw']+' ('+ASOF[l]+')'),('~9K',t['mo']),('#396',t['rk']),('157+',t['hr']),('198',t['vd'])]
    return f'''<!doctype html><html lang="{l}"><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}*{{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{margin:0;background:#0a1030;color:#e8ecf5;font:9.6pt/1.45 "DejaVu Sans",system-ui,sans-serif}}
.pg{{width:210mm;height:297mm;padding:0 0 10mm;position:relative;overflow:hidden}}
.hd{{background:linear-gradient(135deg,#2D6CA8 0%,#2D4486 50%,#2D1D6A 100%);padding:13mm 14mm 10mm;display:flex;gap:7mm;align-items:center}}
.hd img{{height:30mm}}.k{{letter-spacing:.18em;font-size:7.5pt;color:#cfe9ff}}h1{{font:700 26pt Georgia,"DejaVu Serif",serif;margin:1mm 0 1mm}}h1 i{{color:#8fe8ff}}.sb{{font-size:10.5pt;color:#fff}}
.bd{{padding:7mm 14mm 0}}p{{margin:0 0 3mm}}.bio{{color:#cdd6ee;max-width:175mm}}
h2{{font:700 12pt Georgia,"DejaVu Serif",serif;margin:5mm 0 2.5mm;color:#fff;border-bottom:1px solid #2c3a78;padding-bottom:1.2mm}}
.tl{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}.tl div{{background:#121b4a;border-left:3px solid #3fd0ff;border-radius:2mm;padding:3mm 4mm}}.tl b{{display:block;font:700 19pt Georgia,"DejaVu Serif",serif;color:#8fe8ff}}.tl span{{font-size:7.6pt;color:#b9c4e6}}
table{{width:100%;border-collapse:collapse;font-size:8.6pt}}th{{text-align:left;color:#8fe8ff;font-weight:600;border-bottom:1px solid #2c3a78;padding:1.2mm 1.5mm}}td{{padding:1.1mm 1.5mm;border-bottom:1px solid #18235a}}.n{{text-align:right}}th.n{{text-align:right}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}.w b{{color:#fff}}.w p{{margin:0 0 2mm;font-size:8.8pt;color:#cdd6ee}}.pl span{{display:inline-block;border:1px solid #3a4d9c;border-radius:99px;padding:.6mm 2.6mm;margin:0 1.2mm 1.4mm 0;font-size:8pt;color:#e8ecf5}}
.lg{{display:grid;grid-template-columns:repeat(6,1fr);gap:2.2mm}}.lg div{{background:#fff;border-radius:1.6mm;height:15mm;display:flex;align-items:center;justify-content:center;padding:1.2mm}}.lg img{{max-width:100%;max-height:100%;object-fit:contain}}
.ct{{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(135deg,#2D6CA8,#2D4486 50%,#2D1D6A);padding:6mm 14mm;display:flex;justify-content:space-between;align-items:center}}.ct b{{font:700 13pt Georgia,"DejaVu Serif",serif}}.ct small{{display:block;color:#dbe7ff}}.ct div:last-child{{text-align:right;font-size:8.6pt}}
.pg{{page-break-after:always}}.hd.sm{{padding:7mm 14mm}}.hd.sm img{{height:16mm}}.hd.sm h1{{font-size:17pt;margin:0}}.cols{{grid-template-columns:1fr!important}}.cols>div{{margin-bottom:2mm}}</style><div class="pg"><div class="hd"><img src="assets/logo.webp"><div><div class="k">WYRMSCALE SYNDICATE · {t['kit']}</div><h1>Krasmi <i>the Dragon</i></h1><div class="sb">{t['sub']}</div></div></div>
<div class="bd"><p class="bio">{t['bio']}</p>
<h2>{t['reach']}</h2><div class="tl">{''.join(f"<div><b>{a}</b><span>{b}</span></div>" for a,b in tiles)}</div>
<h2>{t['plat']}</h2><table><tr><th>{t['pl']}</th><th>{t['hd']}</th><th class="n">{t['fo']}</th><th class="n">{t['vi']}</th></tr>{rows}</table>
<h2>{t['feat']}</h2><div class="w">{''.join(f"<p><b>{a}</b> · {b}</p>" for a,b in FEAT)}</div></div></div>
<div class="pg"><div class="hd sm"><img src="assets/logo.webp"><div><h1>Krasmi <i>the Dragon</i></h1><div class="sb">{t['sub']}</div></div></div><div class="bd">
<div class="cols"><div><h2>{t['why']}</h2><div class="w">{''.join(f"<p><b>{a}.</b> {b}</p>" for a,b in t['w'])}</div></div><div><h2>{t['pil']}</h2><div class="pl">{''.join(f"<span>{x}</span>" for x in t['pills'])}</div><h2>{t['fit']}</h2><p style="font-size:8.8pt;color:#cdd6ee">{t['fits']}</p></div></div>
<h2>{t['wk']}</h2><div class="lg">{''.join(f'<div><img src="assets/partners/{b}.webp"></div>' for b in BRANDS)}</div></div>
<div class="ct"><div><b>{t['cta']}</b><small>{t['ctat']}</small></div><div>krasmi.official@gmail.com<br>krasmi.wyrmscalesyndicate.com<br>projectdigital.io/creators/Krasmi<br><small>{t['foot']}</small></div></div></div></html>'''
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    for l in('en','fi'):
        f=root/f'_kit_{l}.html';f.write_text(html(l),encoding='utf8');pg.goto(f.as_uri());pg.wait_for_timeout(500)
        pg.pdf(path=str(root/'assets'/f'media-kit-{l}.pdf'),format='A4',print_background=True,prefer_css_page_size=True);f.unlink();print('saved',l,'followers',FOLLOWERS,'views',VIEWS)
    b.close()
