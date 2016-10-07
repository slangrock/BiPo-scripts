#!/usr/bin/env python
import ROOT
import rat
import math
import plot_style
import os
import fnmatch

def get_nhits(isotope,infile):
    """Function to calculate and plot the nhits cut efficiency progression versus different fill levels. Uses the text files as returned by dailycuts.py or nhitscuts.py

     Args:
      isotope (string) : background isotope the cuts were applied to
      infile (string) : name of the input text file
    """
    
    #define graph
    h_z = ROOT.TGraphErrors(91)
    i = 1

    #loop through input file
    for line in infile:
        words = line.split()
        if len(words)!=0:

            #get z level, number of events passing fiducial volume cut and number of events passing nhits cut
            z = float(words[1])
            n_radius = float(words[5])
            n_nhits = float(words[7])

            eff = 0

            #get uncertainty
            n_radius_error = math.sqrt(n_radius)
            n_nhits_error = math.sqrt(n_nhits)

            eff_error = 0

            #if no events are selected within the fiducial volume skip this fill level
            if n_radius == 0:
                i += 1
                continue

            #calculate efficiency
            else:
                eff = n_nhits/n_radius
                eff_error = math.sqrt(math.pow(n_nhits_error/n_radius,2) + math.pow((n_nhits * n_radius_error/math.pow(n_radius,2)),2))

            #set graph points
            h_z.SetPoint(i,z, eff)
            h_z.SetPointError(i, 0.0, eff_error)

            i += 1

    #draw graph and fit with linear function
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_z.GetXaxis().SetTitle("z_{fill} (mm)")
    h_z.GetYaxis().SetTitle("#epsilon(n_{hits})")
    h_z.Draw("ap")
    f1 = ROOT.TF1("f1","pol1",-6000, 4000)
    f1.SetLineColor(50)
    h_z.Fit(f1, "R")

    pad = ROOT.TPad("pada","pada",0.18,0.7,0.6,0.9)
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

    c1.Update()

    c1.Print("/data/langrock/PartialFill/plots/" + isotope + "_Po214_nhits_eff.pdf","pdf" )

    return f1.GetParameter(0), f1.GetParError(0), f1.GetParameter(1), f1.GetParError(1)

def get_fidvol_water(isotope,infile):
    """Function to calculate the efficiency of the fiducial volume cut on water volume events. Uses the text files as returned by dailycuts.py

     Args:
      isotope (string) : background isotope the cuts were applied to
      infile (string) : name of the input text file
    """

    #define graph
    h_z = ROOT.TGraphErrors(91)
    i = 1

    #loop through input file
    for line in infile:
        words = line.split()
        if len(words)!=0:

            #get z level, total number of events in file and events passing the fiducial volume cut
            z = float(words[1])
            n_total = float(words[3])
            n_radius = float(words[5])

            eff = 0

            #get uncertainty
            n_total_error = math.sqrt(n_total)
            n_radius_error = math.sqrt(n_radius)

            eff_error = 0

            #if no events are selected within the fiducial volume skip this fill level
            if n_total == 0:
                i += 1
                continue
               
            #calculate efficiency
            else:
                eff = n_radius/n_total
                eff_error = math.sqrt(math.pow(n_radius_error/n_total,2) + math.pow((n_radius * n_total_error/math.pow(n_total,2)),2))

            #set graph points
            h_z.SetPoint(i,z, eff)
            h_z.SetPointError(i, 0.0, eff_error)

            i += 1

    #draw graph and fit with linear function
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_z.GetXaxis().SetTitle("z_{fill} (mm)")
    h_z.GetYaxis().SetTitle("#epsilon(n_{hits})")
    h_z.Draw("ap")
    f1 = ROOT.TF1("f1","pol1",-6000, 4000)
    f1.SetLineColor(50)
    h_z.Fit(f1, "R")

    pad = ROOT.TPad("pada","pada",0.18,0.7,0.6,0.9)
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


    c1.Update()
    c1.Print("/data/langrock/PartialFill/plots/" + isotope + "_fidvol_water_eff.pdf","pdf" )

    return f1.GetParameter(0), f1.GetParError(0), f1.GetParameter(1), f1.GetParError(1)


