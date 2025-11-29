###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
univslc = university.split()
result=""
for i in range(len(univslc)):
    if univslc[i][0] == univslc[i][0].upper():
        result+=univslc[i][0]
    
print(result)