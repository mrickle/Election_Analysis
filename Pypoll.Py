import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
# The data we need to retrieve
# 1. The total number of votes Cast
# 2. A complete list of candiddates who recieved votes
# 3. The percentage of votes each candiate won
# 4 The total number of votes each candiate won
# 5. The winner of the election based on popular vote