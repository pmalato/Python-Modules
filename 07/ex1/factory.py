from ex0.factory import CreatureFactory
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        sproutling_obj = Sproutling("Sproutling", "Grass")
        return sproutling_obj

    def create_evolved(self) -> Bloomelle:
        bloomelle_obj = Bloomelle("Bloomelle", "Grass/Fairy")
        return bloomelle_obj


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        shiftling_obj = Shiftling("Shiftling", "Normal")
        return shiftling_obj

    def create_evolved(self) -> Morphagon:
        morphagon_obj = Morphagon("Morphagon", "Normal/Dragon")
        return morphagon_obj
