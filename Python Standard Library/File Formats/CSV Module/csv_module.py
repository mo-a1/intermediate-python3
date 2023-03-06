import csv

# https://www.youtube.com/watch?v=q5uM4VKywbA&ab_channel=CoreySchafer

with open("OlympicMedals_2020.csv", "r") as file:
    reader = csv.reader(file)
    dict_reader = csv.DictReader(file)

    # for line in reader:
    #     print(line)

    for line in dict_reader:
        print(line)

with open("test_.csv", mode="w", encoding="utf-8", newline="\n") as output:
    # writer = csv.writer(output, delimiter=",")
    # writer.writerow([1, 2, 3])
    dict_writer = csv.DictWriter(output, fieldnames=["one", "two", "three"], delimiter=",")
    dict_writer.writeheader()
    dict_writer.writerow({"one": 1, "two": 2, "three": 3})

