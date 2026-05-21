def main():
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": {
            "first_kill", "level_10", "treasure_hunter", "speed_demon"
        },
        "Bob": {
            "first_kill", "level_10", "boss_slayer", "collector"
        },
        "Charlie": {
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"
        }
    }

    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")
    print()

    print("=== Achievement Analytics ===")

    alice = players["Alice"]
    bob = players["Bob"]
    charlie = players["Charlie"]

    all_unique = set.union(alice, bob, charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common_all = set.intersection(alice, bob, charlie)
    print(f"Common to all players: {common_all}")

    rare = (
        (alice - bob - charlie) |
        (bob - alice - charlie) |
        (charlie - alice - bob)
    )

    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    main()
