from fastapi import Response
from fastapi import APIRouter

router = APIRouter()


@router.get("/logout")
def logout_user(response: Response):
	# ANNOT: logout_user by deleting cookie ... just a frontend solution yet (otherwise have a flag in local database to reflect login status?)
	response.set_cookie(key="access_token", value=None, httponly=True)
	return None