def get_deltat(isotope, infile):
    """Function to calculate and plot the delta t cut efficiency progression versus different fill levels. Uses the text files as returned by dailycuts.py

     Args:
      isotope (string) : background isotope the cuts were applied to
      infile (string) : name of the input text file
    """

    #define graph
    h_z = ROOT.TGraphErrors(91)
    i = 1

    #loop through input file
    for line in infile:
        words = line.split()
        if len(words)!=0:

            #get z level, number of events passing the nhits cut and number of events passing the deltat cut
            z = float(words[1])
            n_nhits = float(words[7])
            n_deltat = float(words[9])

            eff = 0

            #get uncertainty
            n_nhits_error = math.sqrt(n_nhits)
            n_deltat_error = math.sqrt(n_deltat)

            eff_error = 0

            #if no events are selected within the nhits cut skip this fill level
            if n_nhits == 0:
                i += 1
                continue

            #calculate efficiency
            else:
                eff = n_deltat/n_nhits
                eff_error = math.sqrt(math.pow(n_deltat_error/n_nhits,2) + math.pow((n_deltat * n_nhits_error/math.pow(n_nhits,2)),2))

            #set graph points
            h_z.SetPoint(i,z, eff)
            h_z.SetPointError(i, 0.0, eff_error)

            i += 1

    #draw graph and fit with linear function
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_z.GetXaxis().SetTitle("z_{fill} (mm)")
    h_z.GetYaxis().SetTitle("#epsilon(#Delta t)")
    h_z.Draw("ap")
    f1 = ROOT.TF1("f1","pol1",-6000, 4000)
    f1.SetLineColor(50)
    h_z.Fit(f1, "R")

    pad = ROOT.TPad("pada","pada",0.18,0.3,0.6,0.5)
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

    c1.Update()

    c1.Print("/data/langrock/PartialFill/plots/" + isotope + "_deltat_eff.pdf","pdf")

    return f1.GetParameter(0), f1.GetParameter(1)


def get_fidvolbi(isotope, infile):
    """Function to calculate and plot progression of the efficiency of the fiducial volume cut on the Bismuth candidate versus different fill levels. Uses the text files as returned by dailycuts.py

     Args:
      isotope (string) : background isotope the cuts were applied to
      infile (string) : name of the input text file
    """

    #define graph
    h_z = ROOT.TGraphErrors(91)
    i = 1
 
    #loop through input file
    for line in infile:
        words = line.split()
        if len(words)!=0:

            #get z level, number of events passing the delta t cut and number of events passing the fiducial volume cut
            z = float(words[1])
            n_deltat = float(words[9])
            n_radius = float(words[11])

            eff = 0

            #get uncertainty
            n_deltat_error = math.sqrt(n_deltat)
            n_radius_error = math.sqrt(n_radius)

            eff_error = 0

            #if no events are selected within the time interval skip this fill level
            if n_deltat == 0:
                i += 1
                continue

            #calculate efficiency
            else:
                eff = n_radius/n_deltat
                eff_error = math.sqrt(math.pow(n_radius_error/n_deltat,2) + math.pow((n_radius * n_deltat_error/math.pow(n_deltat,2)),2))

            #set graph points
            h_z.SetPoint(i,z, eff)
            h_z.SetPointError(i, 0.0, eff_error)

            #print calculated efficiency to screen
            print z, eff, eff_error

            i += 1

    #draw graph
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_z.GetXaxis().SetTitle("z_{fill} (mm)")
    h_z.GetYaxis().SetTitle("#epsilon(r_{fidvol}^{Bi})")
    h_z.Draw("ap")

    pad = ROOT.TPad("pada","pada",0.18,0.7,0.6,0.9)
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

    c1.Update()

    c1.Print("/data/langrock/PartialFill/plots/" + isotope + "_fidvolbi_eff.pdf","pdf")

