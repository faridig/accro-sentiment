# 🏗️ TECH DEBT & DIVERGENCES TECHNIQUES

## 📋 OBJECTIF
Ce fichier sert à tracker les divergences techniques entre l'implémentation et la spécification initiale, ainsi que la dette technique accumulée.

**Règles d'utilisation** :
1. Le **Lead-Dev** signale ici toute divergence technique majeure
2. Le **Product Owner** lit ce fichier avant chaque nouvelle planification
3. Les items sont **priorisés** et **datés**
4. Une divergence résolue est déplacée vers `CHANGELOG.md`

## 🚨 DIVERGENCES EN COURS

*Aucune divergence signalée pour le moment - Sprint 0 en cours*

## 💸 DETTE TECHNIQUE ACCUMULÉE

### Sprint 0 - DevOps First
**Date** : 2026-04-17  
**Statut** : 🟡 À évaluer

#### Dette identifiée :
1. **Playwright browser size** - Les browsers installés prennent ~500MB d'espace
   - **Impact** : Augmente le temps d'installation pour les nouveaux développeurs
   - **Priorité** : Low
   - **Solution proposée** : Script d'installation optionnel avec seulement Chromium

2. **CI/CD pipeline complexité** - Pipeline GitHub Actions avec 3 jobs
   - **Impact** : Temps de build plus long (~5-7 minutes)
   - **Priorité** : Low  
   - **Solution proposée** : Optimiser les étapes, cache des dépendances

3. **Dépendances nombreuses** - 10+ dépendances principales
   - **Impact** : Temps d'installation augmenté, surface d'attaque
   - **Priorité** : Medium
   - **Solution proposée** : Évaluer chaque dépendance pour nécessité réelle

## 🔄 DECISIONS TECHNIQUES REVISÉES

*Aucune décision révisée pour le moment*

## 📊 METRIQUES DE DETTE TECHNIQUE

### Couverture de tests
- **Cible** : > 80%
- **Actuel** : 0% (Sprint 0 - structure seulement)
- **Dette** : 80 points

### Complexité cyclomatique moyenne
- **Cible** : < 10
- **Actuel** : À mesurer
- **Dette** : À calculer

### Temps de build CI/CD
- **Cible** : < 3 minutes
- **Actuel** : ~5-7 minutes (estimé)
- **Dette** : 2-4 minutes

### Nombre de dépendances
- **Cible** : < 15 principales
- **Actuel** : 10 principales + 7 dev
- **Dette** : 2 points (dans la cible)

## 🎯 PLAN DE REMBOURSEMENT

### Sprint 1 (Priorité High)
1. **Mettre en place les tests** - Réduire la dette de 80 points
2. **Mesurer la complexité** - Établir une baseline

### Sprint 2 (Priorité Medium)
1. **Optimiser CI/CD** - Réduire le temps de build
2. **Auditer les dépendances** - Supprimer les non-essentielles

### Sprint 3 (Priorité Low)
1. **Optimiser Playwright** - Réduire l'espace disque
2. **Documenter les patterns** - Réduire la dette cognitive

## 📝 NOTES POUR LE PRODUCT OWNER

### Impact business de la dette technique
- **Temps de développement** : +10-15% pour résoudre la dette
- **Fiabilité système** : Risque modéré actuellement
- **Maintenance** : Coût acceptable pour Sprint 0
- **Évolutivité** : Bonne base architecturale

### Recommandations
1. **Sprint 1** : Accepter la dette actuelle, focus sur le core AI engine
2. **Sprint 2** : Allouer 20% du temps au remboursement de dette
3. **Sprint 3** : Réévaluer la dette et ajuster le plan

### Décisions à prendre
- **Budget dette technique** : Quel % du temps allouer par sprint ?
- **Seuil d'alerte** : Quand bloquer les nouvelles features pour dette ?
- **Métriques critiques** : Quelles métriques monitorer en priorité ?

## 👥 RESPONSABILITÉS

### Lead-Dev
- [ ] Signaler les divergences techniques
- [ ] Estimer l'impact de la dette
- [ ] Proposer des solutions

### Product Owner
- [ ] Lire ce fichier avant chaque planning
- [ ] Prioriser le remboursement de dette
- [ ] Valider les solutions proposées

### Reviewer
- [ ] Vérifier que la dette est correctement documentée
- [ ] S'assurer que les solutions respectent la qualité
- [ ] Monitorer les métriques de dette

---

**Dernière mise à jour** : 2026-04-17  
**Product Owner** : PSPO III  
**Lead-Dev** : À désigner  
**Reviewer** : À désigner