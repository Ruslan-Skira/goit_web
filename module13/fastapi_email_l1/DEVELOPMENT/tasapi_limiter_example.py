import redis.asyncio as redis
import uvicorn
from fastapi import Depends, FastAPI

from fastapi_limiter import FastAPILimiter  # pip install fastapi-limiter
from fastapi_limiter.depends import RateLimiter

app = FastAPI()


@app.on_event("startup")
async def startup():
   r = await redis.Redis(host='localhost', port=6379, db=0, encoding="utf-8", decode_responses=True)
   await FastAPILimiter.init(r)


@app.get("/", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def index():
   return {"msg": "Hello World"}


if __name__ == "__main__":
   uvicorn.run("tasapi_limiter_example:app", reload=True)