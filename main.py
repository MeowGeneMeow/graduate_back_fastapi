from fastapi import FastAPI, Response
import uvicorn
import wandb
import os

app = FastAPI()



@app.get("/images/seed_map.png")
async def read_image():
    api = wandb.Api()
    artifact = api.artifact("web_packet_prediction/som_visulization:latest")
    # 从Artifact中获取图像文件
    #image_file = artifact.get(image_name)
    # 下载图像文件到本地
    artifact.files(names=['seed_map.png'])[0].download()
    with open("seed_map.png", "rb") as file:
        image_data = file.read()
    os.remove("seed_map.png")
    return Response(content=image_data, media_type="image/png")


@app.get("/images/u_map.png")
async def read_image():
    api = wandb.Api()
    artifact = api.artifact("web_packet_prediction/som_visulization:latest")
    # 从Artifact中获取图像文件
    #image_file = artifact.get(image_name)
    # 下载图像文件到本地
    artifact.files(names=['u_map.png'])[0].download()
    with open("u_map.png", "rb") as file:
        image_data = file.read()
    os.remove("u_map.png")
    return Response(content=image_data, media_type="image/png")

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
@app.get("/wandb_config_date")
def wandb_config_date(date):
    return {
        "model_version":"",
        "node_number":"",
        "sentence_transformer":"all-mpnet-base-v2"
    }

@app.get("/model_now_detail")
def model_now_detail():

    return "today"

@app.get("/wandb_som_umap")
def wandb_som_umap():

    return "today"

@app.get("/wandb_seed_umap")
def wandb_seed_umap():
    return "today"



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9527)