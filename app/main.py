import jinja2
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user, product

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user.router)
app.include_router(product.router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
