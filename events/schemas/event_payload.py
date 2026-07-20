from pydantic import BaseModel



class ToolPayload(BaseModel):

    name: str

    parameters: dict