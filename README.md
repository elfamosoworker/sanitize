# sanitize.py 🧼

Un petit script Python pour **"sanitizer"** rapidement une URL en remplaçant les `.` par `[.]`, afin d’éviter qu’elle soit cliquable dans un mail, un rapport ou un chat. Très utile en cybersécurité pour partager des IOCs sans risque.

## 🔧 Fonctionnement

- Tu lances le script
- Il te demande une URL (ex: `http://example.com`)
- Il la transforme automatiquement (→ `http://example[.]com`)
- Et la copie dans le presse-papier 📋
- Il te reste plus qu'à la mettre comme IOC.
