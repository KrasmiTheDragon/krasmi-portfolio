# Usage: python3 scripts/set-theme.py brand      (themes: night aurora ember orchid paper graphite brand)
# Bakes the chosen theme into every page. Preview any theme without editing by adding ?theme=name to a page address.
import sys,re,glob,pathlib
t=sys.argv[1];root=pathlib.Path(__file__).resolve().parent.parent
for f in root.glob('*.html'):
    s=f.read_text(encoding='utf8');s=re.sub(r'<html lang="(\w+)"( data-theme="\w+")?',lambda m:'<html lang="%s"%s'%(m.group(1),'' if t=='night' else ' data-theme="%s"'%t),s,count=1);f.write_text(s,encoding='utf8')
print('theme set to',t)
