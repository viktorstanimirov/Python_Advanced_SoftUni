from typing import Dict


class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name: str = name
        self.hp: int = hp
        self.mp: int = mp
        self.skills: Dict = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

        return "Skill already added"

    def player_info(self) -> str:
        result = f"Name: {self.name}\n" \
                 f"Guild: {self.guild}\n" \
                 f"HP: {self.hp}\n" \
                 f"MP: {self.mp}\n"

        for skill, mana in self.skills.items():
            result += f"==={skill} - {mana}"

        return result
