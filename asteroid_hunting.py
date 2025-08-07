import csv
asteroids = []
with open('Asteroids - sheet1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        #print(row)
        asteroids.append(row)
#print(asteroids)
header = asteroids.pop(0)
distances = []

#print(header)

sorted_list = sorted(asteroids, key=lambda x: x[1])

with open('Asteroids - sheet1.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(sorted_list)

print('sorted asteroids based on distance from sun!')


size_list = sorted(asteroids, key = lambda x: x[2], reverse = True)

print('10 largest asteroids are - ')
for i in range(0,10):
    print(size_list[i])

