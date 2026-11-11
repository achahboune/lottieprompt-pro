from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()

# Allow requests from the local file origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

# Simple placeholder Lottie animation (rotating circle)
PLACEHOLDER_ANIMATION={"v":"5.7.6","fr":30,"ip":0,"op":60,"w":200,"h":200,"nm":"Simple Circle","ddd":0,"assets":[],"layers":[{"ddd":0,"ind":1,"ty":4,"nm":"Ellipse","sr":1,"ks":{"o":{"a":0,"k":100},"r":{"a":1,"k":[{"t":0,"s":0},{"t":60,"s":360}]},"p":{"a":0,"k":[100,100,0]},"a":{"a":0,"k":[0,0,0]},"s":{"a":0,"k":[100,100,100]}},"shapes":[{"ty":"el","p":{"a":0,"k":[0,0]},"s":{"a":0,"k":[100,100]},"nm":"Ellipse Path 1"},{"ty":"fl","c":{"a":0,"k":[0.2,0.6,0.8,1]},"nm":"Fill 1"}],"ip":0,"op":60,"st":0,"bm":0}]}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(req: PromptRequest):
    # In a real implementation, the prompt would be processed to create a custom animation.
    # Here we return a static placeholder.
    if not req.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    return {"animation": PLACEHOLDER_ANIMATION}
