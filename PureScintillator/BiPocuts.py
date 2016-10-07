#!/usr/bin/env python
import ROOT
import rat
import sys
import math
import os
import fnmatch

#define what cut selection to run and which radial cut to apply when running the script 
cut = sys.argv[1]
radius_cut = sys.argv[2]

#open file which contains root input file location and names
input_file = open("/users/langrock/plotting_macros/Backgrounds/root_files.txt","r")

#define text file to save output to
output = open("/data/langrock/te_loaded_mergeddata/single_te_loaded_root/" + cut + "_" + radius_cut + ".txt","w")

#run through each file listed in input_file
for line in input_file:
    words = line.split()

    if len(words)!=0:

        infile = words[0]
        isotope = words[1]

        #define output root file to save histograms to
        file_name_data = ROOT.TFile("/data/langrock/te_loaded_mergeddata/single_te_loaded_root/" + isotope + "_" + cut + "_" + radius_cut + ".root","recreate")

        #define histograms
        h_deltat = ROOT.TH1D("h_deltat","h_deltat",10000,0.0,1800000)
        h_deltar = ROOT.TH1D("h_deltar","h_deltar",100,0.0,4000)
        h_rfidvolbi = ROOT.TH1D("h_rfidvolbi","h_rfidvolbi",150,0.0,6000)
        h_nhitspo = ROOT.TH1D("h_nhitspo","h_nhitspo",150,0.0,1500)
        h_nhitsbi = ROOT.TH1D("h_nhitsbi","h_nhitsbi",150,0.0,1500)

        #define variables used for counting the events selected by each cut
        total = 0
        fidvol = 0
        nhits_c = 0
        nhits_noretrig = 0
        timecut = 0
        allev = 0
        all_time = 0
        time_out = 0
        prev_nhits = 0

        inputroot = ROOT.TFile(infile)
        input_tree = inputroot.Get("output")

        #run through events in file
        for i in range(input_tree.GetEntries()):
            #access previous event
            input_tree.GetEntry(i-1)
            nhits_prev = input_tree.nhits
            radius_prev = math.sqrt(input_tree.posx*input_tree.posx+input_tree.posy*input_tree.posy+input_tree.posz*input_tree.posz)
            time_prev = input_tree.uTNSecs + input_tree.uTSecs*math.pow(10,9) + input_tree.uTDays*24*60*60*math.pow(10,9)
            x_prev = input_tree.posx
            y_prev = input_tree.posy
            z_prev = input_tree.posz
            
            #access current event
            input_tree.GetEntry(i)
            nhits = input_tree.nhits
            time = input_tree.uTNSecs + input_tree.uTSecs*math.pow(10,9) + input_tree.uTDays*24*60*60*math.pow(10,9)
            x = input_tree.posx
            y = input_tree.posy
            z = input_tree.posz
            radius = math.sqrt(input_tree.posx*input_tree.posx+input_tree.posy*input_tree.posy+input_tree.posz*input_tree.posz)
            
            #calculate distance and time between events
            delta_t = time - time_prev
            delta_r = math.sqrt(math.pow((x_prev - x),2) + math.pow((y_prev - y),2) + math.pow((z_prev - z),2))
            
            #apply fiducial radius cut
            total += 1
            if radius < 4000:
                fidvol += 1
                h_nhitspo.Fill(nhits)

                #do bipo212 cut selection  
                if cut == "bipo212":

                    #polonium candidate nhits cut
                    if nhits >= 450 and nhits <= 580: #pure scint cut
                        nhits_c += 1                                      
                        h_deltat.Fill(delta_t)

                        #time difference cut
                        if delta_t > 0.05 and delta_t < 3690:
                            all_time += 1
                            h_rfidvolbi.Fill(radius_prev)
                            
                            #fiducial volume cut on bismuth candidate                           
                            if radius_prev < 4000:
                                timecut += 1
                                h_deltar.Fill(delta_r)
                                
                                #distance cut between events
                                if delta_r > 0 and delta_r <= float(radius_cut):
                                    allev += 1
                                    h_nhitsbi.Fill(nhits_prev)
                                   
                                    #nhits cut on bismuth candidate
                                    if nhits_prev >= 100: #pure scint cut
                                        prev_nhits += 1
                                            
                #do bipo214 cut selection
                elif cut == "bipo214":

                    if nhits >= 290 and nhits <= 450: #pure scint cut
                        nhits_c += 1   
                        h_deltat.Fill(delta_t)

                        #apply time difference cut
                        if delta_t > 3690 and delta_t < 1798788:
                            all_time += 1
                            h_rfidvolbi.Fill(radius_prev)
                            
                            #fiducial volume cut on bismuth candidate
                            if radius_prev < 4000:
                                timecut += 1
                                h_deltar.Fill(delta_r)
                                
                                #distance cut between events
                                if delta_r > 0 and delta_r <= float(radius_cut):
                                    allev += 1
                                    h_nhitsbi.Fill(nhits_prev)
                                        
                                    #nhits cut on bismuth candidate
                                    if nhits_prev >= 600: #pure scint cut
                                        prev_nhits += 1


        #save event counts to text file
        output_string = "Isotope: " + str(isotope) + "\t before cut: " + str(total) + "\t fid vol cut: " + str(fidvol) + "\t nhits: " + str(nhits_c) + "\t everything passing timing cut: " + str(all_time) + "\t fiducial volume: " + str(timecut) + "\t deltar: " + str(allev) + "\t bi nhits: " + str(prev_nhits) + "\n"
        output.write(output_string)
        
        #save filled histograms to root file
        file_name_data.Write()

        h_deltat.Delete()
        h_deltar.Delete()
        h_nhitspo.Delete()
        h_nhitsbi.Delete()
        h_rfidvolbi.Delete()    

        file_name_data.Close()

output.close()
