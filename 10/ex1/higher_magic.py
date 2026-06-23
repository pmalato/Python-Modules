from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def spell(target: str, power: int) -> str:
        return base_spell(target, power*multiplier)
    return spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def inner_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return inner_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell(target: str, power: int) -> list:
        return [x(target, power) for x in spells]
    return spell


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Uses lvl {power} Fireball against {target}"

    def burn(target: str, power: int) -> str:
        return f"{target} burns for {power} seconds"

    def fake(target: int, power: str) -> str:
        return ""

    print("\nTesting spell_combiner ...")
    combine = spell_combiner(fireball, burn)
    print(combine("Dragon", 4))
    print("\nTesting power_amplifier ...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 15))
    print("\nTesting conditional_caster ...")
    attempt1 = conditional_caster(fake, burn)
    print(attempt1(0, 30))
    attempt2 = conditional_caster(fireball, burn)
    print(attempt2("Dragon", 23))
    print("\nTesting spell_combiner ...")
    final = spell_sequence([
        combine,
        mega_fireball,
        attempt2])
    print(final("dragon", 30))


if __name__ == "__main__":
    main()
