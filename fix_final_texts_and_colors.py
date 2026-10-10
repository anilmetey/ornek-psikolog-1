import re

# 1. FIX TEXTS
with open("index.html", "r") as f:
    html = f.read()

# Hero text
old_hero_title = '<h1 id="hero-title"><span class="hero-line"><span style="--i:1">Gelişimi</span></span><span class="hero-line"><span style="--i:2"><em>destekleyen</em></span></span><span class="hero-line"><span style="--i:3">güvenli adımlar.</span></span></h1>'
new_hero_title = '<h1 id="hero-title"><span class="hero-line"><span style="--i:1">Çocuk, Ergen ve</span></span><span class="hero-line"><span style="--i:2"><em>Yetişkin</em></span></span><span class="hero-line"><span style="--i:3">Psikoterapisi.</span></span></h1>'
html = html.replace(old_hero_title, new_hero_title)

old_hero_desc = '<p class="hero-description hero-enter" style="--i:4">Özellikle çocuk ve ergenlik döneminde karşılaşılan güçlüklerin çözümünde… İhtiyaçlara özel ve bilimsel temelli bir terapi süreci.</p>'
new_hero_desc = '<p class="hero-description hero-enter" style="--i:4">Bilimsel yaklaşımları temel alan, her yaş grubunun ihtiyacına özel olarak planlanmış yüz yüze ve online psikoterapi süreçleri.</p>'
html = html.replace(old_hero_desc, new_hero_desc)

# Breath section text
html = html.replace('GÜNÜN İÇİNDE KÜÇÜK BİR MOLA', 'NEFES EGZERSİZİ')
html = html.replace('Odaklanmak için<br><em>kısa bir mola.</em>', 'Kısa bir nefes<br><em>egzersizi.</em>')
html = html.replace('Bir an durun. Omuzlarınızı serbest bırakın.<br>Hazır olduğunuzda, dairenin ritmine eşlik edin.', 'Gevşeyin ve hazır hissettiğinizde dairenin ritmine eşlik edin.')
html = html.replace('Molayı başlat', 'Egzersizi başlat')

# Contact section text
html = html.replace('PROFESYONEL DESTEK', 'İLETİŞİM')
html = html.replace('Sağlıklı adımlar için<br><em>iletişime geçin.</em>', 'Randevu ve bilgi<br><em>talebi.</em>')
html = html.replace('Bir randevu talebi, bir soru ya da nereden başlayacağınızı bilmediğiniz bir an… İletişime geçerek başlayabilirsiniz.', 'Sürecin nasıl ilerlediği hakkında bilgi almak veya randevu oluşturmak için aşağıdaki formu kullanabilirsiniz.')

with open("index.html", "w") as f:
    f.write(html)

# 2. FIX COLORS
green_to_neutral = {
    "#102d258c": "#211b158c",
    "#243b2830": "#2b252030",
    "#294133": "#322a24",
    "#2b5949": "#3f352d",
    "#70796f": "#76716a",
    "#b4c4b7": "#d3cbc1",
    "#c0cec3": "#dbd3c9",
    "#c7d5ca": "#e0d9cf",
    "#cbd8ce": "#e5ddd3",
    "#d0dbd2": "#e8e1d7",
    "#d1dcd2": "#e8e1d7",
    "#d5ded3": "#ebe5dc",
    "#e9eee5": "#f5f0eb",
    "#eceee6": "#f7f2ed"
}

with open("style.css", "r") as f:
    css = f.read()
    
for old, new in green_to_neutral.items():
    css = css.replace(old, new)
    css = css.replace(old.upper(), new.upper())
    
with open("style.css", "w") as f:
    f.write(css)

with open("motion.js", "r") as f:
    js = f.read()
    
js = js.replace("#2d533d", "#2d2621")
js = js.replace("#b9d8bf", "#dcd1c6")

with open("motion.js", "w") as f:
    f.write(js)

