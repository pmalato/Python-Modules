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
    member_id: str = Field(default="PT50", min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default=Rank.officer)
    age: int = Field(default=30, ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(default=15, ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now())
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=1000000.0)

    @model_validator(mode='after')
    def validation_rules(self) -> 'SpaceMission':
        invalid: list = []
        fouls: int = 0
        if not self.mission_id.startswith("M"):
            invalid.append("Mission ID must start with 'M'")
            fouls += 1
        if not any(c.rank.value >= Rank.captain.value for c in self.crew):
            invalid.append("Must have at least one Commander or Captain")
            fouls += 1
        if self.duration_days >= 365:
            exp_count = sum(1 for b in self.crew if b.years_experience >= 5)
            if exp_count < len(self.crew) / 2:
                invalid.append(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)")
                fouls += 1
        if not all(i.is_active for i in self.crew):
            invalid.append("All crew members must be active")
            fouls += 1
        if fouls:
            raise ValueError("\n".join(invalid))
        return self


def main() -> None:
    try:
        crew1 = CrewMember(
            name="Sarrah Connor",
            rank=5,
            specialization="Mission Command"
        )
        crew2 = CrewMember(
            name="John Smith",
            rank=3,
            specialization="Navigation"
        )
        crew3 = CrewMember(
            name="Alice Johnson",
            rank=2,
            specialization="Engineering"
        )
        space = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500,
            crew=[crew1, crew2, crew3]
        )
    except ValidationError as e:
        print(e)
        return
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print("Mission: ", space.mission_name)
    print("ID: ", space.mission_id)
    print("destination: ", space.destination)
    print("Duration: ", space.duration_days)
    print("Budget: ", space.budget_millions)
    print("Crew size: ", len(space.crew))
    print("Crew members:")
    for m in space.crew:
        print(f"- {m.name} ({m.rank}) - {m.specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        crew4 = CrewMember(
            name="Beatrix Wonder",
            rank=3,
            specialization="Marine Biologist",
            years_experience=3,
            is_active=False
        )
        space2 = SpaceMission(
            mission_id="M2025_MARIANA",
            mission_name="Mariana exploration site",
            destination="Mariana Trench",
            duration_days=30,
            budget_millions=20000.0,
            crew=[crew4]
        )
    except ValidationError as e:
        for fail in e.errors():
            print(fail["msg"])
            return
    print("Mission: ", space2.mission_name)
    print("ID: ", space2.mission_id)
    print("destination: ", space2.destination)
    print("Duration: ", space2.duration_days)
    print("Budget: ", space2.budget_millions)
    print("Crew size: ", len(space2.crew))
    print("Crew members:")
    for w in space2.crew:
        print(f"- {w.name} ({w.rank}) - {w.specialization}")


if __name__ == "__main__":
    main()
