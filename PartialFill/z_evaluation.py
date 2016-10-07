#!/usr/bin/env python
import ROOT
import rat
import math
import os
import fnmatch
import plot_style

def get_minimal_z(h_z,tree):
    """Function to plot all water volume events which are reconstructed above the fill level

     Args:
      h_z (TH1D) : histogram to plot z - z_level
      tree (TTree) : tree from the input root file
    """

    #get file containing the fill levels and days
    infile = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")

    #loop through files
    for line in infile:
        words = line.split()

        if len(words)!=0:

            #get day and fill level
            d = float(words[0])
            z_level = float(words[1])
            
            #loop through tree
            for i in range(tree.GetEntries()):
                tree.GetEntry(i)
                z = tree.posz
                time = tree.uTDays

                if d != time:
                    continue

                #if the event occurred on the current fill day in the text file, check the event position and fill the histogram if the event was reconstructed above the fill level
                if d == time:
                    if z > z_level:
                        h_z.Fill(z-z_level)

def get_nhits(h_nhits, h_nhits_1, tree):
    """Function to plot and compare the nhits distributions of the water events before and after the fiducial volume cut was applied.

     Args: 
      h_nhits (TH1D) : histogram filled with the nhits of all events
      h_nhits_1 (TH1D) : histogram filled with the nhits of events occurring in the fiducial volume
      tree (TTree) : tree from the input root file
    """

    #get file containing the fill levels and days
    infile = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")

    #loop through files
    for line in infile:
        words = line.split()

        if len(words)!=0:

            #get day and fill level
            d = float(words[0])
            z_level = float(words[1])
            
            #loop through tree
            for i in range(tree.GetEntries()):
                tree.GetEntry(i)
                z = tree.posz
                time = tree.uTDays
                nhits = tree.nhits
                radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                fidvol_value = 5000

                #compare time the event has occurred to the time this fill level was simulated at
                if d != time:
                    continue
                    
                elif d == time:
                    #fill histogram containing all events
                    h_nhits.Fill(nhits)
                    
                    if radius> 0 and radius < fidvol_value and z >= z_level+653:
                        #fill histogram with events reconstructed within the fiducial volume
                        h_nhits_1.Fill(nhits)

    #draw histograms
    c1 = ROOT.TCanvas("c1","",1)
    c1.SetLogy(1)
    c1.Draw()

    h_nhits.SetXTitle("n_{hits}")
    h_nhits.SetYTitle("Intensity per 10 hits bin")
    h_nhits.Draw()
    h_nhits_1.SetLineColor(50)
    h_nhits_1.Draw("same")

    pad = ROOT.TPad("pada","pada",0.5,0.65,0.89,0.85)
    label = ROOT.TPaveText(0.05,0.0,0.95,0.4,"br")

    pad.SetFillStyle(4000)
    pad.SetFillColor(0)
    pad.Draw()
    pad.cd()

    label.SetFillColor(0)
    label.SetLineColor(0)
    label.SetShadowColor(0)
    label.SetTextSize(0.175)
    label.AddText("RAT 5.3.1 production, partial-fill phase")
    label.AddText("MC simulations")
    label.Draw()

    c1.cd()

    l1 = ROOT.TLegend(0.60,0.3,0.9,0.45,"","brNDC")
    l1.AddEntry(h_nhits,"Before fiducial volume cut", "l")
    l1.AddEntry(h_nhits_1,"After fiducial volume cut", "l")
    l1.SetFillColor(0)
    l1.SetTextSize(0.03)
    l1.Draw("same")


def determine_cut_value(hist, ratio):
    """Function to determine a cut value of a histogram based on a given cut efficiency.

     Args:
      hist (TH1D) : histogram on which the cut value is determined
      ratio (float) : desired cut efficiency
    """

    #calculate the integral of the histogram
    all_events = hist.Integral()
    
    #to be determined cut value
    cut = 0

    #loop through all entries in the histogram
    for i in range(hist.GetNbinsX()):
        #reject all events reconstructed on the scintillator-water interface
        if hist.GetBinLowEdge(i)<100:
            continue
        
        #get integral from 0th to ith bin
        integral = hist.Integral(0,i)

        #if the ratio to the overall integral reaches the given ratio, stop loop and return the cut value
        if integral/all_events >= ratio:
            cut = hist.GetBinCenter(i)
            return cut



if __name__ == '__main__':

    #get plot style
    style = plot_style.PlotStyle()
    style.set_style()
    ROOT.gROOT.SetStyle("clearRetro")

    #define histogram for cut definition
    hist = ROOT.TH1D("hist","",150, -2000, 2000)

    #loop through directory containing input root files
    for root, dirs, filenames in os.walk("/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/"):
        filenames.sort()
        for x in filenames:
            if fnmatch.fnmatch(x, "*_Water.ntuple.root"):
                infile = "/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/" + x

                components = x.split(".")

                #open input root file and get tree
                filename = ROOT.TFile(infile)
                tree = filename.Get("output")

                #create new directory
                outdir = "/data/langrock/PartialFill/" + components[0] 
                if not os.path.exists(outdir):
                    os.makedirs(outdir)

                #open output root file
                outputroot = ROOT.TFile(outdir + "/" + components[0] + ".root","recreate")

                #define histogram
                h_nhits = ROOT.TH1D("nhits","", 300, 0, 1500)
                h_nhits_after = ROOT.TH1D("nhits_1","", 300, 0, 1500)
                h_z = ROOT.TH1D("h_z","",150, -2000, 2000)

                #run functions
                get_nhits(h_nhits, h_nhits_after, tree)
                get_minimal_z(h_z,tree)
                
                #write all histograms to file
                outputroot.Write()
                outputroot.Close()

                #add h_z to the histogram for the cut definition
                hist.Add(h_z)
                
    #get cut values for different cut efficiencies
    rej_90 = determine_cut_value(hist, 0.90)
    rej_95 = determine_cut_value(hist, 0.95)
    rej_99 = determine_cut_value(hist, 0.99)

    print rej_90, rej_95, rej_99
