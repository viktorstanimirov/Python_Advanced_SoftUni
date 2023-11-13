class Hero:
    def __init__(self, name: str, health: int, ) -> None:
        self.name = name
        self.health = health

    def defend(self, damage: int) -> str:
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount: int) -> None:
        self.health += amount


# """Test code"""

# hero = Hero("Peter", 100)
# print(hero.defend(50))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))
