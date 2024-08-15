import pandas as pd


def excel_column_to_txt(excel_file, output_file, column_identifier):
    # Load the Excel file
    df = pd.read_excel(excel_file)
    
    # Determine if the column identifier is an index or a name
    if isinstance(column_identifier, int):
        column_data = df.iloc[:, column_identifier]
    else:
        column_data = df[column_identifier]
    
    # Open the output text file for writing
    formatted_items = [f'"{item}"' for item in column_data]

    # Join the list into a single string separated by commas
    output_string = ','.join(formatted_items)
    
    
    
    with open(output_file, 'w') as f:
            f.write(output_string)  # Add a newline at the end if needed

    print(f"Data from column '{column_identifier}' has been written to '{output_file}'.")

# Example usage
if __name__ == "__main__":
    ######################################################################################
    # Specify the Excel input file
    excel_file = 'C:/Users/User/Downloads/TFLink_targets_of_Q00613.xlsx'
    # SPecify the name/location of the output file
    output_file = 'HSF1_TFLink.txt'
    # Specify which column should be converted. Can either put either the name of the column or the index of the column
    column_identifier = 'Name.Target'  # Or use an index, e.g., 0 for the first column
    ######################################################################################
    excel_column_to_txt(excel_file, output_file, column_identifier)