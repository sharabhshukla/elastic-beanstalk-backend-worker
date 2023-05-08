from pydantic import BaseModel, Field, root_validator
from ksuid import Ksuid
from typing import Optional


class Job(BaseModel):
    id: Optional[str] = Field(default_factory=Ksuid)
    name: str
    age: float
    sex: str
    sleeping_time: Optional[float] = Field(default=30, le=3600, ge=0)

    @root_validator
    def id_must_be_str(cls, values):
        values['id'] = str(values['id'])
        return values


class DyDbModel(BaseModel):
    username: str
    jobid: str
    job_input: str
    job_output: str
    job_status: str

