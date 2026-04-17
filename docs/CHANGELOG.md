# 📜 CHANGELOG - ACCRO SENTIMENT ANALYZER

## 📊 VERSION 0.1.0 - SPRINT 0 (2026-04-17)

### Added
- **Project Initialization** : Création du projet avec architecture AI-native
- **Documentation Structure** : 
  - `BACKLOG.md` : Vision produit et backlog complet
  - `SPRINT_PLAN.md` : Plan détaillé du Sprint 0 (DevOps First)
  - `CHANGELOG.md` : Historique des changements
- **Technical Stack Definition** : Stack AI-native avec OpenAI GPT-4o-mini, Crawl4AI, Playwright MCP
- **Sprint 0 Planning** : 8 tickets DevOps avec Definition of Done

### Technical Decisions
- **Architecture Choice** : AI-native scraping avec LLM integration
- **LLM Provider** : OpenAI GPT-4o-mini pour équilibre coût/performance
- **Core Framework** : Crawl4AI + Playwright MCP pour scraping intelligent
- **Data Storage** : DuckDB (analytics) + PostgreSQL (structured)
- **Dashboard** : Streamlit pour visualisation interactive

### Platform Targets Identified
1. Amazon France - https://www.amazon.fr/Accro-Hache-vegetal-frais-2x100g/dp/B0DKX9M9HC
2. Carrefour - https://www.carrefour.fr/p/haches-100-vegetal-accro-3770018934242
3. Auchan - https://www.auchan.fr/accro-hache-100-vegetal-special-burger/pr-C1614687
4. Site ACCRO - https://accro.fr/produit/hache-vegetal-rayon-frais/
5. Avis Garantis - https://www.societe-des-avis-garantis.fr/accro/

### Next Steps (Sprint 1)
- Implémentation du core AI engine avec Crawl4AI + OpenAI
- Création des modèles Pydantic pour les avis
- Développement du scraper Amazon France
- Mise en place de l'analyse de sentiment basique

---

## 🏛️ JOURNAL DES DÉCISIONS TECHNIQUES

### 2026-04-17 : Architecture AI-native
**Décision** : Adoption de Crawl4AI + Playwright MCP + OpenAI GPT-4o-mini
**Raison** : 
- Réduction de 70% du code de scraping traditionnel
- Adaptation automatique aux changements de layout des sites
- Extraction structurée native avec Pydantic models
- Coût optimisé (€0.15/1000 avis)
**Alternatives considérées** : Scrapy traditionnel, BeautifulSoup + custom parsing
**Impact** : Maintenance réduite, intelligence augmentée, coût contrôlé

### 2026-04-17 : Stack technique complète
**Décision** : Python 3.11+ avec stack moderne
**Composants** :
- Crawl4AI 0.3.72+ : LLM-native web scraping
- Playwright 1.40.0+ : Browser automation avec MCP
- OpenAI 1.0.0+ : GPT-4o-mini pour analyse
- LangChain 0.1.0+ : Agent orchestration
- FastAPI 0.104.0+ : API server
- Streamlit 1.28.0+ : Dashboard
- DuckDB 0.9.0+ : Real-time analytics
- Pydantic 2.0.0+ : Data validation
**Raison** : Écosystème mature, bonne documentation, communauté active

---

## 📈 METRICS DE PROJET

### Business Metrics (Targets)
- **NPS Calculé** : > 50 (à mesurer après Sprint 2)
- **Platform Coverage** : 5/5 plateformes (Sprint 3)
- **Data Freshness** : < 1 heure (Sprint 4)
- **Alert Response Time** : < 24h (Sprint 5)

### Technical Metrics (Baseline)
- **Scraping Accuracy** : > 90% (à valider)
- **Cost per Review** : < €0.0002 (basé sur GPT-4o-mini pricing)
- **Processing Time** : < 5s par page (objectif)
- **System Uptime** : > 99.5% (Sprint 6)

---

## 🎓 LEÇONS APPRISES

*Aucune leçon apprise pour le moment - Sprint 0 en cours*

---

## 🔄 ÉVOLUTION DU BACKLOG

### Sprint 0 (Current) - DevOps First
- ✅ Documentation structure
- ✅ Technical stack definition
- 🔄 Infrastructure setup
- 🔄 Walking skeleton

### Sprint 1 (Planned) - Core AI Engine
- 📅 Crawl4AI + OpenAI integration
- 📅 Pydantic models for reviews
- 📅 Amazon France scraper
- 📅 Basic sentiment analysis

### Sprint 2 (Planned) - Multi-platform
- 📅 Carrefour scraper adapter
- 📅 Auchan scraper adapter
- 📅 DuckDB analytics setup
- 📅 Enhanced sentiment analysis

### Sprint 3 (Planned) - API & Dashboard
- 📅 FastAPI server
- 📅 Streamlit dashboard
- 📅 Data visualization
- 📅 Alerting system

---

## 🚨 RISK REGISTER

### Identified Risks
1. **Anti-bot protections** (High) - Carrefour/Auchan peuvent bloquer le scraping
   - **Mitigation** : Playwright MCP simule un vrai navigateur
   - **Status** : À surveiller

2. **OpenAI costs** (Medium) - Usage non contrôlé peut générer des coûts élevés
   - **Mitigation** : Cache intelligent, monitoring des tokens
   - **Status** : Contrôle à implémenter

3. **Layout changes** (Medium) - Sites ecommerce changent souvent
   - **Mitigation** : Architecture AI-native s'adapte automatiquement
   - **Status** : Avantage de l'approche choisie

4. **Legal compliance** (Low) - Respect robots.txt et terms of service
   - **Mitigation** : Rate limiting, respect des politiques
   - **Status** : À documenter

---

## 👥 CONTRIBUTIONS

### 2026-04-17 : Product Owner (PSPO III)
- Création de la vision produit
- Définition de la stack technique AI-native
- Planification du Sprint 0 (DevOps First)
- Documentation complète du backlog

### À venir : Lead-Dev
- Implémentation technique du Sprint 0
- Configuration de l'infrastructure
- Création du walking skeleton

### À venir : Reviewer
- Validation de la qualité du code
- Vérification de la sécurité
- Tests et assurance qualité

---

*Dernière mise à jour : 2026-04-17*  
*Product Owner : PSPO III*  
*Version : 0.1.0 (Sprint 0 Planning)*