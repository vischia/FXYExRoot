#! /usr/bin/env python

"""
   Script to create histograms and cut flow table for lepton+jets.
   
   Francisco Yumiceva (yumiceva@gmail.com)
   Florida Institute of Technology, 2013  

   Modified by Pietro Vischia (pietro.vischia@gmail.com) for hZ analysis in 2HDM with Rui Santos

"""

class cTerm:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'                              

# External packages
import sys
import os
import math
import re
# Check if pyROOT is available
try:
    #from ROOT import *
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
    
ROOT.PyConfig.IgnoreCommandLineOptions = True
from optparse import OptionParser

def main(argv = None):
    if argv == None:
        argv = sys.argv[1:]
    # OPTIONS
    usage = "usage: %prog [options]\n This script analyzes madgraph trees."
    parser = OptionParser(usage)
    parser.add_option("-b", "--batch",
                      action="store_true",
                      help="run ROOT in batch mode.")
    parser.add_option("-s", "--sample",
                      default="madgraph",
                      help="input samples. The options are: madgraph or whizard [default: %default]")
    parser.add_option("-i", "--inputDir", default="", help="Input directory")
    parser.add_option("-g", "--gluons", default=False, help="h to gluons", action="store_true")
    parser.add_option("-o", "--outputDir", default="plots", help="Output directory")
    parser.add_option("-q","--quit",
                      action="store_true",
                      help="quit after reading tree otherwise prompt for keyboard to continue.")
    (options, args) = parser.parse_args(sys.argv[1:])
    #print options
    #print args
    return options

if __name__ == '__main__':

    options = main()
    
    if options.batch:
        ROOT.gROOT.SetBatch()
        print cTerm.GREEN+"Run in batch mode."+cTerm.END
    
    # Load ROOT libraries
    ROOT.gSystem.Load('/home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/ExRootAnalysis/libExRootAnalysis.so')

    # Define the list of histograms
    # Book histograms
    hList = ['PID', 'Status',
             #'Nparticles', 'ProcessID', 'Weight', 'CouplingQED', 'CouplingQCD',
             'num_e', 'num_h', 'num_Z', 'num_b',
             'e_pt', 'e_eta', 'e_phi', 'e_m', 'e_spin', 'h_pt', 'h_eta', 'h_phi', 'h_m', 'h_spin', 'Z_pt', 'Z_eta', 'Z_phi', 'Z_m', 'Z_spin', 'truerecoh_pt', 'truerecoh_eta', 'truerecoh_phi', 'truerecoh_m', 'truerecoh_deltapt', 'truerecoh_deltaeta', 'truerecoh_deltaphi', 'truerecoh_deltam', 'truerecoh_resm', 'truerecoZ_pt', 'truerecoZ_eta', 'truerecoZ_phi', 'truerecoZ_m', 'truerecoZ_deltapt', 'truerecoZ_deltaeta', 'truerecoZ_deltaphi', 'truerecoZ_deltam', 'truerecoZ_resm', 'recoh_pt', 'recoh_eta', 'recoh_phi', 'recoh_m', 'recoh_deltapt', 'recoh_deltaeta', 'recoh_deltaphi', 'recoh_deltam', 'recoh_resm', 'recoZ_pt', 'recoZ_eta', 'recoZ_phi', 'recoZ_m', 'recoZ_deltapt', 'recoZ_deltaeta', 'recoZ_deltaphi', 'recoZ_deltam', 'recoZ_resm', 'inclusive_b_m', 'inclusive_b_pt', 'inclusive_b_eta', 'inclusive_b_phi']
    
    os.system('mkdir -p {outputDir}'.format(outputDir=options.outputDir))

    # Open input files

    initialDirectory='../4b/'
    if options.gluons:
        initialDirectory='../'

    print 'Fetching plots from {initialDirectory}'.format(initialDirectory=initialDirectory)
    plus  = ROOT.TFile("{initialDirectory}Rui_cepc_bb/Events/run_01_decayed_1/results_anal.root".format(initialDirectory=initialDirectory), "READ")
    minus = ROOT.TFile("{initialDirectory}Rui_cepc_bb/Events/run_05_decayed_1/results_anal.root".format(initialDirectory=initialDirectory), "READ")
    
    for h in hList:
        h_plus = plus.Get(h)
        print "Processing histogram ", h
        print type(h_plus)
        h_plus.SetName(h_plus.GetName()+'plus')
        h_minus = minus.Get(h)
        h_minus.SetName(h_minus.GetName()+'minus')

        h_plus.SetLineColor(1)
        h_minus.SetLineColor(2)

        h_plus.SetLineWidth(3)
        h_minus.SetLineWidth(3)

        c = ROOT.TCanvas("c", "c", 800,800)
        c.cd()
        h_plus.SetMaximum(2*h_plus.GetMaximum())
        h_plus.Draw("hist")
        h_minus.Draw("samehist")
        c.Print('{outputDir}/{h}.png'.format(outputDir=options.outputDir,h=h))
        

    print cTerm.GREEN+"Output file name: "+outname+cTerm.END

    if options.quit == False:
        # Wait
        rep = ''
        while not rep in [ 'q', 'Q', '.q', 'qq' 'p']:
            rep = raw_input( '\nenter: ["q",".q" to quit] ["p" or "print" to print all canvas]: ' )
            if 0<len(rep):
                if rep=='quit': rep = 'q'
            #if rep=='p' or rep=='print':

    #del(treeReader)
    #del(chain)
    #del treeReader
    print cTerm.GREEN+"done."+cTerm.END
