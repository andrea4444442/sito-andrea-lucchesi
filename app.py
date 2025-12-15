import os
import smtplib
import logging
from email.message import EmailMessage

from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

load_dotenv()  # legge il file .env

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "chiave-segreta-cambiami-in-produzione")

# Configurazione logging per produzione
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _smtp_send(msg: EmailMessage) -> None:
    host = os.environ.get("MAIL_HOST", "smtp.gmail.com")
    port = int(os.environ.get("MAIL_PORT", "587"))
    user = os.environ.get("MAIL_USER")
    password = os.environ.get("MAIL_PASS")
    
    if not user or not password:
        raise ValueError("MAIL_USER e MAIL_PASS devono essere configurati nelle variabili d'ambiente")
    
    logger.info(f"Tentativo invio email a {msg['To']} via {host}:{port}")
    
    try:
        with smtplib.SMTP(host, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(user, password)
            server.send_message(msg)
        logger.info(f"Email inviata con successo a {msg['To']}")
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"Errore autenticazione SMTP: {e}")
        raise
    except smtplib.SMTPException as e:
        logger.error(f"Errore SMTP: {e}")
        raise
    except Exception as e:
        logger.error(f"Errore generico invio email: {e}")
        raise


def send_contact_emails(nome: str, email: str, messaggio: str) -> None:
    user = os.environ.get("MAIL_USER")
    if not user:
        raise ValueError("MAIL_USER deve essere configurato")
    to_addr = os.environ.get("MAIL_TO", user)

    # 1) Email a te (notifica)
    msg_owner = EmailMessage()
    msg_owner["Subject"] = f"[Sito] Nuovo messaggio da {nome}"
    msg_owner["From"] = f"Website Contact <{user}>"
    msg_owner["To"] = to_addr
    msg_owner["Reply-To"] = email
    msg_owner.set_content(
        "Hai ricevuto un nuovo messaggio dal form contatti.\n\n"
        f"Nome: {nome}\n"
        f"Email: {email}\n\n"
        "Messaggio:\n"
        f"{messaggio}\n"
    )
    _smtp_send(msg_owner)

    # 2) Email al visitatore (conferma)
    msg_user = EmailMessage()
    msg_user["Subject"] = "Conferma ricezione messaggio – Andrea Lucchesi"
    msg_user["From"] = f"Andrea Lucchesi <{user}>"
    msg_user["To"] = email
    msg_user.set_content(
        f"Ciao {nome},\n\n"
        "grazie per avermi contattato. Ho ricevuto correttamente il tuo messaggio e ti risponderò appena possibile.\n\n"
        "—\n"
        "Andrea Lucchesi\n"
        "Email: a.lucchesi1999@gmail.com\n"
        "LinkedIn: https://www.linkedin.com/in/andrea-lucchesi-\n"
    )
    _smtp_send(msg_user)


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/chi-sono")
def chi_sono():
    return render_template("chi-sono.html", title="Chi sono")


@app.route("/contatti", methods=["GET", "POST"])
def contatti():
    if request.method == "POST":
        nome = (request.form.get("nome") or "").strip()
        email = (request.form.get("email") or "").strip()
        messaggio = (request.form.get("messaggio") or "").strip()

        if not nome or not email or not messaggio:
            flash("Compila tutti i campi, per favore.", "error")
            return redirect(url_for("contatti"))

        if "@" not in email or "." not in email:
            flash("Inserisci un'email valida.", "error")
            return redirect(url_for("contatti"))

        try:
            send_contact_emails(nome, email, messaggio)
        except KeyError as e:
            logger.error(f"Variabile d'ambiente mancante: {e}")
            flash("Errore di configurazione del server. Contattami direttamente via email.", "error")
            return redirect(url_for("contatti"))
        except smtplib.SMTPAuthenticationError:
            logger.error("Errore autenticazione email: credenziali non valide")
            flash("Errore nell'invio email. Contattami direttamente via email.", "error")
            return redirect(url_for("contatti"))
        except Exception as e:
            logger.error(f"ERRORE INVIO EMAIL: {repr(e)}", exc_info=True)
            flash("Errore nell'invio email. Riprova o contattami via email direttamente.", "error")
            return redirect(url_for("contatti"))

        flash(f"Grazie {nome}! Messaggio inviato. Riceverai anche una mail di conferma.", "success")
        return redirect(url_for("contatti"))

    return render_template("contatti.html", title="Contatti")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)




