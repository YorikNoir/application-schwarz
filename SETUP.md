# Setup-Anleitung für GitHub Pages

## Schritt 1: GitHub Repository erstellen

1. Gehen Sie zu [github.com](https://github.com) und melden Sie sich an
2. Klicken Sie auf "+" → "New repository"
3. Repository Name: `application-schwarz`
4. Wählen Sie "Public"
5. Klicken Sie "Create repository"

## Schritt 2: Dateien hochladen

Es gibt zwei Möglichkeiten:

### Option A: Über die GitHub Webseite (einfacher)
1. Klicken Sie auf "uploading an existing file"
2. Ziehen Sie alle Dateien aus dem `application-schwarz` Ordner:
   - `index.html`
   - `Katharina_Schwarz_Lebenslauf.pdf`
   - `Kadda_Bewerbungsphoto.png`
   - `qr-code.png`
   - `README.md`
3. Klicken Sie "Commit changes"

### Option B: Mit Git (fortgeschritten)
```bash
cd "D:\Projects\stepACE-Step-1.5\Kadda Application\application-schwarz"
git init
git add .
git commit -m "Initial commit: CV landing page"
git branch -M main
git remote add origin https://github.com/DEIN-USERNAME/application-schwarz.git
git push -u origin main
```

## Schritt 3: GitHub Pages aktivieren

1. Gehen Sie zu Ihrem Repository auf GitHub
2. Klicken Sie auf "Settings" (Einstellungen)
3. Scrollen Sie zu "Pages" (linkes Menü)
4. Unter "Source" wählen Sie:
   - Branch: `main`
   - Folder: `/ (root)`
5. Klicken Sie "Save"
6. Nach 1-2 Minuten ist Ihre Seite live unter:
   `https://DEIN-USERNAME.github.io/application-schwarz/`

## Schritt 4: QR-Code mit echter URL generieren

Sobald Ihre Seite live ist:

```bash
cd "D:\Projects\stepACE-Step-1.5\Kadda Application\application-schwarz"
python generate_qr.py https://DEIN-USERNAME.github.io/application-schwarz/
```

Dann laden Sie das neue `qr-code.png` auf GitHub hoch (ersetzen Sie das alte).

## Schritt 5: Testen

1. Öffnen Sie `https://DEIN-USERNAME.github.io/application-schwarz/`
2. Testen Sie den Download-Button
3. Scannen Sie den QR-Code mit Ihrem Handy

## 📱 QR-Code drucken/teilen

Der QR-Code ist jetzt in `qr-code.png` gespeichert. Sie können ihn:
- Auf Visitenkarten drucken
- In E-Mail-Signaturen einfügen
- Als Sticker drucken
- In Bewerbungen einfügen

## 🔄 Updates

Um den Lebenslauf zu aktualisieren:
1. Generieren Sie eine neue PDF
2. Benennen Sie sie `Katharina_Schwarz_Lebenslauf.pdf`
3. Laden Sie sie auf GitHub hoch (ersetzt die alte Datei)
4. Die Änderungen sind sofort live!

## 📧 Support

Bei Fragen: schwarz.kadda@gmail.com