def get_deltar(isotope, infile):
    """Function to calculate and plot the delta r cut efficiency progression versus different fill levels. Uses the text files as returned by dailycuts.py

     Args:
      isotope (string) : background isotope the cuts were applied to
      infile (string) : name of the input text file
    """

    #define graph
    h_z = ROOT.TGraphErrors(91)
    i = 1

    #loop through input file
    for line in infile:
        words = line.split()
        if len(words)!=0:

            #get z level, number of events passing the fiducial volume cut on the Bismuth candidate and number of events passing the delta r cut
            z = float(words[1])
            n_radius = float(words[11])
            n_deltar = float(words[13])

            eff = 0

            #get uncertainty
            n_radius_error = math.sqrt(n_radius)
            n_deltar_error = math.sqrt(n_deltar)

            eff_error = 0

            #if no events are selected within the fiducial volume skip this fill level
            if n_radius == 0:
                i += 1
                continue

            #calculate efficiency
            else:
                eff = n_deltar/n_radius
                eff_error = math.sqrt(math.pow(n_deltar_error/n_radius,2) + math.pow((n_deltar * n_radius_error/math.pow(n_radius,2)),2))

            #set graph points
            h_z.SetPoint(i,z, eff)
            h_z.SetPointError(i, 0.0, eff_error)

            i += 1

    #draw graph and fit with linear function
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_z.GetXaxis().SetTitle("z_{fill} (mm)")
    h_z.GetYaxis().SetTitle("#epsilon(#Delta r)")
    h_z.Draw("ap")
    f1 = ROOT.TF1("f1","pol1",-6000, 4000)
    f1.SetLineColor(50)
    h_z.Fit(f1, "R")

    pad = ROOT.TPad("pada","pada",0.18,0.7,0.6,0.9)
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

    c1.Print("/data/langrock/PartialFill/plots/" + isotope + "_deltar_eff.pdf","pdf")

    return f1.GetParameter(0), f1.GetParameter(1)


def calc_fid_vol(infile):
    """Function to calculate the fiducial volume cut efficiency based on the detector geometry and fill level. Uses the text files as returned by dailycuts.py

     Args:
      infile (string) : name of the input text file
    """

    #define graph
    h_r = ROOT.TGraph(91)
    i = 1

    #loop through input file
    for line in infile:
        words = line.split()

        if len(words)!=0:

            #define volume variables used to calculate efficiency
            fidvol = 0
            full = 0

            #use different equations based on the fill level in the detector. words[1]==fill level
            if float(words[1])>0:
                #use sphere cap to calculate fiducial volume and full scintillator volume
                h_fidvol = 5000 - (float(words[1]) + 653)
                z = 6000 - float(words[1])
                r_fidvol = 5000
                r = 6000

                fidvol = math.pow(h_fidvol,2)*(3*r_fidvol - h_fidvol)
                full = math.pow(z,2)*(3*r - z)

            elif float(words[1])<0 and (float(words[1])+653)>0:
                #if the fill level is below the equator, the scintillator volume needs to be calculated using the full sphere volume and the volume taken up by the water sphere cap
                #in this case the fiducial volume is still above the equator, therefore to calculate the fiducial volume the sphere cap equation is sufficient
                h_fidvol =  5000 - (float(words[1]) + 653)
                z = float(words[1]) + 6000
                r_fidvol = 5000
                r = 6000

                fidvol = math.pow(h_fidvol,2)*(3*r_fidvol - h_fidvol)
                full = 4*math.pow(r,3) - math.pow(z,2)*(3*r - z)

            else:
                #both the fill level and fiducial volume spread below the equator. both volumes are calculated using the full sphere volume and the volume of the sphere cap not included 
                h_fidvol = float(words[1]) + 653 + 5000
                z = float(words[1]) + 6000
                r_fidvol = 5000
                r = 6000

                fidvol = 4*math.pow(r_fidvol,3) - math.pow(h_fidvol,2)*(3*r_fidvol - h_fidvol)
                full = 4*math.pow(r,3) - math.pow(z,2)*(3*r - z)
                
            #if the scintillator volume is non-existant, skip this fill level
            if full == 0:
                i += 1
                continue

            #calculate efficiency
            efficiency = fidvol/full

            #efficiency has to be <= 1
            if efficiency > 1:
                i+= 1
                continue

            #fill graph
            h_r.SetPoint(i,float(words[1]),efficiency)

            #print efficiencies to screen
            print words[1], efficiency

            i += 1

    #draw graph
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_r.GetXaxis().SetTitle("z_{fill} (mm)")
    h_r.GetYaxis().SetTitle("#epsilon(r_{fidvol})")
    h_r.Draw("ap")

    c1.Print("/data/langrock/PartialFill/plots/r_eff.pdf","pdf")

