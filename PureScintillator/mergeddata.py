#!/usr/bin/env python
import ROOT
import rat
import sys
import math
import os

#define what cut selection to run and which radial cut to apply when running the script 
cut = sys.argv[1]
radius_cut = sys.argv[2]

#define output file name to save histograms to
file_name_data = ROOT.TFile("/data/langrock/te_loaded_mergeddata/" + cut + "_cutsmonth_" + radius_cut + ".root","new")

#define histograms to be saved - one for each cut and each background type
e_original = ROOT.TH1D("e_o","e_o",100,0.01,5)
e_first = ROOT.TH1D("e_f","e_f",100,0.01,5)
e_second = ROOT.TH1D("e_s","e_s",100,0.01,5)
e_bipo212 = ROOT.TH1D("bipo212","bipo212",100,0.01,5)
e_bipo214 = ROOT.TH1D("bipo214","bipo214",100,0.01,5)
e_bi210 = ROOT.TH1D("bi210","bi210",100,0.01,5)
e_po210 = ROOT.TH1D("po210","po210",100,0.01,5)
e_c14 = ROOT.TH1D("c14","c14",100,0.01,5)
e_ndbd = ROOT.TH1D("ndbd","ndbd",100,0.01,5)
e_dbd = ROOT.TH1D("dbd","dbd",100,0.01,5)
e_an = ROOT.TH1D("an","an",100,0.01,5)
e_external = ROOT.TH1D("external","external",100,0.01,5)
e_bipo212_cuts = ROOT.TH1D("bipo212_cuts","bipo212_cuts",100,0.01,5)
e_bipo214_cuts = ROOT.TH1D("bipo214_cuts","bipo214_cuts",100,0.01,5)
e_bi210_cuts = ROOT.TH1D("bi210_cuts","bi210_cuts",100,0.01,5)
e_po210_cuts = ROOT.TH1D("po210_cuts","po210_cuts",100,0.01,5)
e_c14_cuts = ROOT.TH1D("c14_cuts","c14_cuts",100,0.01,5)
e_ndbd_cuts = ROOT.TH1D("ndbd_cuts","ndbd_cuts",100,0.01,5)
e_dbd_cuts = ROOT.TH1D("dbd_cuts","dbd_cuts",100,0.01,5)
e_an_cuts = ROOT.TH1D("an_cuts","an_cuts",100,0.01,5)
e_external_cuts = ROOT.TH1D("external_cuts","external_cuts",100,0.01,5)

e_bipo212_po = ROOT.TH1D("bipo212_po","bipo212_po",100,0.01,5)
e_bipo214_po = ROOT.TH1D("bipo214_po","bipo214_po",100,0.01,5)
e_bi210_po = ROOT.TH1D("bi210_po","bi210_po",100,0.01,5)
e_po210_po = ROOT.TH1D("po210_po","po210_po",100,0.01,5)
e_c14_po = ROOT.TH1D("c14_po","c14_po",100,0.01,5)
e_ndbd_po = ROOT.TH1D("ndbd_po","ndbd_po",100,0.01,5)
e_dbd_po = ROOT.TH1D("dbd_po","dbd_po",100,0.01,5)
e_an_po = ROOT.TH1D("an_po","an_po",100,0.01,5)
e_external_po = ROOT.TH1D("external_po","external_po",100,0.01,5)

e_bipo212_bi = ROOT.TH1D("bipo212_bi","bipo212_bi",100,0.01,5)
e_bipo214_bi = ROOT.TH1D("bipo214_bi","bipo214_bi",100,0.01,5)
e_bi210_bi = ROOT.TH1D("bi210_bi","bi210_bi",100,0.01,5)
e_po210_bi = ROOT.TH1D("po210_bi","po210_bi",100,0.01,5)
e_c14_bi = ROOT.TH1D("c14_bi","c14_bi",100,0.01,5)
e_ndbd_bi = ROOT.TH1D("ndbd_bi","ndbd_bi",100,0.01,5)
e_dbd_bi = ROOT.TH1D("dbd_bi","dbd_bi",100,0.01,5)
e_an_bi = ROOT.TH1D("an_bi","an_bi",100,0.01,5)
e_external_bi = ROOT.TH1D("external_bi","external_bi",100,0.01,5)

e_bipo212_deltat = ROOT.TH1D("bipo212_deltat","bipo212_deltat",10000,0.0,1800000)
e_bipo214_deltat = ROOT.TH1D("bipo214_deltat","bipo214_deltat",10000,0.0,1800000)
e_bi210_deltat = ROOT.TH1D("bi210_deltat","bi210_deltat",10000,0.0,1800000)
e_po210_deltat = ROOT.TH1D("po210_deltat","po210_deltat",10000,0.0,1800000)
e_c14_deltat = ROOT.TH1D("c14_deltat","c14_deltat",10000,0.0,1800000)
e_ndbd_deltat = ROOT.TH1D("ndbd_deltat","ndbd_deltat",10000,0.0,1800000)
e_dbd_deltat = ROOT.TH1D("dbd_deltat","dbd_deltat",10000,0.0,1800000)
e_an_deltat = ROOT.TH1D("an_deltat","an_deltat",10000,0.0,1800000)
e_external_deltat = ROOT.TH1D("external_deltat","external_deltat",10000,0.0,1800000)

e_all_deltat = ROOT.TH1D("all_deltat","all_deltat",10000,0.0,1800000)
e_other_deltat = ROOT.TH1D("other_deltat","other_deltat",10000,0.0,1800000)

e_bipo212_deltar = ROOT.TH1D("bipo212_deltar","bipo212_deltar",100,0.0,4000)
e_bipo214_deltar = ROOT.TH1D("bipo214_deltar","bipo214_deltar",100,0.0,4000)
e_bi210_deltar = ROOT.TH1D("bi210_deltar","bi210_deltar",100,0.0,4000)
e_po210_deltar = ROOT.TH1D("po210_deltar","po210_deltar",100,0.0,4000)
e_c14_deltar = ROOT.TH1D("c14_deltar","c14_deltar",100,0.0,4000)
e_ndbd_deltar = ROOT.TH1D("ndbd_deltar","ndbd_deltar",100,0.0,4000)
e_dbd_deltar = ROOT.TH1D("dbd_deltar","dbd_deltar",100,0.0,4000)
e_an_deltar = ROOT.TH1D("an_deltar","an_deltar",100,0.0,4000)
e_external_deltar = ROOT.TH1D("external_deltar","external_deltar",100,0.0,4000)

e_all_deltar = ROOT.TH1D("all_deltar","all_deltar",100,0.0,4000)
e_other_deltar = ROOT.TH1D("other_deltar","other_deltar",100,0.0,4000)

