class GameObject:
    name = ""
    appearance = ""
    feel = ""
    smell = ""

    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"
    
    def touch(self):
        return f"You touch at the {self.name}. {self.feel}\n"
    
    def sniff(self):
        return f"You smell at the {self.name}. {self.smell}\n"
    
game_object = GameObject("knife", "some appearance", "some feel", "some smell")

game_object.name = "spoon"
print(game_object.sniff())