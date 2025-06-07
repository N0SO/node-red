"""
Update History:
* Mon Oct 23 2023 Mike Heitmann, N0SO <n0so@arrl.net>
- V0.0.1 - First interation
* Sun Jan 14 2024 Mike Heitmann, N0SO <n0so@arrl.net>
- V0.1.0 - Added relay 3 control for remote on/off of Flex 6300.
* Mon May 27 2024 Mike Heitmann, N0SO <n0so@arrl.net>
- V0.1.1 - Moved switch definitions to __init__.py.      
- Added VALIDSWITCHNAMES as choices for the argparser.
- All because I forgot what I called the switch names!       
* Wed Jun 04 2025 Mike Heitmann, N0SO <n0so@arrl.net>
- V1.0.0 - Updated for Flex 8600 name, 
-          New router drove IP address change.      
"""
VERSION = '1.0.0' 
SWITCH_URL = 'http://192.168.4.67/'
CALLSIGN = 'N0SO'

VALIDSWITCHNAMES = [\
                     '1','flex8600pwr',
                     '3','flex6300pwr',
                     '7','hfantenna',
                     '8','6mantenna',
                     'all'
                   ]
