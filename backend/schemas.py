from enum import Enum
from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    AWAITING_WRITTEN = "awaiting_written"
    FINISHED_WRITTEN = "finish_written"
    AWAITING_INTERVIEW = "awaiting_interview"
    FINISHED_INTERVIEW = "finish_interview"
    OFFERED = "offered"
    REJECTED = "rejected"
    STOPPED = "stopped"


class ApplicationCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    company_name: str = Field(min_length=1)
    position_name: str = Field(min_length=1)
    applied_on: date
    status: ApplicationStatus
