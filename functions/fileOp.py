import csv

def minHeightTree(path):
    spreadsheet = []
    with open(path, 'r') as csv_file:
        file = csv.DictReader(csv_file)
        for row in file:
            spreadsheet.append(dict(row))

    heights = []
    for row in spreadsheet:
        tree_height = row["height"]
        heights.append(tree_height)
    shortest_height = min(heights)
    return shortest_height
