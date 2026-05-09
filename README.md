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

### server.lang (7,886 lignes)
![0%](https://progress-bar.xyz/0/?title=server.lang&width=400)

### wordlists.lang
![0%](https://progress-bar.xyz/0/?title=wordlists&width=400)

### Avatar Customization (22 fichiers)
![0%](https://progress-bar.xyz/0/?title=avatar&width=400)

> 💡 **Pour mettre à jour:** Change le nombre dans l'URL (ex: `progress-bar.xyz/25/` pour 25%)

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

## 👤 Auteur(s)

- **Elou4nn** - Créateur et mainteneur du dépots (code source) original

- que vous pouvez trouvé ici: https://github.com/elouannd/HytaleFR

- **Stormwindsky** - Créateur et mainteneur de se dépots (mon propre dépots)

## 📜 License

MIT License - Libre d'utilisation et modification.

---

*Basé sur Hytale Early Access (Janvier 2026)*
