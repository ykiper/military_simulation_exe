

class Agent:
    def __init__(self, codename: str, clearance_level: int):
        self.codename = codename
        self.clearance_level = clearance_level


class Mission:
    def __init__(self, mission_name: str, target: str, assigned_agent: Agent):
        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent

    def briefing(self):
        print(f"mission_name: {self.mission_name}\ntarget: {self.target}\nassigned agent: {self.assigned_agent.codename}")

agent = Agent("dudu", 2)
mission = Mission("oper_x", "Egypt", agent)
mission.briefing()


class MissionManager:
    