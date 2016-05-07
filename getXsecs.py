from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import optparse


def parseInfo(url, gluons):
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
            if gluons:
                if theref.find('results.html') == -1 or theref.find('run_') == -1 :
                    continue
            else:
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
    parser.add_option('-g', dest='gluons', action='store_true', help='run on hZ -> bb (h undecayed)')
    (options, args) = parser.parse_args()

    url = options.targetURL
    gluons = options.gluons
    if url == None:
        print parser.usage
        exit(0)
    else:
        resultDict = parseInfo(url, gluons)
        # print resultDict
if __name__ == '__main__':
    main()




