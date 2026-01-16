from enum import Enum


class ArmorType(Enum):
    CHOBHAM = "chobham"
    COMPOSITE = "composite"
    CERAMIC = "ceramic"


ARMOR_BONUS = {
    ArmorType.CHOBHAM: 100,
    ArmorType.COMPOSITE: 50,
    ArmorType.CERAMIC: 50,
}


class Tank:
    def __init__(self, armor: int, penetration: int, armor_type: ArmorType, name: str = "Unknown"):
        self.armor = armor
        self.penetration = penetration
        self.armor_type = armor_type
        self.name = name

    @property
    def effective_armor(self) -> int:
        """return armor + bonus armor"""
        return self.armor + ARMOR_BONUS.get(self.armor_type, 0)

    def is_vulnerable_to(self, enemy: Tank) -> bool:
        """check if tank vulnerable to enemy"""
        return self.effective_armor <= enemy.penetration

    def swap_armor(self, other: "Tank") -> None:
        """swap armor between two tanks"""
        self.armor, other.armor = other.armor, self.armor

    def __repr__(self) -> str:
        return self.name.lower().replace(" ", "-")
