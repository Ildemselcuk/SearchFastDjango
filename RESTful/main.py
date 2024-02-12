import os
import time

from fastapi import FastAPI, Request, Response
from fastapi_versioning import VersionedFastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


from RESTful.driver.router import router as driver_router


from RESTful.database import SessionLocal, engine


app = FastAPI(
    title="IDENTITY Service",
    description="Each endpoint requires <code>x-user-uuid</code> and <code>x-user-identity-uuid</code> in header "
                "except <code>/docs</code> and <code>/user_identity/by_email</code> endpoints.<br/>"
                "To provide these headers in apidocs, click on <code>Authorize</code> button on top right corner."
                "Enter <code>UUIDs</code> and click all <code>Authorize</code> buttons.<br/>",
    swagger_ui_parameters={"tryItOutEnabled": True},
)

app.include_router(driver_router)

app = VersionedFastAPI(app,
                       enable_latest=True,
                       version_format="{major}",
                       prefix_format="/v{major}",
                       )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=os.getenv('TRUSTED_HOSTS')
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)

    # check if request headers has 'x-user-uuid' and 'x-user-identity-uuid' keys except some endpoints
    if (request.url.components.path.find("user_identity/by_email") == -1
            and request.url.components.path.find("/docs") == -1
            and request.url.components.path.find("/test") == -1
            and request.url.components.path.find("/openapi.json") == -1):
        if request.headers.get('x-user-uuid') is None or request.headers.get('x-user-identity-uuid') is None:
            return Response("Missing x-user-uuid or x-user-identity_uuid in header!", status_code=403)

    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
