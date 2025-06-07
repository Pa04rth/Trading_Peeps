from flask import Flask,jsonify, render_template_string , request
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import csv
import os
from nsepython import nse_largedeals_historical

import traceback


app = Flask(__name__)
#Returns as a string 
def clean_symbols_for_nse(symbols):
    """Remove .NS suffix from symbols for NSE API calls"""
    return [symbol.replace('.NS', '') if isinstance(symbol, str) else symbol for symbol in symbols]

def getSymbolsFromCSV():
    symbols = []
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'stock_names_nse.csv')
    if not os.path.isfile(file_path):
        return "Error: CSV file not found.", 404
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader, None)
            if header is None:
                return "Error: CSV file is empty.", 400
            try:
                symbol_column_index = header.index('Symbol')
                company_column_index = header.index('Company Name')
            except ValueError:
                return "Error: Required columns not found in the CSV header.", 400
            for i, row in enumerate(reader):
                if len(row) > max(symbol_column_index, company_column_index):
                    symbol = row[symbol_column_index].strip()
                    company_name = row[company_column_index].strip()
                    if symbol:
                        symbols.append({'symbol': symbol, 'company_name': company_name})
                else:
                    print(f"Warning: Row {i+2} is malformed and skipped (fewer columns than expected).")
        if not symbols:
            return "No symbols found or extracted from the CSV file.", 200
        return symbols
    except Exception as e:
        return f"Error reading CSV file: {str(e)}", 500
    
def tradedVolumeExceedingCertainPercentage(symbols_data, percentage=0.01, from_date_str=None, to_date_str=None):
    analysis = []
    # end_date = datetime.datetime.now()
    # start_date = end_date - timedelta(days=days)
    # from_date_str = start_date.strftime('%Y-%m-%d')
    # to_date_str = end_date.strftime('%Y-%m-%d')
    print(f"Fetching historical data from {from_date_str} to {to_date_str}...")
    try:
        for entry in symbols_data:
            symbol = entry['symbol']
            company_name = entry['company_name']
            ticker = yf.Ticker(symbol)  # Append ".NS" for NSE stocks
            print(f"Fetching data for {symbol}...")
            data = ticker.history( start=from_date_str, end=to_date_str)
            if data.empty:
                print(f"No historical data found for {symbol}. Skipping this symbol...")
                continue
            volume = data['Volume'].sum()
            if volume == 0 or pd.isna(volume):
                print(f"No volume data found for {symbol}. Skipping this symbol...")
                continue
            outstanding_shares = ticker.info.get('sharesOutstanding')
            if outstanding_shares is None:
                print(f"Outstanding shares data not available for {symbol}. Skipping this symbol...")
                continue
            trading_volume_percentage = (volume / outstanding_shares) * 100
            qualified = trading_volume_percentage >= percentage
            analysis.append({
                'symbol': symbol,
                'company_name': company_name,
                'total_volume': volume,
                'outstanding_shares': outstanding_shares,
                'volume_percentage': trading_volume_percentage,
                'qualified': qualified
            })
            print(f"  {symbol}: Total Volume={volume:,.0f}, Outstanding Shares={outstanding_shares:,.0f}, Volume as % of Outstanding={trading_volume_percentage:.4f} ({trading_volume_percentage:.2%})")
            if qualified:
                print(f"{symbol} qualifies with {trading_volume_percentage:.2f}% trading volume.")
            else:
                print(f"  {symbol} does NOT meet the criteria.")
    except Exception as e:
        print(f"Error fetching historical data: {e}")
    return analysis   

# def tradedVolumePerDayBatch(symbols_data, percentage=0.01, from_date_str=None, to_date_str=None):

#     # Prepare symbol list
#     symbols = [entry['symbol'] for entry in symbols_data]
#     # Download all data at once
#     data = yf.download(
#         tickers=symbols,
#         start=from_date_str,
#         end=(datetime.strptime(to_date_str, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d"),  # yfinance end is exclusive
#         group_by='ticker',
#         auto_adjust=True,
#         threads=True
#     )

#     # Prepare a lookup for company names
#     symbol_to_company = {entry['symbol']: entry['company_name'] for entry in symbols_data}
#     results = []

