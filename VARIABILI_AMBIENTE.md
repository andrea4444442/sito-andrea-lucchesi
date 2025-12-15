# Variabili d'Ambiente Configurate su Render

## ✅ Variabili già configurate:

```
FLASK_SECRET_KEY = chiave-segreta-super-lunga-e-casuale-12345
MAIL_HOST = smtp.gmail.com
MAIL_PASS = rygiasejorptypxd
MAIL_PORT = 587
MAIL_TO = a.lucchesi1999@gmail.com
MAIL_USER = a.lucchesi1999@gmail.com
```

## 🔒 Suggerimento per FLASK_SECRET_KEY

La chiave attuale funziona, ma per maggiore sicurezza potresti usare una chiave più casuale. Ecco una generata automaticamente:

```
FLASK_SECRET_KEY = sfWC1fnBxVLg9LF9262nK8S6ZKlo4Dy0l0PI0F06WaU
```

**Come aggiornarla su Render:**
1. Vai su Render Dashboard → Il tuo servizio → Environment
2. Trova `FLASK_SECRET_KEY`
3. Clicca "Edit" e sostituisci con la nuova chiave
4. Salva e riavvia il servizio

⚠️ **Nota**: Non è obbligatorio cambiarla, quella attuale funziona. È solo una raccomandazione per maggiore sicurezza.

## ✅ Verifica che tutto sia configurato

Tutte le variabili necessarie sono presenti:
- ✅ FLASK_SECRET_KEY (configurata)
- ✅ MAIL_HOST (smtp.gmail.com)
- ✅ MAIL_PASS (App Password Gmail)
- ✅ MAIL_PORT (587)
- ✅ MAIL_TO (email destinatario)
- ✅ MAIL_USER (email mittente)

## 🧪 Test

Dopo aver configurato tutto:
1. Vai su https://andrea-lucchesi-website.onrender.com
2. Prova a inviare un messaggio dal form contatti
3. Controlla i logs su Render se ci sono errori
4. Verifica che i PDF si aprano correttamente

