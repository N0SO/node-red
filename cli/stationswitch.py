import requests
from bs4 import BeautifulSoup
from __init__ import VERSION, CALLSIGN, SWITCH_URL

VALIDSWITCHNAMES = [\
                     '1','flex6600pwr',
                     '7','hfantenna',
                     '8','6mantenna',
                     'all'
                   ]


class stationSwitch():

    def __init__(self, switch_url=None, refresh=True):
        if (switch_url):
            self.switch_url = switch_url # URL provided by caller
        else:
            self.switch_url = SWITCH_URL # default URL from __init__
        if (refresh):
            # Fetch and extract initial state by clearing unused relay #5
            self.extractStat(self.fetchStat())
        else:
            #Set initial relay state 
            self.relays = ['0', '0', '0', '0', '0', '0', '0', '0']

    def fetchStat(self, url=None):
        if (url) == None:
            url= self.switch_url + 'FF0500'
        html_text = requests.get(url)
        soup = BeautifulSoup(html_text.text, 'html.parser')
        stat_text=soup.find('p').get_text()
        return stat_text

    def extractStat(self, stat_text):
        temp=stat_text.split('\n')
        relayStat=[]
        relayStat = temp[1].split(':')
        relayStat[1]=relayStat[1].strip()
        relayStat[1]=relayStat[1].replace('  ',' ',8)
        self.relays = relayStat[1].split(' ')
        return self.relays

    def changeStat(self, urlEnd):
        stat_text = self.fetchStat(self.switch_url + urlEnd)
        relays = self.extractStat(stat_text)
        return relays

    def showStat(self):
        print ("""Station Relay Status:
              Relays:             {}
              Flex 6600 Power:    {} 
              HF Antenna Connect: {}
              6M Dipole Select:   {}""".format(self.relays,
                                                self.relays[0],
                                                self.relays[6],
                                                self.relays[7]))
        return True
        
    def _selectSwitch(self, switch):
        if switch in VALIDSWITCHNAMES:
            print('Valid switch: {}.'.format(switch))
            if (switch == '1') or (switch == 'flex6600pwr'):
                relay = 'FF01'
            elif (switch=='7') or (switch == 'hfantenna'):
                relay = 'FF07'
            elif (switch=='8') or (switch == '6mantenna'):
                relay = 'FF08'
            elif (switch == 'all'):
                relay = 'FFE000'
                
        else:
            relay = None
            
        return relay
        
    def closeSwitch(self, switch):
        relay = self._selectSwitch(switch)
        if relay:
            status = self.changeStat(relay+'01')
        else:
            print('{}: Not a valid switch designation.'.format(switch))
            status = None
            
        return status    

    def openSwitch(self, switch):
        relay = self._selectSwitch(switch)
        if relay:
            status = self.changeStat(relay+'00')
        else:
            print('{}: Not a valid switch designation.'.format(switch))
            status = None
            
        return status    




if __name__ == '__main__':
    s=stationSwitch()
    print(s.relays)
    print(s.switch_url)
