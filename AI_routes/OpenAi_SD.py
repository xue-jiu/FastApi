from fastapi import APIRouter
from Config_AI.open_ai_English import English_Open_AI

AIrouterS = APIRouter()


@AIrouterS.get("/items/{word}")
async def read_items(word: str, name: str = None, ques: str = None):
    English_response = English_Open_AI(ques).response
    return [{"name": word}, {"name": name}, {"response": English_response}]
