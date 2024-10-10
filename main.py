class ClassOne:
    def __init__(self, attribute1):
        self.attribute1 = attribute1

class ClassTwo:
    def __init__(self, attribute2):
        self.attribute2 = attribute2


class ClassThree(ClassOne):
    def __init__(self, attribute1, attribute3):
        super().__init__(attribute1)
        self.attribute3 = attribute3

instance_one = ClassOne("1")
instance_two = ClassTwo("2")
instance_three = ClassThree("1", "3")

print(instance_one.attribute1)
print(instance_two.attribute2)
print(instance_three.attribute1, instance_three.attribute3)

# Я так зрозумів домашку не знаю правильно це чи ні