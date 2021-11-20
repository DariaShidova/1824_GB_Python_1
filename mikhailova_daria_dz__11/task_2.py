class Trapping:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    @staticmethod
    def check(divisible, divisor):
        if divisor == 0:
            return 'на ноль делить нельзя!'
        else:
            return divisible / divisor


print(Trapping.check(12, 0))
print(Trapping.check(12, 6))

