# https://leetcode.com/problems/my-calendar-i

class MyCalendar:
    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.calender :
            if s<end and start<e :
                return False
        self.calender.append([start,end])
        return True
