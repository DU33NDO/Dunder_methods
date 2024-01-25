from __future__ import annotations


class ComplexNumber:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.x} + {self.y}j"

    def __add__(self, new_num: ComplexNumber) -> ComplexNumber:
        result_x = self.x + new_num.x
        result_y = self.y + new_num.y
        sign = "+" if result_y >= 0 else "-"
        return f"{result_x} {sign} {abs(result_y)}j"

    def __sub__(self, new_num: ComplexNumber) -> ComplexNumber:
        result_x = self.x - new_num.x
        result_y = self.y - new_num.y
        sign = "+" if result_y >= 0 else "-"
        return f"{result_x} {sign} {abs(result_y)}j"


a1 = ComplexNumber(3, 5)
a2 = ComplexNumber(5, 8)
print(a1)
print(a1 + a2)
print(a1 - a2)
