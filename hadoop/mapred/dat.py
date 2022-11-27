import os 
import time
import json

for file in os.path('/user/hduser/input'):
    os.system(f"mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/{file}.txt -output /user/hduser/output/{file} -mapper ./mapper.py -reducer ./reducer.py")

time.sleep(3)
count=0
output=dict()
for file in os.path('/user/hduser/output'):
    count+=1
    for line in file:
        word,n = line.split("\t",1)
        t = {count: int(n)}
        print(t)
        if word not in output:
            output = dict([(word,t)])
        else:
            output[word].update(t)

with open('/home/hduser/examples/output.json',"w",encoding="utf-8") as dat:
    json.dump(output,dat)
