Hello, this script will evaluate the percentage success rate for each barcode in your data. It filters by gene, and can also be used to filter by polymerase. It will plot these values in a graph, and then give you the option to save a csv file with the % success rates of every barcode in your filtered set for further analysis/planning.

-----------------------------------------------

You will need: 

- A csv file of all amps you may be interested in, with a column headed 'barcode', a column headed 'sample_ID' and a column headed 'pass_fail'. If you want to sort by polymerase, you will also need a column headed 'polymerase'.

	1) Extra columns are not a problem, don't bother trimming them off
	2) Extra amp info for genes you aren't interested in also aren't a problem. Just do a bulk export and use that data.
	3) Data in the barcode column can be formatted however you want (eg 004, 4, 004F-004R) as long as it's the same throughout your csv file.
	4) Data in the pass_fail column needs to be either PASSED or FAILED, as per your own criteria.


-----------------------------------------------

What to do to run the script:

1) Navigate to the folder where you have put both the provided files and your input csv file.

2) Type in what you want in the following way:

	python3 main.py input_file.csv gene polymerase

	* NB polymerase is optional, if you don't write one then it will default to all data for that gene. Make sure you spell the gene and polymerase as they're written in your input file (case sensitive). You also shouldn't have spaces within the gene or polymerase names*


	So for example, if I want to find the barcode success rates for DRB1 using a polymerase called HaNnaH_Taq, I would type:

	python3 main.py hannahs_import_file.csv DRB1 HaNnaH_Taq


	If I want to find the barcode success rates for DRB1 using all the polymerases I've used in my input file, I would type:

	python3 barcodes.py hannahs_import_file.csv DRB1


-----------------------------------------------

Hannah 04/06/2020