#     # If only one symbol, yfinance returns a single-level DataFrame
#     if isinstance(data.columns, pd.MultiIndex):
#         for symbol in symbols:
#             if symbol not in data.columns.get_level_values(0):
#                 continue
#             symbol_df = data[symbol].copy()
#             symbol_df = symbol_df.reset_index()
#             for _, row in symbol_df.iterrows():
#                 date_str = row['Date'].strftime('%Y-%m-%d')
#                 volume = row['Volume']
#                 if pd.isna(volume) or volume == 0:
#                     continue
#                 ticker = yf.Ticker(symbol)
#                 outstanding_shares = ticker.fast_info.get('sharesOutstanding')
#                 if not outstanding_shares:
#                     continue
#                 trading_volume_percentage = (volume / outstanding_shares) * 100
#                 a = volume - int(outstanding_shares * percentage)
#                 qualified = volume >= (outstanding_shares * percentage)
#                 results.append({
#                     'date': date_str,
#                     'symbol': symbol,
#                     'company_name': symbol_to_company.get(symbol, ''),
#                     'total_volume': volume,
#                     'outstanding_shares': outstanding_shares,
#                     'qualified_percentage_criteria': a,
#                     'qualified': qualified
#                 })
#     else:
#         # Single symbol, single-level columns
#         symbol = symbols[0]
#         symbol_df = data.reset_index()
#         for _, row in symbol_df.iterrows():
#             date_str = row['Date'].strftime('%Y-%m-%d')
#             volume = row['Volume']
#             if pd.isna(volume) or volume == 0:
#                 continue
#             ticker = yf.Ticker(symbol)
#             outstanding_shares = ticker.fast_info.get('sharesOutstanding')
#             if not outstanding_shares:
#                 continue
#             trading_volume_percentage = (volume / outstanding_shares) * 100
#             qualified = trading_volume_percentage >= percentage
#             results.append({
#                 'date': date_str,
#                 'symbol': symbol,
#                 'company_name': symbol_to_company.get(symbol, ''),
#                 'total_volume': volume,
#                 'outstanding_shares': outstanding_shares,
#                 'volume_percentage': trading_volume_percentage,
#                 'qualified': qualified
#             })
#     return results    



