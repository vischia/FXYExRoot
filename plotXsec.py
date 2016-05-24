#! /usr/bin/env python

import sys
import math

from cTerm import *
import scandict as sd


from optparse import OptionParser


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



def printDictEntry(tanbeta, collider, runCode, sinbma, xsec, xsecunc):
    print "---------------------------------------"
    print 'Tanbeta: {tanbeta}, Collider: {collider}, RunCode: {runCode}, Sinbma: {sinbma}, Xsec: {xsec}, XsecUnc: {xsecunc}'.format(tanbeta=tanbeta, collider=collider, runCode=runCode, sinbma=sinbma, xsec=xsec, xsecunc=xsecunc)
    

def drawComparison(g1, g2, title, leg1, leg2, outLabel):

    h1=g1
    h2=g2
    
    h1.SetTitle(title)
    h2.SetTitle(title)

    h1.GetXaxis().SetTitle('tan#beta')
    h1.GetYaxis().SetTitle('#sigma^{2HDM}(ee#rightarrow hZ #rightarrow b#bar{b}b#bar{b})')
    h1.GetYaxis().SetTitleOffset(1.4)
    
    # Build the comparison plots
    c = ROOT.TCanvas("c", title, 800, 800)
    leg = ROOT.TLegend(0.6,0.1,0.9,0.4)

    ROOT.gPad.SetGridx()
    ROOT.gPad.SetGridy()
    
    lowminimum=1.2e-07
    lowmaximum=6.0e-04
    
    if h1.GetName().find('cepc') == -1 and h2.GetName().find('cepc') == -1:
        h1.SetMaximum(1.2e-05)
        h2.SetMaximum(1.2e-05)
        h1.SetMinimum(1.2e-06)
        h2.SetMinimum(1.2e-06)
    if h1.GetName().find('cepc') != -1 and h2.GetName().find('cepc') == -1:
        h1.SetMaximum(lowmaximum)
        h2.SetMaximum(lowmaximum)
        h1.SetMinimum(lowminimum)
        h2.SetMinimum(lowminimum)
        ROOT.gPad.SetLogy()
    if h1.GetName().find('cepc') != -1 and h2.GetName().find('cepc') == -1:
        h1.SetMaximum(lowmaximum)
        h2.SetMaximum(lowmaximum)
        h1.SetMinimum(lowminimum)
        h2.SetMinimum(lowminimum)
        ROOT.gPad.SetLogy()
    if h2.GetName().find('cepc') != -1 and h2.GetName().find('cepc') != -1:
        h1.SetMaximum(6e-05)
        h2.SetMaximum(6e-05)
        h1.SetMinimum(lowminimum)
        h2.SetMinimum(lowminimum)
        #ROOT.gPad.SetLogy()
    if h1.GetName().find('ratio') != -1 or h2.GetName().find('ratio') != -1:
        h1.SetMaximum(0.20)
        h2.SetMaximum(0.20)
        h1.SetMinimum(0.)
        h2.SetMinimum(0.)
        ROOT.gPad.SetLogy()


        
    leg.AddEntry(h1, leg1, "l")
    leg.AddEntry(h2, leg2, "l")

    if h1.GetName().find('ratio') != -1 or h2.GetName().find('ratio') != -1:

        if h1.GetName().find('bpa') != -1:
            h1.Draw("PLA")
        else:
            h1.Draw("PCA")
        if h2.GetName().find('bpa') != -1:
            h2.SetMarkerSize(3)
            h2.Draw("P*")
        else:
            h2.SetMarkerSize(3)
            h2.Draw("P*")

    else:
        h1.Draw("A3")
        h2.Draw("3")
    
    leg.Draw()
    c.Print(options.outputDir+'/'+outLabel+'.png')
    c.Print(options.outputDir+'/'+outLabel+'.pdf')
    


