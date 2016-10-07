#!/usr/bin/env python
import ROOT
import rat
import math
import os
import fnmatch
import optparse
import define_histograms

def get_fill_level():
    #print fill level per day to text file
    print "Needs to be done, two columns, first needs to be the fill day and second column the fill level for that day"

def apply_cuts(chain, isotope, tree, volume):
    """Function to apply BiPo cuts for each day of filling to partial fill samples.

     Args:
      chain (string) : "bipo212" or "bipo214", defines which cut sequence is run
      isotope (string) : background isotope the cuts are applied to
      tree (ROOT:TTree) : Tree from the ntuple file
      volume (string) : volume in which the events were simulated

     Returns:
      string with the event counts for each cut
    """

    #open file which inlcudes fill levels and fill days
    infile = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")

    #define root file to save root files to
    outputroot = ROOT.TFile("/data/langrock/PartialFill/Full/root/" + isotope + "_" + chain + "_" + volume +".root","recreate")

    #define histograms
    hist = define_histograms.DefineHistograms()

    events_full = 0
    events_pocut = 0
    events_deltatcut = 0
    events_bifidvolcut = 0
    events_deltarcut = 0
    events_bicut = 0
    events_allcut = 0

    #get fill days and fill level from file, loop through each line and perform the cut selection on each day of filling
    for line in infile:
        words = line.split()

        if len(words)!=0:

            d = float(words[0])
            z_level = float(words[1])
    
            #loop through the events in the root file
            for i in range(tree.GetEntries()):
                #get variables from previous events
                tree.GetEntry(i-1)
                nhits_prev = tree.nhits
                radius_prev = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                time_prev = tree.uTNSecs + tree.uTSecs*math.pow(10,9) + tree.uTDays*24*60*60*math.pow(10,9)
                energy_prev = tree.energy
                fitValid_prev = tree.fitValid
                x_prev = tree.posx
                y_prev = tree.posy
                z_prev = tree.posz

                #get variables from current events
                tree.GetEntry(i)
                nhits = tree.nhits
                radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                time = tree.uTNSecs + tree.uTSecs*math.pow(10,9) + tree.uTDays*24*60*60*math.pow(10,9)
                energy = tree.energy
                fitValid = tree.fitValid
                x = tree.posx
                y = tree.posy
                z = tree.posz

                #get day at which events were simulated
                day = tree.uTDays

                #define time differance and event distance
                delta_t = time - time_prev
                delta_r = math.sqrt(math.pow((x_prev - x),2) + math.pow((y_prev - y),2) + math.pow((z_prev - z),2))

                fidvol_value = 5000
                
                #if the event was generated on the current day of filling, apply cuts
                if d == day:

                    #fill histograms and count events
                    hist.h_energy_full.Fill(energy)
                    hist.h_nhitspo_full.Fill(nhits)
                    hist.h_nhitsbi_full.Fill(nhits_prev)
                    hist.h_deltat_full.Fill(delta_t)
                    hist.h_deltar_full.Fill(delta_r)
                    hist.h_rfidvolbi_full.Fill(radius_prev)

                    events_full += 1

                    #apply fiducial vlume cut
                    if radius> 0 and radius < fidvol_value and z >= z_level+653:

                        hist.h_energy_pocut.Fill(energy)
                        hist.h_nhitspo_pocut.Fill(nhits)
                        hist.h_nhitsbi_pocut.Fill(nhits_prev)
                        hist.h_deltat_pocut.Fill(delta_t)
                        hist.h_deltar_pocut.Fill(delta_r)
                        hist.h_rfidvolbi_pocut.Fill(radius_prev)
                        
                        events_pocut += 1

                        #bipo212 cut selection
                        if chain == "bipo212":
                            #apply polonium candidate cut
                            if nhits >= 450 and nhits <= 580:

                                hist.h_energy_deltatcut.Fill(energy)
                                hist.h_nhitspo_deltatcut.Fill(nhits)
                                hist.h_nhitsbi_deltatcut.Fill(nhits_prev)
                                hist.h_deltat_deltatcut.Fill(delta_t)
                                hist.h_deltar_deltatcut.Fill(delta_r)
                                hist.h_rfidvolbi_deltatcut.Fill(radius_prev)

                                events_deltatcut += 1

                                #time difference cut
                                if delta_t < 3690:

                                    hist.h_energy_bifidvolcut.Fill(energy)
                                    hist.h_nhitspo_bifidvolcut.Fill(nhits)
                                    hist.h_nhitsbi_bifidvolcut.Fill(nhits_prev)
                                    hist.h_deltat_bifidvolcut.Fill(delta_t)
                                    hist.h_deltar_bifidvolcut.Fill(delta_r)
                                    hist.h_rfidvolbi_bifidvolcut.Fill(radius_prev)

                                    events_bifidvolcut += 1

                                    #fiducial radius cut on bismuth candidate
                                    if radius_prev > 0 and radius_prev < fidvol_value and z_prev >= z_level+653:

                                        hist.h_energy_deltarcut.Fill(energy)
                                        hist.h_nhitspo_deltarcut.Fill(nhits)
                                        hist.h_nhitsbi_deltarcut.Fill(nhits_prev)
                                        hist.h_deltat_deltarcut.Fill(delta_t)
                                        hist.h_deltar_deltarcut.Fill(delta_r)
                                        hist.h_rfidvolbi_deltarcut.Fill(radius_prev)

                                        events_deltarcut += 1

                                        #distance cut
                                        if delta_r > 0 and delta_r < 1500:

                                            hist.h_energy_bicut.Fill(energy)
                                            hist.h_nhitspo_bicut.Fill(nhits)
                                            hist.h_nhitsbi_bicut.Fill(nhits_prev)
                                            hist.h_deltat_bicut.Fill(delta_t)
                                            hist.h_deltar_bicut.Fill(delta_r)
                                            hist.h_rfidvolbi_bicut.Fill(radius_prev)

                                            events_bicut += 1

                                            #nhits cut on the bismuth candidate
                                            if nhits_prev >= 100:

                                                hist.h_energy_allcut.Fill(energy)
                                                hist.h_nhitspo_allcut.Fill(nhits)
                                                hist.h_nhitsbi_allcut.Fill(nhits_prev)
                                                hist.h_deltat_allcut.Fill(delta_t)
                                                hist.h_deltar_allcut.Fill(delta_r)
                                                hist.h_rfidvolbi_allcut.Fill(radius_prev)

                                                events_allcut += 1
                            
                        #bipo214 cut selection
                        elif chain == "bipo214":
                            #nhits cut on polonium candidate
                            if nhits >= 290 and nhits <= 450:

                                hist.h_energy_deltatcut.Fill(energy)
                                hist.h_nhitspo_deltatcut.Fill(nhits)
                                hist.h_nhitsbi_deltatcut.Fill(nhits_prev)
                                hist.h_deltat_deltatcut.Fill(delta_t)
                                hist.h_deltar_deltatcut.Fill(delta_r)
                                hist.h_rfidvolbi_deltatcut.Fill(radius_prev)

                                events_deltatcut += 1

                                #time difference cut
                                if delta_t > 3690 and delta_t < 1798788:

                                    hist.h_energy_bifidvolcut.Fill(energy)
                                    hist.h_nhitspo_bifidvolcut.Fill(nhits)
                                    hist.h_nhitsbi_bifidvolcut.Fill(nhits_prev)
                                    hist.h_deltat_bifidvolcut.Fill(delta_t)
                                    hist.h_deltar_bifidvolcut.Fill(delta_r)
                                    hist.h_rfidvolbi_bifidvolcut.Fill(radius_prev)

                                    events_bifidvolcut += 1

                                    #fiducial volume cut on bismuth candidate
                                    if radius_prev > 0 and radius_prev < fidvol_value and z_prev >= z_level+653:

                                        hist.h_energy_deltarcut.Fill(energy)
                                        hist.h_nhitspo_deltarcut.Fill(nhits)
                                        hist.h_nhitsbi_deltarcut.Fill(nhits_prev)
                                        hist.h_deltat_deltarcut.Fill(delta_t)
                                        hist.h_deltar_deltarcut.Fill(delta_r)
                                        hist.h_rfidvolbi_deltarcut.Fill(radius_prev)
                                        
                                        events_deltarcut += 1

                                        #distance cut
                                        if delta_r > 0 and delta_r < 1500:

                                            hist.h_energy_bicut.Fill(energy)
                                            hist.h_nhitspo_bicut.Fill(nhits)
                                            hist.h_nhitsbi_bicut.Fill(nhits_prev)
                                            hist.h_deltat_bicut.Fill(delta_t)
                                            hist.h_deltar_bicut.Fill(delta_r)
                                            hist.h_rfidvolbi_bicut.Fill(radius_prev)

                                            events_bicut += 1

                                            #nhits cut on the bismuth candidate
                                            if nhits_prev >= 600:

                                                hist.h_energy_allcut.Fill(energy)
                                                hist.h_nhitspo_allcut.Fill(nhits)
                                                hist.h_nhitsbi_allcut.Fill(nhits_prev)
                                                hist.h_deltat_allcut.Fill(delta_t)
                                                hist.h_deltar_allcut.Fill(delta_r)
                                                hist.h_rfidvolbi_allcut.Fill(radius_prev)

                                                events_allcut += 1
    
    #write all histograms to file
    outputroot.Write()
    outputroot.Close()

    #create string with all event counts
    outputstring = isotope + "\t all events: " + str(events_full) + "\t fiducial volume: " + str(events_pocut) + "\t Po nhits cut: " + str(events_deltatcut) + "\t Delta t cut: " + str(events_bifidvolcut) + "\t fiducial volume: " + str(events_deltarcut) + "\t Delta r cut: " + str(events_bicut) + "\t Bi nhits cut: " + str(events_allcut) + "\n " 

    return outputstring

