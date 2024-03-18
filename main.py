from typing import Union
from fastapi import FastAPI, Path
import uvicorn
from AI_routes.OpenAi_SD import AIrouterS
from User_router.user import users
from tortoise.contrib.fastapi import register_tortoise
from  config import  TORTOISE_ORM

app = FastAPI()
app.include_router(AIrouterS, prefix='/AI')
app.include_router(users, prefix='/User')


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(gt=10, lt=100), q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run(app, port=8800)  # , host="0.0.0.0"
