from barcode_report import *
import sys

# taking user input, checking whether there are the right number of inputs
# if correct number of inputs, sets off the report (in barcode_report.py)

counter = 0

while counter == 0:
    if __name__ == "__main__":
        if len(sys.argv) > 4:
            counter += 1
            print("")
            print("You've added too many inputs. Make sure it's barcodes.py csv_file.csv gene polymerase(if wanted)")
            print("")
        elif len(sys.argv) <=2:
            counter += 1
            print("")
            print("You've added too few inputs. Make sure it's barcodes.py csv_file.csv gene polymerase(if wanted)")
            print("")
        elif len(sys.argv) == 4:
            counter += 1
            barcode_report(sys.argv[1], sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 3:
            counter += 1
            barcode_report(sys.argv[1], sys.argv[2])