e_bipo212_rfidvolbi = ROOT.TH1D("bipo212_rfidvolbi","bipo212_rfidvolbi",150,0.0,6000)
e_bipo214_rfidvolbi = ROOT.TH1D("bipo214_rfidvolbi","bipo214_rfidvolbi",150,0.0,6000)
e_bi210_rfidvolbi = ROOT.TH1D("bi210_rfidvolbi","bi210_rfidvolbi",150,0.0,6000)
e_po210_rfidvolbi = ROOT.TH1D("po210_rfidvolbi","po210_rfidvolbi",150,0.0,6000)
e_c14_rfidvolbi = ROOT.TH1D("c14_rfidvolbi","c14_rfidvolbi",150,0.0,6000)
e_ndbd_rfidvolbi = ROOT.TH1D("ndbd_rfidvolbi","ndbd_rfidvolbi",150,0.0,6000)
e_dbd_rfidvolbi = ROOT.TH1D("dbd_rfidvolbi","dbd_rfidvolbi",150,0.0,6000)
e_an_rfidvolbi = ROOT.TH1D("an_rfidvolbi","an_rfidvolbi",150,0.0,6000)
e_external_rfidvolbi = ROOT.TH1D("external_rfidvolbi","external_rfidvolbi",150,0.0,6000)

e_all_rfidvolbi = ROOT.TH1D("all_rfidvolbi","all_rfidvolbi",150,0.0,6000)
e_other_rfidvolbi = ROOT.TH1D("other_rfidvolbi","other_rfidvolbi",150,0.0,6000)

e_bipo212_nhitspo = ROOT.TH1D("bipo212_nhitspo","bipo212_nhitspo",150,0.0,750)
e_bipo214_nhitspo = ROOT.TH1D("bipo214_nhitspo","bipo214_nhitspo",150,0.0,750)
e_bi210_nhitspo = ROOT.TH1D("bi210_nhitspo","bi210_nhitspo",150,0.0,750)
e_po210_nhitspo = ROOT.TH1D("po210_nhitspo","po210_nhitspo",150,0.0,750)
e_c14_nhitspo = ROOT.TH1D("c14_nhitspo","c14_nhitspo",150,0.0,750)
e_ndbd_nhitspo = ROOT.TH1D("ndbd_nhitspo","ndbd_nhitspo",150,0.0,750)
e_dbd_nhitspo = ROOT.TH1D("dbd_nhitspo","dbd_nhitspo",150,0.0,750)
e_an_nhitspo = ROOT.TH1D("an_nhitspo","an_nhitspo",150,0.0,750)
e_external_nhitspo = ROOT.TH1D("external_nhitspo","external_nhitspo",150,0.0,750)

e_all_nhitspo = ROOT.TH1D("all_nhitspo","all_nhitspo",150,0.0,750)
e_other_nhitspo = ROOT.TH1D("other_nhitspo","other_nhitspo",150,0.0,750)

e_bipo212_nhitsbi = ROOT.TH1D("bipo212_nhitsbi","bipo212_nhitsbi",150,0.0,750)
e_bipo214_nhitsbi = ROOT.TH1D("bipo214_nhitsbi","bipo214_nhitsbi",150,0.0,750)
e_bi210_nhitsbi = ROOT.TH1D("bi210_nhitsbi","bi210_nhitsbi",150,0.0,750)
e_po210_nhitsbi = ROOT.TH1D("po210_nhitsbi","po210_nhitsbi",150,0.0,750)
e_c14_nhitsbi = ROOT.TH1D("c14_nhitsbi","c14_nhitsbi",150,0.0,750)
e_ndbd_nhitsbi = ROOT.TH1D("ndbd_nhitsbi","ndbd_nhitsbi",150,0.0,750)
e_dbd_nhitsbi = ROOT.TH1D("dbd_nhitsbi","dbd_nhitsbi",150,0.0,750)
e_an_nhitsbi = ROOT.TH1D("an_nhitsbi","an_nhitsbi",150,0.0,750)
e_external_nhitsbi = ROOT.TH1D("external_nhitsbi","external_nhitsbi",150,0.0,750)

e_all_nhitsbi = ROOT.TH1D("all_nhitsbi","all_nhitsbi",150,0.0,750)
e_other_nhitsbi = ROOT.TH1D("other_nhitsbi","other_nhitsbi",150,0.0,750)

#define variables used for counting the events selected by each cut
c14 = 0
ndbd = 0
dbd = 0
an = 0
bipo212 = 0
bipo214 = 0
bi = 0
po = 0
external = 0

c14_full = 0
ndbd_full = 0
dbd_full = 0
an_full = 0
bipo212_full = 0
bipo214_full = 0
bi_full = 0
po_full = 0
external_full = 0

c14_fidvol = 0
ndbd_fidvol = 0
dbd_fidvol = 0
an_fidvol = 0
bipo212_fidvol = 0
bipo214_fidvol = 0
bi_fidvol = 0
po_fidvol = 0
external_fidvol = 0

c14_nhits = 0
ndbd_nhits = 0
dbd_nhits = 0
an_nhits = 0
bipo212_nhits = 0
bipo214_nhits = 0
bi_nhits = 0
po_nhits = 0
external_nhits = 0

c14_time = 0
ndbd_time = 0
dbd_time = 0
an_time = 0
bipo212_time = 0
bipo214_time = 0
bi_time = 0
po_time = 0
external_time = 0

c14_fidvol2 = 0
ndbd_fidvol2 = 0
dbd_fidvol2 = 0
an_fidvol2 = 0
bipo212_fidvol2 = 0
bipo214_fidvol2 = 0
bi_fidvol2 = 0
po_fidvol2 = 0
external_fidvol2 = 0

c14_deltar = 0
ndbd_deltar = 0
dbd_deltar = 0
an_deltar = 0
bipo212_deltar = 0
bipo214_deltar = 0
bi_deltar = 0
po_deltar = 0
external_deltar = 0

c14_1prev = 0
ndbd_1prev = 0
dbd_1prev = 0
an_1prev = 0
bipo212_1prev = 0
bipo214_1prev = 0
bi_1prev = 0
po_1prev = 0
external_1prev = 0

c14_2prev = 0
ndbd_2prev = 0
dbd_2prev = 0
an_2prev = 0
bipo212_2prev = 0
bipo214_2prev = 0
bi_2prev = 0
po_2prev = 0
external_2prev = 0

c14_3prev = 0
ndbd_3prev = 0
dbd_3prev = 0
an_3prev = 0
bipo212_3prev = 0
bipo214_3prev = 0
bi_3prev = 0
po_3prev = 0
external_3prev = 0


bipo212_both = 0
bipo214_both = 0

#define directory where the input root files are stored
indir = '/data/snoplus/OfficialProcessing/MergedDataSet/MonthData/'

