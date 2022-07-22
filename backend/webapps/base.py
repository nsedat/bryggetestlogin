from fastapi import APIRouter
from webapps.auth import route_logout
from webapps.auth import route_login
from webapps.home import route_home
from webapps.users import route_users


api_router = APIRouter()
api_router.include_router(route_home.router, prefix="", tags=["home-webapp"])
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])
api_router.include_router(route_logout.router, prefix="", tags=["leave-webapp"])
