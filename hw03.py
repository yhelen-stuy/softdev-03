import random
def read_occupations():
    source = open('occupations.csv', 'rU')
    lines = source.read().strip('\n').split('\n')
    source.close()
    csv_dict = {}
    lines.pop(0)
    for line in lines:
        if line[0:1] is '"':
            end_quote = line[1:].find('"') + 1
            fields = [line[1:end_quote], line[end_quote+2:]]
        else:
            fields = line.split(',')
        csv_dict[fields[0]] = float(fields[1])
    return csv_dict

def random_profession(professions):
    

occ = read_occupations()
for x in occ:
    print x + "," + str(occ[x])
