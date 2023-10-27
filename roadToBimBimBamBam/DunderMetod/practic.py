#  https://www.geeksforgeeks.org/dunder-magic-methods-python/

class String:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f'Object: {self.string}'

    def __add__(self, other):
        return self.string + other


if __name__ == '__main__':
    string1 = String('sdfsfsdf')
    print(string1 + 'fsffsf')
