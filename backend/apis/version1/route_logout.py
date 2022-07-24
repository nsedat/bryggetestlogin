from fastapi import Response
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status

router = APIRouter()


@router.get("/logout/")
def logout_user(response: Response) -> Response:
	# ANNOT: logout_user by deleting cookie ... just a frontend solution yet (otherwise have a flag in local database to reflect login status?)
	response.delete_cookie(key="access_token")
	return {"msg": "logged out"}
