#from typing import Optional
#from fastapi import FastAPI
from typing import Optional, List
from fastapi import FastAPI, Query

def find_min(arr):
  """ Returns the minimum value of an integer array."""
  return min(arr)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World :)"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/mini/")
async def minMath(nums : List[int] = Query(None)):
    s = min(nums)
    print(s)
    return s #{"smallest num": s   }
#example: http://127.0.0.1:8000/mini/?nums=2&nums=7
#returns 2

 
