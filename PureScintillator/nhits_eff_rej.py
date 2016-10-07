#!/usr/bin/env python
import ROOT
import rat
import sys
import math

#get polonium production files
Po214 = ROOT.TFile("/data/snoplus/OfficialProcessing/production_4_5/Solar/Po214/Po214.ntuple.root")
Po214_tree = Po214.Get("output")

Po212 = ROOT.TFile("/data/snoplus/OfficialProcessing/production_4_5/Solar/Po212/Po212.ntuple.root")
Po212_tree = Po212.Get("output")

#define rejection and efficiency histograms
efficiency = ROOT.TH1D("efficiency", "efficiency",700,0,700)
rejection = ROOT.TH1D("rejection", "rejection",700,0,700) 

#define upper boundary for nhits cut
n_hits_start = 500

#start loop, continue loop for each nhits boundary above 0
while n_hits_start >= 0:

    #define histograms
    h_nhit = ROOT.TH1D("h_nhit","h_nhit",100,0,700)
    h_nhit_aftercut = ROOT.TH1D("h_nhit_aftercut", "h_nhit_aftercut",100,0,800)
    h_nhit_1 = ROOT.TH1D("h_nhit_1","h_nhit_1",100,0,700)
    h_nhit_aftercut_1 = ROOT.TH1D("h_nhit_aftercut_1", "h_nhit_aftercut_1",100,0,800) 

    #loop through the polonium file for which efficiency is determined
    for i in range(Po214_tree.GetEntries()):
        Po214_tree.GetEntry(i)
        nhits = Po214_tree.nhits
        radius = math.sqrt(Po214_tree.posx*Po214_tree.posx+Po214_tree.posy*Po214_tree.posy+Po214_tree.posz*Po214_tree.posz)
        evIndex = Po214_tree.evIndex

        #apply fiducial volume cut and reject retriggers
        if radius < 4000 and evIndex == 0:    
            h_nhit.Fill(nhits)
            #apply nhits cut with current upper boundary
            if nhits >= 0 and nhits <= n_hits_start: 
                h_nhit_aftercut.Fill(nhits)

    #loop through the polonium file for which rejection is determined
    for i in range(Po212_tree.GetEntries()):
        Po212_tree.GetEntry(i)
        nhits = Po212_tree.nhits
        radius = math.sqrt(Po212_tree.posx*Po212_tree.posx+Po212_tree.posy*Po212_tree.posy+Po212_tree.posz*Po212_tree.posz)
        evIndex = Po212_tree.evIndex

        #apply fiducial volume cut and reject retriggers
        if radius < 4000 and evIndex == 0:    
            h_nhit_1.Fill(nhits)
            #apply nhits cut with current upper boundary
            if nhits >= 0 and nhits <= n_hits_start: 
                h_nhit_aftercut_1.Fill(nhits)

    #calculate efficiency and fill efficiency histogram for current upper boundary
    eff = 0
    if h_nhit.GetEntries() > 0:
        eff = h_nhit_aftercut.GetEntries()/h_nhit.GetEntries()
        efficiency.Fill(n_hits_start,eff)

    #calcualte rejection and fill rejection histogram for current upper boundary
    rej = 0
    if h_nhit_1.GetEntries() > 0:
        rej = 1 - (h_nhit_aftercut_1.GetEntries()/h_nhit_1.GetEntries())
        rejection.Fill(n_hits_start,rej)

    h_nhit.Delete()
    h_nhit_aftercut.Delete()
    h_nhit_1.Delete()
    h_nhit_aftercut_1.Delete()

    #decrase upper boundary
    n_hits_start = n_hits_start - 10


#define plot style
hipStyle = ROOT.TStyle("clearRetro","HIP plots style for publications")

# use plain black on white colors
hipStyle.SetFrameBorderMode(0)
hipStyle.SetCanvasBorderMode(0)
hipStyle.SetPadBorderMode(0)
hipStyle.SetPadBorderSize(0)
hipStyle.SetPadColor(0)
hipStyle.SetCanvasColor(0)
hipStyle.SetTitleColor(0)
hipStyle.SetStatColor(0)
hipStyle.SetFillColor(0)

# use bold lines 
hipStyle.SetHistLineWidth(2)
hipStyle.SetLineWidth(2)

# no title, stats box or fit as default
hipStyle.SetOptTitle(0)
hipStyle.SetOptStat(0)
hipStyle.SetOptFit(0)

# postscript dashes
hipStyle.SetLineStyleString(2,"[12 12]") # postscript dashes

# text style and size
hipStyle.SetTextFont(61)
hipStyle.SetTextSize(0.24)
hipStyle.SetLabelFont(61,"x")
hipStyle.SetLabelFont(61,"y")
hipStyle.SetLabelFont(61,"z")
hipStyle.SetTitleFont(61,"x")
hipStyle.SetTitleFont(61,"y")
hipStyle.SetTitleFont(61,"z")
hipStyle.SetLabelSize(0.04,"x")
hipStyle.SetTitleSize(0.05,"x")
hipStyle.SetTitleColor(1,"x")
hipStyle.SetLabelSize(0.04,"y")
hipStyle.SetTitleSize(0.05,"y")
hipStyle.SetTitleColor(1,"y")
hipStyle.SetLabelSize(0.04,"z")
hipStyle.SetTitleSize(0.05,"z")
hipStyle.SetTitleColor(1,"z")
  
# AXIS OFFSETS
hipStyle.SetTitleOffset(0.8,"x")
hipStyle.SetTitleOffset(0.8,"y")
hipStyle.SetTitleOffset(0.8,"z")

# Legends
hipStyle.SetLegendBorderSize(1)
# graphs - set default martker to cross, rather than .
hipStyle.SetMarkerStyle(2)  # cross +

ROOT.gROOT.SetStyle("clearRetro")

#draw efficiency and rejection histograms
c1 = ROOT.TCanvas("c1","c1",1)
c1.Draw()

l1 = ROOT.TLegend(0.45,0.67,0.87,0.87,"","brNDC")
pada = ROOT.TPad("pada","pada",0.1,0.67,0.55,0.87)

label = ROOT.TPaveText(0.05,0.0,0.95,0.4,"br")

rejection.SetXTitle("upper n_{hits} limit")
rejection.SetYTitle("Cut efficiency/rejection")
rejection.SetAxisRange(0,1.5,"Y")
rejection.SetMarkerColor(30)
rejection.SetMarkerStyle(5)
rejection.SetLineColor(30)
rejection.Draw("p")

efficiency.SetMarkerColor(50)
efficiency.SetMarkerStyle(5)
efficiency.SetLineColor(50)
efficiency.Draw("p same")

l1.AddEntry(efficiency, "Cut efficiency for Po214","l")
l1.AddEntry(rejection, "Cut rejection for Po212","l")
l1.SetFillColor(0)
l1.SetTextSize(0.04)
l1.Draw("same")

pada.SetFillStyle(4000)
pada.SetFillColor(0)
pada.Draw()
pada.cd()

label.SetFillColor(0)
label.SetLineColor(0)
label.SetShadowColor(0)
label.SetTextSize(0.175)
label.AddText("RAT 4.5.0 production, scintillator phase")
label.AddText("MC simulations")
label.Draw()

raw_input("RET to EXIT");