def makeRatio(h1, h2, name):


    print "Processing {h1} and {h2}".format(h1=h1, h2=h2)
    ratio = ROOT.TGraphErrors(29); ratio.SetName(name);
    for ipoint in range(0, 28):
        h1_xval=ROOT.Double(0.)
        h1_yval=ROOT.Double(0.)
        h1.GetPoint(ipoint, h1_xval, h1_yval)
        h1_err=h1.GetErrorY(ipoint)

        h2_xval=ROOT.Double(0.)
        h2_yval=ROOT.Double(0.)
        h2.GetPoint(ipoint, h2_xval, h2_yval)
        h2_err=h2.GetErrorY(ipoint)

        yval = h1_yval/h2_yval if h2_yval != 0 else 0

        yerr = math.sqrt( math.pow(h1_err/h1_yval, 2) + math.pow(h2_err/h2_yval, 2) )  if h2_yval !=0 else 0
        ratio.SetPoint( ipoint, h1_xval, float(yval) )
        ratio.SetPointError( ipoint, 0., float(yerr) )
        if yerr == 0:
            ratio.RemovePoint(ipoint)

            
    ratio.SetLineWidth( h1.GetLineWidth() )
    ratio.SetLineColor( h1.GetLineColor() )
    ratio.SetMarkerColor( h1.GetLineColor() )
    ratio.SetMarkerStyle( 21 )
    ratio.SetFillColor( h1.GetFillColor() )
    ratio.SetLineStyle( h1.GetLineStyle() )

            
    return ratio


    
    
def main(argv = None):
    if argv == None:
        argv = sys.argv[1:]
        
    usage = "usage: %prog [options]\n This script analyzes madgraph trees."
    parser = OptionParser(usage)
    parser.add_option('-b', '--batch',     dest='batch', action="store_true", help='run ROOT in batch mode.')
    parser.add_option('-o', '--outputDir', dest='outputDir', default="plots", help='Output directory')
    parser.add_option('-z', '--zdecay',    dest='zdecay',    help='Z decay mode [bb|mumu]')
    (options, args) = parser.parse_args(sys.argv[1:])
    #print options
    #print args
    return options
 


        

if __name__ == '__main__':


    options = main()


    if options.batch:
        ROOT.gROOT.SetBatch()
        print cTerm.GREEN+"Run in batch mode."+cTerm.END
                                                            
    
    histos = {}
    
    histos['bma_cepc'] = ROOT.TGraphErrors(29); histos['bma_cepc'].SetName('bma_cepc'); histos['bma_cepc'].SetTitle('CEPC: sin(#beta-#alpha) = +1')
    histos['bma_ilc' ] = ROOT.TGraphErrors(29); histos['bma_ilc' ].SetName('bma_ilc' ); histos['bma_ilc' ].SetTitle('ILC: sin(#beta-#alpha) = +1' )
    histos['bpa_cepc'] = ROOT.TGraphErrors(29); histos['bpa_cepc'].SetName('bpa_cepc'); histos['bpa_cepc'].SetTitle('CEPC: sin(#beta+#alpha) = +1')
    histos['bpa_ilc' ] = ROOT.TGraphErrors(29); histos['bpa_ilc' ].SetName('bpa_ilc' ); histos['bpa_ilc' ].SetTitle('ILC: sin(#beta+#alpha) = +1' )

    histos['bma_cepc_scaled'] = ROOT.TGraphErrors(29); histos['bma_cepc_scaled'].SetName('bma_cepc_scaled'); histos['bma_cepc_scaled'].SetTitle('CEPC: sin(#beta-#alpha) = +1')
    histos['bma_ilc_scaled' ] = ROOT.TGraphErrors(29); histos['bma_ilc_scaled' ].SetName('bma_ilc_scaled' ); histos['bma_ilc_scaled' ].SetTitle('ILC: sin(#beta-#alpha) = +1' )
    histos['bpa_cepc_scaled'] = ROOT.TGraphErrors(29); histos['bpa_cepc_scaled'].SetName('bpa_cepc_scaled'); histos['bpa_cepc_scaled'].SetTitle('CEPC: sin(#beta+#alpha) = +1')
    histos['bpa_ilc_scaled' ] = ROOT.TGraphErrors(29); histos['bpa_ilc_scaled' ].SetName('bpa_ilc_scaled' ); histos['bpa_ilc_scaled' ].SetTitle('ILC: sin(#beta+#alpha) = +1' )

    
    histos['bma_cepc'].SetLineWidth(3); histos['bma_cepc_scaled'].SetLineWidth(3)
    histos['bma_ilc' ].SetLineWidth(3); histos['bma_ilc_scaled' ].SetLineWidth(3)
    histos['bpa_cepc'].SetLineWidth(3); histos['bpa_cepc_scaled'].SetLineWidth(3)
    histos['bpa_ilc' ].SetLineWidth(3); histos['bpa_ilc_scaled' ].SetLineWidth(3)

    histos['bma_cepc'].SetLineColor(4); histos['bma_cepc_scaled'].SetLineColor(4)
    histos['bma_ilc' ].SetLineColor(4); histos['bma_ilc_scaled' ].SetLineColor(4)
    histos['bpa_cepc'].SetLineColor(2); histos['bpa_cepc_scaled'].SetLineColor(2)
    histos['bpa_ilc' ].SetLineColor(2); histos['bpa_ilc_scaled' ].SetLineColor(2)

    histos['bma_cepc'].SetFillColor(4); histos['bma_cepc_scaled'].SetFillColor(4)
    histos['bma_ilc' ].SetFillColor(4); histos['bma_ilc_scaled' ].SetFillColor(4)
    histos['bpa_cepc'].SetFillColor(2); histos['bpa_cepc_scaled'].SetFillColor(2)
    histos['bpa_ilc' ].SetFillColor(2); histos['bpa_ilc_scaled' ].SetFillColor(2)
    histos['bma_cepc'].SetLineStyle(1); histos['bma_cepc_scaled'].SetLineStyle(1)
    histos['bma_ilc' ].SetLineStyle(2); histos['bma_ilc_scaled' ].SetLineStyle(2)
    histos['bpa_cepc'].SetLineStyle(1); histos['bpa_cepc_scaled'].SetLineStyle(1)
    histos['bpa_ilc' ].SetLineStyle(2); histos['bpa_ilc_scaled' ].SetLineStyle(2)
   
    tanbetaDict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'12':10,'14':11,'16':12,'18':13,'20':14,'22':15,'24':16,'26':17,'28':18,'30':19,'32':20,'34':21,'36':22,'38':23,'40':24,'42':25,'44':26,'46':27,'48':28,'50':29 }
        


