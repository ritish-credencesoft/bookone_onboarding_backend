from fastapi import FastAPI , Request
import json
# import variables
app = FastAPI()


@app.get("/api")
def runAutomation():
    return {"msg":"Successfull"}

@app.post("/api/runall")
async def getInformation(info : Request):
    req_info = await info.json()
    with open('Data/test2.json', 'w') as f:
        f.write(req_info)
    import index
