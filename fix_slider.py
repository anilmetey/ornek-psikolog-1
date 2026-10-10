import re

with open("index.html", "r") as f:
    html = f.read()

# Remove the old gallery
old_gallery_pattern = re.compile(r'<section class="gallery section-space".*?</section>', re.DOTALL)
html = re.sub(old_gallery_pattern, '', html)

new_gallery = """
    <section class="gallery section-space" id="ofis" aria-labelledby="gallery-title">
      <div class="container">
        <div class="gallery-heading" data-reveal style="margin-bottom: 40px; text-align: center; max-width: 600px; margin-left: auto; margin-right: auto;">
          <span class="eyebrow">TERAPİ ORTAMI</span>
          <h2 id="gallery-title">Ofisimiz</h2>
          <p>Çocukların kendilerini güvende hissederek oyun aracılığıyla iç dünyalarını ifade edebilecekleri ve yetişkinlerin rahatça kendilerine odaklanabilecekleri özenle tasarlanmış terapi alanlarımız.</p>
        </div>
        
        <div class="carousel-wrapper" data-reveal>
          <button class="carousel-btn prev" id="c-prev" aria-label="Önceki Fotoğraf">
            <svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          
          <div class="gallery-carousel" id="gallery-carousel">
            <img src="assets/office_6.jpg" alt="Yetişkin terapi alanı" loading="lazy">
            <img src="assets/office_1.jpg" alt="Oyun terapisi odası genel görünüm" loading="lazy">
            <img src="assets/office_3.jpg" alt="Oyuncak bebek evi" loading="lazy">
            <img src="assets/office_9.jpg" alt="Terapi materyalleri ve oyuncak mutfak" loading="lazy">
            <img src="assets/office_7.jpg" alt="Terapi odası hayvan ve figürler" loading="lazy">
          </div>
          
          <button class="carousel-btn next" id="c-next" aria-label="Sonraki Fotoğraf">
            <svg viewBox="0 0 24 24"><path d="M9 18l6-6-6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
      
      <script>
        document.addEventListener("DOMContentLoaded", () => {
          const carousel = document.getElementById("gallery-carousel");
          const btnPrev = document.getElementById("c-prev");
          const btnNext = document.getElementById("c-next");
          
          if(carousel && btnPrev && btnNext) {
            btnPrev.addEventListener("click", () => {
              carousel.scrollBy({ left: -carousel.clientWidth * 0.8, behavior: 'smooth' });
            });
            btnNext.addEventListener("click", () => {
              carousel.scrollBy({ left: carousel.clientWidth * 0.8, behavior: 'smooth' });
            });
          }
        });
      </script>
    </section>
"""

# Insert new gallery before FAQ
html = html.replace('<section class="faq section-space"', new_gallery + '\n    <section class="faq section-space"')

with open("index.html", "w") as f:
    f.write(html)

with open("style.css", "r") as f:
    css = f.read()

# Remove old gallery css (we added it at the end previously)
css = re.sub(r'/\* OFFICE GALLERY \*/.*', '', css, flags=re.DOTALL)

new_css = """
/* OFFICE GALLERY CAROUSEL */
.carousel-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
}
.gallery-carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  gap: 20px;
  padding: 10px 0 30px;
  -ms-overflow-style: none;
  scrollbar-width: none;
  width: 100%;
}
.gallery-carousel::-webkit-scrollbar {
  display: none;
}
.gallery-carousel img {
  scroll-snap-align: center;
  flex: 0 0 85%;
  max-width: 800px;
  height: 400px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}
@media(min-width: 768px) {
  .gallery-carousel img {
    flex: 0 0 65%;
    height: 500px;
  }
}
.carousel-btn {
  position: absolute;
  top: calc(50% - 15px);
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  background: var(--white);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}
.carousel-btn:hover {
  background: var(--paper);
  transform: translateY(-50%) scale(1.05);
}
.carousel-btn svg {
  width: 24px;
  height: 24px;
}
.carousel-btn.prev {
  left: -25px;
}
.carousel-btn.next {
  right: -25px;
}
@media(max-width: 768px) {
  .carousel-btn {
    display: none; /* Hide buttons on mobile, rely on native swipe */
  }
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
    f.write(new_css)

