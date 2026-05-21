// ───────────────────────── progress bar ─────────────────────────────
const progressBar = document.getElementById('progressBar');
const chapterLabel = document.getElementById('chapterLabel');

function updateProgress() {
  const h = document.documentElement;
  const scrolled = h.scrollTop;
  const max = h.scrollHeight - h.clientHeight;
  const pct = max > 0 ? (scrolled / max) * 100 : 0;
  progressBar.style.width = pct + '%';
}
window.addEventListener('scroll', updateProgress, { passive: true });
window.addEventListener('resize', updateProgress);
updateProgress();

// ───────────────────────── chapter marker ────────────────────────────
const scenes = document.querySelectorAll('.scene');

const chapterObserver = new IntersectionObserver(
  (entries) => {
    // Pick the entry whose center is closest to the viewport center.
    const visible = entries.filter((e) => e.isIntersecting);
    if (!visible.length) return;
    visible.sort(
      (a, b) =>
        Math.abs(a.boundingClientRect.top + a.boundingClientRect.height / 2 - window.innerHeight / 2) -
        Math.abs(b.boundingClientRect.top + b.boundingClientRect.height / 2 - window.innerHeight / 2)
    );
    const top = visible[0].target;
    const label = top.dataset.chapter;
    if (label && chapterLabel.textContent !== label) {
      chapterLabel.textContent = label;
    }
  },
  { threshold: [0.25, 0.5, 0.75], rootMargin: '0px 0px -10% 0px' }
);
scenes.forEach((s) => chapterObserver.observe(s));

// ───────────────────────── reveal on scroll ──────────────────────────
const reveals = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15, rootMargin: '0px 0px -8% 0px' }
);
reveals.forEach((r) => revealObserver.observe(r));

// ───────────────────────── stagger race grid ─────────────────────────
// Add small per-element delays so cards within the race grid cascade in
// instead of all snapping at once.
document.querySelectorAll('.race .reveal').forEach((el, i) => {
  el.style.transitionDelay = Math.min(i * 40, 240) + 'ms';
});

// ───────────────────────── count-up numbers ──────────────────────────
const countUpObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.count, 10);
      if (Number.isNaN(target)) return;
      let current = 0;
      const duration = 900;
      const start = performance.now();
      function step(now) {
        const t = Math.min(1, (now - start) / duration);
        // easeOutExpo
        const eased = 1 - Math.pow(2, -10 * t);
        current = Math.round(eased * target);
        el.textContent = current;
        if (t < 1) requestAnimationFrame(step);
        else el.textContent = target;
      }
      requestAnimationFrame(step);
      countUpObserver.unobserve(el);
    });
  },
  { threshold: 0.6 }
);
document.querySelectorAll('[data-count]').forEach((el) => countUpObserver.observe(el));

// ───────────────────────── rings: scroll-driven activation ──────────
// Each .ring-step on the page lives next to a sticky ripple diagram.
// We pick the step whose centre is closest to the viewport centre and:
//   (a) mark it .is-active (so its body un-fades + its illustration plays)
//   (b) set data-active-ring on .rings-layout so the matching band on
//       the diagram lights up and the caption under it updates.
const ringsLayout = document.getElementById('ringsLayout');
if (ringsLayout) {
  const ringSteps = ringsLayout.querySelectorAll('.ring-step');
  const captionNum = ringsLayout.querySelector('.rings-stage__active-num');
  const captionTitle = ringsLayout.querySelector('.rings-stage__active-title');

  const ringMeta = {
    1: { num: '①', title: 'navigation becomes nature' },
    2: { num: '②', title: 'the bigger picture becomes the start' },
    3: { num: '③', title: 'code, again — review inverts' },
    4: { num: '④', title: 'vibes — code as surface dissolves' },
  };

  let currentActive = null;

  function updateActiveRing() {
    // Find the ring-step whose centre is closest to the viewport centre.
    const vh = window.innerHeight;
    const target = vh / 2;
    let best = null;
    let bestDist = Infinity;
    ringSteps.forEach((step) => {
      const r = step.getBoundingClientRect();
      // Only consider steps that overlap the viewport at all.
      if (r.bottom < 0 || r.top > vh) return;
      const centre = r.top + r.height / 2;
      const dist = Math.abs(centre - target);
      if (dist < bestDist) {
        bestDist = dist;
        best = step;
      }
    });

    if (!best || best === currentActive) return;
    if (currentActive) currentActive.classList.remove('is-active');
    best.classList.add('is-active');
    currentActive = best;

    const ring = best.dataset.ring;
    ringsLayout.setAttribute('data-active-ring', ring);
    const meta = ringMeta[ring];
    if (meta) {
      if (captionNum) captionNum.textContent = meta.num;
      if (captionTitle) captionTitle.textContent = meta.title;
    }
  }

  window.addEventListener('scroll', updateActiveRing, { passive: true });
  window.addEventListener('resize', updateActiveRing);
  // initial pass once layout has settled
  requestAnimationFrame(updateActiveRing);
}

// ───────────────────────── back-to-top click ─────────────────────────
const upScroll = document.querySelector('.hero__scroll--up');
if (upScroll) {
  upScroll.style.cursor = 'pointer';
  upScroll.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ───────────────────────── theme toggle ──────────────────────────────
// The initial theme is applied by the inline script in <head> (avoids
// flash). Here we just handle clicks, persist the choice, and keep
// listening to system-preference changes for users who never click the
// toggle themselves.
const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const root = document.documentElement;
    const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    if (next === 'light') root.setAttribute('data-theme', 'light');
    else root.removeAttribute('data-theme');
    try {
      localStorage.setItem('trie-theme', next);
    } catch (_) {
      /* ignore */
    }
  });
}

// Follow the OS toggle if the user hasn't expressed a preference.
if (window.matchMedia) {
  const mq = window.matchMedia('(prefers-color-scheme: light)');
  mq.addEventListener('change', (e) => {
    let saved = null;
    try {
      saved = localStorage.getItem('trie-theme');
    } catch (_) {}
    if (saved) return; // user has chosen explicitly; leave them alone
    if (e.matches) document.documentElement.setAttribute('data-theme', 'light');
    else document.documentElement.removeAttribute('data-theme');
  });
}
