from pydantic import (  # type: ignore
    BaseModel,
    Field,
    ValidationError,
    model_validator)
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default=datetime)
    location: str = Field(min_length=3, max_length=300)
    contact_type: ContactType = Field(default=1)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str = Field(default="ItsWedmyDudes", max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation(self) -> "AlienContact":
        invalid = []
        if not self.contact_id.startswith("AC"):
            invalid.append(self.contact_id)
        if self.contact_type == ContactType.physical and not self.is_verified:
            invalid.append(self.contact_type)
        if self.contact_type == ContactType.telepathic and\
                self.witness_count <= 3:
            invalid.append(self.contact_id)
        if self.signal_strength >= 7.0 and not self.message_received:
            invalid.append(self.signal_strength)
        return self


def main() -> None:
    try:
        station = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            contact_type=1,
            signal_strength=9.0,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'"
        )
    except ValidationError as e:
        print(e)
        return
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print("ID: ", station.contact_id)
    print("Type: ", station.contact_type)
    print("Location: ", station.location)
    print("Signal: ", station.signal_strength)
    print("Time: ", station.duration_minutes)
    print("Witnesses: ", station.witness_count)
    print("Message: ", station.message_received)
    print("\n======================================")
    print("Expected validation error:")
    try:
        station2 = AlienContact(
            contact_id="2024_001",
            location="Area 51, Nevada",
            contact_type=4,
            signal_strength=9.0,
            duration_minutes=45,
            witness_count=2
        )
    except ValidationError as e:
        print(e)
        return
    print(station2.contact_type)


if __name__ == "__main__":
    main()
