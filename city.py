class City:

    def __init__(self, name, population, factions, wealth, order, defence, strength, diplomacy):
        self.name = name
        self.population = population
        self.factions = factions
        self.wealth = wealth
        self.order = order
        self.defence = defence
        self.strength = strength
        self.diplomacy = diplomacy

    def get_name(self):
        return self.name

    def get_order(self):
        return self.order

    def get_wealth(self):
        return self.wealth

    def description_cite(self):
        print("La cité de" + str(self.name) + " est sympa.")