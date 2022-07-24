from apis.version1.route_logout import logout_user
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

from webapps.auth.route_login import home_response


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/logout/")
def logout_user_api(request: Request):
	response = home_response(request=request, msg='erfolgreich ausgeloggt')
	success = logout_user(response=response)
	return response
