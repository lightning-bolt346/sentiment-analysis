window.Charts = {
  render(data) {
    const container = document.getElementById('charts-container');
    if (!container) return;
    container.innerHTML = `
      <div>
        <strong>Charts stub:</strong>
        <pre style="white-space: pre-wrap; background:#f1f5f9; padding:8px; border-radius:6px;">${escapeHtml(JSON.stringify(data, null, 2))}</pre>
      </div>
    `;
  }
};

function escapeHtml(unsafe) {
  return String(unsafe)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}