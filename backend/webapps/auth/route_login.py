from optparse import Option
from apis.version1.route_login import login_for_access_token
from apis.version1.route_login import get_current_user_from_token
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from webapps.auth.forms import LoginForm
from db.models.users import User
from apis.utils import OAuth2PasswordBearerWithCookie

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login/")
def login(request: Request):
	response = templates.TemplateResponse("auth/login.html", {"request": request})
	return response


def home_response(request: Request, db: Session = Depends(get_db), access_token: str = Depends(oauth2_scheme), msg: str = None):
	try:
		if type(access_token) == str:	# if from cookie ... then split "Bearer 123ludvlvlb..." to match Token class (dict)
			token = {}
			token['access_token'] = access_token.split(' ')[1]
			access_token = token
		current_user: User = get_current_user_from_token(token=access_token['access_token'], db=db)
	except Exception:
		current_user = None
	if current_user:
		username = current_user.username
		info = "Hallo " + username
	else:
		info = 'sie sind nicht eingeloggt : bitte anmelden oder registrieren'
	request._url=request.url_for('home')
	response = templates.TemplateResponse("general_pages/homepage.html", {"request": request, "msg": msg, "info": info})
	return response


@router.post("/login/")
async def login(request: Request, db: Session = Depends(get_db)):
	form = LoginForm(request)
	await form.load_data()
	if await form.is_valid():
		try:
			form.__dict__.update(msg="Login erfolgreich :)")
			response = templates.TemplateResponse("auth/login.html", form.__dict__)
			access_token = login_for_access_token(response=response, form_data=form, db=db)
			response = home_response(request=request, db=db, access_token=access_token, msg='erfolgreich eingeloggt')
			response.set_cookie(key="access_token", value=f"Bearer {access_token['access_token']}", httponly=True)
			return response

		except HTTPException:
			form.__dict__.update(msg="")
			form.__dict__.get("errors").append("Ungültige Email oder verkehrtes Passwort")
			#return templates.TemplateResponse("auth/login.html", form.__dict__)
	return templates.TemplateResponse("auth/login.html", form.__dict__)
