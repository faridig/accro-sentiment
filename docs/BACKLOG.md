# 📋 BACKLOG - ACCRO SENTIMENT ANALYZER

## ⚙️ CONFIGURATION TECHNIQUE

**Langage Principal** : Python 3.11+
**Framework** : AI-native scraping stack
**Type de Projet** : Pipeline d'analyse de sentiment multi-plateformes
**Base de Données** : DuckDB (analytics) + PostgreSQL (stockage)

### STACK TECHNIQUE AI-NATIVE
- **Core AI Scraping** : Crawl4AI + Playwright MCP
- **LLM Engine** : OpenAI GPT-4o-mini (via API)
- **Orchestration** : LangChain Agents + Prefect
- **Web Automation** : Playwright Python
- **Data Processing** : Pandas + Pydantic
- **API Server** : FastAPI
- **Dashboard** : Streamlit
- **Storage** : DuckDB (analytics) + PostgreSQL (structured)
- **Cache** : Redis (optional)
- **Monitoring** : Sentry + Prometheus

### PLATEFORMES CIBLES
1. Amazon France - https://www.amazon.fr/Accro-Hache-vegetal-frais-2x100g/dp/B0DKX9M9HC
2. Carrefour - https://www.carrefour.fr/p/haches-100-vegetal-accro-3770018934242
3. Auchan - https://www.auchan.fr/accro-hache-100-vegetal-special-burger/pr-C1614687
4. Site ACCRO - https://accro.fr/produit/hache-vegetal-rayon-frais/
5. Avis Garantis - https://www.societe-des-avis-garantis.fr/accro/

## 🎯 VISION DU PRODUIT

**Objectif** : Analyser en temps réel les avis clients du produit ACCRO HACHÉ 100% VÉGÉTAL FRAIS sur toutes les plateformes de vente pour :
- Identifier les tendances de satisfaction
- Détecter les points d'amélioration produits
- Alerter sur les avis négatifs critiques
- Générer des insights actionnables pour l'équipe produit

**Public Cible** :
- Équipe produit ACCRO
- Direction marketing
- Service qualité
- Développement produit

## ✅ DEFINITION OF DONE (DoD)

### Pour le REVIEWER
- [ ] **Tests** : Coverage > 80%, tous les tests passent
- [ ] **Code Quality** : Pylint score > 8.5/10, pas de code dupliqué
- [ ] **Documentation** : Docstrings complètes, README à jour
- [ ] **Sécurité** : Aucun secret en dur, .env.example présent
- [ ] **Performance** : Scraping < 5s par page, LLM calls optimisés
- [ ] **Error Handling** : Gestion complète des erreurs, retry logic
- [ ] **Logging** : Logs structurés avec niveaux appropriés
- [ ] **CI/CD** : Pipeline passe, déploiement automatisé

### Pour le LEAD-DEV
- [ ] **Architecture** : Respect des patterns AI-native
- [ ] **LLM Optimization** : Token usage optimisé, caching
- [ ] **Scalability** : Support 1000+ avis simultanés
- [ ] **Maintainability** : Code modulaire, configuration externalisée

### Pour l'UX (si frontend)
- [ ] **Responsive** : Mobile-first, toutes tailles d'écran
- [ ] **Accessibility** : WCAG 2.1 AA compliant
- [ ] **Performance** : LCP < 2.5s, FID < 100ms

## 🏛️ JOURNAL DES DÉCISIONS

### 2026-04-17 : Lancement du projet
- **Décision** : Adoption d'une architecture AI-native avec OpenAI GPT-4o-mini
- **Raison** : Réduction du code de scraping, adaptation automatique aux changements de layout
- **Alternatives considérées** : 
  - Scrapy traditionnel + BeautifulSoup (trop de maintenance)
  - LLM local (Ollama) + scraping classique (moins précis)
- **Impact** : Coût estimé €0.15/1000 avis, maintenance réduite de 70%

### 2026-04-17 : Stack technique
- **Décision** : Crawl4AI + Playwright MCP comme core scraping
- **Raison** : Framework conçu pour les LLMs, extraction structurée native
- **Référence** : Context7 docs /unclecode/crawl4ai et /microsoft/playwright-mcp

