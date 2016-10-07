#!/usr/bin/env python
import ROOT
import rat
import sys
import math
import os
import fnmatch

#define which nhit cut to apply (options are po212, po214, bi212, bi214) when running the script
cut = sys.argv[1]

#open file which contains root input file location and names
input_file = open("root_files.txt","r")

#run through each file listed in input_file
for line in input_file:
    words = line.split()
    if len(words)!=0:

        infile = words[0]
        isotope = words[1]

        total = 0
        fidvol = 0
        nhitscut = 0
        
        #open file
        inputroot = ROOT.TFile(infile)
        input_tree = inputroot.Get("output")

        #loop through entries in file
        for i in range(input_tree.GetEntries()):
            #get variables for current event
            input_tree.GetEntry(i)
            nhits = input_tree.nhits
            x = input_tree.posx
            y = input_tree.posy
            z = input_tree.posz
            radius = math.sqrt(x*x+y*y+z*z)
            evIndex = input_tree.evIndex
                                  
            total += 1                      
            #apply fiducial volume cut. the evIndex cut is to ensure no re-triggered events are included
            if radius < 4000 and evIndex == 0:  
                fidvol += 1

                if cut == "po212":
                    if nhits >= 450 and nhits <= 580:
                        nhitscut += 1
                if cut == "bi212":
                    if nhits >= 100:
                        nhitscut += 1
                if cut == "po214":
                    if nhits >= 290 and nhits <= 450:
                        nhitscut += 1
                if cut == "bi214":
                    if nhits >= 600:
                        nhitscut += 1

        #print results to screen
        print "Isotope: ", isotope, " before cut: ", total, " fid vol cut: ", fidvol, " after cut: ", nhitscut

raw_input("RET to EXIT");
