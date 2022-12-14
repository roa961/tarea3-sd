import os 
import time
import json
from pathlib import Path
count=0
count1=0
files = Path('/user/hduser/input').glob('*')
for file in files:
    count1+=1
    os.system(f"mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/{count1} -mapper ./mapper.py -reducer ./reducer.py")
    
time.sleep(10)

output=dict()

for i in range(1,10):
    with open(f'/user/hduser/output/{i}',"r") as file:
        for line in file:
            word,n = line.split("\t",1)
            t = {count: int(n)}
            print(t)
            if word not in output:
                output = dict([(word,t)])
            else:
                output[word].update(t)

with open('/usr/local/bin/output.json',"w",encoding="utf-8") as dat:
    json.dump(output,dat)
