# Configurazione per Render

## Variabili d'ambiente da configurare

Nel dashboard di Render, vai in **Environment** e aggiungi queste variabili:

### Obbligatorie:
- `MAIL_USER`: La tua email Gmail (es. `tua.email@gmail.com`)
- `MAIL_PASS`: **App Password** di Gmail (NON la password normale!)
  - Per crearla: Google Account → Sicurezza → Verifica in 2 passaggi → Password delle app
  - Genera una nuova password per "Mail" e incollala qui

### Opzionali:
- `MAIL_TO`: Email dove ricevere i messaggi (default: uguale a MAIL_USER)
- `MAIL_HOST`: Server SMTP (default: `smtp.gmail.com`)
- `MAIL_PORT`: Porta SMTP (default: `587`)
- `FLASK_SECRET_KEY`: Chiave segreta per Flask (Render la genera automaticamente se non specificata)

## Note importanti

1. **App Password Gmail**: Gmail richiede una "App Password" per l'autenticazione, non la password normale. Assicurati di averla generata correttamente.

2. **File statici**: I file PDF (CV e tesi) devono essere nella cartella `static/` e verranno serviti automaticamente da Flask.

3. **Logs**: In caso di problemi, controlla i logs su Render per vedere gli errori dettagliati.

4. **Port**: Render imposta automaticamente la variabile `PORT`, il codice la gestisce automaticamente.

