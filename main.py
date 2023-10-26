from fastapi import FastAPI
import uvicorn

app = FastAPI()

## Example

@app.get("/")
def read_root():
    return {"Hello": "World"}


## Database 區域

@app.post("/upload_data")
def upload_data():
    return "not yet"
@app.get("/get_day_summary")
def get_day_summary():
    return "not yet"

@app.get("/get_day_table")
def get_day_table():
    return "not yet"


## Airflow 區域
@app.get("/task_status")
def task_status():
    return "not yet"

## Wandb 區域
@app.get("/wandb_config")
def wandb_config():
    return "not yet"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9527)