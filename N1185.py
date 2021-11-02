import calendar 
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        days=["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        for i in range(1971, year):
            if calendar.isleap(i):
                day+=366
            else:
                day+=365
        for i in range(1,month):
            day+=months.get(i)
            
        if calendar.isleap(year) and month>2:
            day+=1
        day-=1
        return days[day%7]
        
                
