from pydantic import BaseModel


class MachineInput(BaseModel):

    air_temperature_k: float

    process_temperature_k: float

    rotational_speed_rpm: int

    torque_nm: float

    tool_wear_min: int

    type_h: int

    type_l: int

    type_m: int

from pydantic import BaseModel


class MachineInput(BaseModel):

    air_temperature_k: float
    process_temperature_k: float
    rotational_speed_rpm: int
    torque_nm: float
    tool_wear_min: int

    type_h: int
    type_l: int
    type_m: int


class PredictionResponse(BaseModel):

    failure_probability: float

    risk_score: float

    risk_level: str