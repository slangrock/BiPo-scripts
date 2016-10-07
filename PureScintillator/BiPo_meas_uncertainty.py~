#!/usr/bin/env python
import ROOT
import sys
import math

def Thchainuncertainty(scale_other, scale_solar, scale_thchain, scale_uchain, scale_leaching, scale_signal):
    """Function to calculate the uncertainty progression for the BiPo212 measurement during a 6 months scintillator run

     Args:
      scale_other (float) : scale factor to apply to non uchain, thchain, leaching or solar backgrounds
      scale_solar (float) : scale factor to apply to solar events
      scale_thchain (float) : scale factor to apply to thchain events, needs to be the same as scale_signal
      scale_uchain (float) : scale factor to apply to uchain events
      scale_leaching (float) : scale factor to apply to leaching backgrounds
      scale_signal (float): scale factor to apply to BiPo212 events, needs to be the same as scale_thchain
    """

    #define rates for backgrounds after applying plonium and bismuth nhits cuts
    u_chain_rate_pocut = 0.000031940
    u_chain_rate_bicut = 0.001527898
    th_chain_rate_pocut = 0.000022391
    th_chain_rate_bicut = 0.000198704
    solar_rate_pocut = 0.0000723226
    solar_rate_bicut = 0.0014495122
    other_rate_pocut = 0.0000364407
    other_rate_bicut = 0.0088036094

    #leaching backgrounds - pb210 gets completely rejected by nhits cuts. rates are for each month during a 6 month period
    po210_rate_pocut = [0.000046613, 0.000051550, 0.000057407, 0.000063146, 0.000069080, 0.000074203]
    po210_rate_bicut = [15.79891682, 17.47204609, 19.4571237, 21.40229874, 23.41366865, 25.1499948]
    bi210_rate_pocut = [0.247402731, 0.27480601, 0.30722337, 0.338979616, 0.371821282, 0.400236734]
    bi210_rate_bicut = [10.21168707, 11.34277287, 12.68081766, 13.99157458, 15.34713285, 16.51999664]
    
    #random po212 and random bi212 selected by the cuts
    po_mistag = 0.000016596
    bi_mistag = 0.000020679

    #expected rate of BiPo212 coincidences, efficiency of the BiPo212 cuts and the uncertainty on the efficiency
    bipo_rate = 0.0000138121547
    bipo_cut_eff = 0.075
    bipo_cut_eff_error = math.sqrt(math.pow(0.00098,2) + math.pow(0.019,2))

    #define output textfile
    outputfile = open("Thchain_other" + str(scale_other) + "_solar" + str(scale_solar) + "_tchain" + str(scale_thchain) + "_uchain" + str(scale_uchain) + "_leaching" + str(scale_leaching) + "_signal" + str(scale_signal) + ".txt",'w')

    #calculate overall backgrounds rate for the polonium and bismuth nhits cuts over 181 days. needs to be split into monthly intervalls due to the changing leaching rates
    for i in range(0,182):
        backgrounds_rate_po = 0
        backgrounds_rate_bi = 0

        if i <= 31:
            backgrounds_rate_po = u_chain_rate_pocut*scale_uchain + (th_chain_rate_pocut - po_mistag)*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[0]*scale_leaching + bi210_rate_pocut[0]*scale_leaching
            backgrounds_rate_bi = u_chain_rate_bicut*scale_uchain + (th_chain_rate_bicut - bi_mistag)*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + po210_rate_bicut[0]*scale_leaching + bi210_rate_bicut[0]*scale_leaching
        elif i > 31 and i <= 59:
            backgrounds_rate_po = u_chain_rate_pocut*scale_uchain + (th_chain_rate_pocut - po_mistag)*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[1]*scale_leaching + bi210_rate_pocut[1]*scale_leaching
            backgrounds_rate_bi = u_chain_rate_bicut*scale_uchain + (th_chain_rate_bicut - bi_mistag)*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + po210_rate_bicut[1]*scale_leaching + bi210_rate_bicut[1]*scale_leaching
        elif i > 59 and i <= 90:
            backgrounds_rate_po = u_chain_rate_pocut*scale_uchain + (th_chain_rate_pocut - po_mistag)*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[2]*scale_leaching + bi210_rate_pocut[2]*scale_leaching
            backgrounds_rate_bi = u_chain_rate_bicut*scale_uchain + (th_chain_rate_bicut - bi_mistag)*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + po210_rate_bicut[2]*scale_leaching + bi210_rate_bicut[2]*scale_leaching 
        elif i > 90 and i <= 120:
            backgrounds_rate_po = u_chain_rate_pocut*scale_uchain + (th_chain_rate_pocut - po_mistag)*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[3]*scale_leaching + bi210_rate_pocut[3]*scale_leaching
            backgrounds_rate_bi = u_chain_rate_bicut*scale_uchain + (th_chain_rate_bicut - bi_mistag)*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + po210_rate_bicut[3]*scale_leaching + bi210_rate_bicut[3]*scale_leaching
        elif i > 120 and i <= 151:
            backgrounds_rate_po = u_chain_rate_pocut*scale_uchain + (th_chain_rate_pocut - po_mistag)*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[4]*scale_leaching + bi210_rate_pocut[4]*scale_leaching
            backgrounds_rate_bi = u_chain_rate_bicut*scale_uchain + (th_chain_rate_bicut - bi_mistag)*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + po210_rate_bicut[4]*scale_leaching + bi210_rate_bicut[4]*scale_leaching
        else:
            backgrounds_rate_po = u_chain_rate_pocut*scale_uchain + (th_chain_rate_pocut - po_mistag)*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[5]*scale_leaching + bi210_rate_pocut[5]*scale_leaching
            backgrounds_rate_bi = u_chain_rate_bicut*scale_uchain + (th_chain_rate_bicut - bi_mistag)*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + po210_rate_bicut[5]*scale_leaching + bi210_rate_bicut[5]*scale_leaching

        #calculate number of mistagged polonium candidates and mistagging probability of the bismuth candidate
        n_po_mis = backgrounds_rate_po * 3600 * 24 * i * math.pow(4,3)/math.pow(6,3)
        n_po_true = po_mistag * 3600 * 24 * i
        p_bi_mis = 1 - math.exp(-backgrounds_rate_bi * 0.00000347 * math.pow(2,3)/math.pow(6,3))
        p_bi_true = 1 - math.exp(-bi_mistag * 0.00000347 * math.pow(2,3)/math.pow(6,3))

        #calculate mistagged events for each day, including the mistags from the partial fill phase (19.42 - partial fill scintillator volume mistags, math.pow(10,-8) - water volume mistags, 0.005 - combined water-scintillator volume mistags)
        n_coinc_mis = n_po_mis*p_bi_mis + n_po_true*p_bi_mis + n_po_mis*p_bi_true + 19.42 + 8 * math.pow(10,-8) + 0.005

        #calculate remaining BiPo212 coincidences for each day, including the BiPo212 coincidences selected from the partial fill phase (11.04*scale_signal)
        bipo_allcuts = bipo_rate*scale_signal * bipo_cut_eff * 3600 * 24 * i + 11.04*scale_signal
        bipo = bipo_rate*scale_signal * 3600 * 24 * i

        #get all selected coincidences and uncertainties
        counted_coinc = bipo_allcuts + n_coinc_mis
        delta_counted_coinc = math.sqrt(bipo_allcuts + n_coinc_mis)

        syst_err = bipo_cut_eff_error/bipo_cut_eff*bipo_allcuts
        syst_err = 0
        delta_meas_content = math.sqrt(math.pow(delta_counted_coinc,2) + math.pow(syst_err,2))

        #calculate uncertainty on the measurement for each day
        uncertainty = 0
        if bipo_allcuts > 0:
            uncertainty = delta_meas_content/bipo_allcuts*100

        #write results to file for each day
        output_string =  "day: " + str(i) + " \t n_coinc_miss: " + str(n_coinc_mis) + "\t bipo_allcuts: " + str(bipo_allcuts) + "\t stat_uncert: " + str(delta_counted_coinc) + "\t syst_uncer: " + str(syst_err) + "\t uncertanity: " + str(uncertainty) + "\n"
        outputfile.write(output_string)

    outputfile.close()


