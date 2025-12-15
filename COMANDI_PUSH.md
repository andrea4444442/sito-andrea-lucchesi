# Comandi per fare Push su GitHub

## Dopo aver creato il repository su GitHub, esegui questi comandi:

```bash
cd ~/Desktop/Sito
git remote add origin https://github.com/TUO_USERNAME/TUO_REPO.git
git branch -M main
git push -u origin main
```

**Sostituisci:**
- `TUO_USERNAME` = il tuo username GitHub
- `TUO_REPO` = il nome del repository che hai appena creato

## Esempio:
Se il tuo username è `andrealucchesi` e il repo si chiama `sito-andrea-lucchesi`:

```bash
cd ~/Desktop/Sito
git remote add origin https://github.com/andrealucchesi/sito-andrea-lucchesi.git
git branch -M main
git push -u origin main
```

## Dopo il push:
1. Vai su Render Dashboard
2. Vai al tuo servizio → Settings
3. Sezione "Build & Deploy"
4. Clicca "Connect GitHub"
5. Autorizza Render
6. Seleziona il repository appena creato
7. Render farà il deploy automatico con tutti i file, inclusi i PDF!

