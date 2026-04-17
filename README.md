# 🥩 ACCRO Sentiment Analyzer

**AI-native sentiment analysis for ACCRO HACHÉ 100% VÉGÉTAL FRAIS product reviews**

## 🚀 Overview

An intelligent, AI-native system that scrapes and analyzes customer reviews for ACCRO plant-based meat products across multiple e-commerce platforms. Built with cutting-edge LLM technology for adaptive, maintenance-free scraping.

### Key Features
- **🤖 AI-Native Scraping** : Uses LLMs to understand and adapt to website layouts automatically
- **📊 Multi-Platform** : Amazon, Carrefour, Auchan, ACCRO website, and review platforms
- **🎯 Sentiment Analysis** : Real-time classification and theme extraction
- **📈 Actionable Insights** : NPS calculation, trend analysis, alerting system
- **⚡ Real-time Dashboard** : Interactive Streamlit dashboard with live data

## 🏗️ Architecture

### AI-First Stack
```
┌─────────────────────────────────────────────────────┐
│                 ACCRO SENTIMENT ANALYZER            │
├─────────────────────────────────────────────────────┤
│  🤖 Crawl4AI    - LLM-native web scraping          │
│  🧠 OpenAI      - GPT-4o-mini for analysis         │
│  🌐 Playwright  - Browser automation with MCP      │
│  🔗 LangChain   - AI agent orchestration           │
│  🦆 DuckDB      - Real-time analytics              │
│  🚀 FastAPI     - REST API server                  │
│  📊 Streamlit   - Interactive dashboard            │
└─────────────────────────────────────────────────────┘
```

### Target Platforms
1. **Amazon France** - https://www.amazon.fr/Accro-Hache-vegetal-frais-2x100g/dp/B0DKX9M9HC
2. **Carrefour** - https://www.carrefour.fr/p/haches-100-vegetal-accro-3770018934242
3. **Auchan** - https://www.auchan.fr/accro-hache-100-vegetal-special-burger/pr-C1614687
4. **ACCRO Website** - https://accro.fr/produit/hache-vegetal-rayon-frais/
5. **Avis Garantis** - https://www.societe-des-avis-garantis.fr/accro/

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- Git
- OpenAI API key (for GPT-4o-mini)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/your-org/accro-sentiment.git
cd accro-sentiment
```

2. **Set up Python environment**
```bash
# Create virtual environment
python -m venv .venv

# Activate on Linux/Mac
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -e .[dev]
```

4. **Configure environment variables**
```bash
# Copy example file
cp .env.example .env

# Edit .env with your OpenAI API key
# OPENAI_API_KEY=sk-your-actual-key-here
```

5. **Install Playwright browsers**
```bash
playwright install --with-deps chromium firefox webkit
```

**Note**: On CI systems, browsers are installed automatically. For local development, the above command installs all required browsers.

6. **Run the walking skeleton**
```bash
python src/main.py
```

## 📁 Project Structure

```
accro_sentiment/
├── src/                    # Source code
│   ├── main.py            # Entry point
│   └── __init__.py
├── tests/                  # Test suite
│   ├── test_main.py       # Sprint 0 tests
│   └── __init__.py
├── docs/                   # Documentation
│   ├── BACKLOG.md         # Product backlog
│   ├── SPRINT_PLAN.md     # Current sprint plan
│   └── CHANGELOG.md       # Version history
├── config/                 # Configuration files
├── .github/workflows/     # CI/CD pipelines
├── pyproject.toml         # Python dependencies
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🧪 Testing

### Run all tests
```bash
pytest tests/ -v
```

### Run with coverage
```bash
pytest tests/ -v --cov=src --cov-report=html
```

### Code quality checks
```bash
# Format code
black src tests

# Sort imports
isort src tests

# Lint code
flake8 src

# Type checking
mypy src
```

## 🔄 CI/CD Pipeline

The project includes a comprehensive GitHub Actions pipeline:

### Automated Checks
- **Tests** : Runs pytest with coverage on Python 3.11 and 3.12
- **Linting** : flake8, black, isort checks
- **Type Checking** : mypy validation
- **Security** : Secret scanning with gitleaks
- **Build** : Package building and verification

### Pipeline Status
The pipeline runs automatically on:
- Push to `main` or `develop` branches
- Pull requests targeting `main`

### Local Pre-commit
To run CI checks locally before committing:
```bash
# Install pre-commit hooks
pre-commit install

# Run all checks
pre-commit run --all-files
```

## 🔧 Development

### Sprint 0 Status
✅ **DevOps First** - Walking skeleton complete
- Project structure initialized
- CI/CD pipeline configured
- Security setup (.env.example)
- Basic tests implemented

### Next Sprint (Sprint 1)
🎯 **Core AI Engine**
- Crawl4AI + OpenAI integration
- Pydantic models for reviews
- Amazon France scraper implementation
- Basic sentiment analysis

### Contributing
1. Check the `docs/SPRINT_PLAN.md` for current sprint tasks
2. Create a feature branch from `develop`
3. Write tests for new functionality
4. Ensure all tests pass and code quality checks succeed
5. Submit a pull request

## 📊 Metrics & Goals

### Business Goals
- **NPS Score** : > 50 target
- **Platform Coverage** : 100% of identified platforms
- **Alert Response Time** : < 24 hours for negative reviews
- **Data Freshness** : < 1 hour latency

### Technical Goals
- **Scraping Accuracy** : > 90%
- **Cost per Review** : < €0.0002
- **Processing Time** : < 5 seconds per page
- **System Uptime** : > 99.5%

## 🤝 Team Roles

### Product Owner (PSPO III)
- Product vision and backlog management
- Sprint planning and prioritization
- Stakeholder coordination

### Lead Developer
- Technical architecture and implementation
- LLM integration and optimization
- Code quality and performance

### Reviewer (QA Engineer)
- Quality assurance and testing
- Security validation
- Definition of Done enforcement

### UX Designer
- Dashboard design and user experience
- Data visualization
- User interface optimization

## 📚 Documentation

- **`docs/BACKLOG.md`** : Complete product backlog and technical decisions
- **`docs/SPRINT_PLAN.md`** : Current sprint plan with detailed tasks
- **`docs/CHANGELOG.md`** : Version history and lessons learned

## ⚠️ Security Notes

- Never commit `.env` files to version control
- Use `.env.example` as a template for local configuration
- OpenAI API keys should be kept secure
- Respect robots.txt and rate limits of target websites

## 📄 License

This project is proprietary and confidential.

## 📞 Support

For technical issues or questions, please refer to:
- Project documentation in `docs/`
- Sprint planning in `docs/SPRINT_PLAN.md`
- Team coordination through established channels

---

**Last Updated**: 2026-04-17  
**Version**: 0.1.0 (Sprint 0 - DevOps First)  
**Status**: 🟢 Active Development