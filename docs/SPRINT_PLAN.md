# 🚀 SPRINT 0 PLAN - DEVOPS FIRST

**Sprint Goal** : Livrer un "Walking Skeleton" fonctionnel avec toute l'infrastructure DevOps
**Durée** : 3-5 jours
**Date de début** : 2026-04-17
**Date de fin** : 2026-04-21
**Velocity prévue** : 5 points

## 📋 TICKETS DU SPRINT 0

### [PBI-000] SPRINT 0 - DEVOPS FIRST
**Description** : Mise en place de l'infrastructure technique de base
**Priorité** : High | **Estimation** : XL (découpé en sous-tâches)

---

### [PBI-000-01] Configuration du projet Python
**Priorité** : High | **Estimation** : XS

**User Story** : En tant que développeur, je veux un environnement Python 3.11+ configuré avec les dépendances de base, afin de commencer le développement.

**Dépendances** : Aucune

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Structure de projet créée
  - **GIVEN** un dossier de projet vide
  - **WHEN** j'exécute la configuration initiale
  - **THEN** la structure suivante existe : `src/`, `tests/`, `docs/`, `config/`
- [ ] **Scenario 2** : Fichier de dépendances
  - **GIVEN** un environnement Python 3.11+
  - **WHEN** je crée le fichier `pyproject.toml`
  - **THEN** il contient les dépendances principales : crawl4ai, playwright, openai, pydantic
- [ ] **Scenario 3** : Environnement virtuel
  - **GIVEN** le fichier `pyproject.toml`
  - **WHEN** j'installe les dépendances
  - **THEN** toutes les dépendances s'installent sans erreur

---

### [PBI-000-02] Configuration Git et .gitignore
**Priorité** : High | **Estimation** : XS

**User Story** : En tant que développeur, je veux un dépôt Git configuré avec un .gitignore approprié, afin de versionner le code proprement.

**Dépendances** : PBI-000-01

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Initialisation Git
  - **GIVEN** un projet sans contrôle de version
  - **WHEN** j'initialise Git
  - **THEN** le dépôt est créé avec une branche main
- [ ] **Scenario 2** : Fichier .gitignore
  - **GIVEN** un projet Python
  - **WHEN** je crée le fichier .gitignore
  - **THEN** il exclut : __pycache__, .env, .venv, *.log, données sensibles
- [ ] **Scenario 3** : Premier commit
  - **GIVEN** la structure de projet de base
  - **WHEN** je fais le premier commit
  - **THEN** le message est "chore: initial project setup"

---

### [PBI-000-03] Configuration sécurité : .env.example
**Priorité** : High | **Estimation** : XS

**User Story** : En tant que développeur, je veux un template de variables d'environnement, afin de ne jamais coder de secrets en dur.

**Dépendances** : PBI-000-01

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Template de variables
  - **GIVEN** le besoin de configuration sécurisée
  - **WHEN** je crée le fichier `.env.example`
  - **THEN** il contient toutes les variables nécessaires avec des valeurs d'exemple
- [ ] **Scenario 2** : Variables OpenAI
  - **GIVEN** l'intégration OpenAI
  - **WHEN** je vérifie le template
  - **THEN** il contient `OPENAI_API_KEY=sk-example`
- [ ] **Scenario 3** : Documentation
  - **GIVEN** le fichier .env.example
  - **WHEN** un nouveau développeur l'utilise
  - **THEN** il comprend comment créer son propre .env

---

### [PBI-000-04] Walking Skeleton : Point d'entrée minimal
**Priorité** : High | **Estimation** : S

**User Story** : En tant que système, je veux un point d'entrée minimal qui s'exécute, afin de valider que l'infrastructure de base fonctionne.

**Dépendances** : PBI-000-01, PBI-000-02, PBI-000-03

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Fichier main.py
  - **GIVEN** un projet Python configuré
  - **WHEN** je crée `src/main.py`
  - **THEN** il contient un "Hello World" fonctionnel
- [ ] **Scenario 2** : Exécution réussie
  - **GIVEN** le fichier main.py
  - **WHEN** j'exécute `python src/main.py`
  - **THEN** le programme s'exécute sans erreur et affiche un message
- [ ] **Scenario 3** : Import des dépendances
  - **GIVEN** les dépendances installées
  - **WHEN** j'importe crawl4ai et openai dans main.py
  - **THEN** les imports fonctionnent sans erreur

---

### [PBI-000-05] Configuration Playwright
**Priorité** : Medium | **Estimation** : S

**User Story** : En tant que système, je veux Playwright installé et configuré, afin de pouvoir faire du scraping browser-based.

**Dépendances** : PBI-000-01

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Installation Playwright
  - **GIVEN** les dépendances Python
  - **WHEN** j'installe playwright
  - **THEN** la commande `playwright install` s'exécute avec succès
- [ ] **Scenario 2** : Browsers installés
  - **GIVEN** Playwright installé
  - **WHEN** je vérifie les browsers
  - **THEN** Chromium, Firefox et WebKit sont disponibles
