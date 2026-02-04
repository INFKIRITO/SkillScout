from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(
        example="ok",
        description="Health status of the service"
    )
    message: str = Field(
        example="JobGenie AI is running",
        description="Human-readable service message"
    )