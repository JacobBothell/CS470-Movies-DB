import csv

#output file for type information
typeF = open("Type.csv", 'w+')
typeCSV = csv.writer(typeF, delimiter=',')
types = set()
#output file for genra information
genra = open("Genra.csv", 'w+')
genraCSV = csv.writer(genra, delimiter= ',')
genras = set()
#output rating for rating information
rating = open("Rating.csv", 'w+')
ratingCSV = csv.writer(rating, delimiter=',')
ratings = set()
#output file for format information
formatF = open("Format.csv", 'w+')
formatCSV = csv.writer(formatF, delimiter=',')
formats = set()
#output file for resource information
resource = open("Resource.csv", 'w+')
resourceCSV = csv.writer(resource, delimiter=',')

file = open("Movies.csv")
reader = csv.reader(file, delimiter=',')

#going through original data file
#get all of the indexed data
for row in reader:
    print(row[3])
    types.add(row[3])
    genras.add(row[4])
    ratings.add(row[5])
    formats.add(row[6])
        
#change indexed data into list
types = list(types)
genras = list(genras)
ratings = list(ratings)
formats = list(formats)

file = open("Movies.csv")
reader = csv.reader(file, delimiter=',')

for row in reader:
    print(row[2])
    #translate the resource information
    resourceCSV.writerow([row[0], row[1], row[2], types.index(row[3]), genras.index(row[4]), ratings.index(row[5]), formats.index(row[6]), row[7]])

ind = 0
for T in types:
    #translate the type
    typeCSV.writerow([ind, T])
    ind += 1
ind = 0
for G in genras:
    #translate the genre
    genraCSV.writerow([ind, G])
    ind += 1
ind = 0
for R in ratings:
    #translate the rating
    ratingCSV.writerow([ind, R])
    ind += 1
ind = 0
for F in formats:
    #translate the format
    formatCSV.writerow([ind, F])
    ind += 1

file.close()
typeF.close()
genra.close()
rating.close()
formatF.close()
