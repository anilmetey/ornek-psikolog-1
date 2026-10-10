import re

with open("index.html", "r") as f:
    html = f.read()

html = html.replace("Bakırköy <i>·</i> Kadıköy <i>·</i> Online", "Kartal <i>·</i> Online")
html = html.replace("İlk adımı birlikte atalım", "Randevu Alın")
html = html.replace("Beni tanıyın", "Hakkımda")

with open("index.html", "w") as f:
    f.write(html)
