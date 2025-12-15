# ISTRUZIONI DETTAGLIATE - Fix Sito Render

## 📋 STEP 1: Creare App Password di Gmail

**IMPORTANTE**: Gmail non accetta più la password normale per le app. Devi creare una "App Password".

### Procedura:

1. **Vai su Google Account**
   - Apri il browser e vai su: https://myaccount.google.com/
   - Accedi con il tuo account Gmail

2. **Attiva la Verifica in 2 passaggi** (se non già attiva)
   - Clicca su "Sicurezza" nel menu a sinistra
   - Scorri fino a "Accesso a Google"
   - Se "Verifica in 2 passaggi" è disattivata, clicca e attivala
   - Segui le istruzioni per configurarla (richiede il telefono)

3. **Crea App Password**
   - Sempre in "Sicurezza" → "Accesso a Google"
   - Scorri fino a "Password delle app" (appare solo se hai la verifica in 2 passaggi attiva)
   - Clicca su "Password delle app"
   - Seleziona "Mail" come app
   - Seleziona "Altro (nome personalizzato)" come dispositivo
   - Scrivi: "Sito Render" o un nome a tua scelta
   - Clicca "Genera"
   - **COPIA LA PASSWORD GENERATA** (16 caratteri senza spazi, tipo: `abcd efgh ijkl mnop`)
   - ⚠️ **IMPORTANTE**: Questa password la vedrai solo una volta! Salvala subito.

---

## 📋 STEP 2: Configurare Variabili d'Ambiente su Render

1. **Accedi a Render**
   - Vai su: https://dashboard.render.com/
   - Accedi al tuo account

2. **Vai al tuo servizio web**
   - Clicca sul servizio "andrea-lucchesi-website" (o il nome che hai dato)

3. **Apri la sezione Environment**
   - Nel menu a sinistra, clicca su "Environment"
   - Oppure scorri la pagina fino alla sezione "Environment Variables"

4. **Aggiungi le variabili d'ambiente** (una alla volta):

   **Variabile 1: MAIL_USER**
   - Clicca "Add Environment Variable"
   - **Key**: `MAIL_USER`
   - **Value**: La tua email Gmail completa (es. `a.lucchesi1999@gmail.com`)
   - Clicca "Save Changes"

   **Variabile 2: MAIL_PASS**
   - Clicca "Add Environment Variable"
   - **Key**: `MAIL_PASS`
   - **Value**: L'App Password che hai copiato nello STEP 1 (16 caratteri, senza spazi)
   - Clicca "Save Changes"

   **Variabile 3: MAIL_TO** (OPZIONALE)
   - Se vuoi ricevere i messaggi su un'email diversa da MAIL_USER
   - Clicca "Add Environment Variable"
   - **Key**: `MAIL_TO`
   - **Value**: L'email dove vuoi ricevere i messaggi (es. `a.lucchesi1999@gmail.com`)
   - Clicca "Save Changes"
   - ⚠️ Se non la aggiungi, i messaggi arriveranno all'email di MAIL_USER

5. **Verifica le variabili**
   - Dovresti vedere almeno:
     - `MAIL_USER` = la tua email
     - `MAIL_PASS` = l'app password (mostrata come `••••••••`)
   - Se vedi `MAIL_TO`, è opzionale

---

## 📋 STEP 3: Verificare che i File PDF siano Presenti

1. **Controlla la struttura del progetto**
   - I file PDF devono essere esattamente qui:
     ```
     /Users/andrea/Desktop/Sito/
       static/
         CV_Andrea_Lucchesi.pdf
         tesi_magistrale_greenwashing.pdf
     ```

2. **Verifica che i file esistano**
   - Apri Finder
   - Vai su Desktop → Sito → static
   - Dovresti vedere i due file PDF

3. **Se i file non ci sono o hanno nomi diversi**
   - Assicurati che i nomi siano ESATTAMENTE:
     - `CV_Andrea_Lucchesi.pdf` (con maiuscole/minuscole corrette)
     - `tesi_magistrale_greenwashing.pdf`
   - Se i nomi sono diversi, rinominali o aggiorna i link nel file `templates/index.html`

---

## 📋 STEP 4: Fare il Deploy/Re-deploy su Render

