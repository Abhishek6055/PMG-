import pandas as pd
# Defining a fucntion called run_tests which is called by the combine_csv.py 
def run_tests(file_names, output_file_name ):
 

    total_number_of_rows = 0
    # Unit tests to check consistency
    # Counting the total number of rows in the input files. 
    for filename in file_names:
        df = pd.read_csv(filename)
        total_number_of_rows += len(df)

    # # Reading the output file to compare its size with that expected from inputs.
    try: 
        df_combined = pd.read_csv(output_file_name)
        assert total_number_of_rows == df_combined.shape[0], 'sum of the number of rows in each input file should equal the number of rows in the output file'
        assert df_combined.shape[1] == 3, 'output file should contain 3 columns'
        assert len(df_combined.drop_duplicates()) == len(df_combined), 'output file should not have duplicate rows'

    except:
        print("Combined file is empty...")


