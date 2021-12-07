class Arm:
    def __str__(self):
        return "armId: " + str(self.id) + " - Name: '" + self.name + "'"

    def __init__(self, id_, features, name):
        self.id = id_
        self.feature = features
        self.name = name
        self.count = 0


class Context:
    def __str__(self):
        return "contextId: " + str(self.id)

    def __init__(self, id_, features):
        self.id = id_
        self.features = features
