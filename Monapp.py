
import psutil
import schedule
import datetime
import time
import configparser
import psutil

config = configparser.ConfigParser()

config.read('config.ini')
output = config.get('common', 'output')
interval = config.get('common', 'interval')

snapshot_id = 0

class monitor:
    def __init__(self):
        tm = time.time()
        self.cpu = ('CPU load: '+str(psutil.cpu_percent(0, 0))+' %')
        self.vm = ('VM usage: '+str((psutil.virtual_memory().used/1024/1024).__round__(2))+' MB')
        self.swap = ('SWAP usage: '+str((psutil.swap_memory().used/1024/1024).__round__(2))+' MB')
        self.net_s = ('Network (SEND: '+str((psutil.net_io_counters(pernic=False)[0]/1024/1024).__round__(2))+' MB')
        self.net_r = ('Network (RECEIVED): ' + str((psutil.net_io_counters(pernic=False)[1] / 1024 / 1024).__round__(2))+' MB')
        self.timestamp = datetime.datetime.fromtimestamp(tm).strftime('%Y-%m-%d %H:%M:%S')

class text (monitor):

    def __init__(self):
        super().__init__()

    def sumup(self, filename = 'report.txt'):

        global snap_id
        snap_id += 1
        f = open(filename, 'a+')
        f.write('SNAPSHOT {0}: {1}'.format(snap_id, self.timestamp))
        f.write('\n' + '===========================================================')
        f.write('\n' + self.cpu)
        f.write('\n' + self.vm)
        f.write('\n' + self.swap)
        f.write('\n' + self.net_s)
        f.write('\n' + self.net_r + '\n'+'\n')
        f.close()

def output():
    if output == 'txt':
        out_text = text()
        out_text.sumup()
    else:
        quit()


schedule.every(int(interval)).minutes.do(out)

while True:
    schedule.run_pending()
