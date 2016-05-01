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

    # Create output root file
    outname = '{outDir}/results_anal.root'.format(outDir=options.inputDir)
    
    outFile = ROOT.TFile(outname,"RECREATE")
    
    # Create chain of root trees
    chain = ROOT.TChain("LHEF")
    maxEntries = -1
    # MG files
    print "Use dataset: "+options.sample

    chain.Add('{inputDir}/unweighted_events.root'.format(inputDir=options.inputDir))
    
    # setup ntuple object
    treeReader = ROOT.ExRootTreeReader(chain)
    # number of entries
    numberOfEntries = treeReader.GetEntries()
    print "Total number of entries to be processed: " + str(numberOfEntries)

    # Get pointers to branches used in this analysis
    Particles = treeReader.UseBranch("Particle")

    Nparticles  = treeReader.UseBranch("Nparticles")
    ProcessID   = treeReader.UseBranch("ProcessID")
    Weight      = treeReader.UseBranch("Weight")
    CouplingQED = treeReader.UseBranch("CouplingQED")
    CouplingQCD = treeReader.UseBranch("CouplingQCD")
    


    
    # Book histograms
    h_nocut = {}
    h_cut = {}
    h_nocut['PID']        = ROOT.TH1F("PID","Particle ID",50,-25,25)
    h_nocut['Status']     = ROOT.TH1F("Status","Particle status", 6, -3., 3.)
    h_nocut['Nparticles'] = ROOT.TH1F("Nparticles","Number of particles", 26, -1., 25.); 
    h_nocut['ProcessID']  = ROOT.TH1F("ProcessID", "Process ID", 25, 0., 25.);
    h_nocut['Weight']     = ROOT.TH1F("Weight", "Event weight", 100, 0., 0.01);
    h_nocut['CouplingQED']= ROOT.TH1F("CouplingQED", "QED coupling", 100, 0., 0.1);
    h_nocut['CouplingQCD']= ROOT.TH1F("CouplingQCD", "QCD coupling", 100, 0., 0.1);

    # Gen e
    h_nocut['e_pt']   = ROOT.TH1F("e_pt",  "e p_{T} [GeV]",100,0,200)
    h_nocut['e_eta']  = ROOT.TH1F("e_eta", "e #eta",100,-5,5)
    h_nocut['e_phi']  = ROOT.TH1F("e_phi", "e #phi",80,-3.2,3.2)
    h_nocut['e_m']    = ROOT.TH1F("e_m",   "e mass [GeV]",50,150,200)
    h_nocut['e_spin'] = ROOT.TH1F("e_spin","e spin [GeV]",50,150,200)

    # Gen h
    h_nocut['h_pt']   = ROOT.TH1F("h_pt","h p_{T} [GeV]",100,0,200)
    h_nocut['h_eta']  = ROOT.TH1F("h_eta","h #eta",100,-5,5)
    h_nocut['h_phi']  = ROOT.TH1F("h_phi","h #phi",80,-3.2,3.2)
    h_nocut['h_m']    = ROOT.TH1F("h_m","h mass [GeV]",50,150,200)
    h_nocut['h_spin'] = ROOT.TH1F("h_spin","h spin [GeV]",50,150,200)

    # Gen Z
    h_nocut['Z_pt']   = ROOT.TH1F("Z_pt","Z p_{T} [GeV]",100,0,200)
    h_nocut['Z_eta']  = ROOT.TH1F("Z_eta","Z #eta",100,-5,5)
    h_nocut['Z_phi']  = ROOT.TH1F("Z_phi","Z #phi",80,-3.2,3.2)
    h_nocut['Z_m']    = ROOT.TH1F("Z_m","Z mass [GeV]",50,150,200)
    h_nocut['Z_spin'] = ROOT.TH1F("Z_spin","Z spin [GeV]",50,150,200)

    # Gen h from its b daughters
    h_nocut['truerecoh_pt']  = ROOT.TH1F("truerecoh_pt", "Reco h (from daughters) p_{T} [GeV]",100,0,200)
    h_nocut['truerecoh_eta'] = ROOT.TH1F("truerecoh_eta","Reco h (from daughters) #eta",100,-5,5)
    h_nocut['truerecoh_phi'] = ROOT.TH1F("truerecoh_phi","Reco h (from daughters) #phi",80,-3.2,3.2)
    h_nocut['truerecoh_m']   = ROOT.TH1F("truerecoh_m","Reco h (from daughters) mass [GeV]",50,150,200)

    h_nocut['truerecoh_deltapt']  = ROOT.TH1F("truerecoh_deltapt", "Reco h (from daughters) #Delta p_{T} [GeV]",100,0,200)
    h_nocut['truerecoh_deltaeta'] = ROOT.TH1F("truerecoh_deltaeta","Reco h (from daughters) #Delta #eta",100,-5,5)
    h_nocut['truerecoh_deltaphi'] = ROOT.TH1F("truerecoh_deltaphi","Reco h (from daughters) #Delta #phi",80,-3.2,3.2)
    h_nocut['truerecoh_deltam']   = ROOT.TH1F("truerecoh_deltam",  "Reco h (from daughters) #Delta mass [GeV]",50,150,200)
    h_nocut['truerecoh_resm']     = ROOT.TH1F("truerecoh_resm",    "Reco h (from daughters) mass resolution [GeV]",100,-50,50)

    
    # Gen Z from its b daughters
    h_nocut['truerecoZ_pt']  = ROOT.TH1F("truerecoZ_pt", "Reco Z (from daughters) p_{T} [GeV]",100,0,200)
    h_nocut['truerecoZ_eta'] = ROOT.TH1F("truerecoZ_eta","Reco Z (from daughters) #eta",100,-5,5)
    h_nocut['truerecoZ_phi'] = ROOT.TH1F("truerecoZ_phi","Reco Z (from daughters) #phi",80,-3.2,3.2)
    h_nocut['truerecoZ_m']   = ROOT.TH1F("truerecoZ_m",  "Reco Z (from daughters) mass [GeV]",50,150,200)

    h_nocut['truerecoZ_deltapt']  = ROOT.TH1F("truerecoZ_deltapt", "Reco Z (from daughters) #Delta p_{T} [GeV]",100,0,200)
    h_nocut['truerecoZ_deltaeta'] = ROOT.TH1F("truerecoZ_deltaeta","Reco Z (from daughters) #Delta #eta",100,-5,5)
    h_nocut['truerecoZ_deltaphi'] = ROOT.TH1F("truerecoZ_deltaphi","Reco Z (from daughters) #Delta #phi",80,-3.2,3.2)
    h_nocut['truerecoZ_deltam']   = ROOT.TH1F("truerecoZ_deltam",  "Reco Z (from daughters) #Delta mass [GeV]",50,150,200)
    h_nocut['truerecoZ_resm']     = ROOT.TH1F("truerecoZ_resm",    "Reco Z (from daughters) mass resolution [GeV]",100,-50,50)

    # Reco h from chosen bs
    h_nocut['recoh_pt']  = ROOT.TH1F("recoh_pt", "Reco h (from assignment) p_{T} [GeV]",100,0,200)
    h_nocut['recoh_eta'] = ROOT.TH1F("recoh_eta","Reco h (from assignment) #eta",100,-5,5)
    h_nocut['recoh_phi'] = ROOT.TH1F("recoh_phi","Reco h (from assignment) #phi",80,-3.2,3.2)
    h_nocut['recoh_m']   = ROOT.TH1F("recoh_m",  "Reco h (from assignment) mass [GeV]",50,150,200)

    h_nocut['recoh_deltapt']  = ROOT.TH1F("recoh_deltapt", "Reco h (from assignment) #Delta p_{T} [GeV]",100,0,200)
    h_nocut['recoh_deltaeta'] = ROOT.TH1F("recoh_deltaeta","Reco h (from assignment) #Delta #eta",100,-5,5)
    h_nocut['recoh_deltaphi'] = ROOT.TH1F("recoh_deltaphi","Reco h (from assignment) #Delta #phi",80,-3.2,3.2)
    h_nocut['recoh_deltam']   = ROOT.TH1F("recoh_deltam",  "Reco h (from assignment) #Delta mass [GeV]",50,150,200)
    h_nocut['recoh_resm']     = ROOT.TH1F("recoh_resm",    "Reco h (from assignment) mass resolution [GeV]",100,-50,50)
    
    # Reco Z from chosen bs
    h_nocut['recoZ_pt']  = ROOT.TH1F("recoZ_pt", "Reco Z (from assignment) p_{T} [GeV]",100,0,200)
    h_nocut['recoZ_eta'] = ROOT.TH1F("recoZ_eta","Reco Z (from assignment) #eta",100,-5,5)
    h_nocut['recoZ_phi'] = ROOT.TH1F("recoZ_phi","Reco Z (from assignment) #phi",80,-3.2,3.2)
    h_nocut['recoZ_m']   = ROOT.TH1F("recoZ_m",  "Reco Z (from assignment) mass [GeV]",50,150,200)

    h_nocut['recoZ_deltapt']  = ROOT.TH1F("recoZ_deltapt", "Reco Z (from assignment) #Delta p_{T} [GeV]",100,0,200)
    h_nocut['recoZ_deltaeta'] = ROOT.TH1F("recoZ_deltaeta","Reco Z (from assignment) #Delta #eta",100,-5,5)
    h_nocut['recoZ_deltaphi'] = ROOT.TH1F("recoZ_deltaphi","Reco Z (from assignment) #Delta #phi",80,-3.2,3.2)
    h_nocut['recoZ_deltam']   = ROOT.TH1F("recoZ_deltam",  "Reco Z (from assignment) #Delta mass [GeV]",50,150,200)
    h_nocut['recoZ_resm']     = ROOT.TH1F("recoZ_resm",    "Reco Z (from assignment) mass resolution [GeV]",100,-50,50)
    
    h_nocut['inclusive_b_m']   = ROOT.TH1F("inclusive_b_m",  "Inclusive b mass [GeV]",50,0,10)
    h_nocut['inclusive_b_pt']  = ROOT.TH1F("inclusive_b_pt", "Inclusive b p_{T} [GeV]",100,0,200)
    h_nocut['inclusive_b_eta'] = ROOT.TH1F("inclusive_b_eta","Inclusive b #eta",100,-5,5)
    h_nocut['inclusive_b_phi'] = ROOT.TH1F("inclusive_b_phi","Inclusive b #phi",80,-3.2,3.2)

    
    for key in h_nocut.keys():
        h_cut[key] = h_nocut[key].Clone(h_nocut[key].GetName())
        h_cut[key].Sumw2()
        h_nocut[key].Sumw2()
        h_cut[key].SetTitle( h_cut[key].GetTitle() )
        h_nocut[key].SetTitle( h_nocut[key].GetTitle() )
        
    # Loop over all events
    for entry in xrange(0, numberOfEntries):

        # Load selected branches with data from specified event
        treeReader.ReadEntry(entry)

        if entry%2000 == 0:
            print "entry=",entry
            #### 
            if maxEntries!=-1 and maxEntries < entry:
                print cTerm.GREEN+"This sample has a maximum number of entries to process. Stop now."+cTerm.END
                break
        ## Check ttbar production mechanism
        #ttbarMech = 0
        #if Particles[0].PID == 21 and Particles[1].PID == 21: ttbarMech = 1
        #elif Particles[0].PID == 21 and Particles[1].PID != 21: ttbarMech = 2
        #elif Particles[0].PID != 21 and Particles[1].PID == 21: ttbarMech = 2
        #else: ttbarMech = 3
        #h_nocut['ttbar_prod'].Fill( ttbarMech )
        
        # TRootLHEFParticle
        index = 0
        p4_e = ROOT.TLorentzVector()
        p4_h = ROOT.TLorentzVector()
        p4_Z = ROOT.TLorentzVector()
        p4_truerecoh = ROOT.TLorentzVector()
        p4_truerecoZ = ROOT.TLorentzVector()
        p4_recoh = ROOT.TLorentzVector()
        p4_recoZ = ROOT.TLorentzVector()

        num_e = 0
        num_h = 0
        num_Z = 0
        num_b = 0
        
        for p in Particles:
            index += 1
            
            h_nocut['PID'].Fill( p.PID )
            h_nocut['Status'].Fill( p.Status )
            # MG Status code: -1 initial, 2 intermediate, 1 final

            # Initial state electrons
            if math.fabs(p.PID) == 11 and p.Status == -1:
                h_nocut['e_pt'].Fill( p.PT )
                h_nocut['e_eta'].Fill( p.Eta )
                h_nocut['e_phi'].Fill( p.Phi )
                h_nocut['e_m'].Fill( p.M )
                h_nocut['e_spin'].Fill( p.Spin )
                num_e += 1
                
            # Intermediate state h
            if math.fabs(p.PID) == 25 and p.Status == 2:
                p4_h.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                h_nocut['h_pt'].Fill( p.PT )
                h_nocut['h_eta'].Fill( p.Eta )
                h_nocut['h_phi'].Fill( p.Phi )
                h_nocut['h_m'].Fill( p.M )
                h_nocut['h_spin'].Fill( p.Spin )
                num_h += 1
            # Intermediate state Z
            if math.fabs(p.PID) == 23 and p.Status == 2:
                p4_Z.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                h_nocut['Z_pt'].Fill( p.PT )
                h_nocut['Z_eta'].Fill( p.Eta )
                h_nocut['Z_phi'].Fill( p.Phi )
                h_nocut['Z_m'].Fill( p.M )
                h_nocut['Z_spin'].Fill( p.Spin )
                num_Z += 1
            # Final state b
            if math.fabs(p.PID) == 5 and p.Status == 2:
                h_nocut['inclusive_b_pt'].Fill( p.PT )
                h_nocut['inclusive_b_eta'].Fill( p.Eta )
                h_nocut['inclusive_b_phi'].Fill( p.Phi )
                h_nocut['inclusive_b_m'].Fill( p.M )

                # Build true h from b daughters
                if p.Mother1 != -1:
                    if math.fabs(Particles[p.Mother1].PID) == 25:
                        p4temp = ROOT.TLorentzVector()
                        p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                        p4_truerecoh += p4temp

                # Build true Z from b daughters
                if p.Mother1 != -1:
                    if math.fabs(Particles[p.Mother1].PID) == 23:
                        p4temp = ROOT.TLorentzVector()
                        p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                        p4_truerecoZ += p4temp

                  
        
        # end loop over Particles

        if( Nparticles == index+1 ):
            h_nocut['Nparticles'].Fill( Nparticles )
        else:
            h_nocut['Nparticles'].Fill( -1. )

        h_nocut['ProcessID'].Fill(   ProcessID  )
        h_nocut['Weight'].Fill(      Weight     )
        h_nocut['CouplingQED'].Fill( CouplingQED)
        h_nocut['CouplingQCD'].Fill( CouplingQCD)

        
        # Fill true h from daughters histos
        h_nocut['truerecoh_pt'].Fill(  p4_truerecoh.Pt() )
        h_nocut['truerecoh_eta'].Fill( p4_truerecoh.Eta() )
        h_nocut['truerecoh_phi'].Fill( p4_truerecoh.Phi() )
        h_nocut['truerecoh_m'].Fill(   p4_truerecoh.M() )

        # Fill true Z from daughters histos
        h_nocut['truerecoZ_pt'].Fill(  p4_truerecoZ.Pt() )
        h_nocut['truerecoZ_eta'].Fill( p4_truerecoZ.Eta() )
        h_nocut['truerecoZ_phi'].Fill( p4_truerecoZ.Phi() )
        h_nocut['truerecoZ_m'].Fill(   p4_truerecoZ.M() )

        # Fill deltas between true h from daughters and gen h
        h_nocut['truerecoh_deltapt'].Fill(  p4_truerecoh.Pt()  - p4_h.Pt() )
        h_nocut['truerecoh_deltaeta'].Fill( p4_truerecoh.Eta() - p4_h.Eta())
        h_nocut['truerecoh_deltaphi'].Fill( p4_truerecoh.Phi() - p4_h.Phi())
        h_nocut['truerecoh_deltam'].Fill(   p4_truerecoh.M()   - p4_h.M()  )
        if p4_h.M() != 0:
            h_nocut['truerecoh_resm'].Fill(  ( p4_truerecoh.M()   - p4_h.M()) / p4_h.M()  )

        # Fill deltas between true Z from daughters and gen Z
        h_nocut['truerecoZ_deltapt'].Fill(  p4_truerecoZ.Pt()  - p4_Z.Pt() )
        h_nocut['truerecoZ_deltaeta'].Fill( p4_truerecoZ.Eta() - p4_Z.Eta())
        h_nocut['truerecoZ_deltaphi'].Fill( p4_truerecoZ.Phi() - p4_Z.Phi())
        h_nocut['truerecoZ_deltam'].Fill(   p4_truerecoZ.M()   - p4_Z.M()  )
        if p4_Z.M() != 0:
            h_nocut['truerecoZ_resm'].Fill(   ( p4_truerecoZ.M()   - p4_Z.M()) / p4_Z.M()  )
        

        # Check BR
        BR_code = 0
        if (numElectrons > 1 and numMuons ==0 and numTaus ==0) or \
               (numElectrons ==0 and numMuons > 1 and numTaus ==0) or \
               (numElectrons == 1 and numMuons == 1 and numTaus==0) or \
               (numElectrons ==0 and numMuons ==0 and numTaus > 1) or \
               (numElectrons ==1 and numMuons ==0 and numTaus==1) or \
               (numElectrons ==0 and numMuons==1 and numTaus ==1):
            # Dileptons
            BR_code = 1
        elif numElectrons == 1 and numMuons == 0 and numTaus ==0:
            # e+jets
            BR_code = 2
        elif numElectrons == 0 and numMuons == 1 and numTaus ==0:
            # mu+jets
            BR_code = 3
        elif numElectrons == 0 and numMuons == 0 and numTaus ==0:
            # All jets
            BR_code = 5
        else:
            # tau+jets
            BR_code = 4


            
    # END loop over entries

    outFile.cd()
    for key in h_nocut.keys():
        
        if h_nocut[key].GetEntries() > 0:
            h_nocut[key].Write()
        if h_cut[key].GetEntries() > 0:
            h_cut[key].Write()
        
    outFile.Close()
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
