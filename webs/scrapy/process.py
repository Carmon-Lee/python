import json

if __name__ == '__main__':

    for i in range(1, 11):
        with open(str(i) + 'jobs.txt', 'r') as f:
            jobs = json.loads(f.readlines()[0])
        with open('jobs_all.txt','a+') as f:
            for job in jobs:
                f.write(json.dumps(job,ensure_ascii=False))
                f.write('\n')

