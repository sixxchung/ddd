
# # A bit odd, but the only way I've been able to get prefixing of the Dash app
# # to work is by allowing the Dash/Flask app to prefix itself, then mounting
# # it to root
# dash_app = Dash(
#     name=__name__,
#     #server = server,
# )

# app_dash = create_app_dash(requests_pathname_prefix="/dash/")
# app.mount("/dash", WSGIMiddleware(app_dash.server))

# # if __name__ == "__main__":
# #     uvicorn.run(app, port=8000)
# if __name__ == "__main__":
# #   app.run_server(debug=True)
#     dash_app.run_server(
#         port=8000
#     )

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.wsgi import WSGIMiddleware

from app_dash import appDash
#from routers import model_get

app = FastAPI()
app.mount("/dash", WSGIMiddleware(appDash.server))
#app.include_router(model_get.router)

@app.get("/")
async def redirect_root():
    response = RedirectResponse("http://127.0.0.1:8000/dash")
    return response

@app.get("/status")
def get_status():
    return {"status": "ok"}

#----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, port=8000)