from models import Terrorist      
import pandas as pd
from fastapi import FastAPI, UploadFile, File
import io
from db import collection

app = FastAPI()

@app.post("/top-threats")
def top_threats(file: UploadFile = File(...)):
    df = pd.read_csv(io.BytesIO(file.file.read()))
    df = df.sort_values("danger_rate", ascending=False)
    top_1 = df.head(5)     
    top = [Terrorist(name=row["name"],location=row["location"], danger_rate=int(row["danger_rate"]))for x,row in top_1.iterrows()]
    for t in top:
        collection.insert_one(t.model_dump())
    return {"count": len(top), "top": [t.model_dump() for t in top]}
   

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

 












