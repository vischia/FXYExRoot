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
    

def drawComparison(g1, g2, title, outLabel):

    h1=g1
    h2=g2
    
    h1.SetTitle(title)
    h2.SetTitle(title)

    # Build the comparison plots
    c = ROOT.TCanvas("c", title, 800, 800)
    leg = ROOT.TLegend(0.6,0.1,0.9,0.4)

    h1.SetMaximum(1.2e-05)
    h2.SetMaximum(1.2e-05)
    h1.SetMinimum(1.2e-06)
    h2.SetMinimum(1.2e-06)
    if h1.GetName().find('cepc') != -1:
        h1.SetMaximum(6e-05)
        h1.SetMinimum(1e-06)
    if h2.GetName().find('cepc') != -1:
        h1.SetMaximum(6e-05)
        h1.SetMinimum(1e-06)

    leg.AddEntry(h1, h1.GetName(), "l")
    leg.AddEntry(h2, h2.GetName(), "l")

    h1.Draw("LPA")
    h2.Draw("LP")
    
    leg.Draw()
    c.Print(outLabel+'.png')
    c.Print(outLabel+'.pdf')
    
    
def main():

    ROOT.gROOT.SetBatch()
    print cTerm.GREEN+"Run in batch mode."+cTerm.END
                                                            
    
    histos = {}
    
    histos['bma_cepc'] = ROOT.TGraph(29); histos['bma_cepc'].SetName('bma_cepc'); histos['bma_cepc'].SetTitle('CEPC: sin(#beta-#alpha) = +1')
    histos['bma_ilc' ] = ROOT.TGraph(29); histos['bma_ilc' ].SetName('bma_ilc' ); histos['bma_ilc' ].SetTitle('ILC: sin(#beta-#alpha) = +1' )
    histos['bpa_cepc'] = ROOT.TGraph(29); histos['bpa_cepc'].SetName('bpa_cepc'); histos['bpa_cepc'].SetTitle('CEPC: sin(#beta+#alpha) = +1')
    histos['bpa_ilc' ] = ROOT.TGraph(29); histos['bpa_ilc' ].SetName('bpa_ilc' ); histos['bpa_ilc' ].SetTitle('ILC: sin(#beta+#alpha) = +1' )

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
   
    tanbetaDict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'12':10,'14':11,'16':12,'18':13,'20':14,'22':15,'24':16,'26':17,'28':18,'30':19,'32':20,'34':21,'36':22,'38':23,'40':24,'42':25,'44':26,'46':27,'48':28,'50':29 }
        

    for (tanbeta, collider), (runCode, sinbma, xsec) in scandict.bma.viewitems():
        #printDictEntry(tanbeta, collider, runCode, sinbma, xsec)
        if tanbeta == '1':
            continue
            
        if collider == 'cepc':
            histos['bma_cepc'].SetPoint(tanbetaDict[tanbeta]-1,float(tanbeta), float(xsec))
        elif collider == 'ilc':
            histos['bma_ilc'].SetPoint(tanbetaDict[tanbeta]-1,float(tanbeta), float(xsec))
            
    for (tanbeta, collider), (runCode, sinbma, xsec) in scandict.bpa.viewitems():
        #printDictEntry(tanbeta, collider, runCode, sinbma, xsec)
        if collider == 'cepc':
            histos['bpa_cepc'].SetPoint(tanbetaDict[tanbeta]-1,float(tanbeta), float(xsec))
        elif collider == 'ilc':
            histos['bpa_ilc'].SetPoint(tanbetaDict[tanbeta]-1,float(tanbeta), float(xsec))

    drawComparison(histos['bma_cepc'], histos['bma_ilc' ], "sin(#beta-#alpha) = +1", "bma_comparecolliders" )
    drawComparison(histos['bpa_cepc'], histos['bpa_ilc' ], "sin(#beta+#alpha) = +1", "bpa_comparecolliders" )

    drawComparison(histos['bma_cepc'], histos['bpa_cepc' ], "CEPC", "cepc_comparescenarios" )
    drawComparison(histos['bma_ilc'], histos['bpa_ilc' ], "ILC", "ilc_comparescenarios" )  

if __name__ == '__main__':
    main()
