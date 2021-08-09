from fastapi.templating import Jinja2Templates


def view(name, data):
    template = Jinja2Templates(directory='templates')
    return template.TemplateResponse(f"{name}.html", data)
