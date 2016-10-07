
#!/usr/bin/env python
import ROOT
import rat
import sys
import math
import fnmatch
import optparse
import os

parser = optparse.OptionParser( usage = "python %prog [flags]")
parser.add_option("-c", dest="cut_type", help="Cut type, 'po212', 'po214', 'bi212' or 'bi214'")

(options, args) = parser.parse_args()

#loop through directory containing input root files
for root, dirs, filenames in os.walk("/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/"):
    for x in filenames:
        if fnmatch.fnmatch(x, "*_Scint.ntuple.root"):

            infile = "/data/snoplus/OfficialProcessing/production_5_3_1/PartialScint/Merged/" + x

            print x
            components = x.split("_")
            if len(components)!=0:

                #define output text file
                output_file = open("/users/langrock/plotting_macros/Partial_fill/textfiles/" +components[0] + "_nhits_cuts_" + options.cut_type + ".txt",'w' )

                #open input root file and access tree
                filename = ROOT.TFile(infile)
                tree = filename.Get("output")

                #open file including fill levels and days
                infile1 = open("/users/langrock/plotting_macros/Partial_fill/split_level.txt","r")
        
                #define variables to count events
                events_full = 0
                events_radius = 0
                events_nhits = 0

                #loop through input text file
                for line in infile1:
                    words = line.split()

                    if len(words)!=0:

                        d = float(words[0])
                        z_level = float(words[1])

                        fidvol_value = 5000

                        #for each day, run through input root file
                        for i in range(tree.GetEntries()):                           
                            tree.GetEntry(i)
                            nhits = tree.nhits
                            radius = math.sqrt(tree.posx*tree.posx+tree.posy*tree.posy+tree.posz*tree.posz)
                            time = tree.uTNSecs + tree.uTSecs*math.pow(10,9) + tree.uTDays*24*60*60*math.pow(10,9)
                            energy = tree.energy
                            fitValid = tree.fitValid
                            x = tree.posx
                            y = tree.posy
                            z = tree.posz
                            evIndex = tree.evIndex
                            day = tree.uTDays

                            if d != day:
                                continue

                            elif d == day:

                                events_full += 1

                                #apply fiducial volume cut and reject retriggers
                                if radius> 0 and radius < fidvol_value and z >= z_level+653 and evIndex == 0:
                                    events_radius += 1 

                                    #apply nhits cut based on the selected cut type
                                    if options.cut_type == "po212":
                                        if nhits >= 450 and nhits <= 580:
                                            events_nhits +=1

                                    elif options.cut_type == "po214":
                                        if nhits >= 290 and nhits <= 450:
                                            events_nhits +=1

                                    elif options.cut_type == "bi212":
                                        if nhits >= 100:
                                            events_nhits +=1

                                    elif options.cut_type == "bi214":
                                        if nhits >= 600:
                                            events_nhits +=1

                        #write output to file for each fill day
                        output_file.write(str(d))
                        output_file.write('\t')
                        output_file.write(str(z_level))
                        output_file.write("\t total: ")
                        output_file.write(str(events_full))
                        output_file.write("\t radius: ")
                        output_file.write(str(events_radius))
                        output_file.write("\t nhits: ")
                        output_file.write(str(events_nhits))
                        output_file.write('\n')

                output_file.close()
