#!/usr/bin/env python
import ROOT
import rat
import sys
import math

#define what background isotope to plot and which cut (bipo212 or bipo214) to look at
isotope = sys.argv[1]
cut = sys.argv[2]

#open file and get histograms to plot - needs the root files returned by either BiPocuts.py or mergeddata.py 
filename = ROOT.TFile("/data/langrock/te_loaded_mergeddata/single_te_loaded_root/" + isotope + "_" + cut + "_1500.root")
h_time = filename.Get("h_deltat")
h_radius = filename.Get("h_deltar")
h_rfidvolbi = filename.Get("h_rfidvolbi")

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

#draw time difference histogram
c1 = ROOT.TCanvas("c1","c1",1)
c1.Draw()

pada = ROOT.TPad("pada","pada",0.4,0.46,0.89,0.66)
label = ROOT.TPaveText(0.05,0.0,0.95,0.4,"br")

h_time.Rebin(100)

h_time.SetXTitle("#Delta t (ns)")
h_time.SetYTitle("Hits per 18000ns interval")
h_time.SetAxisRange(0,1799000,"X")
h_time.SetTitleOffset(1.2,"y")
h_time.SetLineColor(30)
h_time.SetLineWidth(2)
h_time.Draw()

pada.SetFillStyle(4000)
pada.SetFillColor(0)
pada.Draw()
pada.cd()

label.SetFillColor(0)
label.SetLineColor(0)
label.SetShadowColor(0)
label.SetTextSize(0.175)
label.AddText("RAT 5.0.2 production, Tellurium loaded phase")
label.AddText("MC simulations")
label.Draw()

#draw event distance histogram
c2 = ROOT.TCanvas("c2","c2",1)
c2.Draw()
c2.SetLogy(1)

padb = ROOT.TPad("padb","padb",0.4,0.6,0.89,0.8)
label1 = ROOT.TPaveText(0.05,0.0,0.95,0.4,"br")

h_radius.SetXTitle("#Delta r (mm)")
h_radius.SetYTitle("Events per 40mm bins")
h_radius.SetLineColor(30)
h_radius.SetLineWidth(2)
h_radius.Draw()

padb.SetFillStyle(4000)
padb.SetFillColor(0)
padb.Draw()
padb.cd()

label1.SetFillColor(0)
label1.SetLineColor(0)
label1.SetShadowColor(0)
label1.SetTextSize(0.175)
label1.AddText("RAT 5.0.2 production, Tellurium loaded phase")
label1.AddText("MC simulations")
label1.Draw()

#draw radius histogram
c3 = ROOT.TCanvas("c3","c3",1)
c3.Draw()
c3.SetLogy(1)

padc = ROOT.TPad("padc","padc",0.3,0.25,0.79,0.45)
label2 = ROOT.TPaveText(0.05,0.0,0.95,0.4,"br")

h_rfidvolbi.SetXTitle("r (mm)")
h_rfidvolbi.SetYTitle("Events per 40mm bins")
h_rfidvolbi.SetLineColor(30)
h_rfidvolbi.SetLineWidth(2)
h_rfidvolbi.Draw()

padc.SetFillStyle(4000)
padc.SetFillColor(0)
padc.Draw()
padc.cd()

label2.SetFillColor(0)
label2.SetLineColor(0)
label2.SetShadowColor(0)
label2.SetTextSize(0.175)
label2.AddText("RAT 5.0.2 production, Tellurium loaded phase")
label2.AddText("MC simulations")
label2.Draw()

raw_input("RET to EXIT");

