window.Dashboard = {
  renderResults(data) {
    const sentimentNode = document.getElementById('sentiment-score');
    const phrasesNode = document.getElementById('key-phrases');

    const score = typeof data?.sentiment?.score === 'number' ? data.sentiment.score.toFixed(3) : '-';
    const label = data?.sentiment?.label ?? '-';
    const phrases = Array.isArray(data?.keyPhrases) ? data.keyPhrases : [];

    sentimentNode.textContent = `Sentiment: ${label} (${score})`;
    phrasesNode.textContent = phrases.length ? `Key Phrases: ${phrases.join(', ')}` : 'Key Phrases: -';
  }
};