class Proletariat:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working for the collective!")

class PartyMember(Proletariat):
    def attend_meeting(self):
        print(f"{self.name} attends a party meeting to discuss the revolution.")

class TechnologicalRevolution:
    def __init__(self, name):
        self.name = name

    def innovate(self):
        print(f"{self.name} leads the technological revolution for the people!")

class NationalizeIndustries:
    def __init__(self, industry):
        self.industry = industry

    def Nationalize(self):
        print(f"Comrade Mila nationalizes the {self.industry} industry for the Motherland!")

class RevolutionaryLeader(PartyMember, TechnologicalRevolution):
    def __init__(self, name, revolution_name):
        super().__init__(name)
        self.revolution_name = revolution_name

    def lead_revolution(self):
        print(f"{self.name} is leading the {self.revolution_name} revolution!")

worker1 = Proletariat("Ivan")
party_member1 = PartyMember("Natalia")
tech_leader = TechnologicalRevolution("Sergei")
industry1 = NationalizeIndustries("metal")

worker1.work()
party_member1.attend_meeting()
tech_leader.innovate()
industry1.Nationalize()

leader1 = RevolutionaryLeader("Vladimir", "Digital")
leader1.attend_meeting()
leader1.innovate()
leader1.lead_revolution()