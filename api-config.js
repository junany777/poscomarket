// Local development uses FastAPI on localhost. GitHub Pages uses the small
// OpenDART-only Vercel function; the browser never receives the API key.
const isGitHubPages = window.location.hostname.endsWith('github.io');
window.POSCO_API_BASE_URL = window.POSCO_API_BASE_URL || (isGitHubPages ? 'https://poscomarket.vercel.app' : 'http://localhost:8000');
