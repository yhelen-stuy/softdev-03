import random
def read_occupations():
    # Read the file
    # 'U' is the universal newline (in case the csv file was made in Windows)
    source = open('occupations.csv', 'rU')
    # Strip of newlines at the beginning of end of file before splitting/parsing
    lines = source.read().strip('\n').split('\n')
    source.close()
    csv_dict = {}
    # Remove the title line
    lines.pop(0)
    for line in lines:
        # Check if the job title includes commas and if so account for it
        if line[0:1] is '"':
            # Find the second quote
            end_quote = line[1:].find('"') + 1
            # Define the list accordingly
            fields = [line[1:end_quote], line[end_quote+2:]]
        else:
            fields = line.split(',')
        csv_dict[fields[0]] = float(fields[1])
    return csv_dict

def random_profession(professions):

occ = read_occupations()
for x in occ:
    print x + "," + str(occ[x])
