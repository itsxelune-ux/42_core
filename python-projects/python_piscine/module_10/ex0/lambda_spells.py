def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    avg_power = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:
    print("Testing artifact sorter...")

    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'fire'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'air'}
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}) "
          f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']})")

    print("\nTesting power_filter")
    filtered_artifacts = power_filter(artifacts, 50)
    for i, art in enumerate(filtered_artifacts):
        print(f"artifact {i}: name: {art['name']}, power: {art['power']}")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage_stats")
    mages = [
        {'name': 'Ilka', 'power': 92, 'element': 'fire'},
        {'name': 'Ahamohlanov', 'power': 85, 'element': 'air'}
    ]

    stats_mages = mage_stats(mages)

    print(f"max_power: {stats_mages['max_power']}")
    print(f"min_power: {stats_mages['min_power']}")
    print(f"avg_power: {stats_mages['avg_power']}")


if __name__ == "__main__":
    main()