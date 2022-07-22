from typing import Optional

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import HTTPException


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
	token = request.cookies.get("access_token")
	scheme, param = get_authorization_scheme_param(token)  # scheme will hold "Bearer" and param will hold actual token value
	try:
		current_user: User = get_current_user_from_token(token=param, db=db)
	except HTTPException:
		current_user = None
	if current_user:
		username = current_user.username
		info = "Hallo " + username
	else:
		info = 'sie sind nicht eingeloggt : bitte anmelden oder registrieren'
	return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "msg": msg, "info": info})
