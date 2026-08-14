(() => {
  const PASSWORD = "Shira100";
  const KEY = "vs_auth";

  if (sessionStorage.getItem(KEY) === "1") return;

  const overlay = document.createElement("div");
  overlay.id = "pw-overlay";
  overlay.innerHTML = `
    <div class="pw-box">
      <div class="pw-icon">🔐</div>
      <h2>Dot DiBot · Video Summaries</h2>
      <p>This page is private. Enter the password to continue.</p>
      <input type="password" id="pw-input" placeholder="Password" autocomplete="current-password" />
      <button id="pw-btn">Unlock</button>
      <div id="pw-err"></div>
    </div>
  `;

  const style = document.createElement("style");
  style.textContent = `
    #pw-overlay {
      position: fixed; inset: 0; z-index: 9999;
      background: #0d1117;
      display: flex; align-items: center; justify-content: center;
    }
    .pw-box {
      background: #161b22; border: 1px solid #30363d;
      border-radius: 16px; padding: 40px 36px; max-width: 380px;
      width: 90%; text-align: center; font-family: 'Segoe UI', system-ui, sans-serif;
      color: #e6edf3;
    }
    .pw-icon { font-size: 48px; margin-bottom: 12px; }
    .pw-box h2 { font-size: 20px; font-weight: 700; margin-bottom: 8px; }
    .pw-box p { color: #8b949e; font-size: 14px; margin-bottom: 24px; }
    #pw-input {
      width: 100%; padding: 12px 16px; border-radius: 8px;
      border: 1px solid #30363d; background: #0d1117; color: #e6edf3;
      font-size: 16px; text-align: center; letter-spacing: 3px;
      margin-bottom: 12px; outline: none; transition: border-color 0.2s;
    }
    #pw-input:focus { border-color: #58a6ff; }
    #pw-btn {
      width: 100%; padding: 12px; border-radius: 8px;
      background: #238636; border: none; color: #fff;
      font-size: 15px; font-weight: 600; cursor: pointer;
      transition: background 0.2s;
    }
    #pw-btn:hover { background: #2ea043; }
    #pw-err {
      margin-top: 12px; color: #f85149;
      font-size: 13px; min-height: 18px;
    }
    .pw-shake {
      animation: shake 0.4s ease;
    }
    @keyframes shake {
      0%,100% { transform: translateX(0); }
      20%,60% { transform: translateX(-8px); }
      40%,80% { transform: translateX(8px); }
    }
  `;

  document.head.appendChild(style);
  document.body.appendChild(overlay);

  const input = document.getElementById("pw-input");
  const btn = document.getElementById("pw-btn");
  const err = document.getElementById("pw-err");

  const attempt = () => {
    if (input.value === PASSWORD) {
      sessionStorage.setItem(KEY, "1");
      overlay.style.transition = "opacity 0.3s";
      overlay.style.opacity = "0";
      setTimeout(() => overlay.remove(), 300);
    } else {
      err.textContent = "Wrong password. Try again.";
      input.value = "";
      overlay.querySelector(".pw-box").classList.remove("pw-shake");
      void overlay.querySelector(".pw-box").offsetWidth; // reflow
      overlay.querySelector(".pw-box").classList.add("pw-shake");
    }
  };

  btn.addEventListener("click", attempt);
  input.addEventListener("keydown", e => { if (e.key === "Enter") attempt(); });
  setTimeout(() => input.focus(), 100);
})();
