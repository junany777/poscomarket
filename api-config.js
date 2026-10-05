// Local development uses FastAPI on localhost. GitHub Pages must override this
// with a public HTTPS FastAPI URL; it must never contain the OpenDART API key.
const isGitHubPages = window.location.hostname.endsWith('github.io');
window.POSCO_API_BASE_URL = window.POSCO_API_BASE_URL || (isGitHubPages ? '' : 'http://localhost:8000');
