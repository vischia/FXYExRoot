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


def deltaPhi(v1, v2):

    M_PI = 3.1415926
    result = v1.Phi() - v2.Phi()
    while (result > M_PI):
        result -= 2*M_PI;
    while (result <= -M_PI):
        result += 2*M_PI;
    return result;

def deltaR(v1, v2):
    
   e1 = v1.Eta();
   e2 = v2.Eta();
   dp=deltaPhi(v1, v2)
   result = (e1-e2)*(e1-e2) + dp*dp
   return result

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

    Event = treeReader.UseBranch("Event")

    #Weight = treeReader.UseBranch("Event.Weight")
    
    #Event_size = treeReader.UseBranch("Event_size")
    #
    #Nparticles  = treeReader.UseBranch('Event.Nparticles')
    #ProcessID   = treeReader.UseBranch('Event.ProcessID')
    #Weight      = treeReader.UseBranch('Event.Weight')
    #CouplingQED = treeReader.UseBranch('Event.CouplingQED')
    #CouplingQCD = treeReader.UseBranch('Event.CouplingQCD')

    
    
    # Book histograms
    h_nocut = {}
    h_cut = {}
    h_nocut['PID']        = ROOT.TH1F("PID","Particle ID",50,-25,25)
    h_nocut['Status']     = ROOT.TH1F("Status","Particle status", 6, -3., 3.)
    h_nocut['Nparticles'] = ROOT.TH1F("Nparticles","Number of particles", 26, -1., 25.); 
    h_nocut['Event_size'] = ROOT.TH1F("Event_size", "Event size", 20, 0., 20.);
    h_nocut['ProcessID']  = ROOT.TH1F("ProcessID", "Process ID", 25, 0., 25.);
    h_nocut['Weight']     = ROOT.TH1F("Weight", "Event weight", 1000, 0., 0.01);
    h_nocut['CouplingQED']= ROOT.TH1F("CouplingQED", "QED coupling", 100, 0., 0.1);
    h_nocut['CouplingQCD']= ROOT.TH1F("CouplingQCD", "QCD coupling", 100, 0., 0.1);

    h_nocut['num_e']  = ROOT.TH1F("num_e", "Number of electrons", 5, 0., 5.);
    h_nocut['num_h']  = ROOT.TH1F("num_h", "Number of h", 5, 0., 5.);
    h_nocut['num_Z']  = ROOT.TH1F("num_Z", "Number of Z", 5, 0., 5.);
    h_nocut['num_b']  = ROOT.TH1F("num_b", "Number of b", 5, 0., 5.);
        

    
    # Gen e
    h_nocut['e_pt']   = ROOT.TH1F("e_pt",  "e p_{T} [GeV]",100,0,500)
    h_nocut['e_eta']  = ROOT.TH1F("e_eta", "e #eta",100,-5,5)
    h_nocut['e_phi']  = ROOT.TH1F("e_phi", "e #phi",80,-3.2,3.2)
    h_nocut['e_m']    = ROOT.TH1F("e_m",   "e mass [GeV]",200,0.,200.)
    h_nocut['e_spin'] = ROOT.TH1F("e_spin","e spin [GeV]",6,-3.,3.)

    
    # Gen h
    h_nocut['h_pt']   = ROOT.TH1F("h_pt","h p_{T} [GeV]",100,0,500)
    h_nocut['h_eta']  = ROOT.TH1F("h_eta","h #eta",100,-5,5)
    h_nocut['h_phi']  = ROOT.TH1F("h_phi","h #phi",80,-3.2,3.2)
    h_nocut['h_m']    = ROOT.TH1F("h_m","h mass [GeV]",200,0.,200)
    h_nocut['h_spin'] = ROOT.TH1F("h_spin","h spin [GeV]",6,-3.,3.)

    # Gen Z
    h_nocut['Z_pt']   = ROOT.TH1F("Z_pt","Z p_{T} [GeV]",100,0,500)
    h_nocut['Z_eta']  = ROOT.TH1F("Z_eta","Z #eta",100,-5,5)
    h_nocut['Z_phi']  = ROOT.TH1F("Z_phi","Z #phi",80,-3.2,3.2)
    h_nocut['Z_m']    = ROOT.TH1F("Z_m","Z mass [GeV]",200,0.,200)
    h_nocut['Z_spin'] = ROOT.TH1F("Z_spin","Z spin [GeV]",6,-3.,3.)

    # Differences between h and Z
    h_nocut['hz_deltaphi'] = ROOT.TH1F("hz_deltaphi","#Delta#phi(h, Z)",40,-3.2,3.2)
    h_nocut['hz_deltaR'] = ROOT.TH1F("hz_deltaR","#Delta R(h, Z)",50,0.,5.)

    
    # Gen h from its b daughters
    h_nocut['truerecoh_pt']  = ROOT.TH1F("truerecoh_pt", "Reco h (from daughters) p_{T} [GeV]",100,0,500)
    h_nocut['truerecoh_eta'] = ROOT.TH1F("truerecoh_eta","Reco h (from daughters) #eta",100,-5,5)
    h_nocut['truerecoh_phi'] = ROOT.TH1F("truerecoh_phi","Reco h (from daughters) #phi",80,-3.2,3.2)
    h_nocut['truerecoh_m']   = ROOT.TH1F("truerecoh_m","Reco h (from daughters) mass [GeV]",200,0.,200)

    h_nocut['truerecoh_deltapt']  = ROOT.TH1F("truerecoh_deltapt", "Reco h (from daughters) #Delta p_{T} [GeV]",100,0,500)
    h_nocut['truerecoh_deltaeta'] = ROOT.TH1F("truerecoh_deltaeta","Reco h (from daughters) #Delta #eta",100,-5,5)
    h_nocut['truerecoh_deltaphi'] = ROOT.TH1F("truerecoh_deltaphi","Reco h (from daughters) #Delta #phi",80,-3.2,3.2)
    h_nocut['truerecoh_deltam']   = ROOT.TH1F("truerecoh_deltam",  "Reco h (from daughters) #Delta mass [GeV]",50,0.,200)
    h_nocut['truerecoh_resm']     = ROOT.TH1F("truerecoh_resm",    "Reco h (from daughters) mass resolution [GeV]",100,-10,10)

    h_nocut['truerecoh_sumpt'] = ROOT.TH1F("truerecoh_sumpt", "Sum pT of h daughters [GeV]", 100, 0., 500.)

    h_nocut['truerecoh_internal_deltaphi'] = ROOT.TH1F("truerecoh_internal_deltaphi","#Delta#phi between h daughters",40,-3.2,3.2)
    h_nocut['truerecoh_internal_deltaR']   = ROOT.TH1F("truerecoh_internal_deltaR","#Delta R between h daughters",50,0.,5.)
    
    # Gen Z from its b daughters
    h_nocut['truerecoZ_pt']  = ROOT.TH1F("truerecoZ_pt", "Reco Z (from daughters) p_{T} [GeV]",100,0,500)
    h_nocut['truerecoZ_eta'] = ROOT.TH1F("truerecoZ_eta","Reco Z (from daughters) #eta",100,-5,5)
    h_nocut['truerecoZ_phi'] = ROOT.TH1F("truerecoZ_phi","Reco Z (from daughters) #phi",80,-3.2,3.2)
    h_nocut['truerecoZ_m']   = ROOT.TH1F("truerecoZ_m",  "Reco Z (from daughters) mass [GeV]",200,0.,200)

    h_nocut['truerecoZ_deltapt']  = ROOT.TH1F("truerecoZ_deltapt", "Reco Z (from daughters) #Delta p_{T} [GeV]",100,0,500)
    h_nocut['truerecoZ_deltaeta'] = ROOT.TH1F("truerecoZ_deltaeta","Reco Z (from daughters) #Delta #eta",100,-5,5)
    h_nocut['truerecoZ_deltaphi'] = ROOT.TH1F("truerecoZ_deltaphi","Reco Z (from daughters) #Delta #phi",80,-3.2,3.2)
    h_nocut['truerecoZ_deltam']   = ROOT.TH1F("truerecoZ_deltam",  "Reco Z (from daughters) #Delta mass [GeV]",50,0.,200)
    h_nocut['truerecoZ_resm']     = ROOT.TH1F("truerecoZ_resm",    "Reco Z (from daughters) mass resolution [GeV]",100,-10,10)

    h_nocut['truerecoZ_sumpt'] = ROOT.TH1F("truerecoZ_sumpt", "Sum pT of Z daughters [GeV]", 100, 0., 500.)

    h_nocut['truerecohz_deltaphi'] = ROOT.TH1F("truerecohz_deltaphi","#Delta#phi(h, Z) from daughters",40,-3.2,3.2)
    h_nocut['truerecohz_deltaR'] = ROOT.TH1F("truerecohz_deltaR","#Delta R(h, Z) from daughters",50,0.,5.)

    h_nocut['truerecoz_internal_deltaphi'] = ROOT.TH1F("truerecoz_internal_deltaphi","#Delta#phi between Z daughters",40,-3.2,3.2)
    h_nocut['truerecoz_internal_deltaR']   = ROOT.TH1F("truerecoz_internal_deltaR","#Delta R between Z daughters",50,0.,5.)
    
    
    # Reco h from chosen bs
    h_nocut['recoh_pt']  = ROOT.TH1F("recoh_pt", "Reco h (from assignment) p_{T} [GeV]",100,0,500)
    h_nocut['recoh_eta'] = ROOT.TH1F("recoh_eta","Reco h (from assignment) #eta",100,-5,5)
    h_nocut['recoh_phi'] = ROOT.TH1F("recoh_phi","Reco h (from assignment) #phi",80,-3.2,3.2)
    h_nocut['recoh_m']   = ROOT.TH1F("recoh_m",  "Reco h (from assignment) mass [GeV]",200,0.,200)

    h_nocut['recoh_deltapt']  = ROOT.TH1F("recoh_deltapt", "Reco h (from assignment) #Delta p_{T} [GeV]",100,0,500)
    h_nocut['recoh_deltaeta'] = ROOT.TH1F("recoh_deltaeta","Reco h (from assignment) #Delta #eta",100,-5,5)
    h_nocut['recoh_deltaphi'] = ROOT.TH1F("recoh_deltaphi","Reco h (from assignment) #Delta #phi",80,-3.2,3.2)
    h_nocut['recoh_deltam']   = ROOT.TH1F("recoh_deltam",  "Reco h (from assignment) #Delta mass [GeV]",50,0.,200)
    h_nocut['recoh_resm']     = ROOT.TH1F("recoh_resm",    "Reco h (from assignment) mass resolution [GeV]",100,-10,10)

    h_nocut['recoh_sumpt'] = ROOT.TH1F("recoh_sumpt", "Sum pT of b quarks assigned to h [GeV]", 100, 0., 500.)

    h_nocut['recoh_internal_deltaphi'] = ROOT.TH1F("recoh_internal_deltaphi","#Delta#phi between h assigned bs",40,-3.2,3.2)
    h_nocut['recoh_internal_deltaR']   = ROOT.TH1F("recoh_internal_deltaR","#Delta R between h assigned bs",50,0.,5.)
    
    
    # Reco Z from chosen bs
    h_nocut['recoZ_pt']  = ROOT.TH1F("recoZ_pt", "Reco Z (from assignment) p_{T} [GeV]",100,0,500)
    h_nocut['recoZ_eta'] = ROOT.TH1F("recoZ_eta","Reco Z (from assignment) #eta",100,-5,5)
    h_nocut['recoZ_phi'] = ROOT.TH1F("recoZ_phi","Reco Z (from assignment) #phi",80,-3.2,3.2)
    h_nocut['recoZ_m']   = ROOT.TH1F("recoZ_m",  "Reco Z (from assignment) mass [GeV]",200,0.,200)

    h_nocut['recoZ_deltapt']  = ROOT.TH1F("recoZ_deltapt", "Reco Z (from assignment) #Delta p_{T} [GeV]",100,0,500)
    h_nocut['recoZ_deltaeta'] = ROOT.TH1F("recoZ_deltaeta","Reco Z (from assignment) #Delta #eta",100,-5,5)
    h_nocut['recoZ_deltaphi'] = ROOT.TH1F("recoZ_deltaphi","Reco Z (from assignment) #Delta #phi",80,-3.2,3.2)
    h_nocut['recoZ_deltam']   = ROOT.TH1F("recoZ_deltam",  "Reco Z (from assignment) #Delta mass [GeV]",50,0.,200)
    h_nocut['recoZ_resm']     = ROOT.TH1F("recoZ_resm",    "Reco Z (from assignment) mass resolution [GeV]",100,-10,10)

    h_nocut['recoZ_sumpt'] = ROOT.TH1F("recoZ_sumpt", "Sum pT of b quarks assigned to Z [GeV]", 100, 0., 500.)

    h_nocut['recohz_deltaphi'] = ROOT.TH1F("recohz_deltaphi","#Delta#phi(h, Z) from assignment",40,-3.2,3.2)
    h_nocut['recohz_deltaR'] = ROOT.TH1F("recohz_deltaR","#Delta R(h, Z) from assignment",50,0.,5.)

    h_nocut['recoz_internal_deltaphi'] = ROOT.TH1F("recoz_internal_deltaphi","#Delta#phi between Z daughters",40,-3.2,3.2)
    h_nocut['recoz_internal_deltaR']   = ROOT.TH1F("recoz_internal_deltaR","#Delta R between Z daughters",50,0.,5.)


    h_nocut['inclusive_mu_m']   = ROOT.TH1F("inclusive_mu_m",  "Inclusive muon mass [GeV]",50,0,10)
    h_nocut['inclusive_mu_pt']  = ROOT.TH1F("inclusive_mu_pt", "Inclusive muon p_{T} [GeV]",100,0,500)
    h_nocut['inclusive_mu_eta'] = ROOT.TH1F("inclusive_mu_eta","Inclusive muon #eta",100,-5,5)
    h_nocut['inclusive_mu_phi'] = ROOT.TH1F("inclusive_mu_phi","Inclusive muon #phi",80,-3.2,3.2)
    
    h_nocut['inclusive_b_m']   = ROOT.TH1F("inclusive_b_m",  "Inclusive b mass [GeV]",50,0,10)
    h_nocut['inclusive_b_pt']  = ROOT.TH1F("inclusive_b_pt", "Inclusive b p_{T} [GeV]",100,0,500)
    h_nocut['inclusive_b_eta'] = ROOT.TH1F("inclusive_b_eta","Inclusive b #eta",100,-5,5)
    h_nocut['inclusive_b_phi'] = ROOT.TH1F("inclusive_b_phi","Inclusive b #phi",80,-3.2,3.2)

    # Recoil study
    h_nocut['truerecoil']    = ROOT.TH1F("truerecoil",   "Recoil mass #sqrt{p_{CM}^{2} - p_{Z}^{2}} [GeV]",100,0.,200.)
    h_nocut['recorecoil']    = ROOT.TH1F("recorecoil",   "Recoil mass #sqrt{p_{CM}^{2} - (p_{#mu^{+}} + p_{#mu^{-}} )^{2}} [GeV]",100,0.,200.)
    h_nocut['truealtrecoil']    = ROOT.TH1F("truealtrecoil",   "Recoil mass #sqrt{p_{CM}^{2} - p_{Z}^{2}} [GeV]",100,0.,200.)
    h_nocut['recoaltrecoil']    = ROOT.TH1F("recoaltrecoil",   "Recoil mass #sqrt{p_{CM}^{2} - (p_{#mu^{+}} + p_{#mu^{-}} )^{2}} [GeV]",100,0.,200.)

    h_nocut['recoz_acop'] = ROOT.TH1F("recoz_acop","#Delta#phi(d1, d2) from assignment",20,0.,3.2)    
    
    h_nocut['finalstatemass'] = ROOT.TH1F("finalstatemass" , "Mass of the final state", 100, 0., 500.)
    
    for key in h_nocut.keys():
        h_cut[key] = h_nocut[key].Clone('cut_'+h_nocut[key].GetName())
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

        top = ROOT.TLorentzVector()
        antitop = ROOT.TLorentzVector()
        
        truerecoh_products = []
        truerecoZ_products = []
        recoh_products = []
        recoZ_products = []

        
        init_bList = []
        muList = []
        
        truerecoh_sumpt = 0
        truerecoZ_sumpt = 0
        recoZ_sumpt = 0
        recoh_sumpt = 0
                                
    
        num_e = 0
        num_h = 0
        num_Z = 0
        num_b = 0
        num_m = 0
        
        w=1
        
        for iev in Event:
            h_nocut['Event_size'].Fill(1)
            #h_nocut['Nparticles'].Fill(  iev.Nparticles ) # See below, after event loop
            h_nocut['ProcessID'].Fill(   iev.ProcessID  )
            h_nocut['Weight'].Fill(      iev.Weight     )
            h_nocut['CouplingQED'].Fill( iev.CouplingQED )
            h_nocut['CouplingQCD'].Fill( iev.CouplingQCD )
            w=iev.Weight
            #print iev.Weigh
            ## 250 fb-1
            #w *= 250000.
        #print "-------------------"
        for p in Particles:
            index += 1
            
            h_nocut['PID'].Fill( p.PID, w )
            h_nocut['Status'].Fill( p.Status, w )
            # MG Status code: -1 initial, 2 intermediate, 1 final

            # Initial state electrons
            if math.fabs(p.PID) == 11 and p.Status == -1:
                h_nocut['e_pt'].Fill( p.PT, w )
                h_nocut['e_eta'].Fill( p.Eta, w )
                h_nocut['e_phi'].Fill( p.Phi, w )
                h_nocut['e_m'].Fill( p.M, w )
                h_nocut['e_spin'].Fill( p.Spin, w )
                p4temp = ROOT.TLorentzVector()
                p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                p4_e += p4temp
                num_e += 1
                
            # Intermediate state h
            if math.fabs(p.PID) == 25:
                #and p.Status == 2:
                p4_h.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                h_nocut['h_pt'].Fill( p.PT, w )
                h_nocut['h_eta'].Fill( p.Eta, w )
                h_nocut['h_phi'].Fill( p.Phi, w )
                h_nocut['h_m'].Fill( p.M, w )
                h_nocut['h_spin'].Fill( p.Spin, w )
                num_h += 1
            # Intermediate state Z
            if math.fabs(p.PID) == 23:
                #and p.Status == 2:
                p4_Z.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                h_nocut['Z_pt'].Fill( p.PT, w )
                h_nocut['Z_eta'].Fill( p.Eta, w )
                h_nocut['Z_phi'].Fill( p.Phi, w )
                h_nocut['Z_m'].Fill( p.M, w )
                h_nocut['Z_spin'].Fill( p.Spin, w )
                num_Z += 1
            # Final state mus
            if math.fabs(p.PID) == 13:
                h_nocut['inclusive_b_pt'].Fill( p.PT, w )
                h_nocut['inclusive_b_eta'].Fill( p.Eta, w )
                h_nocut['inclusive_b_phi'].Fill( p.Phi, w )
                h_nocut['inclusive_b_m'].Fill( p.M, w )
                p4tempp = ROOT.TLorentzVector()
                p4tempp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                if p.PID > 0:
                    top += p4tempp
                else:
                    antitop += p4tempp
                num_m += 1
                # Build true Z from muon daughters
                if p.Mother1 != -1:
                    if math.fabs(Particles[p.Mother1].PID) == 23:
                        p4temp = ROOT.TLorentzVector()
                        p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                        p4_truerecoZ += p4temp
                        truerecoZ_sumpt += p.PT
                        truerecoZ_products.append(p4temp)
                        muList.append(b_p4temp)
            # Final state b
            if math.fabs(p.PID) == 5:
                #and p.Status == 2:
                h_nocut['inclusive_b_pt'].Fill( p.PT, w )
                h_nocut['inclusive_b_eta'].Fill( p.Eta, w )
                h_nocut['inclusive_b_phi'].Fill( p.Phi, w )
                h_nocut['inclusive_b_m'].Fill( p.M, w )
                p4tempp = ROOT.TLorentzVector()
                p4tempp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                if p.PID > 0:
                    top += p4tempp
                else:
                    antitop += p4tempp
                num_b += 1
                # Build true h from b daughters
                if p.Mother1 != -1:
                    if math.fabs(Particles[p.Mother1].PID) == 25:
                        p4temp = ROOT.TLorentzVector()
                        p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                        p4_truerecoh += p4temp
                        truerecoh_sumpt += p.PT
                        truerecoh_products.append(p4temp)
                        
                # Build true Z from b daughters
                if p.Mother1 != -1:
                    if math.fabs(Particles[p.Mother1].PID) == 23:
                        p4temp = ROOT.TLorentzVector()
                        p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                        p4_truerecoZ += p4temp
                        truerecoZ_sumpt += p.PT
                        truerecoZ_products.append(p4temp)

                # Build the b list
                b_p4temp = ROOT.TLorentzVector()
                b_p4temp.SetPtEtaPhiE( p.PT, p.Eta, p.Phi, p.E)
                init_bList.append(b_p4temp)

        #if options.inputDir.find('sm') != -1 and num_h != 0:
        #    continue
            
        # end loop over Particles


        for iev in Event:
            if iev.Nparticles != index:
                h_nocut['Nparticles'].Fill(  -1 )
            else:
                h_nocut['Nparticles'].Fill(iev.Nparticles)
                
        h_nocut['num_e'].Fill(num_e)
        h_nocut['num_h'].Fill(num_h)
        h_nocut['num_Z'].Fill(num_Z)
        h_nocut['num_b'].Fill(num_b)

        # Fill true h from daughters histos
        h_nocut['truerecoh_pt'].Fill(  p4_truerecoh.Pt(), w )
        h_nocut['truerecoh_eta'].Fill( p4_truerecoh.Eta(), w )
        h_nocut['truerecoh_phi'].Fill( p4_truerecoh.Phi(), w )
        h_nocut['truerecoh_m'].Fill(   p4_truerecoh.M(), w )

        # Fill true Z from daughters histos
        h_nocut['truerecoZ_pt'].Fill(  p4_truerecoZ.Pt(), w )
        h_nocut['truerecoZ_eta'].Fill( p4_truerecoZ.Eta(), w )
        h_nocut['truerecoZ_phi'].Fill( p4_truerecoZ.Phi(), w )
        h_nocut['truerecoZ_m'].Fill(   p4_truerecoZ.M(), w )

        # Fill deltas between true h from daughters and gen h
        h_nocut['truerecoh_deltapt'].Fill(  p4_truerecoh.Pt()  - p4_h.Pt() , w)
        h_nocut['truerecoh_deltaeta'].Fill( p4_truerecoh.Eta() - p4_h.Eta(), w)
        h_nocut['truerecoh_deltaphi'].Fill( deltaPhi(p4_truerecoh, p4_h), w)
        h_nocut['truerecoh_deltam'].Fill(   p4_truerecoh.M()   - p4_h.M()  , w)
        if p4_h.M() != 0:
            h_nocut['truerecoh_resm'].Fill(  ( p4_truerecoh.M()   - p4_h.M()) / p4_h.M(), w  )

        # Fill deltas between true Z from daughters and gen Z
        h_nocut['truerecoZ_deltapt'].Fill(  p4_truerecoZ.Pt()  - p4_Z.Pt() , w)
        h_nocut['truerecoZ_deltaeta'].Fill( p4_truerecoZ.Eta() - p4_Z.Eta(), w)
        h_nocut['truerecoZ_deltaphi'].Fill( deltaPhi(p4_truerecoZ, p4_Z), w)
        h_nocut['truerecoZ_deltam'].Fill(   p4_truerecoZ.M()   - p4_Z.M()  , w)
        if p4_Z.M() != 0:
            h_nocut['truerecoZ_resm'].Fill(   ( p4_truerecoZ.M()   - p4_Z.M()) / p4_Z.M(), w  )
        

        h_nocut['truerecoh_sumpt'].Fill(truerecoh_sumpt, w)
        h_nocut['truerecoZ_sumpt'].Fill(truerecoZ_sumpt, w)

        # Play with different assignments for the b quarks
        bList = sorted(init_bList, key=lambda v : v.Pt(), reverse=True)

        # Assignment

        # h pair: pair with closest mass
        index1 = -1
        index2 = -1
        closestMass = 9999.

        # z pair: the others
        zindex1 = -1
        zindex2 = -2

        t_ind1=0
        for first in bList:
            t_ind2=0
            for second in bList:
                if first.Pt() != second.Pt() or first.Eta() != second.Eta() or first.Phi() != second.Phi():
                    p4temp = first + second
                    if(math.fabs(p4temp.M() - 120.) < closestMass):
                        closestMass = p4temp.M()
                        index1 = t_ind1
                        index2 = t_ind2
                t_ind2 += 1
            t_ind1 += 1
                        
        p4_recoh += bList[index1]
        p4_recoh += bList[index2]
        recoh_products.append(bList[index1])
        recoh_products.append(bList[index2])
        
        
        if options.inputDir.find('mumu') == -1:
            indexz = 0
            for b in bList:
                if indexz != index1 and indexz != index2:
                    if zindex1 == -1:
                        zindex1 = indexz
                    else:
                        zindex2 = indexz
                    p4_recoZ += b
                indexz += 1
            #print "i1 ", index1, ", i2 ", index2, ", zi1 ", zindex1, ", zi2 ", zindex2
            recoZ_products.append(bList[zindex1])
            recoZ_products.append(bList[zindex2])
        else:
            if options.inputDir.find('sm') == -1:
                recoZ_products.append(muList[0])
                recoZ_products.append(muList[1])
            else:
                recoZ_products.append(ROOT.TLorentzVector())
                recoZ_products.append(ROOT.TLorentzVector())
                
        # Fill true h from daughters histos
        h_nocut['recoh_pt'].Fill(  p4_recoh.Pt(), w )
        h_nocut['recoh_eta'].Fill( p4_recoh.Eta(), w )
        h_nocut['recoh_phi'].Fill( p4_recoh.Phi(), w )
        h_nocut['recoh_m'].Fill(   p4_recoh.M(), w )

        # Fill true Z from daughters histos
        h_nocut['recoZ_pt'].Fill(  p4_recoZ.Pt(), w )
        h_nocut['recoZ_eta'].Fill( p4_recoZ.Eta(), w )
        h_nocut['recoZ_phi'].Fill( p4_recoZ.Phi(), w )
        h_nocut['recoZ_m'].Fill(   p4_recoZ.M(), w )

        # Fill deltas between true h from daughters and gen h
        h_nocut['recoh_deltapt'].Fill(  p4_recoh.Pt()  - p4_h.Pt() , w)
        h_nocut['recoh_deltaeta'].Fill( p4_recoh.Eta() - p4_h.Eta(), w)
        h_nocut['recoh_deltaphi'].Fill( deltaPhi(p4_recoh, p4_h), w)
        h_nocut['recoh_deltam'].Fill(   p4_recoh.M()   - p4_h.M()  , w)
        if p4_h.M() != 0:
            h_nocut['recoh_resm'].Fill(  ( p4_recoh.M()   - p4_h.M()) / p4_h.M(), w  )
            
        # Fill deltas between true Z from daughters and gen Z
        h_nocut['recoZ_deltapt'].Fill(  p4_recoZ.Pt()  - p4_Z.Pt() , w)
        h_nocut['recoZ_deltaeta'].Fill( p4_recoZ.Eta() - p4_Z.Eta(), w)
        h_nocut['recoZ_deltaphi'].Fill( deltaPhi(p4_recoZ, p4_Z), w)
        h_nocut['recoZ_deltam'].Fill(   p4_recoZ.M()   - p4_Z.M()  , w)
        if p4_Z.M() != 0:
            h_nocut['recoZ_resm'].Fill(   ( p4_recoZ.M()   - p4_Z.M()) / p4_Z.M(), w  )
        
        h_nocut['recoZ_sumpt'].Fill(recoZ_sumpt, w)
        h_nocut['recoh_sumpt'].Fill(recoh_sumpt, w)

        h_nocut['hz_deltaphi']        .Fill(deltaPhi(p4_h        , p4_Z        ), w)
        h_nocut['truerecohz_deltaphi'].Fill(deltaPhi(p4_truerecoh, p4_truerecoZ), w)
        h_nocut['recohz_deltaphi']    .Fill(deltaPhi(p4_recoh    , p4_recoZ    ), w)

        h_nocut['hz_deltaR']        .Fill(deltaR(p4_h        , p4_Z        ), w)
        h_nocut['truerecohz_deltaR'].Fill(deltaR(p4_truerecoh, p4_truerecoZ), w)
        h_nocut['recohz_deltaR']    .Fill(deltaR(p4_recoh    , p4_recoZ    ), w)


        # Debug
        if False and (len(truerecoZ_products) != 2 or len(truerecoh_products) != 2):
            print "Z bs: ", len(truerecoZ_products), ", h bs: ", len(truerecoh_products)
            for p in Particles:
                print "-------------"
                print "PID: ", p.PID
                print "Mother1: ", p.Mother1
                print "Mother2: ", p.Mother2
                print "Mother1 ID:", Particles[p.Mother1].PID if p.Mother1 != -1 else -1
                print "Mother2 ID:", Particles[p.Mother2].PID if p.Mother2 != -1 else -1
                print "Status: ", p.Status
            
                
        if options.inputDir.find('sm') != -1:
            if len(truerecoh_products) == 0:
                truerecoh_products = []
                truerecoh_products.append(ROOT.TLorentzVector())
                truerecoh_products.append(ROOT.TLorentzVector())
            if len(truerecoZ_products) == 0:
                truerecoZ_products = []
                truerecoZ_products.append(ROOT.TLorentzVector())
                truerecoZ_products.append(ROOT.TLorentzVector())

        h_nocut['truerecoz_internal_deltaphi'].Fill( deltaPhi(truerecoZ_products[0], truerecoZ_products[1]), w)
        h_nocut['truerecoz_internal_deltaR']  .Fill( deltaR(  truerecoZ_products[0], truerecoZ_products[1]), w)
        h_nocut['truerecoh_internal_deltaphi'].Fill( deltaPhi(truerecoh_products[0], truerecoh_products[1]), w)
        h_nocut['truerecoh_internal_deltaR']  .Fill( deltaR(  truerecoh_products[0], truerecoh_products[1]), w)

        h_nocut['recoz_internal_deltaphi'].Fill( deltaPhi(recoZ_products[0], recoZ_products[1]), w) 
        h_nocut['recoz_internal_deltaR']  .Fill( deltaR(  recoZ_products[0], recoZ_products[1]), w) 
        h_nocut['recoh_internal_deltaphi'].Fill( deltaPhi(recoh_products[0], recoh_products[1]), w) 
        h_nocut['recoh_internal_deltaR']  .Fill( deltaR(  recoh_products[0], recoh_products[1]), w) 

        # Recoil study
        sqrts = 0
        if options.inputDir.find('cepc') != -1:
            sqrts =250+250
        elif options.inputDir.find('ilc') != -1:
            sqrts = 500+500
        s = math.pow(sqrts, 2)
            
        trueEZ = p4_Z.E()
        #recoEZ = recoZ_products[0].Mag() + recoZ_products[1].Mag()

               
        sumzproducts = recoZ_products[0] + recoZ_products[1]
        recoEZ = sumzproducts.E()
        #recoMZ2 = math.pow(recoEZ, 2) - math.pow(sumzproducts.Mag(), 2)
        recoMZ2 = math.pow(sumzproducts.M(), 2)
        #MZ2= 91.2*91.2
        MZ2= math.pow(p4_Z.M(), 2)

        truerecoil = math.sqrt( s + MZ2 - 2*trueEZ*sqrts )
        #print "s ", s, " + recoMZ2 ", recoMZ2, " -2 * recoEZ ", recoEZ, " * sqrts ", sqrts, " = recorecoil ",  s + MZ2 - 2*recoEZ*sqrts
        recorecoil2 = math.fabs(s + recoMZ2 - 2*recoEZ*sqrts )
        recorecoil = math.sqrt( recorecoil2 ) 
        h_nocut['truerecoil'].Fill(truerecoil, w)
        h_nocut['recorecoil'].Fill(recorecoil, w)

        pz2  = math.pow(p4_Z.P(), 2)
        #sumprod = recoZ_products[0] + recoZ_products[1]
        pp2  = math.pow(sumzproducts.P(), 2)
        truealtrecoil = math.sqrt(s-pz2)
        recoaltrecoil = math.sqrt(s-pp2)
        #print "True recoil: ", truerecoil, ", Reco recoil: ", recorecoil, "True alt recoil: ", truealtrecoil, ", Reco altrecoil: ", recoaltrecoil
        h_nocut['truealtrecoil'].Fill(truealtrecoil, w)
        h_nocut['recoaltrecoil'].Fill(recoaltrecoil, w)

        acop = math.fabs(deltaPhi(recoZ_products[0], recoZ_products[1]))
        h_nocut['recoz_acop'].Fill( acop, w)

        # Take out ttbar
        
        h_nocut['finalstatemass'].Fill(top.M(), w)
        h_nocut['finalstatemass'].Fill(antitop.M(), w)
        
        # Cuts
        if truerecoil < 110. or truerecoil > 130:
            continue
        if sumzproducts.M() < 80. or sumzproducts.M() > 100:
            continue
        if math.fabs(sumzproducts.Eta()) > 2.:
            continue
        if acop < 0.2 or acop > 3:
            continue
        
        h_cut['truerecoil'].Fill(truerecoil, w)
        h_cut['recorecoil'].Fill(recorecoil, w)
        h_cut['truealtrecoil'].Fill(truealtrecoil, w)
        h_cut['recoaltrecoil'].Fill(recoaltrecoil, w)
        h_cut['recoz_acop'].Fill( acop, w)
        h_cut['truerecoz_internal_deltaphi'].Fill( deltaPhi(truerecoZ_products[0], truerecoZ_products[1]), w)
        h_cut['truerecoz_internal_deltaR']  .Fill( deltaR(  truerecoZ_products[0], truerecoZ_products[1]), w)
        h_cut['truerecoh_internal_deltaphi'].Fill( deltaPhi(truerecoh_products[0], truerecoh_products[1]), w)
        h_cut['truerecoh_internal_deltaR']  .Fill( deltaR(  truerecoh_products[0], truerecoh_products[1]), w)
        h_cut['recoz_internal_deltaphi'].Fill( deltaPhi(recoZ_products[0], recoZ_products[1]), w) 
        h_cut['recoz_internal_deltaR']  .Fill( deltaR(  recoZ_products[0], recoZ_products[1]), w) 
        h_cut['recoh_internal_deltaphi'].Fill( deltaPhi(recoh_products[0], recoh_products[1]), w) 
        h_cut['recoh_internal_deltaR']  .Fill( deltaR(  recoh_products[0], recoh_products[1]), w) 
        # Fill true h from daughters histos
        h_cut['recoh_pt'].Fill(  p4_recoh.Pt(), w )
        h_cut['recoh_eta'].Fill( p4_recoh.Eta(), w )
        h_cut['recoh_phi'].Fill( p4_recoh.Phi(), w )
        h_cut['recoh_m'].Fill(   p4_recoh.M(), w )
        # Fill true Z from daughters histos
        h_cut['recoZ_pt'].Fill(  p4_recoZ.Pt(), w )
        h_cut['recoZ_eta'].Fill( p4_recoZ.Eta(), w )
        h_cut['recoZ_phi'].Fill( p4_recoZ.Phi(), w )
        h_cut['recoZ_m'].Fill(   p4_recoZ.M(), w )
        # Fill deltas between true h from daughters and gen h
        h_cut['recoh_deltapt'].Fill(  p4_recoh.Pt()  - p4_h.Pt() , w)
        h_cut['recoh_deltaeta'].Fill( p4_recoh.Eta() - p4_h.Eta(), w)
        h_cut['recoh_deltaphi'].Fill( deltaPhi(p4_recoh, p4_h), w)
        h_cut['recoh_deltam'].Fill(   p4_recoh.M()   - p4_h.M()  , w)
        if p4_h.M() != 0:
            h_cut['recoh_resm'].Fill(  ( p4_recoh.M()   - p4_h.M()) / p4_h.M(), w  )
          
        # Fill deltas between true Z from daughters and gen Z
        h_cut['recoZ_deltapt'].Fill(  p4_recoZ.Pt()  - p4_Z.Pt() , w)
        h_cut['recoZ_deltaeta'].Fill( p4_recoZ.Eta() - p4_Z.Eta(), w)
        h_cut['recoZ_deltaphi'].Fill( deltaPhi(p4_recoZ, p4_Z), w)
        h_cut['recoZ_deltam'].Fill(   p4_recoZ.M()   - p4_Z.M()  , w)
        if p4_Z.M() != 0:
            h_cut['recoZ_resm'].Fill(   ( p4_recoZ.M()   - p4_Z.M()) / p4_Z.M(), w  )
        
        h_cut['recoZ_sumpt'].Fill(recoZ_sumpt, w)
        h_cut['recoh_sumpt'].Fill(recoh_sumpt, w)

        h_cut['hz_deltaphi']        .Fill(deltaPhi(p4_h        , p4_Z        ), w)
        h_cut['truerecohz_deltaphi'].Fill(deltaPhi(p4_truerecoh, p4_truerecoZ), w)
        h_cut['recohz_deltaphi']    .Fill(deltaPhi(p4_recoh    , p4_recoZ    ), w)

        h_cut['hz_deltaR']        .Fill(deltaR(p4_h        , p4_Z        ), w)
        h_cut['truerecohz_deltaR'].Fill(deltaR(p4_truerecoh, p4_truerecoZ), w)
        h_cut['recohz_deltaR']    .Fill(deltaR(p4_recoh    , p4_recoZ    ), w)
        


        
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
