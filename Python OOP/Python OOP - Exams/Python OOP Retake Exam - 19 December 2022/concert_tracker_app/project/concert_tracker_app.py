from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer
                            }

    NEEDED_CONCERT_SKILLS = {
        "Rock": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing high pitch notes"],
            "Guitarist": ["play rock"]
        },
        "Metal": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing low pitch notes"],
            "Guitarist": ["play metal"]
        },
        "Jazz": {
            "Drummer": ["play the drums with drum brushes"],
            "Singer": ["sing high pitch notes", "sing low pitch notes"],
            "Guitarist": ["play jazz"]
        }
    }

    def __init__(self) -> None:
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES.keys():
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        current_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(current_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        current_band = Band(name)
        self.bands.append(current_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        current_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(current_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [m.name for m in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        current_musician = self.find_musician(musician_name)
        current_band = self.find_band(band_name)
        current_band.members.append(current_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        if musician_name in [m.name for m in Band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        current_musician = self.find_musician(musician_name)
        Band.members.remove(current_musician)
        return f"{current_musician} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        musician_types = set()
        current_band = self.find_band(band_name)
        [musician_types.add(m.__class__.__name__) for m in current_band.members]

        if len(musician_types) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        current_concert_name = [c for c in self.concerts if c.place == concert_place][0]
        required_skills = self.NEEDED_CONCERT_SKILLS[current_concert_name.genre]

        for m in current_band.members:
            type_m = m.__class__.__name__
            skills = m.skills
            if not set(required_skills[type_m]).issubset(set(skills)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (current_concert_name.audience * current_concert_name.ticket_price) - current_concert_name.expenses
        return (f"{band_name} gained {profit:.2f}$ from the {current_concert_name.genre} "
                f"concert in {current_concert_name.place}.")

    def find_musician(self, name: str):
        musician = [m for m in self.musicians if m.name == name][0]
        return musician

    def find_band(self, name: str):
        band = [b for b in self.bands if b.name == name][0]
        return band
