import { initializeDashboard } from ./dashboard.js;
import { initializeCharts } from ./charts.js;

window.addEventListener(DOMContentLoaded, () => {
  initializeDashboard();
  initializeCharts();
});
