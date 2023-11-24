#Drew Remmenga
#Section F
#1 Hour
# Stackoverflow for help with csv reader function
import csv
def read_csv(csv_name):
    with open(csv_name, 'r',encoding='utf-8') as f:
        read = csv.reader(f)
        my_list=list()
        for row in read:
            my_list.append(row)
        return my_list

def stops_by_race(rows, race):
    return stops_by_column(rows, race, 'subject_race')

def stops_by_sex(rows, sex):
    return stops_by_column(rows, sex, 'subject_sex')

def stops_by_column(rows, word, column):
    i = rows[0].index(column)
    if (column == 'ALL'):
        return len(rows)
    answer = 0
    for row in rows:
        if (row[i].strip() == word):
            answer += 1 
    return answer;
