from pydantic import BaseModel, Field, ValidationError  # type: ignore
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=5, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default=datetime.now())
    is_operational: bool = Field(default=True)
    notes: str = Field(default="WAZAAAAAAAA", max_length=200)


def main() -> None:
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
        )
    except ValidationError as error:
        print(error)
        return
    print("Space Station Data Validation")
    print("========================================")
    print("ID: ", station.station_id)
    print("Name: ", station.name)
    print("Crew: ", station.crew_size)
    print("Power: ", station.power_level)
    print("Oxygen: ", station.oxygen_level)
    if station.is_operational:
        print("Satus: Operational\n")
    else:
        print("Satus: Not operational\n")
    print("========================================")
    print("Expected validation error:")
    try:
        station_error = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=35,
                power_level=85.5,
                oxygen_level=92.3,
                is_operational=False
            )
    except ValidationError as error:
        print(error)
        return
    print(station_error.crew_size)


if __name__ == "__main__":
    main()
