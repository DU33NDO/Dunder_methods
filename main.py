from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, another_point: Point) -> str:
        result_x = self.x + another_point.x
        result_y = self.y + another_point.y
        return f"({result_x}, {result_y})"

    def __sub__(self, another_point: Point) -> Point:
        result_x = self.x - another_point.x
        result_y = self.y - another_point.y
        return f"({result_x}, {result_y})"

    def __eq__(self, another_point: Point) -> bool:
        return self.x == another_point.x and self.y == another_point.y


p1 = Point(5, 0)
p2 = Point(12, 19)
print(str(p1))
print(p1)
print(p1 == p2)
print(p1 + p2)
print(p1 - p2)
