Hello, this script will evaluate the percentage success rate for each barcode in your data. It filters by gene, and can also be used to filter by polymerase. It will plot these values in a graph, and then give you the option to save a csv file with the % success rates of every barcode in your filtered set for further analysis/planning.

-----------------------------------------------

You will need: 

- A csv file of all amps you may be interested in, with a column headed 'barcode', a column headed 'sample_ID' and a column headed 'pass_fail'. If you want to sort by polymerase, you will also need a column headed 'polymerase'.

	1) Extra columns are not a problem, don't bother trimming them off
	2) Extra amp info for genes you aren't interested in also aren't a problem. Just do a bulk export and use that data.
	3) Data in the barcode column can be formatted however you want (eg 004, 4, 004F-004R) as long as it's the same throughout your csv file.
	4) Data in the pass_fail column needs to be either PASSED or FAILED, as per your own criteria.


-----------------------------------------------
How to set-up the script to run on your machine for the first time:

1) Download the folder from GitHub
![downloading files](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/downloading%20files.png)

2) Unzip the folder and put it in your Documents (I renamed mine 'barcode_evaluator_script')
![file layout](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/File%20Layout.png)

3) Navigate to the folder in Terminal and download the required packages
![initial terminal](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/initial%20terminal.png)

-----------------------------------------------
What to do to run the script each time from now on:

1) Put your input CSV file in the barcode evaluator folder. Navigate to this folder in terminal and type in what you need from the script (more info below)

![setting off in terminal](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/setting%20off%20script.png)


2) The second line should be adapted in the following way:

![Image explaining input](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/Example%20input.png)


* NB polymerase is optional, if you don't write one then it will default to all data for that gene. Make sure you spell the gene and polymerase as they're written in your input file (case sensitive). You also shouldn't have spaces within the gene or polymerase names*


So for example, if I want to find the barcode success rates for DRB1 using a polymerase called HaNnaH_Taq, I would type:

python3 main.py hannahs_import_file.csv DRB1 HaNnaH_Taq


If I want to find the barcode success rates for DRB1 using all the polymerases I've used in my input file, I would type:

python3 main.py hannahs_import_file.csv DRB1

3) You will be asked how many of the best/worst barcodes you want listed.

![How many barcodes](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/asking%20for%20bc%20numbers.png)

4) A graph will be plotted (example below)

![Example graph](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/example%20graph.png)

5) You'll be asked whether you want to save an additional CSV of every barcode it's used and their % success rate (prompted to type Y or N)

![% success CSV](https://github.com/hannahmacpherson/barcode_evaluator/blob/master/asking%20for%20bc%20numbers.png)


-----------------------------------------------

Hannah 04/06/2020

