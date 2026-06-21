def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] <= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda y: y["power"])["power"],
        "avg_power": round(
            sum(map(lambda z: z["power"], mages)) / len(mages), 2)
        }


def main() -> None:
    artifact_list: list[dict] = [
        {"name": "Ring", "power": 50, "type": "Mystic"},
        {"name": "Belt", "power": 70, "type": "Levitation"},
        {"name": "Staff", "power": 96, "type": "Fire"},
        {"name": "Diadem", "power": 26, "type": "Water"},
        {"name": "Wings", "power": 45, "type": "Air"}]
    mage_list: list[dict] = [
        {"name": "Merlin", "power": 500, "type": "All"},
        {"name": "Allan", "power": 270, "type": "Fire"},
        {"name": "Dona", "power": 350, "type": "Water"},
        {"name": "Saphire", "power": 450, "type": "Air"},
        {"name": "Barnabas", "power": 300, "type": "Fire"}
    ]
    spell_list = ["Incendio", "Alohomora", "Stupefy", "Accio", "Levicorpus"]
    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifact_list))
    print("\nTesting power filter...")
    print(power_filter(mage_list, 280))
    print("\nTesting spells transformer...")
    print(spell_transformer(spell_list))
    print("\nTesting mage_stats...")
    print(mage_stats(mage_list))


if __name__ == "__main__":
    main()
