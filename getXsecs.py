from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import optparse


def printInfo(url):
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(url)
    html = page.read()

    try:
        print '\n[+] Printing cross sections using BeautifulSoup.'
        soup = BeautifulSoup(html)
        xsecs = soup.findAll('a')
        
        returnDict = {}
        for i in xsecs:
            theref = i['href']
            if theref.find('results.html') == -1 or theref.find('decayed') == -1 :
                continue
            runCode = theref.split('_')[1]
            xsec = i.contents[0]
            unc  = i.contents[2]
            returnDict[runCode] = (xsec, unc)
            print runCode, ': ', xsec, ', ', unc, ', '
        return returnDict
    except Exception as i:
        print "Caught error: ", i
        pass
    

def main():
    parser = optparse.OptionParser('Usage%prog ' + '-u <target url>')
    parser.add_option('-u', dest='targetURL', type='string', help='specify target ULR')

    (options, args) = parser.parse_args()

    url = options.targetURL
    if url == None:
        print parser.usage
        exit(0)
    else:
        resultDict = printInfo(url)
        # print resultDict
if __name__ == '__main__':
    main()




