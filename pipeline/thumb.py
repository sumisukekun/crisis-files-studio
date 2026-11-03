"""サムネイル: エピソードの THUMB 設定から作る。出力: build/<ep>/thumbnail.jpg
usage: python pipeline/thumb.py ep11_onoda
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from common import SANS_BLACK as SANS, SERIF_BLACK as SERIF, load
ep, WORK = load(sys.argv[1]); os.chdir(WORK); C = ep.THUMB
W,H=1920,1080
RED=(214,20,28)
src=Image.open(f"images/{C['image']:03d}.jpg").convert("RGB")
s=H/src.height; src=src.resize((round(src.width*s),H),Image.LANCZOS)
img=Image.new("RGB",(W,H),(0,0,0)); img.paste(src,(-120,0))
img=ImageEnhance.Contrast(img).enhance(1.15)
shade=Image.new("L",(W,H),0); d=ImageDraw.Draw(shade)
for x in range(W):
    a=0 if x<1150 else min(235,int((x-1150)/280*235)); d.line([(x,0),(x,H)],fill=a)
img=Image.composite(Image.new("RGB",(W,H),(0,0,0)),img,shade)
vig=Image.new("L",(W,H),0); ImageDraw.Draw(vig).ellipse([-400,-300,W+400,H+300],fill=255); vig=vig.filter(ImageFilter.GaussianBlur(200))
img=Image.composite(img,Image.new("RGB",(W,H),(0,0,0)),vig)
d=ImageDraw.Draw(img)
def vtext(x,y,text,font,fill,stroke=12,gap=0.96):
    for ch in text:
        w=d.textlength(ch,font=font); d.text((x-w/2,y),ch,font=font,fill=fill,stroke_width=stroke,stroke_fill=(0,0,0)); y+=font.size*gap
vtext(1790,40,C["big"],ImageFont.truetype(SERIF,210),(250,250,250))
vtext(1500,120,C["red"],ImageFont.truetype(SERIF,180),RED,stroke=14,gap=0.98)
f_sub=ImageFont.truetype(SANS,66); sub=C["sub"]
sw=d.textlength(sub,font=f_sub); d.rectangle([W-sw-90,H-140,W,H-40],fill=(0,0,0)); d.text((W-sw-55,H-136),sub,font=f_sub,fill=(255,255,255))
f_tag=ImageFont.truetype(SANS,70); d.rectangle([40,40,230,140],fill=RED); d.text((62,46),"実話",font=f_tag,fill=(255,255,255))
f_l=ImageFont.truetype(SERIF,84); d.text((260,44),C["top"],font=f_l,fill=(255,255,255),stroke_width=8,stroke_fill=(0,0,0))
img.save("thumbnail.jpg",quality=92)
print("thumbnail.jpg ready")
