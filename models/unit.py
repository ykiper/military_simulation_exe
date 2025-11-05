from soldier import Soldier

class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier], strike_options: list[StrikeOption]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        self.strike_options = strike_options

    def briefing(self):
        print(f"unit {self.unit_name}. commander details: ")
        self.commander.report()
