#!/usr/bin/env python3
import dayutils

def main():

   day1 = datetime.datetime(2015, 1, 1)
   day2 = datetime.datetime(2015, 1, 12)

   x = day_range( day1, day2, datetime.timedelta(1) )

   print (x)

   for i in x:
      print(i)

   print( "week buonds", week_bounds(day1) )
   print( "month buonds", month_bounds(day1) )

   print( "is same month ?", is_same_month(day1, day2) )

   t = datetime.timedelta(seconds=2876324)

   print( "sec2str", sec2str(t.total_seconds()) )


   day1 = datetime.datetime(2015, 3, 3)
   day2 = datetime.datetime(2015, 4, 12)

   x = day_range( day1, day2, datetime.timedelta(2) )

   print("Start", day1)
   print("End", day2)
   print("Years loop")
   for i in x.years():
      print(i)
   print("Months loop")
   for i, j in x.months():
      print(i, j)
   print("Days loop")
   for i, j, k in x.days():
      print(i, j, k)


if __name__ == '__main__':
   main()
