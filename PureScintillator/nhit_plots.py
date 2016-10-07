#!/usr/bin/env python
import ROOT
import rat
import sys
import math

#get root files returend by BiPocuts.py or mergeddata.py and retrieve nhits histograms
filename_bi212 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Bi212_bipo212_2000.root")
h_bi212 = filename_bi212.Get("h_nhitspo")

filename_bi214 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Bi214_bipo212_2000.root")
h_bi214 = filename_bi214.Get("h_nhitspo")

filename_bi210 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Bi210_bipo212_2000.root")
h_bi210 = filename_bi210.Get("h_nhitspo")

filename_po212 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Po212_bipo212_2000.root")
h_po212 = filename_po212.Get("h_nhitspo")

filename_po214 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Po214_bipo212_2000.root")
h_po214 = filename_po214.Get("h_nhitspo")

filename_po210 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Po210_bipo212_2000.root")
h_po210 = filename_po210.Get("h_nhitspo")

filename_c14 = ROOT.TFile("/data/langrock/full_scint_analysis/root/C14_bipo212_2000.root")
h_c14 = filename_c14.Get("h_nhitspo")

filename_pb210 = ROOT.TFile("/data/langrock/full_scint_analysis/root/Pb210_bipo212_2000.root")
h_pb210 = filename_pb210.Get("h_nhitspo")

#scale each histogram by its entries
h_bi212.Scale(1/h_bi212.GetEntries())
h_bi214.Scale(1/h_bi214.GetEntries())
h_bi210.Scale(1/h_bi210.GetEntries())
h_po212.Scale(1/h_po212.GetEntries())
h_po214.Scale(1/h_po214.GetEntries())
h_po210.Scale(1/h_po210.GetEntries())
h_c14.Scale(1/h_c14.GetEntries())
h_pb210.Scale(1/h_pb210.GetEntries())

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

#draw histograms
c1 = ROOT.TCanvas("c1","c1",1)
c1.Draw()
c1.SetLogy(1)

l1 = ROOT.TLegend(0.7,0.5,0.85,0.85,"","brNDC")

pada = ROOT.TPad("pada","pada",0.2,0.76,0.65,0.96)
label = ROOT.TPaveText(0.05,0.0,0.95,0.4,"br")


h_c14.SetXTitle("n_{hits}")
h_c14.SetYTitle("Ratio of events per 10 hits bin")
h_c14.SetAxisRange(0.001,1,"Y")
h_c14.SetLineColor(1)
h_c14.SetLineWidth(2)
h_c14.Draw()

h_bi210.SetLineColor(33)
h_bi210.SetLineWidth(2)
h_bi210.Draw("same")

h_po212.SetLineColor(43)
h_po212.SetLineWidth(2)
h_po212.Draw("same")

h_po214.SetLineColor(23)
h_po214.SetLineWidth(2)
h_po214.Draw("same")

h_po210.SetLineColor(13)
h_po210.SetLineWidth(2)
h_po210.Draw("same")

h_pb210.SetLineColor(41)
h_pb210.SetLineWidth(2)
h_pb210.Draw("same")

h_bi212.SetLineColor(597)
h_bi212.SetLineWidth(3)
h_bi212.Draw("same")

h_bi214.SetLineColor(50)
h_bi214.SetLineWidth(3)
h_bi214.Draw("same")

l1.AddEntry(h_bi212,"Bi212", "l")
l1.AddEntry(h_bi214,"Bi214", "l")
l1.AddEntry(h_bi210,"Bi210", "l")
l1.AddEntry(h_po212,"Po212", "l")
l1.AddEntry(h_po214,"Po214", "l")
l1.AddEntry(h_po210,"Po210", "l")
l1.AddEntry(h_c14,"C14", "l")
l1.AddEntry(h_pb210,"Pb210", "l")
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

