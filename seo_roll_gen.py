import pandas as pd
import os


rank_read = pd.read_csv("rank.csv")

n = 0
all_arr = []
for api in rank_read["roll"]:
    roll = str(rank_read["roll"][n])
    all_arr.append(roll)
    #print(new_json)
    #generate(new_json)
    #input("nnn")
    print(n)
    n = n +1
new_data = ""

for api2 in all_arr:
    url = "https://hptuexam.web3o.cloud/rank/"+str(api2)+""
    html_data = "<a href='"+str(url)+"'></a>"
    new_data = new_data + html_data


##save the files
file = open("allresultranklist.html","w")
file.write(new_data)
file.close()

