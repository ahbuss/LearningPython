import csv

with open("../test.csv", mode='w') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(['One,', 'Two', 'Buckle', 'My', 'Shoe'])
    writer.writerow(["three", "four", "shut" "the", "door"])
    writer.writerow(["five", "six", "pick", "up", "sticks"])