- [ ] **Scenario 3** : Test de navigation
  - **GIVEN** un script Playwright de test
  - **WHEN** je l'exécute
  - **THEN** il navigue sur une page web sans erreur

---

### [PBI-000-06] Pipeline CI/CD basique
**Priorité** : Medium | **Estimation** : M

**User Story** : En tant que développeur, je veux un pipeline CI/CD minimal, afin d'automatiser les tests et la qualité.

**Dépendances** : PBI-000-01, PBI-000-02

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Fichier de workflow GitHub Actions
  - **GIVEN** un dépôt GitHub
  - **WHEN** je crée `.github/workflows/ci.yml`
  - **THEN** il définit un pipeline avec tests et linting
- [ ] **Scenario 2** : Tests automatiques
  - **GIVEN** le pipeline CI
  - **WHEN** je push du code
  - **THEN** les tests s'exécutent automatiquement
- [ ] **Scenario 3** : Quality checks
  - **GIVEN** le pipeline CI
  - **WHEN** il s'exécute
  - **THEN** il vérifie le linting et la qualité du code

---

### [PBI-000-07] Documentation initiale
**Priorité** : Medium | **Estimation** : XS

**User Story** : En tant qu'utilisateur, je veux une documentation de base, afin de comprendre comment installer et utiliser le projet.

**Dépendances** : Tous les PBI précédents

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : README.md
  - **GIVEN** un nouveau contributeur
  - **WHEN** il lit le README.md
  - **THEN** il comprend comment installer et exécuter le projet
- [ ] **Scenario 2** : Guide d'installation
  - **GIVEN** le README
  - **WHEN** je suis les étapes
  - **THEN** je peux installer et exécuter le walking skeleton
- [ ] **Scenario 3** : Structure documentée
  - **GIVEN** la documentation
  - **WHEN** je cherche une information
  - **THEN** je trouve la structure du projet et les responsabilités

---

### [PBI-000-08] Tests unitaires de base
**Priorité** : Low | **Estimation** : S

**User Story** : En tant que développeur, je veux une structure de tests, afin de garantir la qualité du code dès le début.

**Dépendances** : PBI-000-01, PBI-000-04

**Critères d'Acceptation (Gherkin)** :
- [ ] **Scenario 1** : Structure de tests
  - **GIVEN** le projet
  - **WHEN** je crée le dossier `tests/`
  - **THEN** il contient une structure organisée (unit/, integration/)
- [ ] **Scenario 2** : Premier test
  - **GIVEN** le point d'entrée main.py
  - **WHEN** j'écris un test unitaire
  - **THEN** il vérifie que main.py fonctionne correctement
- [ ] **Scenario 3** : Exécution des tests
  - **GIVEN** les tests écrits
  - **WHEN** j'exécute `pytest`
  - **THEN** tous les tests passent

---

## 🎯 DEFINITION OF DONE POUR LE SPRINT 0

### Critères de validation
- [ ] **Walking Skeleton** : `python src/main.py` s'exécute sans erreur
- [ ] **Git configuré** : Dépôt initialisé, .gitignore complet
- [ ] **Sécurité** : .env.example présent, aucun secret en dur
- [ ] **Dépendances** : pyproject.toml avec toutes les dépendances principales
- [ ] **Playwright** : Browsers installés, test de navigation fonctionnel
- [ ] **CI/CD** : Pipeline GitHub Actions configuré et fonctionnel
- [ ] **Documentation** : README.md complet et à jour
- [ ] **Tests** : Structure de tests créée, au moins un test passe

### Livrables attendus
1. ✅ Structure de projet complète
2. ✅ Environnement de développement fonctionnel
3. ✅ Pipeline CI/CD opérationnel
4. ✅ Documentation d'installation
5. ✅ "Hello World" AI-native (imports crawl4ai + openai fonctionnels)

### Métriques de succès
- **Temps d'installation** : < 10 minutes pour un nouveau développeur
- **Couverture tests** : > 0% (structure en place)
- **Build success** : 100% des pipelines passent
- **Documentation** : Toutes les étapes documentées

## 🔧 TÂCHES TECHNIQUES DÉTAILLÉES

### 1. Structure de fichiers à créer
```
accro_sentiment/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── config/
│   └── __init__.py
├── docs/
│   ├── BACKLOG.md
│   ├── SPRINT_PLAN.md
│   └── CHANGELOG.md
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── playwright.config.js
```

### 2. Contenu de pyproject.toml
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "accro-sentiment"
version = "0.1.0"
description = "AI-native sentiment analysis for ACCRO product reviews"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "crawl4ai>=0.3.72",
    "playwright>=1.40.0",
    "openai>=1.0.0",
    "langchain>=0.1.0",
    "fastapi>=0.104.0",
    "streamlit>=1.28.0",
    "duckdb>=0.9.0",
    "pydantic>=2.0.0",
    "pandas>=2.0.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "isort>=5.12.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
]

