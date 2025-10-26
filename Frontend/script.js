/*
  Frontend/script.js

  Responsibilities:
    - Provide interactive behavior for the chat demo UI in the frontend folder.
    - Support two modes:
        * demo: no backend required, local canned responses and simulated typing
        * backend: calls POST /api/ai with { message } and expects { reply }
    - Persist conversation to localStorage for quick iteration
    - Provide export/clear controls and theme toggle

  Accessibility & UX:
    - Enter sends a message, Shift+Enter inserts a newline
    - Composer is labeled and keyboard-friendly
    - Messages area uses aria-live for polite updates

  Notes on wiring to a real backend:
    - Implement an API endpoint POST /api/ai that accepts JSON { message }
      and returns { reply: string }.
    - Securely call the OpenAI API from the server (never store API keys in client-side code).
*/

// ---------- Small helpers ----------
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from((r || document).querySelectorAll(s));
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

// ---------- Elements ----------
const messagesEl = $("#messages");
const composer = $("#composer");
const inputEl = $("#input");
const sendBtn = $("#sendBtn");
const modelSelect = $("#modelSelect");
const exportBtn = $("#exportBtn");
const clearBtn = $("#clearBtn");
const statusEl = $("#status");
const themeToggle = $("#themeToggle");
const compactMode = $("#compactMode");

// ---------- State & persistence ----------
const STORAGE_KEY = "codeforge_ai_frontend_v1";
let convo = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");

function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(convo));
}

// ---------- Render helpers ----------
function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function renderMessage(msg) {
  const el = document.createElement("div");
  el.className = "msg " + (msg.role === "user" ? "user" : "assistant");

  const meta = document.createElement("div");
  meta.className = "meta";
  meta.textContent = `${msg.role === "user" ? "You" : "Assistant"} • ${new Date(
    msg.ts
  ).toLocaleTimeString()}`;

  const body = document.createElement("div");
  body.className = "body";
  body.innerHTML = escapeHtml(msg.text).replace(/\n/g, "<br>");

  el.appendChild(meta);
  el.appendChild(body);
  return el;
}

function escapeHtml(str) {
  if (!str) return "";
  return str.replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[
        c
      ])
  );
}

function renderConversation() {
  messagesEl.innerHTML = "";
  convo.forEach((m) => messagesEl.appendChild(renderMessage(m)));
  scrollToBottom();
}

// ---------- Demo response generation (client-side) ----------
// This function returns a friendly, context-aware reply for demo purposes.
function demoGenerateReply(userText) {
  const t = userText.trim().toLowerCase();
  if (!t)
    return "I'm here — ask me anything about the project, e.g. 'How do I run this project?'";
  if (t.includes("run") || t.includes("start") || t.includes("launch")) {
    return "To run the project locally: 1) create a virtualenv, 2) pip install -r requirements.txt, 3) add your OPENAI_API_KEY to a .env file, and 4) run python main.py. Use the Frontend to prototype UI interactions without keys (demo mode).";
  }
  if (t.includes("openai") || t.includes("api key")) {
    return "Never place your OpenAI API key in client-side code. Instead, implement a server endpoint that holds the key and proxies requests. See Frontend/README.md for an example server snippet.";
  }
  if (t.includes("frontend") || t.includes("chat")) {
    return "This frontend demonstrates a local demo-mode chat widget that simulates AI responses and can be wired to a backend endpoint at POST /api/ai. It supports export, clear, theme toggle and compact mode.";
  }
  if (t.length < 30)
    return "Nice short question — here's some guidance: be specific about what file, language, or behavior you want help with (for example: 'Refactor function X to be async').";
  // Default: echo with suggestions
  return `Quick analysis of your message (demo):\n- length: ${t.length} chars\n- suggestions:\n  • Be more specific about the file or function you want changed\n  • Provide expected behavior and an example input/output\n\n(For a real response, switch the model dropdown to 'Use Backend' and implement POST /api/ai.)`;
}

