# ⚠️ CORREZIONE VARIABILI D'AMBIENTE SU RENDER

## ❌ ERRORE COMUNE

Se nel campo **Value** hai scritto qualcosa tipo:
```
(una chiave casuale lunga, tipo: chiave-segreta-super-lunga-e-casuale-12345)
```

Questo è **SBAGLIATO**! Il campo Value deve contenere **SOLO** il valore, senza parentesi o descrizioni.

---

## ✅ COME CORREGGERE

### Per FLASK_SECRET_KEY:

1. Vai su Render Dashboard → Il tuo servizio → Environment
2. Trova la variabile `FLASK_SECRET_KEY`
3. Clicca "Edit" o modificala
4. Nel campo **Value**, metti **SOLO**:
   ```
   chiave-segreta-super-lunga-e-casuale-12345
   ```
   (senza parentesi, senza testo descrittivo)

5. Oppure, per maggiore sicurezza, usa questa chiave generata casualmente:
   ```
   sfWC1fnBxVLg9LF9262nK8S6ZKlo4Dy0l0PI0F06WaU
   ```

6. Clicca "Save Changes"

---

## ✅ VERIFICA TUTTE LE ALTRE VARIABILI

Controlla che anche le altre variabili abbiano **SOLO** il valore, senza testo descrittivo:

### MAIL_USER
**Value deve essere:**
```
a.lucchesi1999@gmail.com
```
(NON "Email: a.lucchesi1999@gmail.com" o altre descrizioni)

### MAIL_PASS
**Value deve essere:**
```
rygiasejorptypxd
```
(SOLO la password, senza spazi o descrizioni)

### MAIL_HOST
**Value deve essere:**
```
smtp.gmail.com
```

### MAIL_PORT
**Value deve essere:**
```
587
```
(SOLO il numero, senza testo)

### MAIL_TO
**Value deve essere:**
```
a.lucchesi1999@gmail.com
```

---

## 📋 CHECKLIST CORREZIONE

- [ ] FLASK_SECRET_KEY: Value = solo la chiave (senza parentesi/descrizioni)
- [ ] MAIL_USER: Value = solo l'email
- [ ] MAIL_PASS: Value = solo la password
- [ ] MAIL_HOST: Value = solo "smtp.gmail.com"
- [ ] MAIL_PORT: Value = solo "587"
- [ ] MAIL_TO: Value = solo l'email

---

## 🔄 DOPO LA CORREZIONE

1. Salva tutte le modifiche
2. Vai su "Events" o "Manual Deploy" → "Deploy latest commit"
3. Aspetta che il deploy finisca
4. Testa il sito

---

## 💡 REGOLA GENERALE

**Il campo "Key"** = nome della variabile (es. `FLASK_SECRET_KEY`)
**Il campo "Value"** = SOLO il valore, niente altro!

Se vedi parentesi, due punti, o testo descrittivo nel Value, rimuovilo!

