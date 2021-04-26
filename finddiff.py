import csv
import sys


def compare():

    if len(sys.argv) < 4:
        print("you must provide  two CSV files and required header value(s)")
        return 1
        sys.exit()
# change to 5 if you want to provide the path for output file. defaults to current dir
    elif len(sys.argv) > 4:
        print("too many arguments")
        return 1
        sys.exit()

    headerValues = []
    masterRows = []
    childRows = []
# store required header values in a list
    matchValues = sys.argv[3].split(',')
    matchvalues_Index = []
    filtered_childRows = []
    diffRows = []
# file1 is master  , file2 is child
    master = sys.argv[1]
    child = sys.argv[2]
# read master file (file1) and get all headerValues
    readcsv(master, True, masterRows, headerValues)

# get index of required matchvalues in headerValues
    for matchvalue in matchValues:
        try:
            matchvalues_Index.append(headerValues[0].index(matchvalue))
        except ValueError:
            print("couldn't find  header values matching the provided values. Hint: headers values are case-sensitive")
            return 1
            sys.exit()

# read child file (file2)
    readcsv(child, False, childRows)
# filter childRows using required header Values (matchValues) index
    filtered_childRows = list(
        map(lambda row: [row[x] for x in matchvalues_Index], childRows))

    for row in masterRows:
        try:
            # filter each row using required header Values (matchValues) index
            filtered_row = list(map(row.__getitem__, matchvalues_Index))
            # if row doesnt exist in child rows ,append it to diffRows[]
            if check(filtered_row, filtered_childRows, matchvalues_Index):
                diffRows.append(row)
        # to handle empty lines
        except IndexError:
            continue

    # write diffrows to a CSV file ,
    # if you want to provide output path
    # if len(sys.argv) == 5:
    #     outputPath = sys.argv[4]
    # else:
    #     outputPath = ".\diff_rows.csv"

    with open(".\diff_rows.csv", "w", newline='') as output:
        csvWriter = csv.writer(output)
        csvWriter.writerows(headerValues)
        csvWriter.writerows(diffRows)


def check(mrow, crows, valuesIndexs):
  # for each master row , check if it exists in child rows, if exists , return false (not different), else return true (different)
    if any(mrow == sublist for sublist in crows):
        return False
    else:
        return True


def readcsv(path, ismaster, rows, headerValues=None):
    # read content of a CSV file ,if file is master (file1):add its header values to headerValues[]
    with open(path, newline='') as csvf:
        csvreader = csv.reader(csvf)
        if ismaster:
            colums = next(csvreader)
            headerValues.append(colums)
        else:
            next(csvreader)
        for row in csvreader:
            rows.append(row)


compare()
