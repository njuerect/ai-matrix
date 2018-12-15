import os
from subprocess import check_output
import numpy as np

count=int(check_output("ls | grep log- | wc -l", shell=True).decode('utf-8'))
log_dir=check_output("ls | grep log", shell=True).decode('utf-8').split()
file_list=check_output("ls log-0", shell=True).decode('utf-8').split()

data=dict()
for logfile in file_list:
    data[logfile]=dict()
    for logdir in log_dir:
        data[logfile][logdir]=[]
        filename=os.path.join(logdir, logfile)
        f=open(filename, 'rt')
        f.readline()
        for line in f:
            data[logfile][logdir].append(float(line.split('\n')[0].split()[-1]))

#print(data['avg_pool.csv'])

data_new=dict()
for logfile in file_list:
    data_new[logfile]=[]
    for logdir in log_dir:
        data_new[logfile].append(data[logfile][logdir])
    data_new[logfile]=np.array(data_new[logfile])

#print(data_new['avg_pool.csv'])

data_median=dict()
for logfile in file_list:
    data_median[logfile]=np.median(data_new[logfile], axis=0)

#print(data_median['avg_pool.csv'])
for logfile in file_list:
    print(logfile+" :")
    print(','.join("%.3f" % x for x in data_median[logfile]))
