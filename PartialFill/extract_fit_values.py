#!/usr/bin/env python
import ROOT
import rat
import math
import plot_style
import os
import fnmatch

def get_filllevelgraph():
    """Function to create graph showing the fill level for each day
    """
    #define graph
    gr_filllevel = ROOT.TGraph(91)

    infile = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")
    l = 0

    #run through file and fill graph with fill level for each day
    for line in infile:
        words = line.split()

        gr_filllevel.SetPoint(l,float(words[0]), float(words[1]))
    
        l +=1

    return gr_filllevel

def get_time_vs_z(time_z, tree):
    """Function to plot the z position of an event version the fill day
    """

    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        time = tree.uTDays
        z = tree.posz

        time_z.Fill(time,z)

    #get fill level graph
    gr = get_filllevelgraph()

    #draw histogram and graph
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    time_z.SetXTitle("t (days)")
    time_z.SetYTitle("z (mm)")
    time_z.SetTitleOffset(1.0,"Y")
    time_z.SetLabelSize(0.03,"Y")
    time_z.Draw("colz")

    c1.Modified()
    c1.Update()

    gr.SetLineColor(50)
    gr.SetLineWidth(3)
    gr.Draw("c same")

    c1.Modified()
    c1.Update()

    pad = ROOT.TPad("pada","pada",0.18,0.2,0.6,0.4)
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

    c1.Print("/data/langrock/PartialFill/" + isotope + "/plots/time_vs_z.png","png")

def get_time_vs_nhits(time_nhits, tree):
    """Function to plot the nhits of an event versus fill day
    """

    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        time = tree.uTDays
        nhits = tree.nhits

        time_nhits.Fill(time,nhits)

    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    time_nhits.SetXTitle("t (days)")
    time_nhits.SetYTitle("n_{hits}")
    time_nhits.SetTitleOffset(1.0,"Y")
    time_nhits.SetLabelSize(0.03,"Y")
    time_nhits.Draw("colz")

    pad = ROOT.TPad("pada","pada",0.18,0.5,0.6,0.7)
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

    c1.Print("/data/langrock/PartialFill/" + isotope + "/plots/time_vs_nhits.png","png")

def get_nhits_diff_times(tree):
    """Function to fill nhits histograms for three arbitrary fill days
    """

    h_nhits = ROOT.TH1D("time_nhits","",150, 0,1500)
    h_nhits_1 = ROOT.TH1D("time_nhits_1","",150, 0,1500)
    h_nhits_2 = ROOT.TH1D("time_nhits_2","",150, 0,1500)

    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        time = tree.uTDays
        nhits = tree.nhits

        if time == 1661:
            h_nhits.Fill(nhits)
        elif time == 1690:
            h_nhits_1.Fill(nhits)
        if time == 1730:
            h_nhits_2.Fill(nhits)

    #scale histograms to number of entries
    h_nhits.Scale(1/h_nhits.GetEntries())
    h_nhits_1.Scale(1/h_nhits_1.GetEntries())
    h_nhits_2.Scale(1/h_nhits_2.GetEntries())

    c1 = ROOT.TCanvas("c1","",1)
    c1.SetLogy(1)
    c1.Draw()
    h_nhits_2.SetXTitle("n_{hits}")
    h_nhits_2.SetYTitle("Intensity per 10 hits bin")
    h_nhits_2.Draw()

    h_nhits_1.SetLineColor(50)
    h_nhits_1.Draw("same")

    h_nhits.SetLineColor(30)
    h_nhits.Draw("same")

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

    l1 = ROOT.TLegend(0.60,0.3,0.8,0.45,"","brNDC")
    l1.AddEntry(h_nhits,"Day 1661", "l")
    l1.AddEntry(h_nhits_1,"Day 1690", "l")
    l1.AddEntry(h_nhits_2,"Day 1730", "l")
    l1.SetFillColor(0)
    l1.SetTextSize(0.03)
    l1.Draw("same")

    c1.Print("/data/langrock/PartialFill/plots/nhits_diffdays.pdf","pdf")

def get_r(h_r, tree):
    """Function to reconstructed radius of events
    """

    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)

        h_r.Fill(math.fabs(radius))

def get_nhits_vs_z(isotope, tree):
    """Function to plot the nhits progression for each fill level
    """
    number = 0

    #loop through the simulated days
    for d in range(1642,1734):

        #ignore day 1666 (no files for that day)
        if d == 1666:
            continue

        z_nhits = ROOT.TH2D("nhits_z","",150,-10000, 10000,150, 0,1500)

        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            z = tree.posz
            nhits = tree.nhits
            time = tree.uTDays

            if time == d:
                z_nhits.Fill(z,nhits)

        #plot histogram
        c1 = ROOT.TCanvas("c1","",1)
        c1.Draw()
        z_nhits.SetXTitle("z (mm)")
        z_nhits.SetYTitle("n_{hits}")
        z_nhits.SetTitleOffset(1.0,"Y")
        z_nhits.SetLabelSize(0.03,"Y")
        z_nhits.SetAxisRange(0,1000,"Y")
        z_nhits.SetAxisRange(0,28,"Z")
        z_nhits.Draw("colz")

        pad = ROOT.TPad("pada","pada",0.18,0.75,0.6,0.95)
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

        c1.Print("/data/langrock/PartialFill/" + isotope + "/plots/z_vs_nhits-" + str(number) + ".png","png")

        number += 1

        z_nhits.Delete()

