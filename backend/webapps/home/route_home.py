from typing import Optional

from apis.version1.route_login import get_current_user_from_token
from webapps.auth.route_login import home_response
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
	response = home_response(request=request, db=db, msg=msg, access_token=token)
	return response
