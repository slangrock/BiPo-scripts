
#!/usr/bin/env python
import ROOT
import rat
import sys
import math
import fnmatch
import optparse
import os

#select cut type when running the script
parser = optparse.OptionParser( usage = "python %prog [flags]")
parser.add_option("-c", dest="cut_type", help="Cut type, 'bipo212' or 'bipo214'")

(options, args) = parser.parse_args()

#loop through directory with input root files
for root, dirs, filenames in os.walk("/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/"):
    for x in filenames:
        #find BiPo21x files
        if fnmatch.fnmatch(x, "*Bi21*Po21*_Scint.ntuple.root"):

            infile = "/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/" + x

            print x
            components = x.split("_")
            if len(components)!=0:

                #open output text file
                output_file = open("/users/langrock/plotting_macros/Partial_fill/textfiles/" +components[0] + "_nhits_cuts_" + options.cut_type + ".txt",'w' )

                #open input root file and access tree
                filename = ROOT.TFile(infile)
                tree = filename.Get("output")

                #open file containing fill levels and days
                infile1 = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")
        
                #define variables used to count events
                events_full = 0
                events_radius = 0
                events_nhits = 0
                events_time = 0
                events_fidvolbi = 0
                events_deltar = 0

                #apply cut selection for each day and fill level
                for line in infile1:
                    words = line.split()

                    if len(words)!=0:

                        d = float(words[0])
                        z_level = float(words[1])

                        fidvol_value = 5000

                        for i in range(tree.GetEntries()):
                            tree.GetEntry(i-1)
                            nhits_prev = tree.nhits
                            radius_prev = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                            time_prev = tree.uTNSecs + tree.uTSecs*math.pow(10,9) + tree.uTDays*24*60*60*math.pow(10,9)
                            x_prev = tree.posx
                            y_prev = tree.posy
                            z_prev = tree.posz
                            
                            tree.GetEntry(i)
                            nhits = tree.nhits
                            radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                            time = tree.uTNSecs + tree.uTSecs*math.pow(10,9) + tree.uTDays*24*60*60*math.pow(10,9)
                            x = tree.posx
                            y = tree.posy
                            z = tree.posz
                            day = tree.uTDays


                            delta_t = time - time_prev
                            delta_r = math.sqrt(math.pow((x_prev - x),2) + math.pow((y_prev - y),2) + math.pow((z_prev - z),2))

                            if d != day:
                                continue

                            elif d == day:

                                events_full += 1

                                #apply fiducal volume cut
                                if radius> 0 and radius < fidvol_value and z >= z_level+653:
                                    events_radius += 1 

                                    #BiPo212 cut selection
                                    if options.cut_type == "bipo212":
                                        if nhits >= 450 and nhits <= 580:
                                            events_nhits +=1

                                            if delta_t < 3690:
                                                events_time += 1

                                                if radius_prev > 0 and radius_prev < fidvol_value and z_prev >= z_level+653:
                                                    events_fidvolbi += 1

                                                    if delta_r > 0 and delta_r < 1500:
                                                        events_deltar += 1


                                    #BiPo214 cut selection
                                    elif options.cut_type == "bipo214":
                                        if nhits >= 290 and nhits <= 450:
                                            events_nhits +=1
                    
                                            if delta_t > 3690 and delta_t < 1798788:
                                                events_time += 1

                                                if radius_prev > 0 and radius_prev < fidvol_value and z_prev >= z_level+653:
                                                    events_fidvolbi += 1
                                                    
                                                    if delta_r > 0 and delta_r < 1500:
                                                        events_deltar += 1

                        #write events to file for each day
                        output_file.write(str(d))
                        output_file.write('\t')
                        output_file.write(str(z_level))
                        output_file.write("\t total: ")
                        output_file.write(str(events_full))
                        output_file.write("\t radius: ")
                        output_file.write(str(events_radius))
                        output_file.write("\t nhits: ")
                        output_file.write(str(events_nhits))
                        output_file.write("\t deltat: ")
                        output_file.write(str(events_time))
                        output_file.write("\t fidvolBi: ")
                        output_file.write(str(events_fidvolbi))
                        output_file.write("\t deltae: ")
                        output_file.write(str(events_deltar))
                        output_file.write('\n')

                output_file.close()
