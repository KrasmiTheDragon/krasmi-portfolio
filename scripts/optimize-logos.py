# Usage (needs Pillow: pip install pillow):  python3 scripts/optimize-logos.py
# Converts every PNG/JPG in assets/partners/ into a cropped, small WebP with the same name (originals are kept).
import os
from PIL import Image,ImageChops
D=os.path.join(os.path.dirname(__file__),'..','assets','partners')
for f in sorted(os.listdir(D)):
    n,e=os.path.splitext(f)
    if e.lower() not in('.png','.jpg','.jpeg'):continue
    im=Image.open(os.path.join(D,f)).convert('RGBA');flat=Image.alpha_composite(Image.new('RGBA',im.size,(255,255,255,255)),im).convert('RGB')
    if all(min(flat.getpixel(p))>240 for p in [(2,2),(im.width-3,2),(2,im.height-3),(im.width-3,im.height-3)]):
        bb=ImageChops.invert(flat.convert('L')).point(lambda v:255 if v>12 else 0).getbbox()
        if bb:
            p=max(4,int(.03*max(im.size)));im=im.crop((max(bb[0]-p,0),max(bb[1]-p,0),min(bb[2]+p,im.width),min(bb[3]+p,im.height)))
    im.thumbnail((360,180));im.save(os.path.join(D,n+'.webp'),'WEBP',quality=86,method=6);print('ok',n+'.webp',im.size)
