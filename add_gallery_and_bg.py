import re

# 1. ADD CSS
css_addition = """
/* OFFICE GALLERY */
.gallery-grid {
    display: flex;
    flex-direction: column;
    gap: 40px;
}
.gallery-heading {
    max-width: 500px;
}
.gallery-heading h2 {
    font-size: clamp(38px, 6vw, 65px);
    line-height: 1.1;
    margin-bottom: 20px;
}
.gallery-heading p {
    font-size: 13px;
    opacity: 0.8;
}
.gallery-images {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
}
.gallery-images img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
    transition: transform 0.3s var(--ease);
}
.gallery-images img:hover {
    transform: scale(1.02);
}

/* FAINT PORTRAIT BACKGROUND */
body::before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-image: url('assets/portrait-hero.webp');
  background-position: calc(50% + 300px) center;
  background-size: cover;
  background-repeat: no-repeat;
  opacity: 0.05;
  z-index: -1;
  pointer-events: none;
  mix-blend-mode: multiply;
}
@media (max-width: 740px) {
  body::before {
    background-position: center;
    background-size: 150%;
    opacity: 0.03;
  }
}
"""

with open("style.css", "a") as f:
    f.write(css_addition)

# 2. ADD HTML
html_gallery = """
    <section class="gallery section-space" id="ofis" aria-labelledby="gallery-title">
      <div class="container gallery-grid">
        <div class="gallery-heading" data-reveal>
          <span class="eyebrow">TERAPİ ORTAMI</span>
          <h2 id="gallery-title">Oyun Terapisi<br><em>Odamız</em></h2>
          <p>Çocukların kendilerini güvende hissederek, oyun aracılığıyla iç dünyalarını ifade edebilecekleri özel tasarlanmış terapi alanımız.</p>
        </div>
        <div class="gallery-images" data-reveal>
          <img src="assets/office_1.jpg" alt="Oyun terapisi odası genel görünüm" loading="lazy">
          <img src="assets/office_2.jpg" alt="Ahşap oyuncak bebek evi" loading="lazy">
          <img src="assets/office_3.jpg" alt="Oyun terapisi detaylar" loading="lazy">
          <img src="assets/office_4.jpg" alt="Terapi materyalleri" loading="lazy">
          <img src="assets/office_5.jpg" alt="Terapi odası köşesi" loading="lazy">
        </div>
      </div>
    </section>
"""

with open("index.html", "r") as f:
    c = f.read()

# Insert the gallery section just before the FAQ section
c = c.replace('<section class="faq section-space"', html_gallery + '\n    <section class="faq section-space"')

with open("index.html", "w") as f:
    f.write(c)

