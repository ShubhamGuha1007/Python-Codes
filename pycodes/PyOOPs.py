class Pokemon:
    def __init__(self,name,move):
        self.name=name
        self.move=move
    def call(self):
        print("hey ",self.name)
    def action(self):
        print(" \n Use",self.move)
pokemon1=Pokemon('Pikachu','Thunderbolt')
pokemon2=Pokemon('Gliscor','Rock Slide')


pokemon1.call()
pokemon1.action()
pokemon2.call()
pokemon2.action()