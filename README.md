# scival_collaboration_network
Scripts for manipulating publication data from SciVal in order to create diagrams of collaborating researchers. 
To use this, you need a two .csv files as inputs. 

The first is a list of the members you are interested in making a graph of. There should be no headers, and each 
line in the .csv file should have the format "Lastname","Firstname". 

The second file is data exported from SciVal. The data exported should have three columns: Authors, Citations, and EID.

Keep both of those .csv files in the same folder as the python script, and edit the file names within the script to match your files.
The output will be another .csv file. This outputted .csv file can then be used as the input to cytoscape. 

There is currently a known bug where .csv files generated differently will cause errors. If you see an encoding error in your error log, try 
uncommenting out one of lines 9-11 and try running again.

In Cytoscape, import the data from the output.csv file. When importing, make the "from" column the source node, and make the "to"
column the target node. Once in Cytoscape, you can import the styles.xml file to edit the appearance of your graph. You can download 
the yFiles layouts to get additional layout options (yFiles Hierarchical seems to work quite well).