#run through directory
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        if not f == "StatisticsMonthData.pdf":
            infile = indir + f

            #open the files in directory and access the tree
            fin = ROOT.TFile(infile)
            tin = fin.Get("T")

            print "Processing ", infile

            #loop through all the entries
            for i in range(tin.GetEntries()):
                #get variabels for current event
                tin.GetEntry(i)
                nhits = tin.nhits
                radius = math.sqrt(tin.posx*tin.posx+tin.posy*tin.posy+tin.posz*tin.posz)
                time = tin.uTNSecs + tin.uTSecs*math.pow(10,9) + tin.uTDays*24*60*60*math.pow(10,9)
                mcIndex = tin.mcIndex
                energy = tin.energy
                fitValid = tin.fitValid
                x = tin.posx
                y = tin.posy
                z = tin.posz

                #check for valid fit
                if not fitValid:
                    continue

                #identify event type of current event
                iso = ""
                if mcIndex<9800000:
                    iso="c14"
                elif mcIndex<18400000:
                    iso="0nu"
                elif mcIndex<113100000:
                    iso="2nu"
                elif mcIndex<113900000:
                    iso="an"
                elif mcIndex<119400000:
                    iso="bipo212"
                elif mcIndex<245100000:
                    iso="bipo214"
                elif mcIndex<442900000:
                    iso="bi210"
                elif mcIndex<758000000:
                    iso="po210"
                else:
                    iso="external"

                #count the total number of events for each event type
                if iso=="c14":
                    c14_full+=1
                elif iso=="0nu":
                    ndbd_full+=1
                elif iso=="2nu":
                    dbd_full+=1
                elif iso=="an":
                    an_full+=1
                elif iso=="bipo212":
                    bipo212_full+=1
                elif iso=="bipo214":
                    bipo214_full+=1
                elif iso=="bi210":
                    bi_full+=1
                elif iso=="po210":
                    po_full+=1
                else:
                    external_full+=1
            
                #apply fiducial volume cut
                if radius < 4000:

                    #fill nhitsspectrum for all events
                    e_all_nhitspo.Fill(nhits)
                    #fill nhits spectrum with events that are not bipo212 or bipo214
                    if iso!="bipo212" and iso!="bipo214":
                        e_other_nhitspo.Fill(nhits)

                    #for each events type count number of events passing the fiducial volume cut and fill energy and nhits spectra before the polonium nhits cut is applied
                    if iso=="c14":
                        c14_fidvol+=1
                        e_c14.Fill(energy)
                        e_c14_nhitspo.Fill(nhits)
                    elif iso=="0nu":
                        ndbd_fidvol+=1
                        e_ndbd.Fill(energy)
                        e_ndbd_nhitspo.Fill(nhits)
                    elif iso=="2nu":
                        dbd_fidvol+=1
                        e_dbd.Fill(energy)
                        e_dbd_nhitspo.Fill(nhits)
                    elif iso=="an":
                        an_fidvol+=1
                        e_an.Fill(energy)
                        e_an_nhitspo.Fill(nhits)
                    elif iso=="bipo212":
                        bipo212_fidvol+=1
                        e_bipo212.Fill(energy)
                        e_bipo212_nhitspo.Fill(nhits)
                    elif iso=="bipo214":
                        bipo214_fidvol+=1
                        e_bipo214.Fill(energy)
                        e_bipo214_nhitspo.Fill(nhits)
                    elif iso=="bi210":
                        bi_fidvol+=1
                        e_bi210.Fill(energy)
                        e_bi210_nhitspo.Fill(nhits)
                    elif iso=="po210":
                        po_fidvol+=1
                        e_po210.Fill(energy)
                        e_po210_nhitspo.Fill(nhits)
                    else:
                        external_fidvol+=1
                        e_external.Fill(energy)
                        e_external_nhitspo.Fill(nhits)

                    # bipo212 cut selection ======================================================================================================================================
                    if cut == "bipo212":

                        #apply po212 nhits cuts and count all events which pass the cut for each type
                        if nhits >= 180 and nhits <= 330: #bipo212

                            if iso=="c14":
                                c14_nhits+=1
                            elif iso=="0nu":
                                ndbd_nhits+=1
                            elif iso=="2nu":
                                dbd_nhits+=1
                            elif iso=="an":
                                an_nhits+=1
                            elif iso=="bipo212":
                                bipo212_nhits+=1
                            elif iso=="bipo214":
                                bipo214_nhits+=1
                            elif iso=="bi210":
                                bi_nhits+=1
                            elif iso=="po210":
                                po_nhits+=1
                            else:
                                external_nhits+=1
           
                            #create for loop  with j >=2
                            for j in range(1,3):
                                #subtract j from current event i and access that entry id - for j==1 it is equivalent to the previous event, for j==2 it is equivalent to the event before the previous event
                                p = i-j
                                tin.GetEntry(p)
                                nhits_prev = tin.nhits
                                radius_prev = math.sqrt(tin.posx*tin.posx+tin.posy*tin.posy+tin.posz*tin.posz)
                                time_prev = tin.uTNSecs + tin.uTSecs*math.pow(10,9) + tin.uTDays*24*60*60*math.pow(10,9)
                                mcIndex_prev = tin.mcIndex
                                energy_prev = tin.energy
                                fitValid_prev = tin.fitValid
                                x_prev = tin.posx
                                y_prev = tin.posy
                                z_prev = tin.posz
                    
                                #define the time difference and distance between event i and event p 
                                delta_t = time - time_prev
                                delta_r = math.sqrt(math.pow((x_prev - x),2) + math.pow((y_prev - y),2) + math.pow((z_prev - z),2))

                                #check if p has a valid fit
                                if not fitValid_prev:
                                    continue

                                #fill the time difference of all surviving events into a histogram
                                e_all_deltat.Fill(delta_t)                      
                                #fill the time difference of all non bipo21x events into a histogram
                                if iso!="bipo212" and iso!="bipo214":
                                    e_other_deltat.Fill(delta_t)

                                #for each event type, fill the time difference histogram
                                if iso=="c14":
                                    e_c14_deltat.Fill(delta_t)
                                elif iso=="0nu":
                                    e_ndbd_deltat.Fill(delta_t)
                                elif iso=="2nu":
                                    e_dbd_deltat.Fill(delta_t)
                                elif iso=="an":
                                    e_an_deltat.Fill(delta_t)
                                elif iso=="bipo212":
                                    e_bipo212_deltat.Fill(delta_t)
                                elif iso=="bipo214":
                                    e_bipo214_deltat.Fill(delta_t)
                                elif iso=="bi210":
                                    e_bi210_deltat.Fill(delta_t)
                                elif iso=="po210":
                                    e_po210_deltat.Fill(delta_t)
                                else:
                                    e_external_deltat.Fill(delta_t)
                    
                                #if the time difference exceeds the cut limit abort
                                if delta_t > 3690: 
                                    break

                                #apply time limit cut
                                if delta_t > 0.05 and delta_t < 3690:        
                                    
                                    #fill event radius of previous events into histograms, for all events and non bipo21x events
                                    e_all_rfidvolbi.Fill(radius_prev)
                                    if iso!="bipo212" and iso!="bipo214":
                                        e_other_rfidvolbi.Fill(radius_prev)
        
                                    #count all events of each type passing this cut
                                    if iso=="c14":
                                        e_c14_rfidvolbi.Fill(radius_prev)
                                        c14_time+=1
                                    elif iso=="0nu":
                                        e_ndbd_rfidvolbi.Fill(radius_prev)
                                        ndbd_time+=1
                                    elif iso=="2nu":
                                        e_dbd_rfidvolbi.Fill(radius_prev)
                                        dbd_time+=1
                                    elif iso=="an":
                                        e_an_rfidvolbi.Fill(radius_prev)
                                        an_time+=1
                                    elif iso=="bipo212":
                                        e_bipo212_rfidvolbi.Fill(radius_prev)
                                        bipo212_time+=1
                                    elif iso=="bipo214":
                                        e_bipo214_rfidvolbi.Fill(radius_prev)
                                        bipo214_time+=1
                                    elif iso=="bi210":
                                        e_bi210_rfidvolbi.Fill(radius_prev)
                                        bi_time+=1
                                    elif iso=="po210":
                                        e_po210_rfidvolbi.Fill(radius_prev)
                                        po_time+=1
                                    else:
                                        e_external_rfidvolbi.Fill(radius_prev)
                                        external_time+=1

                                    #apply fiducial radius cut on the previous event and count and fill distance histograms as for the previous cuts
                                    if radius_prev < 4000:

                                        e_all_deltar.Fill(delta_r)
                                        if iso!="bipo212" and iso!="bipo214":
                                            e_other_deltar.Fill(delta_r)

                                        if iso=="c14":
                                            e_c14_deltar.Fill(delta_r)
                                            c14_fidvol2+=1
                                        elif iso=="0nu":
                                            e_ndbd_deltar.Fill(delta_r)
                                            ndbd_fidvol2+=1
                                        elif iso=="2nu":
                                            e_dbd_deltar.Fill(delta_r)
                                            dbd_fidvol2+=1
                                        elif iso=="an":
                                            e_an_deltar.Fill(delta_r)
                                            an_fidvol2+=1
                                        elif iso=="bipo212":
                                            e_bipo212_deltar.Fill(delta_r)
                                            bipo212_fidvol2+=1
                                        elif iso=="bipo214":
                                            e_bipo214_deltar.Fill(delta_r)
                                            bipo214_fidvol2+=1
                                        elif iso=="bi210":
                                            e_bi210_deltar.Fill(delta_r)
                                            bi_fidvol2+=1
                                        elif iso=="po210":
                                            e_po210_deltar.Fill(delta_r)
                                            po_fidvol2+=1
                                        else:
                                            e_external_deltar.Fill(delta_r)
                                            external_fidvol2+=1

                                        #apply distance cut between the two events with the limit defined when running the script. Count all events and fill nhits histograms for the previous event as for the previous cuts
                                        if delta_r > 0 and delta_r < float(radius_cut):
                                            
                                            e_all_nhitsbi.Fill(nhits_prev)
                                            if iso!="bipo212" and iso!="bipo214":
                                                e_other_nhitsbi.Fill(nhits_prev)

                                            if iso=="c14":
                                                e_c14_nhitsbi.Fill(nhits_prev)
                                                c14_deltar+=1
                                            elif iso=="0nu":
                                                e_ndbd_nhitsbi.Fill(nhits_prev)
                                                ndbd_deltar+=1
                                            elif iso=="2nu":
                                                e_dbd_nhitsbi.Fill(nhits_prev)
                                                dbd_deltar+=1
                                            elif iso=="an":
                                                e_an_nhitsbi.Fill(nhits_prev)
                                                an_deltar+=1
                                            elif iso=="bipo212":
                                                e_bipo212_nhitsbi.Fill(nhits_prev)
                                                bipo212_deltar+=1
                                            elif iso=="bipo214":
                                                e_bipo214_nhitsbi.Fill(nhits_prev)
                                                bipo214_deltar+=1
                                            elif iso=="bi210":
                                                e_bi210_nhitsbi.Fill(nhits_prev)
                                                bi_deltar+=1
                                            elif iso=="po210":
                                                e_po210_nhitsbi.Fill(nhits_prev)
                                                po_deltar+=1
                                            else:
                                                e_external_nhitsbi.Fill(nhits_prev)
                                                external_deltar+=1
                                                
                                            #apply cuts to reject bi214 events
                                            if nhits_prev >= 300 and nhits_prev <= 680: 
                                                continue
                                            
                                            #apply nhits cut on the previous event
                                            elif nhits_prev >= 10:
                                            
                                                e_original.Fill(energy)
                                                #define type of previous event
                                                iso_prev = ""
                                                if mcIndex_prev<9800000:
                                                    iso_prev="c14"
                                                elif mcIndex_prev<18400000:
                                                    iso_prev="0nu"
                                                elif mcIndex_prev<113100000:
                                                    iso_prev="2nu"
                                                elif mcIndex_prev<113900000:
                                                    iso_prev="an"
                                                elif mcIndex_prev<119400000:
                                                    iso_prev="bipo212"
                                                elif mcIndex_prev<245100000:
                                                    iso_prev="bipo214"
                                                elif mcIndex_prev<442900000:
                                                    iso_prev="bi210"
                                                elif mcIndex_prev<758000000:
                                                    iso_prev="po210"
                                                else:
                                                    iso_prev="external"
                                    
                                                #fill energy spectrum for polonium candidate and count polonium candidates passing all cuts. "_cuts" histograms are filled with the energy of both polonium and bismuth candidate, "_po" and "_bi" histograms are filled with the respective polonium or bismuth candidate energy only
                                                if iso=="c14":
                                                    c14+=1
                                                    e_c14_cuts.Fill(energy)
                                                    e_c14_po.Fill(energy)
                                                elif iso=="0nu":
                                                    ndbd+=1
                                                    e_ndbd_cuts.Fill(energy)
                                                    e_ndbd_po.Fill(energy)
                                                elif iso=="2nu":
                                                    dbd+=1
                                                    e_dbd_cuts.Fill(energy)
                                                    e_dbd_po.Fill(energy)
                                                elif iso=="an":
                                                    an+=1
                                                    e_an_cuts.Fill(energy)
                                                    e_an_po.Fill(energy)
                                                elif iso=="bipo212":
                                                    bipo212+=1
                                                    e_bipo212_cuts.Fill(energy)
                                                    e_bipo212_po.Fill(energy)
                                                elif iso=="bipo214":
                                                    bipo214+=1
                                                    e_bipo214_cuts.Fill(energy)
                                                    e_bipo214_po.Fill(energy)
                                                elif iso=="bi210":
                                                    bi+=1
                                                    e_bi210_cuts.Fill(energy)
                                                    e_bi210_po.Fill(energy)
                                                elif iso=="po210":
                                                    po+=1
                                                    e_po210_cuts.Fill(energy)
                                                    e_po210_po.Fill(energy)
                                                else:
                                                    external+=1
                                                    e_external_cuts.Fill(energy)
                                                    e_external_po.Fill(energy)
                    
                                                #count bismuth candidates passing all cuts for each type. If a candidate for j==1 is found abort loop
                                                if j==1:
                                                    e_first.Fill(energy_prev)
                                                    if iso_prev=="c14":
                                                        c14_1prev+=1
                                                        e_c14_cuts.Fill(energy_prev)
                                                        e_c14_bi.Fill(energy_prev)
                                                    elif iso_prev=="0nu":
                                                        ndbd_1prev+=1
                                                        e_ndbd_cuts.Fill(energy_prev)
                                                        e_ndbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="2nu":
                                                        dbd_1prev+=1
                                                        e_dbd_cuts.Fill(energy_prev)
                                                        e_dbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="an":
                                                        an_1prev+=1
                                                        e_an_cuts.Fill(energy_prev)
                                                        e_an_bi.Fill(energy_prev)
                                                    elif iso_prev=="bipo212":
                                                        e_bipo212_cuts.Fill(energy_prev)
                                                        e_bipo212_bi.Fill(energy_prev)                                                    
                                                        bipo212_1prev+=1
                                                    elif iso_prev=="bipo214":
                                                        e_bipo214_cuts.Fill(energy_prev)
                                                        e_bipo214_bi.Fill(energy_prev)
                                                        bipo214_1prev+=1
                                                    elif iso_prev=="bi210":
                                                        e_bi210_cuts.Fill(energy_prev)
                                                        e_bi210_bi.Fill(energy_prev)
                                                        bi_1prev+=1
                                                    elif iso_prev=="po210":
                                                        po_1prev+=1
                                                        e_po210_cuts.Fill(energy_prev)
                                                        e_po210_bi.Fill(energy_prev)
                                                    else:
                                                        external_1prev+=1
                                                        e_external_cuts.Fill(energy_prev)
                                                        e_external_bi.Fill(energy_prev)

                                                    #count all events for which the polonium and bismuth candidate are of the same coincidence type
                                                    if iso=="bipo212" and iso_prev=="bipo212":
                                                        bipo212_both += 1
                                                    
                                                    if iso=="bipo214" and iso_prev=="bipo214":
                                                        bipo214_both += 1

                                                    break
                                    
                                                #if no event for j==1 is found, repeat for j==2
                                                if j==2:
                                                    e_second.Fill(energy_prev)
                                                    if iso_prev=="c14":
                                                        c14_2prev+=1
                                                        e_c14_cuts.Fill(energy_prev)
                                                        e_c14_bi.Fill(energy_prev)
                                                    elif iso_prev=="0nu":
                                                        ndbd_2prev+=1
                                                        e_ndbd_cuts.Fill(energy_prev)
                                                        e_ndbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="2nu":
                                                        dbd_2prev+=1
                                                        e_dbd_cuts.Fill(energy_prev)
                                                        e_dbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="an":
                                                        an_2prev+=1
                                                        e_an_cuts.Fill(energy_prev)
                                                        e_an_bi.Fill(energy_prev)
                                                    elif iso_prev=="bipo212":
                                                        e_bipo212_cuts.Fill(energy_prev)
                                                        e_bipo212_bi.Fill(energy_prev)
                                                        bipo212_2prev+=1
                                                    elif iso_prev=="bipo214":
                                                        e_bipo214_cuts.Fill(energy_prev)
                                                        e_bipo214_bi.Fill(energy_prev)
                                                        bipo214_2prev+=1
                                                    elif iso_prev=="bi210":
                                                        e_bi210_cuts.Fill(energy_prev)
                                                        e_bi210_bi.Fill(energy_prev)
                                                        bi_2prev+=1
                                                    elif iso_prev=="po210":
                                                        e_po210_cuts.Fill(energy_prev)
                                                        e_po210_bi.Fill(energy_prev)
                                                        po_2prev+=1
                                                    else:
                                                        external_2prev+=1
                                                        e_external_cuts.Fill(energy_prev)
                                                        e_external_bi.Fill(energy_prev)
                                                        
                                                    if iso=="bipo212" and iso_prev=="bipo212":
                                                        bipo212_both += 1
                                                    
                                                    if iso=="bipo214" and iso_prev=="bipo214":
                                                        bipo214_both += 1

                    # bipo214 cut selection =======================================================================================================================================================

                    if cut == "bipo214":

                        #apply po214 nhits cuts and count all events which pass the cut for each type
                        if nhits >= 140 and nhits <= 280: #bipo214
                            
                            if iso=="c14":
                                c14_nhits+=1
                            elif iso=="0nu":
                                ndbd_nhits+=1
                            elif iso=="2nu":
                                dbd_nhits+=1
                            elif iso=="an":
                                an_nhits+=1
                            elif iso=="bipo212":
                                bipo212_nhits+=1
                            elif iso=="bipo214":
                                bipo214_nhits+=1
                            elif iso=="bi210":
                                bi_nhits+=1
                            elif iso=="po210":
                                po_nhits+=1
                            else:
                                external_nhits+=1

                            #create for loop  with j >=3
                            for j in range(1,4):
                                #subtract j from current event i and access that entry id - for j==1 it is equivalent to the previous event, for j==2 it is equivalent to the event before the previous event
                                p = i-j
                                tin.GetEntry(p)
                                nhits_prev = tin.nhits
                                radius_prev = math.sqrt(tin.posx*tin.posx+tin.posy*tin.posy+tin.posz*tin.posz)
                                time_prev = tin.uTNSecs + tin.uTSecs*math.pow(10,9) + tin.uTDays*24*60*60*math.pow(10,9)
                                mcIndex_prev = tin.mcIndex
                                energy_prev = tin.energy
                                fitValid_prev = tin.fitValid
                                x_prev = tin.posx
                                y_prev = tin.posy
                                z_prev = tin.posz

                                #define the time difference and distance between event i and event p                    
                                delta_t = time - time_prev
                                delta_r = math.sqrt(math.pow((x_prev - x),2) + math.pow((y_prev - y),2) + math.pow((z_prev - z),2))

                                #check if p has a valid fit
                                if not fitValid_prev:
                                    continue

                                #fill the time difference of all surviving events into a histogram
                                e_all_deltat.Fill(delta_t)                      
                                #fill the time difference of all non bipo21x events into a histogram
                                if iso!="bipo212" and iso!="bipo214":
                                    e_other_deltat.Fill(delta_t)

                                #for each event type, fill the time difference histogram
                                if iso=="c14":
                                    e_c14_deltat.Fill(delta_t)
                                elif iso=="0nu":
                                    e_ndbd_deltat.Fill(delta_t)
                                elif iso=="2nu":
                                    e_dbd_deltat.Fill(delta_t)
                                elif iso=="an":
                                    e_an_deltat.Fill(delta_t)
                                elif iso=="bipo212":
                                    e_bipo212_deltat.Fill(delta_t)
                                elif iso=="bipo214":
                                    e_bipo214_deltat.Fill(delta_t)
                                elif iso=="bi210":
                                    e_bi210_deltat.Fill(delta_t)
                                elif iso=="po210":
                                    e_po210_deltat.Fill(delta_t)
                                else:
                                    e_external_deltat.Fill(delta_t)

                                #if the time difference exceeds the cut limit abort
                                if delta_t > 1798788: 
                                    break
            
                                #apply time limit cut
                                if delta_t > 3690 and delta_t < 1798788: 

                                    #fill event radius of previous events into histograms, for all events and non bipo21x events
                                    e_all_rfidvolbi.Fill(radius_prev)
                                    if iso!="bipo212" and iso!="bipo214":
                                        e_other_rfidvolbi.Fill(radius_prev)

                                    #count all events of each type passing this cut
                                    if iso=="c14":
                                        e_c14_rfidvolbi.Fill(radius_prev)
                                        c14_time+=1
                                    elif iso=="0nu":
                                        e_ndbd_rfidvolbi.Fill(radius_prev)
                                        ndbd_time+=1
                                    elif iso=="2nu":
                                        e_dbd_rfidvolbi.Fill(radius_prev)
                                        dbd_time+=1
                                    elif iso=="an":
                                        e_an_rfidvolbi.Fill(radius_prev)
                                        an_time+=1
                                    elif iso=="bipo212":
                                        e_bipo212_rfidvolbi.Fill(radius_prev)
                                        bipo212_time+=1
                                    elif iso=="bipo214":
                                        e_bipo214_rfidvolbi.Fill(radius_prev)
                                        bipo214_time+=1
                                    elif iso=="bi210":
                                        e_bi210_rfidvolbi.Fill(radius_prev)
                                        bi_time+=1
                                    elif iso=="po210":
                                        e_po210_rfidvolbi.Fill(radius_prev)
                                        po_time+=1
                                    else:
                                        e_external_rfidvolbi.Fill(radius_prev)
                                        external_time+=1

                                     #apply fiducial radius cut on the previous event and count and fill distance histograms as for the previous cuts
                                   if radius_prev < 4000:

                                        e_all_deltar.Fill(delta_r)
                                        if iso!="bipo212" and iso!="bipo214":
                                            e_other_deltar.Fill(delta_r)

                                        if iso=="c14":
                                            e_c14_deltar.Fill(delta_r)
                                            c14_fidvol2+=1
                                        elif iso=="0nu":
                                            e_ndbd_deltar.Fill(delta_r)
                                            ndbd_fidvol2+=1
                                        elif iso=="2nu":
                                            e_dbd_deltar.Fill(delta_r)
                                            dbd_fidvol2+=1
                                        elif iso=="an":
                                            e_an_deltar.Fill(delta_r)
                                            an_fidvol2+=1
                                        elif iso=="bipo212":
                                            e_bipo212_deltar.Fill(delta_r)
                                            bipo212_fidvol2+=1
                                        elif iso=="bipo214":
                                            e_bipo214_deltar.Fill(delta_r)
                                            bipo214_fidvol2+=1
                                        elif iso=="bi210":
                                            e_bi210_deltar.Fill(delta_r)
                                            bi_fidvol2+=1
                                        elif iso=="po210":
                                            e_po210_deltar.Fill(delta_r)
                                            po_fidvol2+=1
                                        else:
                                            e_external_deltar.Fill(delta_r)
                                            external_fidvol2+=1

                                        #apply distance cut between the two events with the limit defined when running the script. Count all events and fill nhits histograms for the previous event as for the previous cuts
                                        if delta_r > 0 and delta_r < float(radius_cut):

                                            e_all_nhitsbi.Fill(nhits_prev)
                                            if iso!="bipo212" and iso!="bipo214":
                                                e_other_nhitsbi.Fill(nhits_prev)

                                            if iso=="c14":
                                                e_c14_nhitsbi.Fill(nhits_prev)
                                                c14_deltar+=1
                                            elif iso=="0nu":
                                                e_ndbd_nhitsbi.Fill(nhits_prev)
                                                ndbd_deltar+=1

                                            elif iso=="2nu":
                                                e_dbd_nhitsbi.Fill(nhits_prev)
                                                dbd_deltar+=1
                                            elif iso=="an":
                                                e_an_nhitsbi.Fill(nhits_prev)
                                                an_deltar+=1
                                            elif iso=="bipo212":
                                                e_bipo212_nhitsbi.Fill(nhits_prev)
                                                bipo212_deltar+=1
                                            elif iso=="bipo214":
                                                e_bipo214_nhitsbi.Fill(nhits_prev)
                                                bipo214_deltar+=1
                                            elif iso=="bi210":
                                                e_bi210_nhitsbi.Fill(nhits_prev)
                                                bi_deltar+=1
                                            elif iso=="po210":
                                                e_po210_nhitsbi.Fill(nhits_prev)
                                                po_deltar+=1
                                            else:
                                                e_external_nhitsbi.Fill(nhits_prev)
                                                external_deltar+=1

                                            #apply nhits cut on the previous event
                                            if nhits_prev >= 300 and nhits_prev <= 680: 
                                                
                                                e_original.Fill(energy)
                                                #define type of previous event
                                                iso_prev = ""
                                                if mcIndex_prev<9800000:
                                                    iso_prev="c14"
                                                elif mcIndex_prev<18400000:
                                                    iso_prev="0nu"
                                                elif mcIndex_prev<113100000:
                                                    iso_prev="2nu"
                                                elif mcIndex_prev<113900000:
                                                    iso_prev="an"
                                                elif mcIndex_prev<119400000:
                                                    iso_prev="bipo212"
                                                elif mcIndex_prev<245100000:
                                                    iso_prev="bipo214"
                                                elif mcIndex_prev<442900000:
                                                    iso_prev="bi210"
                                                elif mcIndex_prev<758000000:
                                                    iso_prev="po210"
                                                else:
                                                    iso_prev="external"

                                                #fill energy spectrum for polonium candidate and count polonium candidates passing all cuts. "_cuts" histograms are filled with the energy of both polonium and bismuth candidate, "_po" and "_bi" histograms are filled with the respective polonium or bismuth candidate energy only
                                                if iso=="c14":
                                                    c14+=1
                                                    e_c14_cuts.Fill(energy)
                                                    e_c14_po.Fill(energy)
                                                elif iso=="0nu":
                                                    ndbd+=1
                                                    e_ndbd_cuts.Fill(energy)
                                                    e_ndbd_po.Fill(energy)
                                                elif iso=="2nu":
                                                    dbd+=1
                                                    e_dbd_cuts.Fill(energy)
                                                    e_dbd_po.Fill(energy)
                                                elif iso=="an":
                                                    an+=1
                                                    e_an_cuts.Fill(energy)
                                                    e_an_po.Fill(energy)
                                                elif iso=="bipo212":
                                                    bipo212+=1
                                                    e_bipo212_cuts.Fill(energy)
                                                    e_bipo212_po.Fill(energy)
                                                elif iso=="bipo214":
                                                    bipo214+=1
                                                    e_bipo214_cuts.Fill(energy)
                                                    e_bipo214_po.Fill(energy)
                                                elif iso=="bi210":
                                                    bi+=1
                                                    e_bi210_cuts.Fill(energy)
                                                    e_bi210_po.Fill(energy)
                                                elif iso=="po210":
                                                    po+=1
                                                    e_po210_cuts.Fill(energy)
                                                    e_po210_po.Fill(energy)
                                                else:
                                                    external+=1
                                                    e_external_cuts.Fill(energy)
                                                    e_external_po.Fill(energy)
                    
                                                #count bismuth candidates passing all cuts for each type. If a candidate for j==1 is found abort loop
                                                if j==1:
                                                    e_first.Fill(energy_prev)
                                                    if iso_prev=="c14":
                                                        c14_1prev+=1
                                                        e_c14_cuts.Fill(energy_prev)
                                                        e_c14_bi.Fill(energy_prev)
                                                    elif iso_prev=="0nu":
                                                        ndbd_1prev+=1
                                                        e_ndbd_cuts.Fill(energy_prev)
                                                        e_ndbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="2nu":
                                                        dbd_1prev+=1
                                                        e_dbd_cuts.Fill(energy_prev)
                                                        e_dbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="an":
                                                        an_1prev+=1
                                                        e_an_cuts.Fill(energy_prev)
                                                        e_an_bi.Fill(energy_prev)
                                                    elif iso_prev=="bipo212":
                                                        e_bipo212_cuts.Fill(energy_prev)
                                                        e_bipo212_bi.Fill(energy_prev)                                                    
                                                        bipo212_1prev+=1
                                                    elif iso_prev=="bipo214":
                                                        e_bipo214_cuts.Fill(energy_prev)
                                                        e_bipo214_bi.Fill(energy_prev)
                                                        bipo214_1prev+=1
                                                    elif iso_prev=="bi210":
                                                        e_bi210_cuts.Fill(energy_prev)
                                                        e_bi210_bi.Fill(energy_prev)
                                                        bi_1prev+=1
                                                    elif iso_prev=="po210":
                                                        po_1prev+=1
                                                        e_po210_cuts.Fill(energy_prev)
                                                        e_po210_bi.Fill(energy_prev)
                                                    else:
                                                        external_1prev+=1
                                                        e_external_cuts.Fill(energy_prev)
                                                        e_external_bi.Fill(energy_prev)

                                                    #count all events for which the polonium and bismuth candidate are of the same coincidence type
                                                    if iso=="bipo212" and iso_prev=="bipo212":
                                                        bipo212_both += 1
                                                    
                                                    if iso=="bipo214" and iso_prev=="bipo214":
                                                        bipo214_both += 1

                                                    break

                                                #if no event for j==1 is found, repeat for j==2, if event is found abort loop                                   
                                                if j==2:
                                                    e_second.Fill(energy_prev)
                                                    if iso_prev=="c14":
                                                        c14_2prev+=1
                                                        e_c14_cuts.Fill(energy_prev)
                                                        e_c14_bi.Fill(energy_prev)
                                                    elif iso_prev=="0nu":
                                                        ndbd_2prev+=1
                                                        e_ndbd_cuts.Fill(energy_prev)
                                                        e_ndbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="2nu":
                                                        dbd_2prev+=1
                                                        e_dbd_cuts.Fill(energy_prev)
                                                        e_dbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="an":
                                                        an_2prev+=1
                                                        e_an_cuts.Fill(energy_prev)
                                                        e_an_bi.Fill(energy_prev)
                                                    elif iso_prev=="bipo212":
                                                        e_bipo212_cuts.Fill(energy_prev)
                                                        e_bipo212_bi.Fill(energy_prev)
                                                        bipo212_2prev+=1
                                                    elif iso_prev=="bipo214":
                                                        e_bipo214_cuts.Fill(energy_prev)
                                                        e_bipo214_bi.Fill(energy_prev)
                                                        bipo214_2prev+=1
                                                    elif iso_prev=="bi210":
                                                        e_bi210_cuts.Fill(energy_prev)
                                                        e_bi210_bi.Fill(energy_prev)
                                                        bi_2prev+=1
                                                    elif iso_prev=="po210":
                                                        e_po210_cuts.Fill(energy_prev)
                                                        e_po210_bi.Fill(energy_prev)
                                                        po_2prev+=1
                                                    else:
                                                        external_2prev+=1
                                                        e_external_cuts.Fill(energy_prev)
                                                        e_external_bi.Fill(energy_prev)
                                                
                                                    if iso=="bipo212" and iso_prev=="bipo212":
                                                        bipo212_both += 1
                                                    
                                                    if iso=="bipo214" and iso_prev=="bipo214":
                                                        bipo214_both += 1

                                                    break
                                    
                                                #if no event for j==2 is found, repeat for j==3
                                                if j==3:
                                                    e_second.Fill(energy_prev)
                                                    if iso_prev=="c14":
                                                        c14_3prev+=1
                                                        e_c14_cuts.Fill(energy_prev)
                                                        e_c14_bi.Fill(energy_prev)
                                                    elif iso_prev=="0nu":
                                                        ndbd_3prev+=1
                                                        e_ndbd_cuts.Fill(energy_prev)
                                                        e_ndbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="2nu":
                                                        dbd_3prev+=1
                                                        e_dbd_cuts.Fill(energy_prev)
                                                        e_dbd_bi.Fill(energy_prev)
                                                    elif iso_prev=="an":
                                                        an_3prev+=1
                                                        e_an_cuts.Fill(energy_prev)
                                                        e_an_bi.Fill(energy_prev)
                                                    elif iso_prev=="bipo212":
                                                        e_bipo212_cuts.Fill(energy_prev)
                                                        e_bipo212_bi.Fill(energy_prev)
                                                        bipo212_3prev+=1
                                                    elif iso_prev=="bipo214":
                                                        e_bipo214_cuts.Fill(energy_prev)
                                                        e_bipo214_bi.Fill(energy_prev)
                                                        bipo214_3prev+=1
                                                    elif iso_prev=="bi210":
                                                        e_bi210_cuts.Fill(energy_prev)
                                                        e_bi210_bi.Fill(energy_prev)
                                                        bi_3prev+=1
                                                    elif iso_prev=="po210":
                                                        e_po210_cuts.Fill(energy_prev)
                                                        e_po210_bi.Fill(energy_prev)
                                                        po_3prev+=1
                                                    else:
                                                        external_3prev+=1
                                                        e_external_cuts.Fill(energy_prev)
                                                        e_external_bi.Fill(energy_prev)
                                                
                                                    if iso=="bipo212" and iso_prev=="bipo212":
                                                        bipo212_both += 1
                                                    
                                                    if iso=="bipo214" and iso_prev=="bipo214":
                                                        bipo214_both += 1


                                    
