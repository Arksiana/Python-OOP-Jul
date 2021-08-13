class DecorationRepository:
    def __init__(self):
        self.decorations: list = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        for el in self.decorations:
            if el.name == decoration.name:
                self.decorations.remove(decoration)
                return True
        return False

    def find_by_type(self, decoration_type):
        for el in self.decorations:
            if el.__class__.__name__ == decoration_type:
                return el
        return 'None'