def Uchainuncertainty(scale_other, scale_solar, scale_thchain, scale_uchain, scale_leaching, scale_signal):
    """Function to calculate the uncertainty progression for the BiPo212 measurement during a 6 months scintillator run

     Args:
      scale_other (float) : scale factor to apply to non uchain, thchain, leaching or solar backgrounds
      scale_solar (float) : scale factor to apply to solar events
      scale_thchain (float) : scale factor to apply to thchain events
      scale_uchain (float) : scale factor to apply to uchain events, needs to be the same as scale_signal
      scale_leaching (float) : scale factor to apply to leaching backgrounds
      scale_signal (float): scale factor to apply to BiPo212 events, needs to be the same as scale_uchain
    """

    #define rates for backgrounds after applying plonium and bismuth nhits cuts
    u_chain_rate_pocut = 0.000255233
    u_chain_rate_bicut = 0.000165358
    th_chain_rate_pocut = 0.000043019
    th_chain_rate_bicut = 0.000024082
    solar_rate_pocut = 0.0002638602
    solar_rate_bicut = 0.0000870058
    other_rate_pocut = 0.000077439
    other_rate_bicut = 0.000027392

    #leaching backgrounds - pb210 gets completely rejected by nhits cuts. rates are for each month during a 6 month period
    po210_rate_pocut = [0.00107211, 0.001185648, 0.001320355, 0.001452354, 0.001588845, 0.001706672]
    po210_rate_bicut = 0
    bi210_rate_pocut = [2.015238883, 2.238454504, 2.502512723, 2.761185779, 3.028700218, 3.260160573]
    bi210_rate_bicut = [0.001715097, 0.001905068, 0.002129798, 0.002349945, 0.002577617, 0.002774605]

    #random po214 and random bi214 selected by the cuts   
    po_mistag = 0.000146942
    bi_mistag = 0.000135001

    #expected rate of BiPo214 coincidences, efficiency of the BiPo212 cuts and the uncertainty on the efficiency
    bipo_rate = 0.0001552589
    bipo_cut_eff = 0.165
    bipo_cut_eff_error = math.sqrt(math.pow(0.00225,2) + math.pow(0.009,2))

    #define output textfile
    outputfile = open("Uchain_other" + str(scale_other) + "_solar" + str(scale_solar) + "_tchain" + str(scale_thchain) + "_uchain" + str(scale_uchain) + "_leaching" + str(scale_leaching) + "_signal" + str(scale_signal) + ".txt",'w')

    #calculate overall backgrounds rate for the polonium and bismuth nhits cuts over 181 days. needs to be split into monthly intervalls due to the changing leaching rates
    for i in range(0,182):
        backgrounds_rate_po = 0
        backgrounds_rate_bi = 0

        if i <= 31:
            backgrounds_rate_po = (u_chain_rate_pocut - po_mistag)*scale_uchain + th_chain_rate_pocut*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[0]*scale_leaching + bi210_rate_pocut[0]*scale_leaching
            backgrounds_rate_bi = (u_chain_rate_bicut - bi_mistag)*scale_uchain + th_chain_rate_bicut*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + bi210_rate_bicut[0]*scale_leaching
        elif i > 31 and i <= 59:
            backgrounds_rate_po = (u_chain_rate_pocut - po_mistag)*scale_uchain + th_chain_rate_pocut*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[1]*scale_leaching + bi210_rate_pocut[1]*scale_leaching
            backgrounds_rate_bi = (u_chain_rate_bicut - bi_mistag)*scale_uchain + th_chain_rate_bicut*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + bi210_rate_bicut[1]*scale_leaching
        elif i > 59 and i <= 90:
            backgrounds_rate_po = (u_chain_rate_pocut - po_mistag)*scale_uchain + th_chain_rate_pocut*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[2]*scale_leaching + bi210_rate_pocut[2]*scale_leaching
            backgrounds_rate_bi = (u_chain_rate_bicut - bi_mistag)*scale_uchain + th_chain_rate_bicut*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + bi210_rate_bicut[2]*scale_leaching
        elif i > 90 and i <= 120:
            backgrounds_rate_po = (u_chain_rate_pocut - po_mistag)*scale_uchain + th_chain_rate_pocut*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[3]*scale_leaching + bi210_rate_pocut[3]*scale_leaching
            backgrounds_rate_bi = (u_chain_rate_bicut - bi_mistag)*scale_uchain + th_chain_rate_bicut*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + bi210_rate_bicut[3]*scale_leaching
        elif i > 120 and i <= 151:
            backgrounds_rate_po = (u_chain_rate_pocut - po_mistag)*scale_uchain + th_chain_rate_pocut*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[4]*scale_leaching + bi210_rate_pocut[4]*scale_leaching
            backgrounds_rate_bi = (u_chain_rate_bicut - bi_mistag)*scale_uchain + th_chain_rate_bicut*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + bi210_rate_bicut[4]*scale_leaching
        else:
            backgrounds_rate_po = (u_chain_rate_pocut - po_mistag)*scale_uchain + th_chain_rate_pocut*scale_thchain + solar_rate_pocut*scale_solar + other_rate_pocut*scale_other + po210_rate_pocut[5]*scale_leaching + bi210_rate_pocut[5]*scale_leaching
            backgrounds_rate_bi = (u_chain_rate_bicut - bi_mistag)*scale_uchain + th_chain_rate_bicut*scale_thchain + solar_rate_bicut*scale_solar + other_rate_bicut*scale_other + bi210_rate_bicut[5]*scale_leaching

 
        #calculate number of mistagged polonium candidates and mistagging probability of the bismuth candidate
        n_po_mis = backgrounds_rate_po * 3600 * 24 * i * math.pow(4,3)/math.pow(6,3)
        n_po_true = po_mistag * 3600 * 24 * i
        p_bi_mis = 1 - math.exp(-backgrounds_rate_bi * 0.0018 * math.pow(2,3)/math.pow(6,3))
        p_bi_true = 1 - math.exp(-bi_mistag * 0.0018 * math.pow(2,3)/math.pow(6,3))

        #calculate mistagged events for each day, including the mistags from the partial fill phase (0.90 - partial fill scintillator volume mistags, 2.58*math.pow(10,-5) - water volume mistags, 0.34 - combined water-scintillator volume mistags)
        n_coinc_mis = n_po_mis*p_bi_mis + n_po_true*p_bi_mis + n_po_mis*p_bi_true + 0.90 + 2.58 * math.pow(10,-5) + 0.34

        #calculate remaining BiPo212 coincidences for each day, including the BiPo212 coincidences selected from the partial fill phase (208.18*scale_signal)
        bipo_allcuts = bipo_rate*scale_signal * bipo_cut_eff * 3600 * 24 * i + 208.18*scale_signal

        #get all selected coincidences and uncertainties
        counted_coinc = bipo_allcuts + n_coinc_mis
        delta_counted_coinc = math.sqrt(bipo_allcuts + n_coinc_mis)

        syst_err = bipo_cut_eff_error/bipo_cut_eff*bipo_allcuts
        syst_err = 0
        delta_meas_content = math.sqrt(math.pow(delta_counted_coinc,2) + math.pow(syst_err,2))

        #calculate uncertainty on the measurement for each day
        uncertainty = 0
        if bipo_allcuts > 0:
            uncertainty = delta_meas_content/bipo_allcuts*100

        #calculate uncertainty on the measurement for each day
        output_string =  "day: " + str(i) + " \t n_coinc_miss: " + str(n_coinc_mis) + "\t bipo_allcuts: " + str(bipo_allcuts) + "\t stat_uncert: " + str(delta_counted_coinc) + "\t syst_uncer: " + str(syst_err) + "\t uncertanity: " + str(uncertainty) + "\n"
        outputfile.write(output_string)
        
    outputfile.close()

