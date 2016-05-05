#! /usr/bin/env python

import sys

from cTerm import *
import scandict

try:
    import ROOT
    print cTerm.GREEN+"ROOT module imported"+cTerm.END
except:
    print cTerm.RED+"\nError: Cannot load PYROOT, make sure you have setup ROOT in the path"
    print "and pyroot library is also defined in the variable PYTHONPATH, try:\n"+cTerm.END
    if (os.getenv("PYTHONPATH")):
        print " setenv PYTHONPATH ${PYTHONPATH}:$ROOTSYS/lib\n"
    else:
        print " setenv PYTHONPATH $ROOTSYS/lib\n"
    print "Exit now\n"
    sys.exit()



def printDictEntry(tanbeta, collider, runCode, sinbma, xsec):
    print "---------------------------------------"
    print 'Tanbeta: {tanbeta}, Collider: {collider}, RunCode: {runCode}, Sinbma: {sinbma}, Xsec: {xsec}'.format(tanbeta=tanbeta, collider=collider, runCode=runCode, sinbma=sinbma, xsec=xsec)
    

def drawComparison(h1, h2, title, outLabel):

    g1 = ROOT.TGraph(h1)
    g2 = ROOT.TGraph(h2)
    
    # Build the comparison plots
    c = ROOT.TCanvas("c", "c", 800, 800)
    leg = ROOT.TLegend(0.8,0.8,0.9,0.9)

    c.cd()
    c.SetTitle(title)
    g1.SetMaximum(10*g1.GetMaximum())

    leg.AddEntry(g1, g1.GetName(), "l")
    leg.AddEntry(g2, g2.GetName(), "l")
    
    g1.Draw("pal")
    g2.Draw("pal")

    leg.Draw()
    c.Print(outLabel+'.png')
    c.Print(outLabel+'.pdf')
    
    
def main():

    histos = {}
    
    histos['bma_cepc'] = ROOT.TH1F('bma_cepc', 'CEPC: sin(#beta-#alpha) = +1', 51, 0., 51.)
    histos['bma_ilc' ] = ROOT.TH1F('bma_ilc' , 'ILC: sin(#beta-#alpha) = +1' , 51, 0., 51.)
    histos['bpa_cepc'] = ROOT.TH1F('bpa_cepc', 'CEPC: sin(#beta+#alpha) = +1', 51, 0., 51.)
    histos['bpa_ilc' ] = ROOT.TH1F('bpa_ilc' , 'ILC: sin(#beta+#alpha) = +1' , 51, 0., 51.)

    histos['bma_cepc'].SetLineWidth(3)
    histos['bma_ilc' ].SetLineWidth(3)
    histos['bpa_cepc'].SetLineWidth(3)
    histos['bpa_ilc' ].SetLineWidth(3)

    histos['bma_cepc'].SetLineColor(1)
    histos['bma_ilc' ].SetLineColor(1)
    histos['bpa_cepc'].SetLineColor(2)
    histos['bpa_ilc' ].SetLineColor(2)

    histos['bma_cepc'].SetLineStyle(1)
    histos['bma_ilc' ].SetLineStyle(2)
    histos['bpa_cepc'].SetLineStyle(1)
    histos['bpa_ilc' ].SetLineStyle(2)
   
    
    for (tanbeta, collider), (runCode, sinbma, xsec) in scandict.bma.viewitems():
        #printDictEntry(tanbeta, collider, runCode, sinbma, xsec)
        if collider is 'cepc':
            histos['bma_cepc'].Fill(float(tanbeta), float(xsec))
        elif collider is 'ilc':
            histos['bma_ilc'].Fill(float(tanbeta), float(xsec))

    for (tanbeta, collider), (runCode, sinbma, xsec) in scandict.bpa.viewitems():
        #printDictEntry(tanbeta, collider, runCode, sinbma, xsec)
        if collider is 'cepc':
            histos['bpa_cepc'].Fill(float(tanbeta), float(xsec))
        elif collider is 'ilc':
            histos['bpa_ilc'].Fill(float(tanbeta), float(xsec))


    drawComparison(histos['bma_cepc'], histos['bma_ilc' ], "sin(#beta-#alpha) = +1", "bma_comparecolliders" )
    drawComparison(histos['bpa_cepc'], histos['bpa_ilc' ], "sin(#beta+#alpha) = +1", "bpa_comparecolliders" )

    drawComparison(histos['bma_cepc'], histos['bpa_cepc' ], "CEPC", "cepc_comparescenarios" )
    drawComparison(histos['bma_ilc'], histos['bpa_ilc' ], "ILC", "cepc_comparescenarios" )  

if __name__ == '__main__':
    main()

