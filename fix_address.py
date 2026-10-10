with open("index.html", "r") as f:
    html = f.read()

target = '<div class="contact-locations"><span><svg><use href="#pin"/></svg> Kartal, İstanbul</span><span><i class="online-dot"></i> Online</span></div>'

replacement = target + '<div style="margin-top:20px; font-size:14px; line-height:1.6; max-width:350px;"><strong>Adres:</strong> Esentepe Mah. Anadolu Caddesi AND Pastel A Blok 5/2 Kat:2 34870 Kartal/İstanbul</div>'

html = html.replace(target, replacement)

with open("index.html", "w") as f:
    f.write(html)