#write all counted events for each cut to file
output = open("/data/langrock/te_loaded_mergeddata/" + cut + "_cutsmonth_" + radius_cut + ".txt","w")

c14_string = "c14_full: " + str(c14_full) +  "\t c14_fidvol: " + str(c14_fidvol) +  "\t c14_nhits: " + str(c14_nhits) +  "\t c14_time: " + str(c14_time) +  "\t c14_fidvol2: " + str(c14_fidvol2) + "\t deltar: " + str(c14_deltar) + "\t c14: " + str(c14) + "\t c14_1prev: " + str(c14_1prev) + "\t c14_2prev: " + str(c14_2prev) + "\t c14_3prev: " + str(c14_3prev)
ndbd_string = "ndbd_full: " + str(ndbd_full) + "\t ndbd_fidvol: " + str(ndbd_fidvol) +  "\t ndbd_nhits: " + str(ndbd_nhits) +  "\t ndbd_time: " + str(ndbd_time) +  "\t ndbd_fidvol2: " + str(ndbd_fidvol2) + "\t deltar: " + str(ndbd_deltar)  + "\t ndbd: " + str(ndbd) + "\t ndbd_1prev: " + str(ndbd_1prev) + "\t ndbd_2prev: " + str(ndbd_2prev) + "\t ndbd_3prev: " + str(ndbd_3prev)
dbd_string = "dbd_full: " + str(dbd_full) + "\t dbd_fidvol: " + str(dbd_fidvol) +  "\t dbd_nhits: " + str(dbd_nhits) +  "\t dbd_time: " + str(dbd_time) +  "\t dbd_fidvol2: " + str(dbd_fidvol2) + "\t deltar: " + str(dbd_deltar)  + "\t dbd: " + str(dbd) + "\t dbd_1prev: " + str(dbd_1prev) + "\t dbd_2prev: " + str(dbd_2prev) + "\t dbd_3prev: " + str(dbd_3prev)
an_string = "an_full: " + str(an_full) + "\t an_fidvol: " + str(an_fidvol) +  "\t an_nhits: " + str(an_nhits) +  "\t an_time: " + str(an_time) +  "\t an_fidvol2: " + str(an_fidvol2) + "\t deltar: " + str(an_deltar) + "\t an: " + str(an) + "\t an_1prev: " + str(an_1prev) + "\t an_2prev: " + str(an_2prev) + "\t an_3prev: " + str(an_3prev)
bipo212_string = "bipo212_full: " + str(bipo212_full) + "\t bipo212_fidvol: " + str(bipo212_fidvol) +  "\t bipo212_nhits: " + str(bipo212_nhits) +  "\t bipo212_time: " + str(bipo212_time) +  "\t bipo212_fidvol2: " + str(bipo212_fidvol2) + "\t deltar: " + str(bipo212_deltar)  + "\t bipo212: " + str(bipo212) + "\t bipo212_1prev: " + str(bipo212_1prev) + "\t bipo212_2prev: " + str(bipo212_2prev) + "\t bipo212_3prev: " + str(bipo212_3prev)
bipo214_string = "bipo214_full: " + str(bipo214_full) + "\t bipo214_fidvol: " + str(bipo214_fidvol) +  "\t bipo214_nhits: " + str(bipo214_nhits) +  "\t bipo214_time: " + str(bipo214_time) +  "\t bipo214_fidvol2: " + str(bipo214_fidvol2) + "\t deltar: " + str(bipo214_deltar)  + "\t bipo214: " + str(bipo214) + "\t bipo214_1prev: " + str(bipo214_1prev) + "\t bipo214_2prev: " + str(bipo214_2prev) + "\t bipo214_3prev: " + str(bipo214_3prev)
bi210_string = "bi210_full: " + str(bi_full) + "\t bi210_fidvol: " + str(bi_fidvol) +  "\t bi210_nhits: " + str(bi_nhits) +  "\t bi210_time: " + str(bi_time) +  "\t bi210_fidvol2: " + str(bi_fidvol2) + "\t deltar: " + str(bi_deltar)  + "\t bi210: " + str(bi) + "\t bi210_1prev: " + str(bi_1prev) + "\t bi210_2prev: " + str(bi_2prev) + "\t bi210_3prev: " + str(bi_3prev)
po210_string =  "po210_full: " + str(po_full) + "\t po210_fidvol: " + str(po_fidvol) +  "\t po210_nhits: " + str(po_nhits) +  "\t po210_time: " + str(po_time) +  "\t po210_fidvol2: " + str(po_fidvol2) + "\t deltar: " + str(po_deltar)  + "\t po210: " + str(po) + "\t po210_1prev: " + str(po_1prev) + "\t po210_2prev: " + str(po_2prev) + "\t po210_3prev: " + str(po_3prev)
external_string =  "external_full: " + str(external_full) + "\t external_fidvol: " + str(external_fidvol) +  "\t external_nhits: " + str(external_nhits) +  "\t external_time: " + str(external_time) +  "\t external_fidvol2: " + str(external_fidvol2) + "\t deltar: " + str(external_deltar)  + "\t external: " + str(external) + "\t external_1prev: " + str(external_1prev) + "\t external_2prev: " + str(external_2prev) + "\t external_3prev: " + str(external_3prev)
bipo212_both_string = "bipo212_both: " + str(bipo212_both)
bipo214_both_string = "bipo214_both: " + str(bipo214_both)

