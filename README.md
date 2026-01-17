# Hytale French Translation / Traduction Française Hytale

🇫🇷 **Pack de traduction française pour Hytale Early Access**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Elou4nn/HytaleFR)
[![Hytale](https://img.shields.io/badge/Hytale-Early%20Access-orange.svg)](https://hytale.com)

## 📥 Installation

1. **Télécharger** le dossier `FrenchPack`
2. **Copier** vers `~/Library/Application Support/Hytale/UserData/Mods/` (Mac)
   ou `%AppData%/Hytale/UserData/Mods/` (Windows)
3. **Lancer Hytale**
4. **Aller** dans Worlds → Clic droit sur un monde → Activer "FrenchTranslation"

## 📊 Progression

| Fichier | Lignes | Statut |
|---------|--------|--------|
| server.lang | 7,886 | ⏳ En cours |
| wordlists.lang | - | ⏳ En cours |
| Avatar Customization (22 files) | ~200 | ⏳ En cours |

## 🤝 Contribuer

Les contributions sont les bienvenues! 

1. Fork le repo
2. Traduis des sections dans les fichiers `.lang`
3. Crée une Pull Request

### Format des fichiers `.lang`
```properties
# Les clés restent en anglais, seules les valeurs sont traduites
key.name = Valeur traduite en français
# Préserve les variables: {id}, {count}, {username}
message.hello = Bonjour {username}!
```

## 📁 Structure

```
FrenchPack/
├── manifest.json
├── Server/Languages/fr-FR/
│   ├── server.lang      (Traductions principales)
│   └── wordlists.lang
└── Common/Languages/fr-FR/
    └── avatarCustomization/  (22 fichiers)
```

## 👤 Auteur

- **Elou4nn** - Créateur et mainteneur

## 📜 License

MIT License - Libre d'utilisation et modification.

---

*Basé sur Hytale Early Access (Janvier 2026)*
