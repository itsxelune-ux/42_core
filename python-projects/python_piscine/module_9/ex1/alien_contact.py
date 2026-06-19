from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    contact_type: ContactType
    location: str = Field(min_length=3, max_length=100)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals should include received messages")
        return self
    
def main():
    print("Alien Contact Log Validation")
    print("=" * 40)

    print("Valid contact report:")

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.radio,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )

        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'\n")

    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    print("=" * 40)

    print("Invalid contact report:")

    try:
        bad_contact = AlienContact(
            contact_id="AC_999",
            timestamp=datetime.now(),
            contact_type=ContactType.telepathic,
            location="Unknown Sector",
            signal_strength=6.0,
            duration_minutes=30,
            witness_count=2,
            message_received=None,
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

if __name__ == "__main__":
    main()