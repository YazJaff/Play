class fruit:
    def __init__(self,color,shape):
        self.color=color
        self.shape=shape
    def sayhi(self):
        self.color='Sphere'+self.color
        print(f"Hi.\nI am {self.color}and{self.shape}")       
orange=fruit('Orange','Round')
#orange.sayhi()