## 📊 PRODUCT BACKLOG ITEMS (PBI)

### PBI-001 : [EPIC] CORE AI SCRAPING ENGINE
**Description** : Moteur de scraping AI-native capable de s'adapter automatiquement à n'importe quelle plateforme ecommerce
**Valeur** : High | **Complexité** : L
**Dépendances** : Aucune

#### PBI-001-01 : Configuration Crawl4AI avec OpenAI
**User Story** : En tant que développeur, je veux configurer Crawl4AI avec OpenAI GPT-4o-mini, afin d'extraire des avis structurés
**Estimation** : M

#### PBI-001-02 : Playwright MCP Integration
**User Story** : En tant que système, je veux utiliser Playwright MCP pour la navigation et interaction, afin de bypasser les protections anti-bot
**Estimation** : M

#### PBI-001-03 : Pydantic Models pour avis
**User Story** : En tant que data engineer, je veux des modèles Pydantic pour les avis, afin d'avoir une structure de données cohérente
**Estimation** : S

### PBI-002 : [EPIC] PLATFORM ADAPTERS
**Description** : Adaptateurs spécifiques pour chaque plateforme cible
**Valeur** : High | **Complexité** : L
**Dépendances** : PBI-001

#### PBI-002-01 : Amazon France Scraper
**User Story** : En tant que marketeur, je veux scraper tous les avis Amazon France, afin d'analyser la satisfaction clients
**Estimation** : M

#### PBI-002-02 : Carrefour Scraper
**User Story** : En tant que marketeur, je veux scraper les avis Carrefour, afin de comprendre la perception en grande distribution
**Estimation** : M

#### PBI-002-03 : Auchan Scraper
**User Story** : En tant que marketeur, je veux scraper les avis Auchan, afin d'avoir une vue complète multi-retailers
**Estimation** : M

### PBI-003 : [EPIC] SENTIMENT ANALYSIS PIPELINE
**Description** : Pipeline d'analyse de sentiment avec LLM
**Valeur** : High | **Complexité** : L
**Dépendances** : PBI-001

#### PBI-003-01 : Classification de sentiment
**User Story** : En tant que responsable qualité, je veux classifier les avis en Positif/Négatif/Neutre, afin de calculer un NPS
**Estimation** : M

#### PBI-003-02 : Extraction de thèmes
**User Story** : En tant que chef produit, je veux identifier les thèmes récurrents (goût, texture, prix), afin de prioriser les améliorations
**Estimation** : M

#### PBI-003-03 : Génération d'insights
**User Story** : En tant que directeur, je veux des insights actionnables, afin de prendre des décisions éclairées
**Estimation** : S

### PBI-004 : [EPIC] DATA STORAGE & API
**Description** : Stockage des données et API d'accès
**Valeur** : Medium | **Complexité** : M
**Dépendances** : PBI-001, PBI-003

#### PBI-004-01 : Base de données DuckDB
**User Story** : En tant qu'analyste, je veux une base DuckDB, afin de faire des requêtes analytiques rapides
**Estimation** : S

#### PBI-004-02 : API FastAPI
**User Story** : En tant qu'intégrateur, je veux une API REST, afin de connecter d'autres systèmes
**Estimation** : M

#### PBI-004-03 : Cache Redis
**User Story** : En tant qu'administrateur, je veux un cache Redis, afin de réduire les appels LLM coûteux
**Estimation** : S

### PBI-005 : [EPIC] DASHBOARD & MONITORING
**Description** : Interface de visualisation et monitoring
**Valeur** : Medium | **Complexité** : M
**Dépendances** : PBI-004

#### PBI-005-01 : Dashboard Streamlit
**User Story** : En tant qu'utilisateur business, je veux un dashboard interactif, afin de visualiser les tendances
**Estimation** : M

#### PBI-005-02 : Alerting système
**User Story** : En tant que responsable, je veux des alertes sur avis négatifs, afin de réagir rapidement
**Estimation** : S

