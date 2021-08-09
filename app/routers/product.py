from fastapi.routing import Request, APIRouter
from app.lib import view

router = APIRouter(prefix='/products')


@router.get('')
def list_products(request: Request):
    return view.view('user', {
        "request": request
    })
