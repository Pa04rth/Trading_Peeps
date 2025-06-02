import pandas as pd

def clean_nse_data():
    try:
        # Read the NSE data, skip the first row since it contains merged headers
        df = pd.read_csv('nse.csv', skiprows=1)
        
        # Create new dataframe with required columns
        cleaned_df = pd.DataFrame(columns=['Symbol', 'Company Name'])
        
        # Get the first column which contains symbols
        symbols = df.iloc[:, 0]  # First column contains symbols
        
        # Clean and add symbols
        cleaned_df['Symbol'] = symbols.str.strip('" ').apply(lambda x: f"{x}.NS" if pd.notnull(x) and x != '' else '')
        
        # Add company names (leaving blank for now as they're not in the source data)
        cleaned_df['Company Name'] = 'N/A'
        
        # Remove any empty or invalid symbols
        cleaned_df = cleaned_df[cleaned_df['Symbol'].str.len() > 3]
        
        # Remove entries with 'Symbol.NS' or other invalid entries
        cleaned_df = cleaned_df[~cleaned_df['Symbol'].str.contains('Symbol')]
        
        # Sort by Symbol
        cleaned_df = cleaned_df.sort_values('Symbol')
        
        # Save to new CSV
        cleaned_df.to_csv('stock_names_nse.csv', index=False)
        print("Successfully created cleaned NSE stock list in stock_names_nse.csv")
        print(f"Total stocks processed: {len(cleaned_df)}")
        
    except Exception as e:
        print(f"Error processing NSE data: {str(e)}")
        print("Please check if nse.csv exists and has the correct format")

if __name__ == "__main__":
    clean_nse_data()