def get_nhits(isotope, tree):
    """Function to get nhits histogram for each day
    """

    #loop through range of simulated days
    for d in range(1642,1743):

        h_nhits = ROOT.TH1D("nhits","",150, 0,1500)

        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            nhits = tree.nhits
            time = tree.uTDays

            if time == d:
                h_nhits.Fill(nhits)

        #plot histogram
        c1 = ROOT.TCanvas("c1","",1)
        c1.Draw()
        h_nhits.SetXTitle("n_{hits}")
        h_nhits.SetYTitle("Intensity per 10 hits bin")
        h_nhits.Draw()

        pad = ROOT.TPad("pada","pada",0.48,0.6,0.9,0.8)
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

        c1.Print("/data/langrock/PartialFill/" + isotope + "/plots/nhits_" + str(d) + ".pdf","pdf")

        h_nhits.Delete()

def get_rfit_vs_r(isotope, tree):
    """Function to plot true event radius versus fitted event radius
    """

    #loop through range of simulated days
    for d in range(1642,1743):

        r_fit_r = ROOT.TH2D("r_fit_r","",100, 0.0, 2000.0, 300, 0.0, 8000.0)

        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            x = tree.posx
            y = tree.posy
            z = tree.posz
            mcx = tree.mcPosx
            mcy = tree.mcPosy
            mcz = tree.mcPosz

            radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
            mc_radius = math.sqrt(tree.mcPosx*tree.mcPosx+tree.mcPosy*tree.mcPosy+tree.mcPosz*tree.mcPosz)

            delta_r = math.sqrt(math.pow((mcx - x),2) + math.pow((mcy - y),2) + math.pow((mcz - z),2))
            time = tree.uTDays

            if time == d:

                r_fit_r.Fill(math.fabs(delta_r),math.fabs(mc_radius))

        #plot histogram
        c1 = ROOT.TCanvas("c1","",1)
        c1.Draw()
        r_fit_r.SetXTitle("|r_{mc} - r_{fit}| (mm)")
        r_fit_r.SetYTitle("|r_{mc}| (mm)")
        r_fit_r.SetTitleOffset(1.0,"Y")
        r_fit_r.SetLabelSize(0.03,"Y")
        r_fit_r.SetLabelSize(0.03,"X")
        r_fit_r.Draw("colz")

        pad = ROOT.TPad("pada","pada",0.18,0.2,0.6,0.4)
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

        c1.Print("/data/langrock/PartialFill/" + isotope + "/plots/r_fit_vs_r_" + str(d) + ".png","png")

        r_fit_r.Delete()

def get_rfit_vs_z(isotope, tree):
    """Plot true z position of events versus reconstructed event radius
    """

    #loop through range of simulated days
    for d in range(1642,1743):

        r_fit_z = ROOT.TH2D("r_fit_z","",100, 0.0, 2000.0, 150, -10000.0, 10000.0)

        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            x = tree.posx
            y = tree.posy
            z = tree.posz
            mcx = tree.mcPosx
            mcy = tree.mcPosy
            mcz = tree.mcPosz

            delta_r = math.sqrt(math.pow((mcx - x),2) + math.pow((mcy - y),2) + math.pow((mcz - z),2))
            time = tree.uTDays

            if time == d:

                r_fit_z.Fill(math.fabs(delta_r),mcz)

        #plot histogram
        c1 = ROOT.TCanvas("c1","",1)
        c1.Draw()
        r_fit_z.SetXTitle("|r_{mc} - r_{fit}| (mm)")
        r_fit_z.SetYTitle("z_{mc} (mm)")
        r_fit_z.SetTitleOffset(1.0,"Y")
        r_fit_z.SetLabelSize(0.03,"Y")
        r_fit_z.SetLabelSize(0.03,"X")
        r_fit_z.Draw("colz")

        pad = ROOT.TPad("pada","pada",0.15,0.2,0.57,0.4)
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

        c1.Print("/data/langrock/PartialFill/" + isotope + "/plots/r_fit_vs_z_" + str(d) + ".png","png")

        r_fit_z.Delete()

