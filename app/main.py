from fastapi import FastAPI
from fastapi import status
from controller import router

app = FastAPI()

@app.get("/")
async def index():
    return dict(
        is_success=True, 
        status_code=status.HTTP_200_OK, 
        message="acmecorp-developer-iq-git-service",
        data=None
    )

app.include_router(router, prefix="/git")

# if __name__ == "__main__":
#     from uvicorn import run
#     run("main:app", host="localhost", port=86, reload=True)