if __name__ == '__main__':
    """Script to apply cuts to input root files. Input root files need to have the structure Isotope_fillvolume.root.
    """

    parser = optparse.OptionParser( usage = "python %prog [flags]")
    parser.add_option("-v", dest="volume", help="Partial Fill Volume, 'water' or 'scint'")
    parser.add_option("-c", dest="cut_type", help="Cut type, 'bipo212' or 'bipo214'")

    (options, args) = parser.parse_args()

    #define output text file
    output = open("/data/langrock/PartialFill/Full/" + options.cut_type + "_" + options.volume +".txt",'a')

    #loop through directory with the input root files
    for root, dirs, filenames in os.walk("/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/"):
        for x in filenames:

            #find the files for events produced in the water volume
            if options.volume == "water":
                if fnmatch.fnmatch(x, "*_Water.ntuple.root"):
                    infile = "/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/" + x

                    components = x.split("_")
                    if len(components)!=0:

                        #open files
                        filename = ROOT.TFile(infile)
                        treename = filename.Get("output")
                        
                        #apply cut selection
                        event_counts = apply_cuts(options.cut_type, components[0], treename, options.volume)

                        #save event counts to file
                        output.write(event_counts)

                        
            #find the files for events produced in the scintillator volume
            if options.volume == "scint":
                if fnmatch.fnmatch(x, "*_Scint.ntuple.root"):
                    infile = "/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/" + x

                    components = x.split("_")
                    if len(components)!=0:

                        #open file
                        filename = ROOT.TFile(infile)
                        treename = filename.Get("output")

                        #apply cut selection
                        event_counts = apply_cuts(options.cut_type, components[0], treename, options.volume)

                        #save event counts to file
                        output.write(event_counts)

    output.close()
