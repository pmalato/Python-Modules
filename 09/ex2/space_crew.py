from pydantic import (  # type: ignore
    BaseModel,
    Field,
    ValidationError,
    model_validator)
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default=2)
    age: int = Field(get=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default=datetime)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=1000000.0)

    @model_validator(mode='after')
    def 


def main() -> None:
    print("Space Mission Crew Validation")


if __name__ == "__main__":
    main()