#### PBI-005-03 : Rapports automatiques
**User Story** : En tant que manager, je veux des rapports hebdomadaires, afin de suivre l'évolution
**Estimation** : S

### PBI-006 : [EPIC] DEPLOYMENT & DEVOPS
**Description** : Infrastructure et déploiement
**Valeur** : Low | **Complexité** : M
**Dépendances** : Tous les PBI précédents

#### PBI-006-01 : Dockerization
**User Story** : En tant que DevOps, je veux des conteneurs Docker, afin de déployer facilement
**Estimation** : M

#### PBI-006-02 : CI/CD Pipeline
**User Story** : En tant que développeur, je veux un pipeline CI/CD, afin d'automatiser les tests et déploiements
**Estimation** : M

#### PBI-006-03 : Monitoring Prometheus
**User Story** : En tant qu'ops, je veux du monitoring, afin de garantir la disponibilité
**Estimation** : S

## 🚀 ROADMAP

### PHASE 1 : MVP (Sprint 0-2)
- ✅ Sprint 0 : DevOps First - Walking Skeleton
- 🔄 Sprint 1 : Core AI Engine + Amazon scraper
- 📅 Sprint 2 : Sentiment analysis + DuckDB storage

### PHASE 2 : SCALING (Sprint 3-4)
- 📅 Sprint 3 : Multi-platform adapters (Carrefour, Auchan)
- 📅 Sprint 4 : API + Dashboard Streamlit

### PHASE 3 : PRODUCTION (Sprint 5-6)
- 📅 Sprint 5 : Alerting + Monitoring
- 📅 Sprint 6 : CI/CD + Deployment

## 📈 METRICS DE SUCCÈS

### Business Metrics
- **NPS Calculé** : > 50 cible
- **Temps de réponse aux avis négatifs** : < 24h
- **Couverture plateformes** : 100% des avis scrapés
- **Fraîcheur données** : < 1h de latence

### Technical Metrics
- **Précision classification** : > 90%
- **Coût par avis** : < €0.0002
- **Temps de scraping** : < 5s par page
- **Disponibilité système** : > 99.5%

## 🔧 CONFIGURATION ENVIRONNEMENT

### Variables d'environnement requises
```bash
OPENAI_API_KEY=sk-...           # OpenAI API key
DATABASE_URL=postgresql://...   # PostgreSQL connection
REDIS_URL=redis://...           # Redis cache (optional)
SENTRY_DSN=...                  # Error monitoring
```

### Dépendances Python principales
```txt
crawl4ai>=0.3.72
playwright>=1.40.0
openai>=1.0.0
langchain>=0.1.0
fastapi>=0.104.0
streamlit>=1.28.0
duckdb>=0.9.0
pydantic>=2.0.0
pandas>=2.0.0
```

## 👥 RÔLES ET RESPONSABILITÉS

### Product Owner (moi)
- Définition du backlog et priorisation
- Validation des user stories
- Coordination entre les agents

### Lead-Dev
- Implémentation technique
- Architecture et code quality
- Intégration LLM et scraping

### Reviewer
- Validation qualité code
- Tests et sécurité
- Respect Definition of Done

### UX Designer
- Design dashboard Streamlit
- Expérience utilisateur
- Visualisation données

## 📝 NOTES DE PLANIFICATION

### Risques identifiés
1. **Anti-bot protections** : Carrefour/Auchan peuvent bloquer le scraping
2. **Coûts OpenAI** : Nécessite monitoring strict des tokens
3. **Changements de layout** : Les sites ecommerce changent souvent
4. **Legalité scraping** : Respect robots.txt et rate limiting

### Mitigations prévues
1. **Playwright MCP** : Simule un vrai navigateur
2. **Cache intelligent** : Réduit les appels LLM redondants
3. **Architecture adaptable** : LLM comprend les changements
4. **Rate limiting** : Respect des politiques des sites

### Décisions techniques pendantes
- Choix entre Redis ou in-memory cache
- Niveau de parallélisme scraping
- Fréquence des mises à jour
- Stratégie de backup données

---

*Dernière mise à jour : 2026-04-17*
*Version : 1.0.0*
*Product Owner : PSPO III*