### Se è la prima volta:
1. Vai su Render Dashboard
2. Clicca "New +" → "Web Service"
3. Connetti il tuo repository Git (GitHub/GitLab)
4. Render dovrebbe rilevare automaticamente `render.yaml`
5. Clicca "Create Web Service"

### Se il servizio esiste già:
1. Vai al tuo servizio su Render
2. Clicca su "Manual Deploy" → "Deploy latest commit"
   - Oppure fai un push su Git e Render farà il deploy automatico

3. **Aspetta che il deploy finisca**
   - Vedi i log in tempo reale
   - Dovresti vedere: "Build successful" e poi "Your service is live"

---

## 📋 STEP 5: Testare il Sito

### Test 1: Verifica che il sito sia online
- Vai su: https://andrea-lucchesi-website.onrender.com
- Dovresti vedere la homepage

### Test 2: Testare i PDF
- Clicca su "Scarica CV"
  - Dovrebbe aprire/scaricare il PDF
- Clicca su "Scarica la tesi"
  - Dovrebbe aprire/scaricare il PDF
- ⚠️ Se non funziona, controlla i logs su Render (vedi STEP 6)

### Test 3: Testare il form contatti
1. Vai su "Contatti"
2. Compila il form:
   - Nome: Test
   - Email: una tua email (per ricevere la conferma)
   - Messaggio: Test messaggio
3. Clicca "Invia messaggio"
4. Dovresti vedere un messaggio di successo verde
5. Controlla la tua email (sia quella di MAIL_USER che quella che hai inserito nel form)
   - Dovresti ricevere 2 email:
     - Una notifica a te (MAIL_USER o MAIL_TO)
     - Una conferma all'email inserita nel form

---

## 📋 STEP 6: Controllare i Logs in caso di Problemi

1. **Su Render Dashboard**
   - Vai al tuo servizio
   - Clicca su "Logs" nel menu a sinistra
   - Vedi i log in tempo reale

2. **Cosa cercare nei log:**
   - Se vedi errori tipo "MAIL_USER e MAIL_PASS devono essere configurati" → le variabili d'ambiente non sono configurate
   - Se vedi "SMTPAuthenticationError" → l'App Password è sbagliata o non è stata creata correttamente
   - Se vedi "File not found" per i PDF → i file non sono nella cartella static/

3. **Per testare manualmente:**
   - Prova a inviare un messaggio dal form
   - Guarda i log in tempo reale per vedere l'errore esatto

---

## 🔧 RISOLUZIONE PROBLEMI COMUNI

### Problema: "Errore nell'invio email"
**Soluzioni:**
1. Verifica che MAIL_USER e MAIL_PASS siano configurate (STEP 2)
2. Verifica che l'App Password sia corretta (STEP 1)
3. Controlla i logs su Render per l'errore specifico

### Problema: PDF non si aprono
**Soluzioni:**
1. Verifica che i file esistano nella cartella `static/` (STEP 3)
2. Verifica che i nomi dei file siano esatti (case-sensitive)
3. Prova ad aprire direttamente:
   - https://andrea-lucchesi-website.onrender.com/static/CV_Andrea_Lucchesi.pdf
   - https://andrea-lucchesi-website.onrender.com/static/tesi_magistrale_greenwashing.pdf
4. Se funziona con l'URL diretto ma non con i bottoni, potrebbe essere un problema del browser (prova in incognito)

### Problema: Il sito non si aggiorna dopo le modifiche
**Soluzioni:**
1. Fai un nuovo deploy manuale (STEP 4)
2. Verifica che i file siano stati committati su Git
3. Aspetta qualche minuto (Render può impiegare tempo)

---

## ✅ CHECKLIST FINALE

Prima di considerare tutto risolto, verifica:

- [ ] App Password Gmail creata e copiata
- [ ] MAIL_USER configurata su Render
- [ ] MAIL_PASS configurata su Render (con App Password)
- [ ] File PDF presenti in `static/`
- [ ] Deploy completato con successo
- [ ] Sito accessibile online
- [ ] PDF si aprono correttamente
- [ ] Form contatti invia email (test con una tua email)

---

## 📞 Se Niente Funziona

1. Controlla i logs su Render (STEP 6)
2. Verifica che tutte le variabili d'ambiente siano configurate
3. Prova a fare un nuovo deploy
4. Se il problema persiste, condividi l'errore esatto dai logs

