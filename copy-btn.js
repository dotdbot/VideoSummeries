(() => {
  // Button
  const btn = document.createElement('button');
  btn.id = 'copy-btn';
  btn.innerHTML = '📋 Copy post';

  // Styles
  const style = document.createElement('style');
  style.textContent = `
    #copy-btn {
      position: fixed;
      bottom: 28px;
      right: 28px;
      background: #238636;
      color: #fff;
      border: none;
      border-radius: 10px;
      padding: 11px 20px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      z-index: 8000;
      box-shadow: 0 4px 16px rgba(0,0,0,0.5);
      transition: background 0.2s, transform 0.1s, opacity 0.2s;
      font-family: 'Segoe UI', system-ui, sans-serif;
      letter-spacing: 0.2px;
    }
    #copy-btn:hover  { background: #2ea043; transform: translateY(-1px); }
    #copy-btn:active { transform: scale(0.97); }
    #copy-btn.copied { background: #1f6feb; }
    #copy-btn.error  { background: #b62324; }

    @media (max-width: 600px) {
      #copy-btn { bottom: 16px; right: 16px; padding: 10px 16px; font-size: 13px; }
    }
  `;

  document.head.appendChild(style);
  document.body.appendChild(btn);

  btn.addEventListener('click', () => {
    const container = document.querySelector('.container');
    if (!container) return;

    // Deep clone so we can mutate without touching the DOM
    const clone = container.cloneNode(true);

    // Remove navigation elements (back link, footer links, copy button itself)
    ['.back', 'footer', '#copy-btn'].forEach(sel => {
      clone.querySelectorAll(sel).forEach(el => el.remove());
    });

    // Replace every <a> with just its visible text (strip URLs)
    clone.querySelectorAll('a').forEach(a => {
      a.replaceWith(document.createTextNode(a.textContent));
    });

    // Remove <script> tags
    clone.querySelectorAll('script, style').forEach(el => el.remove());

    // Grab plain text — innerText respects visibility / whitespace better than textContent
    const raw = (clone.innerText || clone.textContent || '').trim();

    // Collapse 3+ consecutive blank lines into 2
    const text = raw.replace(/\n{3,}/g, '\n\n');

    navigator.clipboard.writeText(text).then(() => {
      btn.innerHTML = '✅ Copied!';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.innerHTML = '📋 Copy post';
        btn.classList.remove('copied');
      }, 2500);
    }).catch(() => {
      btn.innerHTML = '❌ Failed';
      btn.classList.add('error');
      setTimeout(() => {
        btn.innerHTML = '📋 Copy post';
        btn.classList.remove('error');
      }, 2500);
    });
  });
})();
