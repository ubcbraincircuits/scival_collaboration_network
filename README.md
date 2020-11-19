# scival_collaboration_network
Scripts for manipulating publication data from SciVal in order to create diagrams of collaborating researchers. 
To use this, you need a two .csv files as inputs. 

The first is a list of the members you are interested in making a graph of. There should be no headers, and each 
line in the .csv file should have the format "Lastname","Firstname". 

The second file is data exported from SciVal. The data exported should have three columns: Authors, Citations, and EID.

Keep both of those .csv files in the same folder as the python script, and edit the file names within the script to match your files.
The output will be another .csv file.