def tradedVolumePerDayBatch(symbols_data, percentage=0.01, from_date_str=None, to_date_str=None):
    # Prepare symbol list
    symbols = [entry['symbol'] for entry in symbols_data]

    # Download historical price & volume data once for all symbols
    data = yf.download(
        tickers=symbols,
        start=from_date_str,
        end=(datetime.strptime(to_date_str, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d"),
        group_by='ticker',
        auto_adjust=True,
        threads=True
    )

    # Prepare lookup for company names
    symbol_to_company = {entry['symbol']: entry['company_name'] for entry in symbols_data}

    # Fetch outstanding shares once per symbol (use fast_info for speed)
    outstanding_shares_map = {}
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            outstanding = ticker.fast_info.get('sharesOutstanding')
            # fallback if fast_info is empty
            if not outstanding:
                outstanding = ticker.info.get('sharesOutstanding', None)
            outstanding_shares_map[symbol] = outstanding
        except Exception as e:
            print(f"Failed to fetch sharesOutstanding for {symbol}: {e}")
            outstanding_shares_map[symbol] = None

    results = []

    # Check if multiple symbols (multi-index) or single symbol (single-index)
    if isinstance(data.columns, pd.MultiIndex):
        for symbol in symbols:
            if symbol not in data.columns.get_level_values(0):
                continue
            symbol_df = data[symbol].reset_index()
            outstanding_shares = outstanding_shares_map.get(symbol)
            if not outstanding_shares:
                continue
            for _, row in symbol_df.iterrows():
                volume = row['Volume']
                if pd.isna(volume) or volume == 0:
                    continue
                date_str = row['Date'].strftime('%Y-%m-%d')
                trading_volume_percentage = (volume / outstanding_shares) * 100
                a = volume - int(outstanding_shares * percentage)
                qualified = volume >= (outstanding_shares * percentage)
                results.append({
                    'date': date_str,
                    'symbol': symbol,
                    'company_name': symbol_to_company.get(symbol, ''),
                    'total_volume': volume,
                    'outstanding_shares': outstanding_shares,
                    'qualified_percentage_criteria': a,
                    'qualified': qualified
                })
    else:
        # Single symbol case
        symbol = symbols[0]
        symbol_df = data.reset_index()
        outstanding_shares = outstanding_shares_map.get(symbol)
        if outstanding_shares:
            for _, row in symbol_df.iterrows():
                volume = row['Volume']
                if pd.isna(volume) or volume == 0:
                    continue
                date_str = row['Date'].strftime('%Y-%m-%d')
                trading_volume_percentage = (volume / outstanding_shares) * 100
                qualified = trading_volume_percentage >= percentage
                results.append({
                    'date': date_str,
                    'symbol': symbol,
                    'company_name': symbol_to_company.get(symbol, ''),
                    'total_volume': volume,
                    'outstanding_shares': outstanding_shares,
                    'volume_percentage': trading_volume_percentage,
                    'qualified': qualified
                })

    return results
 
#Function to fetch bulk deals for a given symbol 
def bulkDealsFromSymbols(listOfSymbols, from_date_str=None, to_date_str=None):
    try:
        print(f"Fetching bulk deals for {len(listOfSymbols)} symbols from {from_date_str} to {to_date_str}")
        
        all_deals_in_period = nse_largedeals_historical(
            from_date=from_date_str,
            to_date=to_date_str,
            mode="bulk_deals"
        )
        
        if all_deals_in_period is None or all_deals_in_period.empty:
            print("No bulk deals found in the specified date range.")
            return []

        print("Columns in DataFrame:", all_deals_in_period.columns.tolist())
        
        # Use BD_SYMBOL from NSE API response
        nse_symbol_column = 'BD_SYMBOL'
        
        # Convert your CSV symbols to match NSE format
        symbols_set = set(symbol.strip().upper() for symbol in listOfSymbols)
        print("Looking for symbols:", symbols_set)
        
        # Filter deals and handle symbol format differences
        relevant_deals = all_deals_in_period[
            all_deals_in_period[nse_symbol_column].str.replace('.NS', '').str.upper().isin(symbols_set)
        ]
        
        # Convert to list of dictionaries
        bulkDeals = relevant_deals.to_dict(orient='records')
        
        print(f"Found {len(bulkDeals)} relevant bulk deals")
        if bulkDeals:
            print("Sample deal:", bulkDeals[0])
            
        return bulkDeals

    except Exception as e:
        print(f"Error fetching bulk deals: {str(e)}")
        traceback.print_exc()
        return []
    
def fetchAllBulkDeals(daysInPast=30):
    print("\n=== Starting fetchAllBulkDeals function ===")
    
    # Get dates in correct format for NSE API
    end_date = datetime.now()  # Using datetime directly
    start_date = end_date - timedelta(days=daysInPast)
    
    from_date_str = start_date.strftime('%d-%m-%Y')  # NSE format: DD-MM-YYYY
    to_date_str = end_date.strftime('%d-%m-%Y')
    
    print(f"Date Range: {from_date_str} to {to_date_str}")

    try:
        print("Calling NSE API for bulk deals...")
        # Fixed: Pass parameters by name to avoid confusion
        bulk_deals_data = nse_largedeals_historical(from_date=from_date_str, 
                                       to_date=to_date_str,
                                       mode="bulk_deals")
        
        # Rest of the function remains the same...
        print(f"Response Type: {type(bulk_deals_data)}")
        
        if isinstance(bulk_deals_data, pd.DataFrame):
            print(f"Received DataFrame with shape: {bulk_deals_data.shape}")
            
            if bulk_deals_data.empty:
                print("DataFrame is empty - no bulk deals found")
                return []
                
            print("\nFirst few rows of data:")
            print(bulk_deals_data.head())
            
            all_bulk_deals = bulk_deals_data.to_dict(orient='records')
            print(f"\nSuccessfully converted to {len(all_bulk_deals)} bulk deal records")
            
            if all_bulk_deals:
                print("\nSample bulk deal:")
                print(all_bulk_deals[0])
            
            return all_bulk_deals
        else:
            print(f"Unexpected response type: {type(bulk_deals_data)}")
            return []

    except Exception as e:
        print("\n=== Error in fetchAllBulkDeals ===")
        print(f"Error type: {type(e)}")
        print(f"Error message: {str(e)}")
        print("Stack trace:", traceback.format_exc())
        return []
    finally:
        print("\n=== Completed fetchAllBulkDeals function ===")
    

@app.route("/api/bulk-deals", methods=["GET"])
def bulkDealsReport():
    try:
        print("\n=== Starting Bulk Deals Report Generation ===")
        
        # Initialize parameters
        report_period_days = 10
        volume_percentage_threshold = request.args.get('min-volume', default=1, type=float)
        volume_percentage_threshold /= 100  # Convert to decimal
        end_date = datetime.now()
        start_date = end_date - timedelta(days=report_period_days)
        from_date_str = start_date.strftime('%Y-%m-%d')
        to_date_str = end_date.strftime('%Y-%m-%d')

        # Step 1: Get symbols from CSV
        print("\n1. Getting symbols from CSV...")
        symbols_data_from_csv_result = getSymbolsFromCSV()
        if isinstance(symbols_data_from_csv_result, tuple):
            error_message, status_code = symbols_data_from_csv_result
            return render_template_string(f"<h1>Error:</h1><p>{error_message}</p>"), status_code

        symbols_data_from_csv = symbols_data_from_csv_result
        if not symbols_data_from_csv:
            return render_template_string("<h1>No Symbols Found</h1><p>The CSV file did not provide any symbols.</p>")

        print(f"Found {len(symbols_data_from_csv)} symbols in CSV")

        # Step 2: Get qualified symbols
        print("\n2. Analyzing trading volumes to find qualified symbols...")
        per_day_analysis = tradedVolumePerDayBatch(
            symbols_data_from_csv,
            percentage=volume_percentage_threshold,
            from_date_str=from_date_str,
            to_date_str=to_date_str
        )

        qualified_per_day = [data for data in per_day_analysis if data['qualified']]
        qualified_symbols = list(set(data['symbol'] for data in qualified_per_day))
        
        print(f"Found {len(qualified_symbols)} qualified symbols")
        
        # Step 3: First fetch all bulk deals for the period
        print("\n3a. Fetching all bulk deals for the period...")
        all_bulk_deals_in_period = fetchAllBulkDeals(report_period_days)
        if not all_bulk_deals_in_period:
            print("No bulk deals found in the specified period")
            all_bulk_deals = []
        else:
            print(f"Found {len(all_bulk_deals_in_period)} total bulk deals in the period")

        # Step 3: Get bulk deals only for qualified symbols
        print("\n3. Fetching bulk deals for qualified symbols...")
        nse_date_from = start_date.strftime('%d-%m-%Y')  # NSE format
        nse_date_to = end_date.strftime('%d-%m-%Y')      # NSE format
        print(f"Using NSE date range: {nse_date_from} to {nse_date_to}")
        # Clean symbols before passing to NSE API
        clean_qualified_symbols = clean_symbols_for_nse(qualified_symbols)
        print(f"Original symbols: {qualified_symbols}")
        print(f"Cleaned symbols for NSE: {clean_qualified_symbols}")
        
        all_bulk_deals = bulkDealsFromSymbols(
            listOfSymbols=clean_qualified_symbols,  # Use cleaned symbols
            from_date_str=nse_date_from,
            to_date_str=nse_date_to
        )
        
        print(f"Found {len(all_bulk_deals)} bulk deals")

        # Step 4: Generate HTML Report
        print("\n4. Generating HTML report...")
        report_html = "<h1>Comprehensive Stock Report</h1>"
        report_html += f"<h3>Analysis Period: {from_date_str} to {to_date_str}</h3>"

        # Show Volume Analysis Table First
        report_html += "<h2>1. Daily Volume Analysis:</h2>"
        if per_day_analysis:
            report_html += "<table border='1' cellpadding='5' cellspacing='0' style='width:100%; border-collapse: collapse;'>"
            report_html += """
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Symbol</th>
                        <th>Company Name</th>
                        <th>Total Volume</th>
                        <th>Outstanding Shares</th>
                        <th>Required Volume Difference</th>
                        <th>Qualified</th>
                    </tr>
                </thead>
                <tbody>
            """
            # Sort by date and symbol
            sorted_analysis = sorted(per_day_analysis, key=lambda x: (x['date'], x['symbol']))
            
            for analysis in sorted_analysis:
                qualified_status = "✅" if analysis['qualified'] else "❌"
                report_html += f"""
                    <tr>
                        <td>{analysis['date']}</td>
                        <td>{analysis['symbol']}</td>
                        <td>{analysis['company_name']}</td>
                        <td>{analysis['total_volume']:,}</td>
                        <td>{analysis['outstanding_shares']:,}</td>
                        <td>{analysis['qualified_percentage_criteria']:,}</td>
                        <td>{qualified_status}</td>
                    </tr>
                """
            report_html += "</tbody></table>"
        else:
            report_html += "<p>No volume analysis data available.</p>"
        

        # Show Qualified Symbols with Dates
        report_html += "<h2>2. Qualified Symbols Summary:</h2>"
        if qualified_per_day:
            report_html += "<table border='1' cellpadding='5' cellspacing='0' style='width:100%; border-collapse: collapse;'>"
            report_html += """
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Symbol</th>
                        <th>Company Name</th>
                        <th>Volume</th>
                        <th>Volume Requirement</th>
                    </tr>
                </thead>
                <tbody>
            """
            
            # Sort qualified entries by date and symbol
            sorted_qualified = sorted(qualified_per_day, key=lambda x: (x['date'], x['symbol']))
            
            # Group by symbol to show latest qualification date
            symbol_data = {}
            for entry in sorted_qualified:
                symbol = entry['symbol']
                if symbol not in symbol_data:
                    symbol_data[symbol] = entry
                
                report_html += f"""
                    <tr>
                        <td>{entry['date']}</td>
                        <td>{entry['symbol']}</td>
                        <td>{entry['company_name']}</td>
                        <td>{entry['total_volume']:,}</td>
                        <td>{entry['qualified_percentage_criteria']:,}</td>
                    </tr>
                """
            report_html += "</tbody></table>"
            
            # Add a summary count
            report_html += f"<p>Total unique qualified symbols: {len(set(data['symbol'] for data in qualified_per_day))}</p>"
        else:
            report_html += "<p>No symbols qualified based on volume criteria.</p>"

        # Replace the Bulk Deals section in bulkDealsReport function with:

        # Replace the Bulk Deals section with:

        # Show All Bulk Deals first
        report_html += "<h2>3. All Bulk Deals in Period:</h2>"
        if all_bulk_deals_in_period:
            report_html += "<table border='1' cellpadding='5' cellspacing='0' style='width:100%; border-collapse: collapse;'>"
            report_html += """
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Symbol</th>
                        <th>Company Name</th>
                        <th>Client Name</th>
                        <th>Buy/Sell</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Remarks</th>
                    </tr>
                </thead>
                <tbody>
            """
            for deal in all_bulk_deals_in_period:
                report_html += f"""
                    <tr>
                        <td>{deal.get('BD_DT_DATE', 'N/A')}</td>
                        <td>{deal.get('BD_SYMBOL', 'N/A')}</td>
                        <td>{deal.get('BD_SCRIP_NAME', 'N/A')}</td>
                        <td>{deal.get('BD_CLIENT_NAME', 'N/A')}</td>
                        <td>{deal.get('BD_BUY_SELL', 'N/A')}</td>
                        <td>{deal.get('BD_QTY_TRD', 'N/A'):,}</td>
                        <td>₹{deal.get('BD_TP_WATP', 'N/A'):,.2f}</td>
                        <td>{deal.get('BD_REMARKS', 'N/A')}</td>
                    </tr>
                """
            report_html += "</tbody></table>"
            
            # Add summary for all deals
            total_all_deals = len(all_bulk_deals_in_period)
            total_all_buy_deals = sum(1 for deal in all_bulk_deals_in_period if deal.get('BD_BUY_SELL') == 'BUY')
            total_all_sell_deals = sum(1 for deal in all_bulk_deals_in_period if deal.get('BD_BUY_SELL') == 'SELL')
            
            report_html += f"""
                <div style='margin-top: 20px;'>
                    <p><strong>All Deals Summary:</strong></p>
                    <ul>
                        <li>Total Bulk Deals: {total_all_deals}</li>
                        <li>Buy Deals: {total_all_buy_deals}</li>
                        <li>Sell Deals: {total_all_sell_deals}</li>
                    </ul>
                </div>
            """
        else:
            report_html += "<p>No bulk deals found in the specified period.</p>"

        # Then show Bulk Deals for Qualified Symbols
        report_html += "<h2>4. Bulk Deals for Qualified Symbols Only:</h2>"
        if all_bulk_deals:
            report_html += "<table border='1' cellpadding='5' cellspacing='0' style='width:100%; border-collapse: collapse;'>"
            report_html += """
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Symbol</th>
                        <th>Company Name</th>
                        <th>Client Name</th>
                        <th>Buy/Sell</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Remarks</th>
                    </tr>
                </thead>
                <tbody>
            """
            for deal in all_bulk_deals:
                report_html += f"""
                    <tr>
                        <td>{deal.get('BD_DT_DATE', 'N/A')}</td>
                        <td>{deal.get('BD_SYMBOL', 'N/A')}</td>
                        <td>{deal.get('BD_SCRIP_NAME', 'N/A')}</td>
                        <td>{deal.get('BD_CLIENT_NAME', 'N/A')}</td>
                        <td>{deal.get('BD_BUY_SELL', 'N/A')}</td>
                        <td>{deal.get('BD_QTY_TRD', 'N/A'):,}</td>
                        <td>₹{deal.get('BD_TP_WATP', 'N/A'):,.2f}</td>
                        <td>{deal.get('BD_REMARKS', 'N/A')}</td>
                    </tr>
                """
            report_html += "</tbody></table>"
            
            # Add summary statistics for qualified symbols
            total_deals = len(all_bulk_deals)
            total_buy_deals = sum(1 for deal in all_bulk_deals if deal.get('BD_BUY_SELL') == 'BUY')
            total_sell_deals = sum(1 for deal in all_bulk_deals if deal.get('BD_BUY_SELL') == 'SELL')
            
            report_html += f"""
                <div style='margin-top: 20px;'>
                    <p><strong>Qualified Symbols Deals Summary:</strong></p>
                    <ul>
                        <li>Total Bulk Deals: {total_deals}</li>
                        <li>Buy Deals: {total_buy_deals}</li>
                        <li>Sell Deals: {total_sell_deals}</li>
                    </ul>
                </div>
            """
        else:
            report_html += "<p>No bulk deals found for qualified symbols.</p>"

        # Wrap in HTML template
        final_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Stock Analysis Report</title>
            <style>
                body {{ 
                    font-family: Arial; 
                    margin: 20px; 
                    line-height: 1.6;
                }}
                table {{ 
                    border-collapse: collapse; 
                    width: 100%; 
                    margin-bottom: 20px;
                }}
                th, td {{ 
                    padding: 12px 8px; 
                    text-align: left; 
                    border: 1px solid #ddd; 
                }}
                th {{ 
                    background-color: #f2f2f2; 
                    font-weight: bold;
                }}
                tr:nth-child(even) {{ 
                    background-color: #f9f9f9; 
                }}
                tr:hover {{
                    background-color: #f5f5f5;
                }}
            </style>
        </head>
        <body>
            {report_html}
        </body>
        </html>
    """

        print("\n=== Report Generation Complete ===")
        return render_template_string(final_html)

    except Exception as e:
        print(f"Error generating report: {str(e)}")
        traceback.print_exc()
        return render_template_string(f"<h1>Error</h1><p>{str(e)}</p>"), 500

if __name__ == "__main__":
    
    app.run(debug=True, threaded=True, timeout=300)
   

