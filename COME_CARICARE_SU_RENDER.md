# 📤 Come Caricare i File PDF su Render

## ✅ Ho già fatto:
- ✅ Inizializzato Git
- ✅ Aggiunto tutti i file (inclusi i PDF) a Git
- ✅ Fatto il commit

## 📋 PROSSIMI PASSI:

### OPZIONE 1: Se Render è già connesso a GitHub/GitLab

1. **Verifica su Render Dashboard**
   - Vai su Render → Il tuo servizio
   - Guarda la sezione "Git Repository"
   - Dovresti vedere il link al repository (es. `github.com/tuousername/repo`)

2. **Connetti il repository locale a quello remoto**
   - Apri Terminal
   - Vai nella cartella del progetto:
     ```bash
     cd ~/Desktop/Sito
     ```

3. **Aggiungi il remote (sostituisci con il tuo URL)**
   ```bash
   git remote add origin https://github.com/TUO_USERNAME/TUO_REPO.git
   ```
   Oppure se usi GitLab:
   ```bash
   git remote add origin https://gitlab.com/TUO_USERNAME/TUO_REPO.git
   ```

4. **Fai push**
   ```bash
   git branch -M main
   git push -u origin main
   ```

5. **Render farà il deploy automatico**
   - Render rileverà il nuovo commit
   - Farà il deploy automaticamente
   - I PDF saranno disponibili!

---

### OPZIONE 2: Se NON hai ancora un repository su GitHub/GitLab

1. **Crea un nuovo repository**
   - Vai su https://github.com (o GitLab)
   - Clicca "New repository"
   - Nome: `sito-andrea-lucchesi` (o come preferisci)
   - NON inizializzare con README (abbiamo già i file)
   - Clicca "Create repository"

2. **Connetti il repository locale**
   - GitHub ti mostrerà i comandi
   - Esegui questi comandi nel Terminal (sostituisci TUO_USERNAME e TUO_REPO):
     ```bash
     cd ~/Desktop/Sito
     git remote add origin https://github.com/TUO_USERNAME/TUO_REPO.git
     git branch -M main
     git push -u origin main
     ```

3. **Connetti Render al repository**
   - Vai su Render Dashboard
   - Vai al tuo servizio → Settings
   - Sezione "Build & Deploy"
   - Clicca "Connect GitHub" (o GitLab)
   - Autorizza Render
   - Seleziona il repository appena creato
   - Render farà il deploy automatico

---

### OPZIONE 3: Se Render NON usa Git (deploy manuale)

Se Render è configurato per deploy manuale (senza Git):

1. **Vai su Render Dashboard**
2. **Vai al tuo servizio → Settings**
3. **Sezione "Build & Deploy"**
4. **Cerca "Manual Deploy" o "Upload Files"**
5. **Carica manualmente tutti i file**, inclusi i PDF nella cartella `static/`

⚠️ **Nota**: L'opzione con Git è molto più semplice e consigliata!

---

## ✅ VERIFICA FINALE

Dopo il push/deploy:

1. Vai su https://andrea-lucchesi-website.onrender.com
2. Prova a scaricare i PDF:
   - Clicca "Scarica CV" → dovrebbe funzionare
   - Clicca "Scarica la tesi" → dovrebbe funzionare
3. Oppure prova direttamente:
   - https://andrea-lucchesi-website.onrender.com/static/CV_Andrea_Lucchesi.pdf
   - https://andrea-lucchesi-website.onrender.com/static/tesi_magistrale_greenwashing.pdf

---

## 🔍 Come verificare se Render usa Git

Su Render Dashboard → Il tuo servizio:
- Se vedi "Connected to GitHub/GitLab" → usa Git (Opzione 1 o 2)
- Se vedi solo "Manual Deploy" → deploy manuale (Opzione 3)

