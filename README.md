# BiPo-scripts

Scripts used to study Bi212Po212 and Bi214Po214 measurements in the pure scintillator and partia water-scintillator run phase of SNO+. To run any of these files ROOT, the SNO+ RAT and a python environment have to be loaded. Please be aware that in the current state all scripts contain hardcoded directory paths which will have to be adjusted for different users.

## Pure Scintillator Phase Scripts

To run the entire Bi21xPo21x cut selection on the RAT ROOT ntuples listed in root_files.txt do 

    $ python BiPocuts.py 'cut' 'deltar_cut'

'cut' can have the values 'bipo212' or 'bipo214' dependent on which selection needs to be run. 'deltar_cut' is the cut value on the distance between Polonium and Bismuth candidate in mm, e.g. for a distance cut of 1500mm select '1500'. This script counts all events selected by each cut and saves the resulting numbers to a text file. It also fills histograms, which are saved to root files. 

To purely study the cut efficiencies of different nhits cuts on different isotopes, run 

    $ python nhitscuts.py 'cut' 

Here, 'cut' can have the values 'po212', 'po214', 'bi212' or 'bi214'. It counts all events within the given fiducial volume and all events surviving the applied nhits cuts on all files listed in root_files.txt and prints the resulting numbers to the screen.

The script 

    $ python nhits_eff_rej.py

produces efficiency and rejection plots for a certain range of nhits cuts. This script was used to study the best Polonium cut nhits efficiency limits. It is currently set up to study the Po214 efficiency progression versus the Po212 rejection over varying upper nhits cut limits.

To plot the histograms returned by BiPocuts.py, run 

    $ python plots.py 'isotope' 'cut'

with 'isotope' being the studied background as listed in the second column of root_files.txt and 'cut' being 'bipo212' or 'bipo214'. It is currently set up to plot histograms produced with 'deltar_cut'=='1500'. The nhits distributions for a selected number of isotopes can be plotted using 

    $ python nhit_plots.py

All input files used for this script are produced by BiPocuts.py.

All these scripts are used to study cut efficiencies of the Bi21xPo21x on different isotopes. Using the target rates for each isotope, the expected Bi21xPo21x coincidences and mistagged coincidences can be calculated using 

    $ python BiPo_meas_uncertainty.py

This script uses the rates of each background after applying the various nhits cuts to the target rates as well as the target rates of the Bi21xPo21x coincidence and the expected efficiency of the cut selection. Different background levels can be studied. The script calculates the event yields and the uncertainty on the measurement for each day over a run time of 180 days and saves the results for each day to a text file. It also produces the uncertainty progression plots for 180 days.

To apply the cut selection to the one month Tellurium loaded merged data set, use 

    $ python mergeddata.py 'cut' 'deltar_cut' 

with 'cut' being 'bipo212' or 'bipo214' and 'deltar_cut' being the distance cut value as above. This script counts the event yields and saves them to a text file and it fills histograms which are saved to output root files.

##Partial Fill Phase Scripts

To run the full Bi21xPo21x cut selection on partial fill root files, run 

    $ python apply_cuts.py -c 'cut' -v 'volume'

All input root files must have the structure Isotope_fillvolume.root. The -c flag defines which cut selection is applied ('bipo212' or 'bipo214') and the -v flag determines in which fill volume the events were produced ('water' or 'scint'). This script counts all events passing each cut and saves them to text files and writes the filled histograms to output root files over the entire fill period. To get the event yield for each day of filling, run 

    $ python dailycuts.py -c 'cut'

instead. Equivalent to the Pure Scintillator scripts, the cut efficiencies of the nhits cuts on each background isotope can be studied using 

    $ python nhitscuts.py -c 'cut'

This script monitors the resulting event yields from the 'po212', 'po214' 'bi212' and 'bi214' cuts for each day of filling. 

    $ python plot_cutefficiency_progression.py 

uses the output of these two scripts to calculate the cut efficiencies for each fill level (for cuts with changing cut efficiency) or the overall cut efficiency (for cuts which do not change over the fill time). The two scripts 

    $ python extract_fit_values.py 

and 

    $ python z_evaluation.py

contain tools to determine the cuts applied to the RAT partial fill files. 

    $ python BiPo_meas_uncertainty.py

does the same as the Pure Scintillator script, monitor the progression of the uncertainties and event yields over a 180 day pure scintillator run. However, this script includes the results from the partial fill analysis and produces the uncertainty progression plots comparing an analysis uncluding partial fill and without partial fill studies.

The file split_level.txt includes two columns, the first one containing the day on which the filling took place and the second contains the equivalent fill level. The function get_fill_level() in apply_cuts.py is designed to produce this file with information from the database, but this function still needs to be written. The files define_histograms.py and plot_style.py contain classes used in various different scripts. 