def create_plot(graph, input_file):
    """Read from file produce by the above functions to plot progression of uncertainty over 6 months.
    """
    inputfile = open(input_file,'r')

    months = 0
    #loop over file
    for line in inputfile:
        words = line.split()
        if len(words)!=0:
            #get day and uncertainty
            day = float(words[1])
            uncertainty = float(words[11])

            #if day is multiple of 30, set marker point
            if (day/30)%1 == 0 and (day/30) > 0:
                graph.SetPoint(months, day, uncertainty)
                months += 1

if __name__ == '__main__':
    #run thuncertainty and uchainuncertainty for different background scenarios
    Thchainuncertainty(1, 1, 1, 1, 1, 1)
    Thchainuncertainty(10, 1, 1, 1, 1, 1)
    Thchainuncertainty(1, 10, 1, 1, 1, 1)
    Thchainuncertainty(1, 1, 10, 1, 1, 10)
    Thchainuncertainty(1, 1, 1, 10, 1, 1)
    Thchainuncertainty(1, 1, 1, 1, 10, 1)
    Thchainuncertainty(10, 10, 1, 10, 1, 1)
    Thchainuncertainty(1, 1, 1, 1, 2, 1)
    Thchainuncertainty(1, 1, 1, 1, 3, 1)
    Thchainuncertainty(1, 1, 1, 1, 4, 1)
    Thchainuncertainty(1, 1, 1, 1, 5, 1)
    Thchainuncertainty(1, 1, 1, 1, 6, 1)
    Thchainuncertainty(1, 1, 1, 1, 7, 1)
    Thchainuncertainty(1, 1, 1, 1, 8, 1)
    Thchainuncertainty(1, 1, 1, 1, 9, 1)
    Thchainuncertainty(1, 1, 1, 1, 0.1, 1)
    Thchainuncertainty(1, 1, 0.9, 1, 1, 0.9)
    Thchainuncertainty(1, 1, 0.8, 1, 1, 0.8)
    Thchainuncertainty(1, 1, 0.7, 1, 1, 0.7)
    Thchainuncertainty(1, 1, 0.6, 1, 1, 0.6)
    Thchainuncertainty(1, 1, 0.5, 1, 1, 0.5)
    Thchainuncertainty(1, 1, 0.4, 1, 1, 0.4)
    Thchainuncertainty(1, 1, 0.3, 1, 1, 0.3)
    Thchainuncertainty(1, 1, 0.2, 1, 1, 0.2)
    Thchainuncertainty(1, 1, 0.1, 1, 1, 0.1)

    Uchainuncertainty(1, 1, 1, 1, 1, 1)
    Uchainuncertainty(10, 1, 1, 1, 1, 1)
    Uchainuncertainty(1, 10, 1, 1, 1, 1)
    Uchainuncertainty(1, 1, 10, 1, 1, 1)
    Uchainuncertainty(1, 1, 1, 10, 1, 10)
    Uchainuncertainty(1, 1, 1, 1, 10, 1)
    Uchainuncertainty(10, 10, 10, 1, 1, 1)
    Uchainuncertainty(1, 1, 1, 1, 2, 1)
    Uchainuncertainty(1, 1, 1, 1, 3, 1)
    Uchainuncertainty(1, 1, 1, 1, 4, 1)
    Uchainuncertainty(1, 1, 1, 1, 5, 1)
    Uchainuncertainty(1, 1, 1, 1, 6, 1)
    Uchainuncertainty(1, 1, 1, 1, 7, 1)
    Uchainuncertainty(1, 1, 1, 1, 8, 1)
    Uchainuncertainty(1, 1, 1, 1, 9, 1)
    Uchainuncertainty(1, 1, 1, 1, 0.1, 1)
    Uchainuncertainty(1, 1, 1, 0.9, 1, 0.9)
    Uchainuncertainty(1, 1, 1, 0.8, 1, 0.8)
    Uchainuncertainty(1, 1, 1, 0.7, 1, 0.7)
    Uchainuncertainty(1, 1, 1, 0.6, 1, 0.6)
    Uchainuncertainty(1, 1, 1, 0.5, 1, 0.5)
    Uchainuncertainty(1, 1, 1, 0.4, 1, 0.4)
    Uchainuncertainty(1, 1, 1, 0.3, 1, 0.3)
    Uchainuncertainty(1, 1, 1, 0.2, 1, 0.2)
    Uchainuncertainty(1, 1, 1, 0.1, 1, 0.1)

    #make some plots ------------------------------------
    graph_th_normal = ROOT.TGraph(6)
    graph_th_partial = ROOT.TGraph(6)
    graph_th_10 = ROOT.TGraph(6)
    graph_th_leach_0p1 = ROOT.TGraph(6)
    graph_th_leach_5 = ROOT.TGraph(6)

    create_plot(graph_th_normal, "../Backgrounds/Thchain_other1_solar1_tchain1_uchain1_leaching1_signal1_nosys.txt")
    create_plot(graph_th_partial, "Thchain_other1_solar1_tchain1_uchain1_leaching1_signal1.txt")

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

    #plot thchain progression
    c1 = ROOT.TCanvas()
    c1.Draw()

    l3 = ROOT.TLegend(0.5,0.6,0.85,0.85,"","brNDC")
    
    graph_th_partial.GetXaxis().SetTitle("time (days)")
    graph_th_partial.GetYaxis().SetTitle("Uncertainty (%)")
    graph_th_partial.SetMarkerSize(2)
    graph_th_partial.SetMarkerColor(30)
    graph_th_partial.SetLineWidth(2)
    graph_th_partial.SetLineColor(30)
    graph_th_partial.Draw("ac*")
    graph_th_partial.GetXaxis().SetRangeUser(0,180)
    graph_th_partial.GetYaxis().SetRangeUser(0,80)
    graph_th_partial.Draw("c*")

    c1.Update()

    graph_th_normal.SetMarkerSize(2)
    graph_th_normal.SetMarkerColor(50)
    graph_th_normal.SetLineWidth(2)
    graph_th_normal.SetLineColor(50)
    graph_th_normal.Draw("c* same")

    c1.Update()


    c1.Update()

    l3.AddEntry(graph_th_partial,"Partial + Scintillator", "lp")
    l3.AddEntry(graph_th_normal,"Pure Scintillator only", "lp")
    l3.SetFillColor(0)
    l3.SetTextSize(0.04)
    l3.Draw("same")

    c1.Update()

    c1.Print("/users/langrock/Dropbox/Thesis/Images/Backgrounds/Thchain_uncertainty.pdf","pdf")


    graph_u_normal = ROOT.TGraph(6)
    graph_u_partial = ROOT.TGraph(6)
    graph_u_10 = ROOT.TGraph(6)
    graph_u_leach_0p1 = ROOT.TGraph(6)
    graph_u_leach_10 = ROOT.TGraph(6)

    create_plot(graph_u_normal, "../Backgrounds/Uchain_other1_solar1_tchain1_uchain1_leaching1_signal1_nosyst.txt")
    create_plot(graph_u_partial, "Uchain_other1_solar1_tchain1_uchain1_leaching1_signal1.txt")

    #plot uchain progression
    c2 = ROOT.TCanvas()
    c2.Draw()

    l2 = ROOT.TLegend(0.5,0.6,0.85,0.85,"","brNDC")
    
    graph_u_partial.GetXaxis().SetTitle("time (days)")
    graph_u_partial.GetYaxis().SetTitle("Uncertainty (%)")
    graph_u_partial.SetMarkerSize(2)
    graph_u_partial.SetMarkerColor(30)
    graph_u_partial.SetLineWidth(2)
    graph_u_partial.SetLineColor(30)
    graph_u_partial.Draw("ac*")
    graph_u_partial.GetXaxis().SetRangeUser(0,180)
    graph_u_partial.GetYaxis().SetRangeUser(0,20)
    graph_u_partial.Draw("c*")

    c2.Update()

    graph_u_normal.SetMarkerSize(2)
    graph_u_normal.SetMarkerColor(50)
    graph_u_normal.SetLineWidth(2)
    graph_u_normal.SetLineColor(50)
    graph_u_normal.Draw("c* same")

    c2.Update()

    l2.AddEntry(graph_u_partial,"Partial + Scintillator", "lp")
    l2.AddEntry(graph_u_normal,"Pure Scintillator only", "lp")
    l2.SetFillColor(0)
    l2.SetTextSize(0.04)
    l2.Draw("same")

    c2.Update()

    c2.Print("/users/langrock/Dropbox/Thesis/Images/Backgrounds/Uchain_uncertainty.pdf","pdf")

raw_input("RET to EXIT");
