import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import csv



# takes csv input file and filters it by gene and polymerase to output a dataframe
def make_dataframe(amp_csv, gene, polymerase='all'):
    df = pd.read_csv(amp_csv)
    df = df.loc[df['gene'] == gene]
    if polymerase != "all":
        df = df.loc[df['polymerase'] == polymerase]
    rows = row_counter(df)
    if rows == 0: # aka dataframe is empty
        sys.exit("Filtered data has zero rows, the gene or polymerase may be different to how they are written in your input file.")
    else:
        return df

# counts how many rows in dataframe. If you've sorted it, it will therefore tell you how many amps your data after this point is based on
def row_counter(df):
    row_count = len(df)
    return row_count

# works out the average number of amps per barcode in your (possibly filtered by gene/polymerase) dataframe
def average_amps_per_barcode(df):
    filtered_df = df[['barcode', 'sample_ID']]
    filtered_grouped_df = filtered_df.groupby(['barcode']).size().reset_index(name='counts')
    mean_amps_per_bc = filtered_grouped_df['counts'].mean()
    return mean_amps_per_bc

def barcode_success_rate(df):
        # creates a dataframe with a % success rate per barcode (NB only two columns in resulting dataframe + index)
        x,y = 'barcode', 'pass_fail'
        # sorts dataframe to group it by both barcode and pass/fail. Gives pass/fail for each barcode a score out of 1
        counted_df = df.groupby(x)[y].value_counts(normalize=True)
        # converts this score into a percentage and labels the column accordingly
        percentage_df = counted_df.mul(100)
        percentage_df = percentage_df.rename('percentage_success').reset_index()
        # only keeps the success rate (%) of the pass column
        success_rate_df = percentage_df.loc[percentage_df['pass_fail'] == "PASSED"].reset_index(drop=True)
        # get rid of pass_fail column because now every line says PASS lol
        success_rate_df = success_rate_df.drop(columns='pass_fail')
        return success_rate_df

# what it says on the tin, saves the dataframe to a csv file in your local area
def save_df_to_csv_tabbed(df, gene, polymerase='all'):
    df.to_csv(f'{gene}_{polymerase}_polymerase_percentage_success_data.csv',sep='\t', index=False)

# sorts dataframe by % success, then prints out the worst x you specify 
def worst_barcodes(df, number_of_barcodes=5):
    # in case number_of_barcodes comes as a string, converting to integer
    number_of_barcodes_int = int(number_of_barcodes)
    success_rate_df = barcode_success_rate(df)
    success_rate_df = success_rate_df.sort_values(by='percentage_success', ascending=True)
    chop_by_number_of_bc = success_rate_df[:number_of_barcodes_int]
    #convert to string so you don't print the index
    printable_version = chop_by_number_of_bc.to_string(index=False)
    return printable_version

def best_barcodes(df, number_of_barcodes=5):
    # sorts dataframe by % success, then prints out the worst x you specify
    #in case number_of_barcodes comes as a string, converting to integer
    number_of_barcodes_int = int(number_of_barcodes)
    success_rate_df = barcode_success_rate(df)
    success_rate_df = success_rate_df.sort_values(by='percentage_success', ascending=False)
    chop_by_number_of_bc = success_rate_df[:number_of_barcodes_int]
    #convert to string so you don't print the index
    printable_version = chop_by_number_of_bc.to_string(index=False)
    return printable_version

def best_and_worst_barcodes(df, number_of_barcodes=5):
    worst = worst_barcodes(df, number_of_barcodes)
    best = best_barcodes(df, number_of_barcodes)
    return best, worst

def percentage_success_for_particular_barcode(barcode, df):
    df_of_success_rates = barcode_success_rate(df)
    df_for_barcode = df_of_success_rates.loc[df_of_success_rates['barcode'] == barcode]
    df_as_string =  df_for_barcode.to_string(index=False)
    print(df_as_string)

def number_of_amps_per_barcode(df):
    filtered_df = df[['barcode', 'sample_ID']]
    filtered_grouped_df = filtered_df.groupby(['barcode']).size().reset_index(name='counts')
    return filtered_grouped_df

def plot_barcode_success_rate(amp_csv, gene, polymerase='all'):
    df = make_dataframe(amp_csv, gene, polymerase)
    amps_per_bc = number_of_amps_per_barcode(df)
    success_rate = barcode_success_rate(df)
    number_of_amps = row_counter(df)

    success_and_amps_per_bc = success_rate.merge(amps_per_bc, left_on='barcode', right_on='barcode')
    print(success_and_amps_per_bc)

    plt.figure(figsize = (18,7))
    plot_order = success_and_amps_per_bc.sort_values(by='percentage_success', ascending=True).barcode.values
    
    plot = sns.barplot(x="barcode", y="percentage_success", data=success_and_amps_per_bc, order=plot_order)
    plot.set(
        xlabel="{gene} Barcodes".format(gene=gene), 
        ylabel = "Percentage Success Rate", 
        title='Percentage Success for {gene} Barcodes over a Total of {number_of_amps} Amplifications using {polymerase} Polymerase(s)'.format(gene=gene, number_of_amps=number_of_amps, polymerase = polymerase))
    plt.setp(plot.get_xticklabels(), rotation=90)
    plt.setp(plot.set_yticklabels([0,20,40,60,80,100]), rotation=90)
    #plot2 = sns.lineplot(x="barcode", y="counts", data=success_and_amps_per_bc, order=plot_order)
 






def save_plot_png(amp_csv, gene, polymerase='all'):
    plot = plot_barcode_success_rate(amp_csv, gene, polymerase)
    plt.savefig(f'barcode_success_graph_for_{gene}_{polymerase}.png')


        
















            