[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 88

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
```

### 3. Contenu de .env.example
```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Database Configuration (optional for Sprint 0)
# DATABASE_URL=postgresql://user:password@localhost:5432/accro_sentiment

# Cache Configuration (optional for Sprint 0)
# REDIS_URL=redis://localhost:6379/0

# Monitoring (optional for Sprint 0)
# SENTRY_DSN=https://your-sentry-dsn.ingest.sentry.io/xxxx

# Playwright Configuration
PLAYWRIGHT_BROWSERS_PATH=/home/user/.cache/ms-playwright

# Application Settings
LOG_LEVEL=INFO
ENVIRONMENT=development
```

### 4. Script main.py de démonstration
```python
#!/usr/bin/env python3
"""
ACCRO Sentiment Analyzer - Walking Skeleton
Sprint 0: DevOps First implementation
"""

import asyncio
import logging
from typing import Optional

# Third-party imports (will be used in future sprints)
# from crawl4ai import AsyncWebCrawler
# from openai import OpenAI
# from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    """Main entry point for the ACCRO Sentiment Analyzer."""
    logger.info("🚀 Starting ACCRO Sentiment Analyzer - Sprint 0")
    
    # Sprint 0: Simple demonstration
    print("\n" + "="*50)
    print("ACCRO SENTIMENT ANALYZER - WALKING SKELETON")
    print("="*50)
    
    # Simulate future functionality
    platforms = ["Amazon", "Carrefour", "Auchan", "ACCRO Website", "Avis Garantis"]
    
    print("\n📊 Target Platforms:")
    for i, platform in enumerate(platforms, 1):
        print(f"  {i}. {platform}")
    
    print("\n🤖 AI-Native Architecture Components:")
    components = [
        "Crawl4AI - LLM-native web scraping",
        "OpenAI GPT-4o-mini - Sentiment analysis",
        "Playwright MCP - Browser automation",
        "LangChain - AI agent orchestration",
        "DuckDB - Real-time analytics",
    ]
    
    for component in components:
        print(f"  • {component}")
    
    print("\n✅ Sprint 0 Goals:")
    print("  1. DevOps infrastructure ✅")
    print("  2. Python environment ✅")
    print("  3. Git configuration ✅")
    print("  4. Security setup (.env.example) ✅")
    print("  5. Walking skeleton ✅")
    
    print("\n🎯 Next Steps (Sprint 1):")
    print("  • Implement Crawl4AI + OpenAI integration")
    print("  • Create Pydantic models for reviews")
    print("  • Build Amazon France scraper")
    
    print("\n" + "="*50)
    logger.info("✅ Walking skeleton executed successfully!")
    logger.info("📁 Project structure ready for Sprint 1 development")


if __name__ == "__main__":
    asyncio.run(main())
```

## 📅 PLAN D'EXÉCUTION

### Jour 1 : Foundation
1. ✅ Créer structure de projet
2. ✅ Configurer pyproject.toml
3. ✅ Initialiser Git avec .gitignore
4. ✅ Créer .env.example

### Jour 2 : Core Setup
1. ✅ Installer dépendances
2. ✅ Configurer Playwright
3. ✅ Créer walking skeleton (main.py)
4. ✅ Tester l'exécution

### Jour 3 : Quality & Docs
1. ✅ Configurer CI/CD pipeline
2. ✅ Créer structure de tests
3. ✅ Écrire README.md
4. ✅ Documenter l'installation

### Jour 4 : Validation
1. ✅ Exécuter tous les tests
2. ✅ Vérifier le pipeline CI/CD
3. ✅ Valider Definition of Done
4. ✅ Préparer handoff pour Sprint 1

## 🚨 RISQUES ET MITIGATIONS

### Risque 1 : Problèmes d'installation Playwright
- **Mitigation** : Script d'installation avec retry logic
- **Fallback** : Mode headless optional

### Risque 2 : Compatibilité Python 3.11
- **Mitigation** : Tester sur multiple versions
- **Fallback** : Support Python 3.10+

### Risque 3 : Secrets exposés accidentellement
- **Mitigation** : .gitignore strict, pre-commit hooks
- **Fallback** : Scan automatique dans CI/CD

## 👥 RÉPARTITION DES TÂCHES

### Lead-Dev responsibilities:
- Implémenter la structure technique
- Configurer Playwright et dépendances
- Créer le walking skeleton
- Setup CI/CD pipeline

### Reviewer responsibilities:
- Vérifier la qualité du code
- Valider la sécurité (.env.example)
- Tester l'installation complète
- Vérifier Definition of Done

### Product Owner (moi):
- Valider les user stories
- Assurer l'alignement avec la vision
- Préparer le Sprint 1 backlog

---

**STATUS** : 🟡 EN COURS  
**PROGRESS** : 0/8 tickets complétés  
**NEXT STEP** : Implémentation technique par Lead-Dev

*Document créé le : 2026-04-17*  
*Product Owner : PSPO III*