// Simulate streaming typing effect for assistant replies
async function appendAssistantStreaming(text) {
  const placeholder = { role: "assistant", text: "", ts: Date.now() };
  convo.push(placeholder);
  persist();
  // create element and append; we'll update innerText progressively
  const el = renderMessage(placeholder);
  messagesEl.appendChild(el);
  scrollToBottom();

  // simulate chunked output
  const chunks = chunkString(text, 60);
  for (const chunk of chunks) {
    placeholder.text += chunk;
    // update the last message DOM body
    el.querySelector(".body").innerHTML = escapeHtml(placeholder.text).replace(
      /\n/g,
      "<br>"
    );
    scrollToBottom();
    await sleep(220 + Math.random() * 120);
  }
  // update stored convo entry
  const last = convo[convo.length - 1];
  last.text = placeholder.text;
  last.ts = placeholder.ts;
  persist();
}

function chunkString(str, size) {
  const out = [];
  for (let i = 0; i < str.length; i += size) out.push(str.slice(i, i + size));
  return out;
}

// ---------- Send flow: handles demo and backend modes ----------
async function sendMessage(text) {
  if (!text.trim()) return;
  const userMsg = { role: "user", text, ts: Date.now() };
  convo.push(userMsg);
  persist();
  messagesEl.appendChild(renderMessage(userMsg));
  scrollToBottom();

  const mode = modelSelect.value; // 'demo' or 'backend'
  if (mode === "demo") {
    statusEl.textContent = "Thinking (demo)…";
    await sleep(300 + Math.random() * 400);
    const reply = demoGenerateReply(text);
    await appendAssistantStreaming(reply);
    statusEl.textContent = "Demo mode — no API calls made.";
  } else {
    // Backend mode: call a server endpoint
    statusEl.textContent = "Calling backend /api/ai…";
    try {
      const res = await fetch("/api/ai", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      if (!res.ok) throw new Error(`Server error ${res.status}`);
      const json = await res.json();
      const reply =
        json && (json.reply || json.choices?.[0]?.text)
          ? json.reply || json.choices?.[0]?.text
          : "No reply from server.";
      await appendAssistantStreaming(reply);
      statusEl.textContent = "Response received.";
    } catch (err) {
      const errMsg = `Error calling backend: ${err.message}`;
      await appendAssistantStreaming(errMsg);
      statusEl.textContent = "Backend error — see console for details.";
      console.error(err);
    }
  }
}

// ---------- Controls ----------
composer.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = inputEl.value;
  inputEl.value = "";
  sendMessage(text);
});

// Keyboard: Enter sends, Shift+Enter newline
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    composer.dispatchEvent(new Event("submit", { cancelable: true }));
  }
});

exportBtn.addEventListener("click", () => {
  const dataStr = JSON.stringify(convo, null, 2);
  const blob = new Blob([dataStr], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `conversation-${new Date().toISOString()}.json`;
  a.click();
  URL.revokeObjectURL(url);
});

clearBtn.addEventListener("click", () => {
  if (!confirm("Clear the conversation? This cannot be undone.")) return;
  convo = [];
  persist();
  renderConversation();
});

modelSelect.addEventListener("change", () => {
  if (modelSelect.value === "demo")
    statusEl.textContent = "Demo mode active — no API calls made.";
  else
    statusEl.textContent = "Backend mode selected — POST /api/ai will be used.";
});

themeToggle &&
  themeToggle.addEventListener("change", (e) => {
    if (e.target.checked)
      document.documentElement.setAttribute("data-theme", "light");
    else document.documentElement.removeAttribute("data-theme");
  });

compactMode &&
  compactMode.addEventListener("change", (e) => {
    if (e.target.checked) document.body.classList.add("compact");
    else document.body.classList.remove("compact");
  });

// ---------- Initialize UI ----------
function init() {
  // If there is no conversation, seed a welcome message from assistant
  if (convo.length === 0) {
    convo.push({
      role: "assistant",
      text: "Hello! I'm CodeForge AI — try asking how to run the project or how to wire a backend. (Demo mode active.)",
      ts: Date.now(),
    });
    persist();
  }
  renderConversation();
  // bring focus to the input for quick typing
  inputEl.focus();
}

// Run initialization after DOMContent loaded
document.addEventListener("DOMContentLoaded", init);

/* End of script.js */
