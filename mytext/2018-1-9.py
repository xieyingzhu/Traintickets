"""Train tickets query via command-line.
Usage:
    tickets [-gdtkz] <from> <to> <date>



Options:

   -h,--help   显示帮助菜单

   -g          高铁

   -d          动车

   -t          特快

   -k          快速

   -z          直达



Example:

   tickets 上海 北京 2017-12-05

"""

from docopt import docopt
import requests
from stations import stations



class Tickiets(object):
    def printTrainInfo(self):
        arguments = docopt(__doc__)

        print(arguments['<date>'], arguments['<from>'], arguments['<to>'])

        date = arguments['<date>']

        fromstation = stations.get(arguments['<from>'])

        tostation = stations.get(arguments['<to>'])

        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-12&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=HZH&purpose_codes=ADULT'.format(
            date, fromstation, tostation)

        r = requests.get(url)

        print(url)
        #print(r.json())
        #分析12306中返回列车信息数据

        allresults = r.json()
        allTickets = allresults['data']['result']
        print(len(allTickets),allTickets)
        rows = self.parse_train(allTickets)
        print(rows)

def parse_train(self,allTickets):
    row = []
    for ticket in allTickets:
         trainlist = ticket.split('|')
         trainrow = []
         trainrow.extend(trainlist[3:6])
         trainrow.extend(trainlist[8:11])
         trainrow.extend(trainlist[32:20:-1])
         row.append(trainrow)
    return rows




if __name__ == '__main__':
    Tickiets().printTrainInfo()