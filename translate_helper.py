#!/usr/bin/env python3
"""
Hytale Translation Helper
Aide à la traduction des fichiers .lang pour Hytale
"""

import os
import json
import re
from pathlib import Path

# Configuration
LANG_DIR = Path("FrenchPack/Server/Languages/fr-FR")
PROGRESS_FILE = Path("translation_progress.json")
START_LINE = 3570  # Ignorer les premières lignes (commandes techniques)

def parse_lang_file(filepath: Path) -> dict:
    """Parse un fichier .lang et retourne un dict {key: value}"""
    entries = {}
    current_section = ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Skip lines before START_LINE
            if line_num < START_LINE:
                continue
                
            line = line.rstrip('\n')
            
            # Section headers (comments like # === section ===)
            if line.startswith('# ==='):
                current_section = line
                continue
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Parse key = value
            if '=' in line:
                key, _, value = line.partition('=')
                key = key.strip()
                value = value.strip()
                
                entries[key] = {
                    'value': value,
                    'section': current_section,
                    'line': line_num,
                    'translated': False
                }
    
    return entries

def load_progress() -> dict:
    """Charge la progression de traduction"""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'translated_keys': [], 'skipped_keys': []}

def save_progress(progress: dict):
    """Sauvegarde la progression"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

def export_for_translation(entries: dict, output_file: str = "to_translate.txt"):
    """Exporte les entrées dans un format facile à traduire"""
    with open(output_file, 'w', encoding='utf-8') as f:
        current_section = ""
        for key, data in entries.items():
            if data['section'] != current_section:
                current_section = data['section']
                f.write(f"\n{current_section}\n{'='*60}\n\n")
            
            f.write(f"KEY: {key}\n")
            f.write(f"EN:  {data['value']}\n")
            f.write(f"FR:  \n")  # Empty for translation
            f.write(f"\n")
    
    print(f"✅ Exporté vers {output_file}")
    print(f"   {len(entries)} entrées à traduire")

def import_translations(input_file: str, lang_file: Path):
    """Importe les traductions depuis un fichier texte"""
    translations = {}
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('KEY:'):
            key = line[4:].strip()
            i += 1
            
            # Skip EN line
            if i < len(lines) and lines[i].strip().startswith('EN:'):
                i += 1
            
            # Get FR line
            if i < len(lines) and lines[i].strip().startswith('FR:'):
                fr_value = lines[i].strip()[3:].strip()
                if fr_value:  # Only if translated
                    translations[key] = fr_value
        i += 1
    
    print(f"📥 Trouvé {len(translations)} traductions")
    
    # Apply translations to lang file
    apply_translations(translations, lang_file)

def apply_translations(translations: dict, lang_file: Path):
    """Applique les traductions au fichier .lang"""
    with open(lang_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = 0
    for i, line in enumerate(lines):
        if '=' in line and not line.strip().startswith('#'):
            key = line.split('=')[0].strip()
            if key in translations:
                # Preserve the key, replace the value
                lines[i] = f"{key} = {translations[key]}\n"
                modified += 1
    
    with open(lang_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✅ Appliqué {modified} traductions à {lang_file}")

def get_stats(entries: dict, progress: dict) -> dict:
    """Calcule les statistiques de traduction"""
    total = len(entries)
    translated = len(progress.get('translated_keys', []))
    skipped = len(progress.get('skipped_keys', []))
    remaining = total - translated - skipped
    
    return {
        'total': total,
        'translated': translated,
        'skipped': skipped,
        'remaining': remaining,
        'percent': round((translated / total) * 100, 1) if total > 0 else 0
    }

def interactive_translate(entries: dict, progress: dict, start_from: int = 0):
    """Mode de traduction interactif"""
    keys = list(entries.keys())
    translated_keys = set(progress.get('translated_keys', []))
    skipped_keys = set(progress.get('skipped_keys', []))
    
    print("\n🎮 Mode Traduction Interactif")
    print("Commandes: [Enter] = passer, [q] = quitter, [s] = sauvegarder\n")
    
    count = 0
    for i, key in enumerate(keys[start_from:], start_from):
        if key in translated_keys or key in skipped_keys:
            continue
        
        data = entries[key]
        print(f"\n[{i+1}/{len(keys)}] {data['section']}")
        print(f"Key: {key}")
        print(f"EN:  {data['value']}")
        
        try:
            fr_input = input("FR:  ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        
        if fr_input.lower() == 'q':
            break
        elif fr_input.lower() == 's':
            progress['translated_keys'] = list(translated_keys)
            progress['skipped_keys'] = list(skipped_keys)
            save_progress(progress)
            print("💾 Progression sauvegardée!")
            continue
        elif fr_input == '':
            skipped_keys.add(key)
        else:
            translated_keys.add(key)
            # Here you would update the actual file
            count += 1
    
    # Save at the end
    progress['translated_keys'] = list(translated_keys)
    progress['skipped_keys'] = list(skipped_keys)
    save_progress(progress)
    print(f"\n💾 Progression sauvegardée! ({count} nouvelles traductions)")

def main():
    print("=" * 60)
    print("   🎮 Hytale Translation Helper")
    print("   Traduction Française pour Hytale")
    print("=" * 60)
    
    # Parse the main lang file
    server_lang = LANG_DIR / "server.lang"
    if not server_lang.exists():
        print(f"❌ Fichier non trouvé: {server_lang}")
        return
    
    print(f"\n📖 Chargement de {server_lang}...")
    entries = parse_lang_file(server_lang)
    progress = load_progress()
    
    stats = get_stats(entries, progress)
    print(f"\n📊 Statistiques:")
    print(f"   Total: {stats['total']} entrées")
    print(f"   Traduites: {stats['translated']} ({stats['percent']}%)")
    print(f"   Passées: {stats['skipped']}")
    print(f"   Restantes: {stats['remaining']}")
    
    print("\n🔧 Actions disponibles:")
    print("   1. Exporter pour traduction (to_translate.txt)")
    print("   2. Importer les traductions")
    print("   3. Mode interactif")
    print("   4. Afficher les sections")
    print("   5. Quitter")
    
    try:
        choice = input("\nChoix: ").strip()
    except (EOFError, KeyboardInterrupt):
        return
    
    if choice == '1':
        export_for_translation(entries)
    elif choice == '2':
        import_file = input("Fichier à importer [to_translate.txt]: ").strip()
        if not import_file:
            import_file = "to_translate.txt"
        import_translations(import_file, server_lang)
    elif choice == '3':
        interactive_translate(entries, progress)
    elif choice == '4':
        sections = set(d['section'] for d in entries.values())
        print("\n📂 Sections:")
        for section in sorted(sections):
            count = sum(1 for d in entries.values() if d['section'] == section)
            print(f"   {section} ({count} entrées)")
    else:
        print("👋 Au revoir!")

if __name__ == "__main__":
    main()
