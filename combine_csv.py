# Run the python script in Command line which conatins the CSV files - python combine_csv.py filename1.csv filename2.csv 

# Python library to handle reading and doing operations on .csv files
import pandas as pd
# python library to access commandline arguments/Interacting with the host via command line 
import sys

# Defining inputs and output 
file_names = sys.argv[1:]
output_file_name = 'combined.csv'

# Checking if the file names are missing .csv at the end and appending .csv if missing
for i in range(len(file_names)):
    if file_names[i].find('.csv') == -1:
       file_names[i] += '.csv'
    
# The main program
if __name__ == "__main__":
    
    # Initializing an empty data frame that will hold combined data
    df_combined = pd.DataFrame()
    
    # Looping over each file, reading it and adding additional column with the filename.
    for filename in sys.argv[1:]:
        df = pd.read_csv(filename)
        df['filename'] = [filename for i in range(len(df))]
        # Append the current input file data to the big combined data frame
        df_combined = df_combined.append(df,ignore_index=True)
    
    # Saving output dataframe to the directory specified by the user
    df_combined.to_csv(output_file_name, index = False)

    # Calling tests to test for consistncy
    from test_combine_csv import run_tests

    run_tests(file_names, output_file_name)


###############################################################################


 #print To stdout
 
   # with open(output_file_name, 'r') as f:
        #for line in f.readlines():
          #  print(line.strip())

##############################################################################
          
#Function to check if the OS path /file is there or Missing - output error if not found 

#def check_if_all_dir_exits(arguments):
    """
    Check if all the given files exists using for loop. If not give an error message and close the program.
    If all okay than than move forward.
    :param arguments:
    :return:
    """
    #for file_name in arguments:
        #if not os.path.exists(file_name):
            #sys.exit(f"File does not exists, {file_name}")
    #print("All files exists. Moving forward.")
