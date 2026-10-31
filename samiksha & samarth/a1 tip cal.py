bill = 84.50
tip_percent = 18
people = 4

tip = (round(bill*tip_percent/100, 2))
total = (round(bill+tip, 2))
per_person =(round(total/people, 2))

print("Tip", tip)
print("Total", total)
print("Per_person", per_person)