def get_rfit_vs_nhits(isotope, tree):
    """Function to plot the reconstructed event radius versus the nhits in the fiducial volume 
    """
        r_fit_nhits = ROOT.TH2D("r_fit_nhits","",150, 0,1500, 200, 0.0, 5000.0)

        #get file with fill days and fill levels
        read_infile = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")

        for line in read_infile:
            words = line.split()

            if len(words)!=0:

                d = float(words[0])
                z_level = float(words[1])
        
                for i in range(tree.GetEntries()):                           
                    tree.GetEntry(i)
                    nhits = tree.nhits
                    radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                    evIndex = tree.evIndex
                    z = tree.posz
                    
                    day = tree.uTDays

                    fidvol_value = 5000

                    if d == day:

                        #apply fiducial volume cut
                        if radius> 0 and radius < fidvol_value and z >= z_level+653 and evIndex==0:

                            r_fit_nhits.Fill(nhits,radius)

        #plot histogram
        c1 = ROOT.TCanvas("c1","",1)
        c1.Draw()
        r_fit_nhits.SetXTitle("n_{hits}")
        r_fit_nhits.SetYTitle("r (mm)")
        r_fit_nhits.SetTitleOffset(1.0,"Y")
        r_fit_nhits.SetLabelSize(0.03,"Y")
        r_fit_nhits.SetLabelSize(0.03,"X")
        r_fit_nhits.Draw("colz")

        pad = ROOT.TPad("pada","pada",0.48,0.2,0.9,0.4)
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

        c1.Print("/users/langrock/Dropbox/Thesis/Images/Backgrounds/" + isotope + "r_vs_nhits.png","png")

        r_fit_nhits.Delete()



def cut_r(tree):
    """Function to get events within a certain event radius
    """
    events_all = 0
    events_r = 0

    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)

        events_all += 1

        if radius < 5000:
            events_r += 1

    print events_all, events_r

def r_external(tree):
    """Function to plot the reconstructed event radius for external backgrounds for fill levels above and below the equator
    """

    r_above = ROOT.TH1D("r_above","",300, 0.0, 8000.0)
    r_below = ROOT.TH1D("r_below","",300, 0.0, 8000.0)     
    
    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
        time = tree.uTDays

        if time <= 1686:
            r_above.Fill(radius)

        elif time > 1686:
            r_below.Fill(radius)


    #plot histograms
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    r_below.SetXTitle("r (mm)")
    r_below.SetYTitle("Intensity per 26.7mm")
    r_below.SetTitleOffset(1.0,"Y")
    r_below.SetLabelSize(0.03,"Y")
    r_below.SetLabelSize(0.03,"X")
    r_below.SetLineColor(50)
    r_below.Draw()

    r_above.SetLineColor(30)
    r_above.Draw("same")

    pad = ROOT.TPad("pada","pada",0.18,0.5,0.6,0.7)
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

    l1 = ROOT.TLegend(0.20,0.4,0.4,0.6,"","brNDC")
    l1.AddEntry(r_above,"z_k >= 0", "l")
    l1.AddEntry(r_below,"z_k < 0", "l")
    l1.SetFillColor(0)
    l1.SetTextSize(0.03)
    l1.Draw("same")

    c1.Print("/data/langrock/PartialFill/plots/Externals_radius.pdf","pdf")       


if __name__ == '__main__':

    #get plot style
    style = plot_style.PlotStyle()
    style.set_style()
    ROOT.gROOT.SetStyle("clearRetro")

    #run through directory containing the input root files
    for root, dirs, filenames in os.walk("/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/"):
        for x in filenames:
            #find matching files
            if fnmatch.fnmatch(x, "*_Scint.ntuple.root"):
                infile = "/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/" + x

                components = x.split("_")
                if len(components)!=0:

                    #open file and get tree
                    filename = ROOT.TFile(infile)
                    treename = filename.Get("output")

                    #run different plot scripts
                    get_nhits_diff_times(treename)
                    r_external(treename)
                    get_rfit_vs_nhits(components[0], treename) 
                    cut_r(treename)

                    #create directory to save output root files
                    outdir = "/data/langrock/PartialFill/" + components[0] 
                    if not os.path.exists(outdir):
                        os.makedirs(outdir)
                  
                    #create output root file
                    outputroot = ROOT.TFile(outdir + "/" + components[0] + ".root","recreate")

                    #define histograms
                    time_z = ROOT.TH2D("time_z","",100,1642, 1742,150, -10000,10000)
                    time_nhits = ROOT.TH2D("time_nhits","",100,1642, 1742,150, 0,1500)
                    h_r = ROOT.TH1D("h_r","",300, 0.0, 8000.0)   

                    get_time_vs_z(time_z, treename)
                    get_time_vs_nhits(time_nhits, treename)
                    get_r(h_r, treename)

                    #write histograms to file
                    outputroot.Write()
                    outputroot.Close()


    raw_input("RET to exit")
