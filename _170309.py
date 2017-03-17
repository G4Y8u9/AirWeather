"""METAR searcher."""
import requests
from bs4 import BeautifulSoup


def getHTMLText(data):
    """Get HTML text."""
    try:
        hd = {'user-agent': 'Chrome/10'}
        url = 'http://www.metcaac.com/hbinfo/app/common/search/' + data
        r = requests.request('POST', url, headers=hd, timeout=10)
        # print(r.url)   # Use for test
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.RequestException:
        """The detail is in func 'getMetar'."""
        return 1
    except():
        """Other exceptions, unlikely to be used."""
        return 2


def parseHTML(html):
    """Get the METAR from HTML text."""
    try:
        soup = BeautifulSoup(html, "html.parser")
        a = soup.find(class_="stationrpt")
        return a.ul.li.string
    except():
        pass


def getMETAR(data):
    """Pack above two funcs."""
    flag = getHTMLText(data)
    if flag is 1:
        """
        If the airport is non-existent, we'll nevet get the htmltext.
        So we need a flag (which is 1 and 2 in this case) to judge
        whether we need to use the second func.
        """
        print('No such airport found!')
    elif flag is 2:
        """Hope never use this line...XD"""
        print('Something wrong happened!')
    else:
        print(parseHTML(getHTMLText(data)))


def main():
    """Main func."""
    airportList = [
        'ZBAA',   # Beijing Capital International Airport
        'ZSPD',   # Shanghai Pudong International Airport
        'ZYTX',   # Shenyang Taoxian International Airport, my hometown XD
        'ABCD'    # A non-existent airport code
        ]
    for each in airportList:
        print('Getting METAR of', each+':')
        getMETAR(each)


main()
