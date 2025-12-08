'''Write a program that converts speed in meters per second to speed in kilometers per hour. 
Define a function ms_to_kmh(ms) that returns the calculated speed in km/h. Sample result:

10 m/s = 36 km/h
35 m/s = 126 km/h'''

n1 = int(input("Predksc w metrach na sekunde: "))

converter = lambda ms: ms*3.6
result = converter(n1)
print(f"{n1}m/s = {result}km/h")