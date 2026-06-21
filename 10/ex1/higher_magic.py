from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def spell(target: str, power: int) -> str:
        ...


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def spell(target: str, power: int) -> str:
        ...


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell(target: str, power: int) -> str:
        ...


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Uses lvl {power} Fireball against {target}"

    def burn(target: str, power: int) -> str:
        return f"{target} burns for {power} seconds"

    print("Testing spell_combiner ...")
    combine = spell_combiner(fireball, burn)
    print(combine("Dragon", 4))


if __name__ == "__main__":
    main()