output.write(c14_string)
output.write("\n")
output.write(ndbd_string)
output.write("\n")
output.write(dbd_string)
output.write("\n")
output.write(an_string)
output.write("\n")
output.write(bipo212_string)
output.write("\n")
output.write(bipo214_string)
output.write("\n")
output.write(bi210_string)
output.write("\n")
output.write(po210_string)
output.write("\n")
output.write(external_string)
output.write("\n")
output.write(bipo212_both_string)
output.write("\n")
output.write(bipo214_both_string)
output.write("\n")

output.close()

#write histograms to file
file_name_data.Write()

e_original.Delete()
e_first.Delete()
e_second.Delete()
e_bipo212.Delete()
e_bipo214.Delete()
e_bi210.Delete()
e_po210.Delete()
e_c14.Delete()
e_ndbd.Delete()
e_dbd.Delete()
e_an.Delete()
e_external.Delete()
e_bipo212_cuts.Delete()
e_bipo214_cuts.Delete()
e_bi210_cuts.Delete()
e_po210_cuts.Delete()
e_c14_cuts.Delete()
e_ndbd_cuts.Delete()
e_dbd_cuts.Delete()
e_an_cuts.Delete()
e_external_cuts.Delete()

e_bipo212_po.Delete()
e_bipo214_po.Delete()
e_bi210_po.Delete()
e_po210_po.Delete()
e_c14_po.Delete()
e_ndbd_po.Delete()
e_dbd_po.Delete()
e_an_po.Delete()
e_external_po.Delete()

