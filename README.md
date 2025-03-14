# Python Template

Ce projet me fournit une base pour démarrer un projet Python avec une configuration prête à l'emploi pour le tooling, la documentation, le linter, et l'intégration continue (CI).

## Fonctionnalités

- **Tooling** : configuration de base pour travailler avec Python (pre-commit).
- **Linter** : configuration de `Ruff` pour s'assurer que le code respecte les bonnes pratiques.
- **Formatage** : configuration de **Black** pour garantir un style de code uniforme et de **isort** pour trier les imports de manière cohérente.
- **CI/CD** : intégration avec GitHub Actions pour l'exécution des tests et le déploiement automatique.
- **Documentation** : structure de base pour générer de la documentation avec MKDocs.
- **Virtual env** : script pour créer un envrionnement virtuel et installer les dépendances.

## Envrionnement virtuel

```sh
python -m venv .venv && source .venv/bin/activate
```

## Run app

```sh
python -m MyQtApp
```
