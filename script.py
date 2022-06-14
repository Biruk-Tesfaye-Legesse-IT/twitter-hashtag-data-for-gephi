import codecs
import csv
import json
import re


def sourceDestinationFormatter(hashTagsFilePath):
    csvFile = open('s-d.csv', 'a')
    csvWriter = csv.writer(csvFile)

    types_of_encoding = ["utf8"]
    for encoding_type in types_of_encoding:
        with codecs.open(hashTagsFilePath, encoding="utf8", errors='replace') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter='\n')
            print("Here")
            for row in csv_reader:
                for rowTwo in row:
                    for sourceTag in eval(rowTwo):
                        for destinationTag in eval(rowTwo):
                            # if not the same hash
                            if(sourceTag['text'] is not destinationTag['text']):
                                if(bool(re.match('^[a-zA-Z0-9]*$',sourceTag['text']))==True):
                                    if(bool(re.match('^[a-zA-Z0-9]*$',destinationTag['text']))==True):

                                        csvWriter.writerow(
                                            [str(sourceTag['text']).encode('utf-8', 'ignore').decode("utf8", "ignore"), str(destinationTag['text']).encode('utf-8', 'ignore').decode("utf8", "ignore")])


def weightCounter():
    all_edges = []

    csvFile = open('final.csv', 'a')

    csvWriter = csv.writer(csvFile)

    csvWriter.writerow(
        ["Source", "Target", "Weight", "Type"])

    types_of_encoding = ["utf8"]
    for encoding_type in types_of_encoding:
        with codecs.open("./s-d.csv", encoding=encoding_type, errors='replace') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter='\n')
            for row in csv_reader:
                if(len(row) > 0):
                    sourceTag = row[0].split(",")[0]
                    destinationTag = row[0].split(",")[1]

                    all_edges.append((sourceTag, destinationTag))

    for edge in all_edges:
        count = all_edges.count(edge) + all_edges.count((edge[1], edge[0]))
        csvWriter.writerow(
            [str(edge[0]), str(edge[1]), count, "undirected"])


sourceDestinationFormatter("./tweets5.csv")
weightCounter()
