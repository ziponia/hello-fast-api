from fastapi.routing import APIRouter, Request

from app.lib import view

router = APIRouter()


@router.get("/users")
def get_users(request: Request):
    return view.view('index', {
        "request": request,
        "name": "kuby!"
    })