e_bipo212_bi.Delete()
e_bipo214_bi.Delete()
e_bi210_bi.Delete()
e_po210_bi.Delete()
e_c14_bi.Delete()
e_ndbd_bi.Delete()
e_dbd_bi.Delete()
e_an_bi.Delete()
e_external_bi.Delete()

e_bipo212_deltat.Delete()
e_bipo214_deltat.Delete()
e_bi210_deltat.Delete()
e_po210_deltat.Delete()
e_c14_deltat.Delete()
e_ndbd_deltat.Delete()
e_dbd_deltat.Delete()
e_an_deltat.Delete()
e_external_deltat.Delete()

e_all_deltat.Delete()
e_other_deltat.Delete()

e_bipo212_deltar.Delete()
e_bipo214_deltar.Delete()
e_bi210_deltar.Delete()
e_po210_deltar.Delete()
e_c14_deltar.Delete()
e_ndbd_deltar.Delete()
e_dbd_deltar.Delete()
e_an_deltar.Delete()
e_external_deltar.Delete()

e_all_deltar.Delete()
e_other_deltar.Delete()

e_bipo212_rfidvolbi.Delete()
e_bipo214_rfidvolbi.Delete()
e_bi210_rfidvolbi.Delete()
e_po210_rfidvolbi.Delete()
e_c14_rfidvolbi.Delete()
e_ndbd_rfidvolbi.Delete()
e_dbd_rfidvolbi.Delete()
e_an_rfidvolbi.Delete()
e_external_rfidvolbi.Delete()

e_all_rfidvolbi.Delete()
e_other_rfidvolbi.Delete()

e_bipo212_nhitspo.Delete()
e_bipo214_nhitspo.Delete()
e_bi210_nhitspo.Delete()
e_po210_nhitspo.Delete()
e_c14_nhitspo.Delete()
e_ndbd_nhitspo.Delete()
e_dbd_nhitspo.Delete()
e_an_nhitspo.Delete()
e_external_nhitspo.Delete()

e_all_nhitspo.Delete()
e_other_nhitspo.Delete()

e_bipo212_nhitsbi.Delete()
e_bipo214_nhitsbi.Delete()
e_bi210_nhitsbi.Delete()
e_po210_nhitsbi.Delete()
e_c14_nhitsbi.Delete()
e_ndbd_nhitsbi.Delete()
e_dbd_nhitsbi.Delete()
e_an_nhitsbi.Delete()
e_external_nhitsbi.Delete()

e_all_nhitsbi.Delete()
e_other_nhitsbi.Delete()

#raw_input("RET to EXIT");
