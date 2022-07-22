# brygge test login

## Challenge:
>
> Deﬁniere wie die User Registrierung und der Login für Brygge Nutzer funktionieren kann und baue
die BE API dafür in Python.
>
---
###
### Requirements A:
* Python
* API
* user registration
* user login
---
### Requirements B:
* scalability
* fast
* low impact on GUI
* few dependencies
* documentation by definition (thnx fastapi)
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
you may create venv for this ... but it's intended to run in a separate docker container environment ...
```
git clone https://github.com/nsedat/bryggetestlogin.git
cd bryggetestlogin
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
visit http://127.0.0.1:8000/ with your browser
```

or using docker:
```
get Dockerfile from https://github.com/nsedat/bryggetestlogin.git
docker build -t bryggetestlogin .
docker run --rm -it -p 8000:8000 bryggetestlogin
visit http://127.0.0.1:8000/ with your browser
```


## unit tests
```
cd .\bryggetestlogin\
cd .\backend\
pytest
```
---

## annots:
* only basic implementation to show technology
* no comments in code - because classes, functions and logic should be self explanatory; if not: refactor
* no use of venv because intended to be running in dockerized environment
* using sqlite (for smaller footprint here - but in live environment it should use mongodb)
* no i18n and localization (german only)

---

## future features (not implemented yet)

* TODO: validate register request by mail-auth (register, receive mail, click on link in mail, then fully registered)
* TODO: autologin after successful registration (and click link)
* TODO: use HTTPS (currently only HTTP for simplicity)
* TODO: use 2FA in production ?!
* TODO: use captcha to defeat robots
* TODO: better password security checks (> 4 chars; eg 10 chars with upper, lower, numbers and symbols)
* TODO: more unit tests (call in directory 'backend' with 'pytest')
* TODO: needs deactivate and delete user (from admin-frontend - but can be done with database-tools as well)
* TODO: allow user to change password
* TODO: password forgotten functionality
* TODO: clarify how user roles are administrated ("on behalf of", "give and remove rights", ...)

---

EOF