def estimate_deltar(infile):
    """Function to calculate the delta r volume cut efficiency based on the detector geometry and fill level. Uses the text files as returned by dailycuts.py

     Args:
      infile (string) : name of the input text file
    """

    #define graph
    h_r = ROOT.TGraph(91)
    i = 1

    #loop through input file
    for line in infile:
        words = line.split()

        if len(words)!=0:

            #define volume variables used to calculate efficiency
            #delta r volume is always the volume of a sphere
            deltar = 4*math.pow(1500,3)
            full = 0

            #use different equations based on the fill level in the detector. words[1]==fill level
            if float(words[1])>0:
                #use sphere cap to calculate fiducial volume
                h_fidvol = 5000 - (float(words[1]) + 653)
                r_fidvol = 5000

                full = math.pow(h_fidvol,2)*(3*r_fidvol - h_fidvol)

            else:
                #if the fill level is below the equator, the scintillator volume needs to be calculated using the full sphere volume and the volume taken up by the water sphere cap
                h_fidvol = float(words[1]) + 653 + 5000
                r_fidvol = 5000

                full = 4*math.pow(r_fidvol,3) - math.pow(h_fidvol,2)*(3*r_fidvol - h_fidvol)
                
            #if the fiducial volume is non-existant, skip this fill level
            if full == 0:
                i += 1
                continue

            #calculate efficiency
            efficiency = deltar/full

            #efficiency has to be <= 1
            if efficiency > 1:
                i+= 1
                continue

            #fill graph
            h_r.SetPoint(i,float(words[1]),efficiency)

            #print efficiencies to screen
            print words[1], efficiency

            i += 1

    #draw graph
    c1 = ROOT.TCanvas("c1","",1)
    c1.Draw()
    h_r.GetXaxis().SetTitle("z_{fill} (mm)")
    h_r.GetYaxis().SetTitle("#epsilon(#Delta r)")
    h_r.Draw("ap")

    c1.Print("/data/langrock/PartialFill/plots/deltar_eff.pdf","pdf")

if __name__ == '__main__':
    """Script to monitor the cut efficiency progression over the entire fill period. Requires the output of dailycuts.py or nhitscuts.py.
    """
    
    #get plot style
    style = plot_style.PlotStyle()
    style.set_style()
    ROOT.gROOT.SetStyle("clearRetro")

    #loop through directory containing the text files
    for root, dirs, filenames in os.walk("/users/langrock/plotting_macros/Partial_fill/textfiles/"):
        filenames.sort()
        for x in filenames:
            
            if fnmatch.fnmatch(x, "*.txt"):
                
                #open text files
                infile = open('/users/langrock/plotting_macros/Partial_fill/textfiles/' + x,'r')

                components = x.split('_')

                print get_deltat(components[0], infile)
                print get_deltar(components[0], infile)
                print get_nhits(components[0],infile)
                print get_fidvol_water(components[0], infile)
                get_fidvolbi(components[0], infile)
                
                estimate_deltar(infile)
                calc_fid_vol(infile)
