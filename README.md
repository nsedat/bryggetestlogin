# brygge test login

## Aufgabe:
Deﬁniere wie die User Registrierung und der Login für Brygge Nutzer funktionieren kann und baue
die BE API dafür in Python. Erstelle Dein eigenes Github/Gitlab Projekt und share die Ownership
dann mit @steinke Wir reviewen den Code und stellen dann im Meeting ein paar Fragen.

### -> Anforderungen A:
* Python
* API
* user registration
* user login

### -> Anforderungen B:
* scalability
* fast
* low impact on GUI
* few dependencies
* ...

### Umsetzung:
* ...

---

## Technology Stack:
* FastAPI
* Uvicorn (fast async http server)
* Pytest
* Sqlalchemy
* SQLite
* JWT (JSON Web Tokens)

---

! a lot code used from free available fastapi pattern

---

## How to start the app ?
```
git clone https://github.com/nsedat/bryggetestlogin.git
cd .\bryggetestlogin\
cd .\backend\
pip install -r .\requirements.txt
uvicorn main:app --reload
visit 127.0.0.1:8000/ with browser
```

## unit tests
```
cd .\bryggetestlogin\
cd .\backend\
pytest
```

## annots:
* no comments (because classes, functions and logic should be self explanatory - otherwise refactor)
* no use of venv because intended to be running in dockerized environment
* using sqlite (for smaller footprint here - but in live environment it should use mongodb)
* no i18n and localization (german only)


## future features

* TODO: use HTTPS (currently only HTTP for simplicity)
* TODO: use 2FA in production ?!
* TODO: validate register request by mail-auth (register, receive mail, click on link in mail, then fully registered)
  * no autologin after registration yet
* TODO: better password security checks (> 4 chars)
* TODO: more unit tests (call in directory 'backend' with 'pytest')
* TODO: needs deactivate and delete user (from admin-frontend - but can be done with database-tools as well)
* TODO: allow user to change password

---

EOF
