document.addEventListener('DOMContentLoaded', () => {
  const controls = document.getElementById('controls');
  const dashboard = document.getElementById('dashboard');
  const charts = document.getElementById('charts');

  controls.innerHTML = `
    <div class="card grid">
      <textarea id="text-input" class="input" rows="4" placeholder="Type text to analyze..."></textarea>
      <div>
        <button id="analyze-btn" class="btn primary">Analyze Sentiment</button>
      </div>
    </div>
  `;

  dashboard.innerHTML = `
    <div class="grid">
      <div class="card" id="sentiment-score">Sentiment: -</div>
      <div class="card" id="key-phrases">Key Phrases: -</div>
    </div>
  `;

  charts.innerHTML = `
    <div class="card" id="charts-container">Charts will render here.</div>
  `;

  document.getElementById('analyze-btn').addEventListener('click', async () => {
    const text = /** @type {HTMLTextAreaElement} */(document.getElementById('text-input')).value.trim();
    if (!text) return;
    try {
      const result = await window.ApiClient.analyzeText(text);
      window.Dashboard.renderResults(result);
      window.Charts.render(result);
    } catch (err) {
      console.error(err);
      alert('Failed to analyze. Check backend is running.');
    }
  });
});