# 🔧 Correggi il Repository su Render

## ❌ PROBLEMA:
Render è collegato a: `https://github.com/Andrea4444442/andrea-lucchesi-website`
Ma il repository che abbiamo creato è: `https://github.com/Andrea4444442/sito-andrea-lucchesi`

## ✅ SOLUZIONE:

### Opzione 1: Cambia il repository su Render (CONSIGLIATO)

1. **Su Render Dashboard** → Il tuo servizio → Settings → Build & Deploy
2. Trova la sezione **"Repository"**
3. Clicca **"Edit"** accanto a Repository
4. Cambia l'URL da:
   ```
   https://github.com/Andrea4444442/andrea-lucchesi-website
   ```
   a:
   ```
   https://github.com/Andrea4444442/sito-andrea-lucchesi
   ```
5. Clicca **"Save"**
6. Render farà automaticamente un nuovo deploy con il repository corretto!

### Opzione 2: Rinomina il repository GitHub

Se preferisci mantenere il nome `andrea-lucchesi-website`:
1. Vai su GitHub → Il repository `sito-andrea-lucchesi`
2. Settings → Scroll fino a "Danger Zone"
3. Clicca "Change repository name"
4. Rinomina in: `andrea-lucchesi-website`
5. Render dovrebbe rilevarlo automaticamente

---

## ✅ VERIFICA DOPO LA CORREZIONE:

1. Render dovrebbe fare un nuovo deploy automatico
2. Vai su https://andrea-lucchesi-website.onrender.com
3. Prova i PDF:
   - https://andrea-lucchesi-website.onrender.com/static/CV_Andrea_Lucchesi.pdf
   - https://andrea-lucchesi-website.onrender.com/static/tesi_magistrale_greenwashing.pdf
4. Prova il form contatti

---

## 📋 ALTRE VERIFICHE:

Assicurati che:
- ✅ **Branch**: `main` (corretto)
- ✅ **Build Command**: `pip install -r requirements.txt` (corretto)
- ✅ **Start Command**: `gunicorn app:app` (corretto)
- ✅ **Auto-Deploy**: On (attivo)

