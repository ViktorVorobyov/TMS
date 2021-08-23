"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""

class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.overal = hours * 60 * 60 + minutes * 60 + seconds

    def __eg__(self, other):
        return self.overal == other.overal

    def __ne__(self, other):
        return self.overal != other.overal

    def __gt__(self, other):
        return self.overal > other.overal

    def __lt__(self, other):
        return self.overal < other.overal

    def __ge__(self, other):
        return self.overal <= other.overal

    def __le__(self, other):
        return self.overal >= other.overal