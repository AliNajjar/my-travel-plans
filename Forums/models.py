class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = 0

    def __str__(self):
        return 'Name: {} \nAge: {}'.format(self.name, self.age)


class Post:
    def __init__(self, title, subject):
        self.title = title
        self.subject = subject

    def __str__(self):
        return 'Title: {} \nContent: {}'.format(self.title, self.subject)
