import { ApiClient } from ./api.js;

const apiClient = new ApiClient();

export function initializeDashboard() {
  const controls = document.getElementById(controls);
  const dashboard = document.getElementById(dashboard);

  controls.innerHTML = `
    <div class="grid">
      <textarea id="input-text" placeholder="Enter text to analyze" rows="4" style="width:100%"></textarea>
      <div>
        <button id="analyze-btn" class="button">Analyze Sentiment</button>
      </div>
    </div>
  `;

  dashboard.innerHTML = `
    <div class="grid">
      <div class="card" id="sentiment-result">No analysis yet.</div>
      <div class="card" id="key-phrases">Key phrases will appear here.</div>
    </div>
  `;

  document.getElementById(analyze-btn).addEventListener(click, async () => {
    const text = /** @type {HTMLTextAreaElement} */(document.getElementById(input-text)).value.trim();
    if (!text) return;
    const result = await apiClient.analyzeText(text);
    renderResult(result);
  });
}

function renderResult(result) {
  const sentimentEl = document.getElementById(sentiment-result);
  const phrasesEl = document.getElementById(key-phrases);

  if (!result) {
    sentimentEl.textContent = No
