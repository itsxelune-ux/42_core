class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __repr__(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, status: str):
        super().__init__(name, height)
        self.color = color
        self.status = status

    def __repr__(self):
        return f"{super().__repr__()}, {self.color} flowers {self.status}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, status: str, point):
        super().__init__(name, height, color, status)
        self.points = point

    def __repr__(self):
        return f"{super().__repr__()}, Prize points: {self.points}"


class GardenManager:
    class GardenStats:
        def __init__(self):
            self.gardenstats = {}

        def add_garden(self, owner: str):
            if owner not in self.gardenstats:
                self.gardenstats[owner] = {
                    "total_growth": 0,
                    "plants_count": 0,
                    "regular": 0,
                    "flowering": 0,
                    "prize": 0,
                }

        def add_plant(self, owner: str, plant):
            self.add_garden(owner)
            if isinstance(plant, PrizeFlower):
                p_type = "prize"
            elif isinstance(plant, FloweringPlant):
                p_type = "flowering"
            else:
                p_type = "regular"
            self.gardenstats[owner][p_type] += 1
            self.gardenstats[owner]["plants_count"] += 1

        def add_grow(self, owner: str):
            if owner in self.gardenstats:
                count = self.gardenstats[owner]["plants_count"]
                self.gardenstats[owner]["total_growth"] += count

    def __init__(self):
        self.gardens = {}
        self.stats = self.GardenStats()

    def add_plant(self, owner: str, plant: Plant) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
        self.stats.add_plant(owner, plant)
        print(f"Added {plant.name} to {owner}'s garden")

    @classmethod
    def create_garden_network(cls):
        network = cls()
        network.gardens = {}
        network.gardens["Bob"] = []
        cuc = PrizeFlower("Cucumber", 10, "White", "Blooming", 92)
        network.gardens["Bob"].append(cuc)
        network.stats.add_plant("Bob", cuc)
        return network

    def help_grow(self, owner: str):
        if owner not in self.gardens:
            print("There is no garden with this owner")
            return
        print(f"{owner}'s is helping all plants grow...")
        for i in self.gardens[owner]:
            i.grow()
        self.stats.add_grow(owner)

    def report(self, owner: str):
        if owner not in self.gardens:
            print("There is no garden with this owner")
            return
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.gardens[owner]:
            print(f"- {plant}")
        print()
        print(
            f"Plant added: {self.stats.gardenstats[owner]['plants_count']}, "
            f"Total growth: {self.stats.gardenstats[owner]['total_growth']}cm"
        )
        regular = self.stats.gardenstats[owner]["regular"]
        flowering = self.stats.gardenstats[owner]["flowering"]
        prize = self.stats.gardenstats[owner]["prize"]
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )

    def common_info(self):
        for owner, garden in self.gardens.items():
            for plant in garden:
                if not self.validate_height(plant.height):
                    print("Height validation test: False")
                    return
        print("Height validation test: True")

        score_parts = []
        for owner, plants in self.gardens.items():
            total_score = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_score += plant.points
            # add total growth to match demo scoring
            total_score += self.stats.gardenstats[owner]["total_growth"]
            score_parts.append(f"{owner}: {total_score}")

        print(f"Garden scores - {', '.join(score_parts)}")
        print(f"Total gardens managed: {len(self.gardens)}", end="")

    @staticmethod
    def validate_height(height):
        return height > 0


def main():
    print("=== Garden Management System Demo ===")
    print()
    gm = GardenManager.create_garden_network()
    gm.add_plant("Alice", Plant("Oak Tree", 100))
    gm.add_plant("Alice", FloweringPlant("Rose", 25, "red", "(blooming)"))
    sunflower = PrizeFlower("Sunflower", 50, "yellow", "(blooming)", 10)
    gm.add_plant("Alice", sunflower)
    print()
    gm.help_grow("Alice")
    print()
    gm.report("Alice")
    print()
    gm.common_info()


if __name__ == "__main__":
    main()
