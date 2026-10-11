class language:
    def __init__(self, popularity, speed , users):
        self.popularity = popularity
        self.speed = speed
        self.users = users

    def liked_by_programmers(self):
        return True
    
class swift(language):
    def __init__(self, popularity, speed, users):
        super().__init__(popularity, speed, users)

        def accuracy(self):
            return True

class javascript(language):
    def __init__(self, popularity, speed, users):
        super().__init__(popularity, speed, users)

        def debugging_ability(self):
            return True
        
class rust(language):
    def __init__(self, popularity, speed, users):
        super().__init__(popularity, speed, users)

class superprogrammer(swift, javascript):
    def __init__(self, popularity, speed, users):
        super().__init__(popularity, speed, users)

ale = superprogrammer('ale', 300, 500000)
print(ale.popularity,ale.speed,ale.users)
print(ale.liked_by_programmers())
# print(ale.syntax())