# (scenario, collider, tanbeta) : ( runCode, xsec, xsecUnc, branchingRatio)
    bma = {}
    bpa = {}
    if options.zdecay == 'bb':
        bma = sd.bma_bb
        bpa = sd.bpa_bb
    elif options.zdecay == 'mumu':
        bma = sd.bma_mumu
        bpa = sd.bpa_mumu
    
    
    for (tanbeta, collider), (runCode, sinbma, xsec, xsecunc) in bma.viewitems():
    #printDictEntry(tanbeta, collider, runCode, sinbma, xsec, xsecunc)
        if tanbeta == '1':
            continue
            
        if collider == 'cepc':
            histos['bma_cepc'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xsec))
            histos['bma_cepc'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsecunc))
            (rc, xs, xsunc, br) = sd.gg[('bma','cepc',tanbeta)]
            histos['bma_cepc_scaled'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xs)*float(br))
            histos['bma_cepc_scaled'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsunc)*float(br))
            
        elif collider == 'ilc':
            histos['bma_ilc'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xsec))
            histos['bma_ilc'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsecunc))
            (rc, xs, xsunc, br) = sd.gg[('bma','ilc',tanbeta)]
            histos['bma_ilc_scaled'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xs)*float(br))
            histos['bma_ilc_scaled'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsunc)*float(br))

    for (tanbeta, collider), (runCode, sinbma, xsec, xsecunc) in bpa.viewitems():
        #printDictEntry(tanbeta, collider, runCode, sinbma, xsec, xsecunc)
        if collider == 'cepc':
            histos['bpa_cepc'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xsec))
            histos['bpa_cepc'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsecunc))
            if tanbeta == '2' or tanbeta == '5' or tanbeta == '10':
                (rc, xs, xsunc, br) = sd.gg[('bpa','cepc',tanbeta)]
                histos['bpa_cepc_scaled'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xs)*float(br))
                histos['bpa_cepc_scaled'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsunc)*float(br))

        elif collider == 'ilc':
            histos['bpa_ilc'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xsec))
            histos['bpa_ilc'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsecunc))
            if tanbeta == '2' or tanbeta == '5' or tanbeta == '10':
                (rc, xs, xsunc, br) = sd.gg[('bpa','ilc',tanbeta)]
                histos['bpa_ilc_scaled'].SetPoint(     tanbetaDict[tanbeta]-1, float(tanbeta), float(xs)*float(br))
                histos['bpa_ilc_scaled'].SetPointError(tanbetaDict[tanbeta]-1, 0             , float(xsunc)*float(br))

    drawComparison(histos['bma_cepc'], histos['bma_ilc' ], "sin(#beta-#alpha) = +1", "CEPC", "ILC", options.zdecay+"_bma_comparecolliders" )
    drawComparison(histos['bpa_cepc'], histos['bpa_ilc' ], "sin(#beta+#alpha) = +1", "CEPC", "ILC", options.zdecay+"_bpa_comparecolliders" )

    drawComparison(histos['bma_cepc'], histos['bpa_cepc' ], "CEPC", "sin(#beta-#alpha) = +1", "sin(#beta+#alpha) = +1", options.zdecay+"_cepc_comparescenarios" )
    drawComparison(histos['bma_ilc'], histos['bpa_ilc' ], "ILC", "sin(#beta-#alpha) = +1", "sin(#beta+#alpha) = +1",    options.zdecay+"_ilc_comparescenarios" )  

    drawComparison(histos['bma_cepc'], histos['bma_cepc_scaled'], "CEPC, sin(#beta-#alpha) = +1", "h#rightarrow bb", "h#rightarrow gg", options.zdecay+"_bma_cepc_bbggcomparison" )
    drawComparison(histos['bma_ilc' ], histos['bma_ilc_scaled' ], "ILC, sin(#beta-#alpha) = +1" , "h#rightarrow bb", "h#rightarrow gg", options.zdecay+"_bma_ilc_bbggcomparison" )
    drawComparison(histos['bpa_cepc'], histos['bpa_cepc_scaled'], "CEPC, sin(#beta+#alpha) = +1", "h#rightarrow bb", "h#rightarrow gg", options.zdecay+"_bpa_cepc_bbggcomparison" )
    drawComparison(histos['bpa_ilc' ], histos['bpa_ilc_scaled' ], "ILC, sin(#beta+#alpha) = +1" , "h#rightarrow bb", "h#rightarrow gg", options.zdecay+"_bpa_ilc_bbggcomparison" )

    drawComparison(histos['bma_cepc_scaled'], histos['bpa_cepc_scaled'], "CEPC, h#rightarrow gg", "sin(#beta-#alpha) = +1", "sin(#beta+#alpha) = +1", options.zdecay+"_cepc_gg_comparescenarios")
    drawComparison(histos['bma_ilc_scaled' ], histos['bpa_ilc_scaled' ], "ILC, h#rightarrow gg" , "sin(#beta-#alpha) = +1", "sin(#beta+#alpha) = +1", options.zdecay+"_ilc_gg_comparescenarios")

    
    histos['bma_cepc_ratio'] = makeRatio(histos['bma_cepc'], histos['bma_cepc_scaled'], options.zdecay+"_bma_cepc_ratio")
    histos['bpa_cepc_ratio'] = makeRatio(histos['bpa_cepc'], histos['bpa_cepc_scaled'], options.zdecay+"_bpa_cepc_ratio")
    histos['bma_ilc_ratio' ] = makeRatio(histos['bma_ilc' ], histos['bma_ilc_scaled' ], options.zdecay+"_bma_ilc_ratio")
    histos['bpa_ilc_ratio' ] = makeRatio(histos['bpa_ilc' ], histos['bpa_ilc_scaled' ], options.zdecay+"_bpa_ilc_ratio")

    drawComparison(histos['bma_cepc_ratio'], histos['bpa_cepc_ratio'], "CEPC, h#rightarrow b#bar{b} / h#rightarrow gg", "sin(#beta-#alpha) = +1", "sin(#beta+#alpha) = +1", options.zdecay+"_cepc_ratio_comparescenarios")
    drawComparison(histos['bma_ilc_ratio' ], histos['bpa_ilc_ratio' ], "ILC, h#rightarrow b#bar{b} / h#rightarrow gg" , "sin(#beta-#alpha) = +1", "sin(#beta+#alpha) = +1", options.zdecay+"_ilc_ratio_comparescenarios")
    
