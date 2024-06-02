
from pydantic import BaseModel
class Diabetic(BaseModel):
    HighBP: bool
    HighChol: bool
    BMI: int
    DiffWalk: bool
    Sex: bool
    Age: int