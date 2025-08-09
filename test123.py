class Animal:
    def __init__(self):
        self.num_eye = 2


    def breath(self):
        print("inhale")

    def show_eye(self):
        print(f"he has {self.num_eye} eyes")

class Fish(Animal):
    def __init__(self):
        super().__init__()


    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breath()
nemo.show_eye()