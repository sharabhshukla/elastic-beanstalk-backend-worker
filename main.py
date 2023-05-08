from fastapi import FastAPI, Response, status
from time import sleep
from src.data_models import Job, DyDbModel
from src.db_utils import create_entry, update_job_status
from loguru import logger
import json

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def root_msg():
    return Response(content="This is the root", status_code=status.HTTP_200_OK)


@app.get("/healthz")
def health_ping():
    return Response(content='Ok', status_code=status.HTTP_200_OK)


@app.post("/run_job", status_code=status.HTTP_200_OK)
def run_job(job: Job):
    dydb_data = DyDbModel(username="admin", jobid=job.id, job_input=json.dumps(job.json()),
                          job_output="NA", job_status="Created")
    create_entry(table_name="job-status", item=dydb_data.dict())
    update_job_status(username="admin", job_id=job.id, new_status="Processing")
    logger.info(f"Running job with id {job.id}")
    logger.info(f"sleeping for {job.sleeping_time} seconds")
    sleep(job.sleeping_time)
    logger.info("Job done!!")
    update_job_status(username="admin", job_id=job.id, new_status="Done")
    return Response(content='Job done', status_code=status.HTTP_200_OK)
