class animal :
    name = color = ""

    def __init__(self, animal_name, animal_color):
        self.name = animal_name
        self.color = animal_color

    def makesound(self, sound):
        print(self.name, "is", sound)


    def eat(self, food):
        print(self.name, "is eating", food)
        
cat = animal("max", "grey")
cat.makesound("meowing")
cat.eat("chicken")

cat = animal("bravo", "yellow")
cat.makesound("barking")
cat.eat("snack")

bird = animal("tweety", "white")
bird.makesound("chirping")
cat.eat("corn")