#! /usr/bin/env python

"""
   Script to create histograms and cut flow table for lepton+jets.
   
   Francisco Yumiceva (yumiceva@gmail.com)
   Florida Institute of Technology, 2013  

   Modified by Pietro Vischia (pietro.vischia@gmail.com) for hZ analysis in 2HDM with Rui Santos

"""

from cTerm import *

# External packages
import sys
import os
import math
import re

import scandict as sd

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
    parser.add_option("-z", "--zdecay", dest='zdecay', help="z decay [bb|mumu]")
    parser.add_option('-t', '--tanbeta', dest='tanbeta', help='Specify the desired tan(beta) [2 --> 50]')
    parser.add_option('-c', '--collider', dest='collider', help='Specify the desired collider [cepc|ilc]')
    parser.add_option("-o", "--outputDir", default="plots", help="Output directory")
    parser.add_option('-n', '--normalizeToOne', dest='normalizeToOne', action='store_true')
    parser.add_option("-q","--quit",
                      action="store_true",
                      help="quit after reading tree otherwise prompt for keyboard to continue.")
    (options, args) = parser.parse_args(sys.argv[1:])
    #print options
    #print args
    return options

if __name__ == '__main__':

    options = main()


    tanbeta = options.tanbeta
    collider = options.collider
    zdecay = options.zdecay
    normToOne = options.normalizeToOne
    
    if options.batch:
        ROOT.gROOT.SetBatch()
        print cTerm.GREEN+"Run in batch mode."+cTerm.END

    ROOT.gStyle.SetOptStat(0)
        
    # Load ROOT libraries
    ROOT.gSystem.Load('/home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/ExRootAnalysis/libExRootAnalysis.so')

    # Define the list of histograms
    # Book histograms
    hList = ['PID', 'Status',
             #'Nparticles', 'ProcessID', 'Weight', 'CouplingQED', 'CouplingQCD',
             'num_e', 'num_h', 'num_Z', 'num_b',
             'e_pt', 'e_eta', 'e_phi', 'e_m', 'e_spin', 'h_pt', 'h_eta', 'h_phi', 'h_m', 'h_spin', 'Z_pt', 'Z_eta', 'Z_phi', 'Z_m', 'Z_spin', 'truerecoh_pt', 'truerecoh_eta', 'truerecoh_phi', 'truerecoh_m', 'truerecoh_deltapt', 'truerecoh_deltaeta', 'truerecoh_deltaphi', 'truerecoh_deltam', 'truerecoh_resm', 'truerecoZ_pt', 'truerecoZ_eta', 'truerecoZ_phi', 'truerecoZ_m', 'truerecoZ_deltapt', 'truerecoZ_deltaeta', 'truerecoZ_deltaphi', 'truerecoZ_deltam', 'truerecoZ_resm', 'recoh_pt', 'recoh_eta', 'recoh_phi', 'recoh_m', 'recoh_deltapt', 'recoh_deltaeta', 'recoh_deltaphi', 'recoh_deltam', 'recoh_resm', 'recoZ_pt', 'recoZ_eta', 'recoZ_phi', 'recoZ_m', 'recoZ_deltapt', 'recoZ_deltaeta', 'recoZ_deltaphi', 'recoZ_deltam', 'recoZ_resm', 'inclusive_b_m', 'inclusive_b_pt', 'inclusive_b_eta', 'inclusive_b_phi',
             'truerecoh_sumpt',
             # 'truerecoZ_sumpt',
             'recoZ_sumpt',
             #, 'recoh_sumpt'
             'hz_deltaphi', 'truerecohz_deltaphi', 'recohz_deltaphi', 'hz_deltaR', 'truerecohz_deltaR', 'recohz_deltaR',
             'truerecoil', 'recorecoil', 'truealtrecoil', 'recoaltrecoil', 'recoz_acop',
             'truerecoz_internal_deltaphi', 'truerecoz_internal_deltaR', 'truerecoh_internal_deltaphi', 'truerecoh_internal_deltaR', 'recoz_internal_deltaphi', 'recoz_internal_deltaR', 'recoh_internal_deltaphi', 'recoh_internal_deltaR',
             'cut_truerecoil', 'cut_recorecoil', 'cut_truealtrecoil', 'cut_recoaltrecoil', 'cut_recoz_acop', 'cut_truerecoz_internal_deltaphi', 'cut_truerecoz_internal_deltaR', 'cut_truerecoh_internal_deltaphi', 'cut_truerecoh_internal_deltaR', 'cut_recoz_internal_deltaphi', 'cut_recoz_internal_deltaR', 'cut_recoh_internal_deltaphi', 'cut_recoh_internal_deltaR', 'cut_recoh_pt', 'cut_recoh_eta', 'cut_recoh_phi', 'cut_recoh_m', 'cut_recoZ_pt', 'cut_recoZ_eta', 'cut_recoZ_phi', 'cut_recoZ_m', 'cut_recoh_deltapt', 'cut_recoh_deltaeta', 'cut_recoh_deltaphi', 'cut_recoh_deltam', 'cut_recoh_resm', 'cut_recoZ_deltapt', 'cut_recoZ_deltaeta', 'cut_recoZ_deltaphi', 'cut_recoZ_deltam', 'cut_recoZ_resm', 'cut_recoZ_sumpt', 'cut_recoh_sumpt', 'cut_hz_deltaphi', 'cut_truerecohz_deltaphi', 'cut_recohz_deltaphi', 'cut_hz_deltaR', 'cut_truerecohz_delta,R' 'cut_recohz_deltaR'

             
    ]

    logYList = [ 'hz_deltaphi', 'truerecohz_deltaphi', 'recohz_deltaphi', 'hz_deltaR', 'truerecohz_deltaR', 'recohz_deltaR' ]

    
    fullOutputDir = '{outputDir}/{collider}_{tanbeta}_z{zdecay}'.format(outputDir=options.outputDir,collider=collider,tanbeta=tanbeta,zdecay=zdecay)
    os.system('mkdir -p {fullOutputDir}'.format(fullOutputDir=fullOutputDir))

    # Open input files

    initialDirectory='../'

    print 'Fetching plots from {initialDirectory}'.format(initialDirectory=initialDirectory)

    # Dictionary Format: (tanbeta, collider) : (runCode, sinbma, xsec) )
    
    bmad = {}
    bpad = {}
    if zdecay == 'bb':
        bmad = sd.bma_bb
        bpad = sd.bpa_bb
    elif zdecay == 'mumu':
        bmad = sd.bma_mumu
        bpad = sd.bpa_mumu
    
    
    # No madspin anymore
    #print "Opening file {initialDirectory}Rui_cepc_{zdecay}/Events/run_{runCode}_decayed_1/results_anal.root".format(initialDirectory=initialDirectory,runCode=sd.bma[(tanbeta,collider)][0])
    #bma  = ROOT.TFile("{initialDirectory}Rui_cepc_{zdecay}/Events/run_{runCode}_decayed_1/results_anal.root".format(initialDirectory=initialDirectory,runCode=sd.bma[(tanbeta,collider)][0]), "READ")
    #bpa = ROOT.TFile("{initialDirectory}Rui_cepc_{zdecay}/Events/run_{runCode}_decayed_1/results_anal.root".format(initialDirectory=initialDirectory,runCode=sd.bpa[(tanbeta,collider)][0]), "READ")
    print "Opening file {initialDirectory}Rui_cepc_{zdecay}/Events/run_{runCode}/results_anal.root".format(initialDirectory=initialDirectory,zdecay=zdecay,runCode=bmad[('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][0])
    bma  = ROOT.TFile("{initialDirectory}Rui_cepc_{zdecay}/Events/run_{runCode}/results_anal.root".format(initialDirectory=initialDirectory,zdecay=zdecay,runCode=bmad[ ('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][0]), "READ")
    bpa = ROOT.TFile("{initialDirectory}Rui_cepc_{zdecay}/Events/run_{runCode}/results_anal.root".format(initialDirectory=initialDirectory,zdecay=zdecay,runCode=bpad[('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][0]), "READ")

    sm = ROOT.TFile("{initialDirectory}Rui_cepc_sm{zdecay}/Events/run_{runCode}/results_anal.root".format(initialDirectory=initialDirectory,zdecay=zdecay,runCode=sd.sm[('{collider}'.format(collider=collider),'sm{zdecay}'.format(zdecay=zdecay))][0]), "READ")

    bma_xsec = bmad[('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][2]
    bpa_xsec = bpad[('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][2]
    sm_xsec = sd.sm[('{collider}'.format(collider=collider),'sm{zdecay}'.format(zdecay=zdecay))][1]
    
    for h in hList:
        h_bma = bma.Get(h)
        if not h_bma:
            continue
        print "Processing histogram ", h
        print type(h_bma)
        h_bma.SetName(h_bma.GetName()+'bma')
        h_bpa = bpa.Get(h)
        h_bpa.SetName(h_bpa.GetName()+'bpa')

        h_sm = sm.Get(h)
        if h_sm:
            h_sm.SetName(h_sm.GetName()+'sm')
            h_sm.SetLineColor(3)
            h_sm.SetLineWidth(3)
            
        h_bma.SetLineColor(4)
        h_bpa.SetLineColor(2)
        
        
        h_bma.SetLineWidth(3)
        h_bpa.SetLineWidth(3)

        # Normalize to 250 fb-1
        
        
        bma_xsec = bmad[('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][2]
        bpa_xsec = bpad[('{tanbeta}'.format(tanbeta=tanbeta),'{collider}'.format(collider=collider))][2]
        sm_xsec = sd.sm[('{collider}'.format(collider=collider),'sm{zdecay}'.format(zdecay=zdecay))][1]

        print "bma: ", bma_xsec
        print "bpa: ", bpa_xsec
        print "sm: ", sm_xsec
        h_bma.Scale( 250000. * float(bma_xsec) / 1000.)
        h_bpa.Scale( 250000. * float(bpa_xsec) / 1000.)
        if h_sm:
            h_sm.Scale( 250000. * float(sm_xsec) / 1000.)


        print h_bma.Integral()
        print h_bpa.Integral()
        if h_sm:
            print h_sm.Integral()

        if normToOne:
            if h_bma.Integral() != 0:
                h_bma.Scale( 1. / float(h_bma.Integral()) )
            if h_bpa.Integral() != 0:
                h_bpa.Scale( 1. / float(h_bpa.Integral()) )
            if h_sm:
                if h_sm.Integral() != 0:
                    h_sm.Scale( 1. / float(h_sm.Integral()) )
            
        h_comp_bma = ROOT.TH1F()
        h_comp_bpa = ROOT.TH1F()

        if h_bma.GetName().find('truerecoh_sumpt') != -1:
            h_comp_bma=bma.Get('truerecoZ_sumpt')
            h_comp_bma.SetName(h_comp_bma.GetName()+'bma')
            h_comp_bpa=bpa.Get('truerecoZ_sumpt')
            h_comp_bpa.SetName(h_comp_bpa.GetName()+'bpa')
        elif h_bma.GetName().find('recoh_sumpt') != -1 and h_bma.GetName().find('truerecoh_sumpt') == -1:
            h_comp_bma=bma.Get('recoZ_sumpt')
            h_comp_bma.SetName(h_comp_bma.GetName()+'bma')
            h_comp_bpa=bpa.Get('recoZ_sumpt')
            h_comp_bpa.SetName(h_comp_bpa.GetName()+'bpa')

            
        c = ROOT.TCanvas("c", "c", 800,800)
        c.cd()
        h_bma.SetMaximum(2*h_bma.GetMaximum())
        if h_bpa.GetMaximum() > h_bma.GetMaximum():
            h_bma.SetMaximum(2*h_bpa.GetMaximum())
        if h_sm:
            if h_sm.GetMaximum() > h_bma.GetMaximum():
                h_bma.SetMaximum(2*h_sm.GetMaximum())
        h_bma.Draw("hist")
        h_bpa.Draw("samehist")
        if h_sm:
            h_sm.Draw("samehist")

        if h in logYList:
            ROOT.gPad.SetLogy()
        # With SM added, always logy
        ROOT.gPad.SetLogy()
            
        leg = ROOT.TLegend(0.8,0.8,0.99,0.99)
        leg.AddEntry(h_bma, "SM-like", "l")
        leg.AddEntry(h_bpa, "Wrong-sign", "l")
        if h_sm:
            leg.AddEntry(h_sm, "SM backgrounds", "l")
        
        if h_comp_bma.GetName().find('sumpt') != -1:
            h_comp_bma.SetLineColor(1)
            h_comp_bpa.SetLineColor(2)
            h_comp_bma.SetLineWidth(3)
            h_comp_bpa.SetLineWidth(3)
            h_comp_bma.SetLineStyle(2)
            h_comp_bpa.SetLineStyle(2)
            h_comp_bma.Draw("samehist")
            h_comp_bpa.Draw("samehist")

        leg.Draw()
        c.Print('{fullOutputDir}/{h}.png'.format(fullOutputDir=fullOutputDir,h=h))
        c.Print('{fullOutputDir}/{h}.pdf'.format(fullOutputDir=fullOutputDir,h=h))
        
        
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
