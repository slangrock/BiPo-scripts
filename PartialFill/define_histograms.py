#!/usr/bin/env python
import ROOT

class DefineHistograms:
    """Class to define all histograms to be filled for SMELLIE analysisthe Partial fill analysis


    """


    def __init__(self):
        self.h_energy_full = ROOT.TH1D("h_energy_full", "", 100, 0.01, 5)
        self.h_energy_pocut = ROOT.TH1D("h_energy_pocut", "", 100, 0.01, 5)
        self.h_energy_deltatcut = ROOT.TH1D("h_energy_deltatcut", "", 100, 0.01, 5)
        self.h_energy_bifidvolcut = ROOT.TH1D("h_energy_bifidvolcut", "", 100, 0.01, 5)
        self.h_energy_deltarcut = ROOT.TH1D("h_energy_deltarcut", "", 100, 0.01, 5)
        self.h_energy_bicut = ROOT.TH1D("h_energy_bicut", "", 100, 0.01, 5)
        self.h_energy_allcut = ROOT.TH1D("h_energy_allcut", "", 100, 0.01, 5)
        self.h_nhitspo_full = ROOT.TH1D("h_nhitspo_full", "", 150, 0.0, 1500)
        self.h_nhitspo_pocut = ROOT.TH1D("h_nhitspo_pocut", "", 150, 0.0, 1500)
        self.h_nhitspo_deltatcut = ROOT.TH1D("h_nhitspo_deltatcut", "", 150, 0.0, 1500)
        self.h_nhitspo_bifidvolcut = ROOT.TH1D("h_nhitspo_bifidvolcut", "", 150, 0.0, 1500)
        self.h_nhitspo_deltarcut = ROOT.TH1D("h_nhitspo_deltarcut", "", 150, 0.0, 1500)
        self.h_nhitspo_bicut = ROOT.TH1D("h_nhitspo_bicut", "", 150, 0.0, 1500)
        self.h_nhitspo_allcut = ROOT.TH1D("h_nhitspo_allcut", "", 150, 0.0, 1500)
        self.h_nhitsbi_full = ROOT.TH1D("h_nhitsbi_full", "", 150, 0.0, 1500)
        self.h_nhitsbi_pocut = ROOT.TH1D("h_nhitsbi_pocut", "", 150, 0.0, 1500)
        self.h_nhitsbi_deltatcut = ROOT.TH1D("h_nhitsbi_deltatcut", "", 150, 0.0, 1500)
        self.h_nhitsbi_bifidvolcut = ROOT.TH1D("h_nhitsbi_bifidvolcut", "", 150, 0.0, 1500)
        self.h_nhitsbi_deltarcut = ROOT.TH1D("h_nhitsbi_deltarcut", "", 150, 0.0, 1500)
        self.h_nhitsbi_bicut = ROOT.TH1D("h_nhitsbi_bicut", "", 150, 0.0, 1500)
        self.h_nhitsbi_allcut = ROOT.TH1D("h_nhitsbi_allcut", "", 150, 0.0, 1500)
        self.h_deltat_full = ROOT.TH1D("h_deltat_full", "", 10000, 0.0, 1800000)
        self.h_deltat_pocut = ROOT.TH1D("h_deltat_pocut", "", 10000, 0.0, 1800000)
        self.h_deltat_deltatcut = ROOT.TH1D("h_deltat_deltatcut", "", 10000, 0.0, 1800000)
        self.h_deltat_bifidvolcut = ROOT.TH1D("h_deltat_bifidvolcut", "", 10000, 0.0, 1800000)
        self.h_deltat_deltarcut = ROOT.TH1D("h_deltat_deltarcut", "", 10000, 0.0, 1800000)
        self.h_deltat_bicut = ROOT.TH1D("h_deltat_bicut", "", 10000, 0.0, 1800000)
        self.h_deltat_allcut = ROOT.TH1D("h_deltat_allcut", "", 10000, 0.0, 1800000)
        self.h_deltar_full = ROOT.TH1D("h_deltar_full", "", 100, 0.0, 4000)
        self.h_deltar_pocut = ROOT.TH1D("h_deltar_pocut", "", 100, 0.0, 4000)
        self.h_deltar_deltatcut = ROOT.TH1D("h_deltar_deltatcut", "", 100, 0.0, 4000)
        self.h_deltar_bifidvolcut = ROOT.TH1D("h_deltar_bifidvolcut", "", 100, 0.0, 4000)
        self.h_deltar_deltarcut = ROOT.TH1D("h_deltar_deltarcut", "", 100, 0.0, 4000)
        self.h_deltar_bicut = ROOT.TH1D("h_deltar_bicut", "", 100, 0.0, 4000)
        self.h_deltar_allcut = ROOT.TH1D("h_deltar_allcut", "", 100, 0.0, 4000)
        self.h_rfidvolbi_full = ROOT.TH1D("h_rfidvolbi_full", "", 150, 0.0, 6000)
        self.h_rfidvolbi_pocut = ROOT.TH1D("h_rfidvolbi_pocut", "", 150, 0.0, 6000)
        self.h_rfidvolbi_deltatcut = ROOT.TH1D("h_rfidvolbi_deltatcut", "", 150, 0.0, 6000)
        self.h_rfidvolbi_bifidvolcut = ROOT.TH1D("h_rfidvolbi_bifidvolcut", "", 150, 0.0, 6000)
        self.h_rfidvolbi_deltarcut = ROOT.TH1D("h_rfidvolbi_deltarcut", "", 150, 0.0, 6000)
        self.h_rfidvolbi_bicut = ROOT.TH1D("h_rfidvolbi_bicut", "", 150, 0.0, 6000)
        self.h_rfidvolbi_allcut = ROOT.TH1D("h_rfidvolbi_allcut", "", 150, 0.0, 6000)


