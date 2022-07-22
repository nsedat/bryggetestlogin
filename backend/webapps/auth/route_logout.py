from apis.version1.route_logout import logout_user
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/logout/")
def logout(request: Request):
	response = templates.TemplateResponse("general_pages/homepage.html", {"request": request, "msg": 'erfolgreich ausgeloggt'})
	success = logout_user(response=response)

	return response
