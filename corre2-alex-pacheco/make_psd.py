# Builds a layered PSD per format: Fundo / FOTO AQUI (empty) / Frente.
import sys
from PIL import Image
from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer
for fmt in ('feed','story'):
    back=Image.open(f'output/corre2-{fmt}-camada-fundo.png').convert('RGBA')
    front=Image.open(f'output/corre2-{fmt}-camada-frente.png').convert('RGBA')
    psd=PSDImage.new('RGBA',back.size)
    psd.append(PixelLayer.frompil(back,psd,'Fundo (cores, CORRE, logo)'))
    psd.append(PixelLayer.frompil(Image.new('RGBA',back.size,(0,0,0,0)),psd,'FOTO AQUI - cole o recorte nesta camada'))
    psd.append(PixelLayer.frompil(front,psd,'Frente (titulo, km, data, papel, infos)'))
    psd.save(f'output/corre2-{fmt}.psd')
    chk=PSDImage.open(f'output/corre2-{fmt}.psd'); print(fmt,[l.name for l in chk], chk.size)
