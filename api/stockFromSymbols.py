import yfinance as yf
import pandas as pd

import os

file_contents = [
    # Previous file contents (from your first question)...
    # New file contents below:
    """
    ESS.csv  
    ETN.csv  
    ETR.csv  
    ETSY.csv  
    EVRG.csv  
    EW.csv  
    EXC.csv  
    EXPD.csv  
    EXPE.csv  
    EXR.csv  
    F.csv  
    FANG.csv  
    FAST.csv  
    FCX.csv  
    FDS.csv  
    FDX.csv  
    FE.csv  
    FFIV.csv  
    FL.csv  
    FICO.csv  
    FIS.csv  
    FTTB.csv  
    FLT.csv  
    FMC.csv  
    FOX.csv  
    FOXA.csv  
    FRT.csv  
    FSLR.csv  
    """,
    """
    FINI.csv  
    FTV.csv  
    GD.csv  
    GE.csv  
    GEHC.csv  
    GEN.csv  
    GILD.csv  
    GIS.csv  
    GL.csv  
    GLW.csv  
    GM.csv  
    GNRC.csv  
    GOOG.csv  
    GOOGL.csv  
    GPC.csv  
    GPN.csv  
    GRMN.csv  
    GS.csv  
    GWW.csv  
    HAL.csv  
    HAS.csv  
    HBAN.csv  
    HCACsv  
    HD.csv  
    HES.csv  
    HIG.csv  
    HIL.csv  
    HLT.csv  
    """,
    """
    ITW.csv
    IVZ.csv
    J.csv
    JBHT.csv
    JCL.csv
    JKHY.csv
    JNJ.csv
    JNPR.csv
    JPM.csv
    K.csv
    KDP.csv
    KEY.csv
    KEYS.csv
    KHC.csv
    KIM.csv
    KLAC.csv
    KMB.csv
    KML.csv
    KMX.csv
    KO.csv
    KR.csv
    KVUE.csv
    L.csv
    LDOS.csv
    LEN.csv
    LH.csv
    LHX.csv
    LIN.csv
    LKO.csv
    """,
    """
    LIV.csv
    LMT.csv
    LNT.csv
    LOW.csv
    LRCX.csv
    LUV.csv
    LVS.csv
    LW.csv
    LYB.csv
    LYV.csv
    MA.csv
    MAASV
    MAR.csv
    MAS.csv
    MCD.csv
    MCHP.csv
    MCK.csv
    MCO.csv
    MDLZ.csv
    MDT.csv
    MET.csv
    META.csv
    MGML.csv
    MHK.csv
    MKC.csv
    MKTX.csv
    MLM.csv
    """,
    """
    MMC.csv
    MMM.csv
    MNST.csv
    MO.csv
    MOH.csv
    MOS.csv
    MPC.csv
    MPWR.csv
    MRK.csv
    MRNA.csv
    MRO.csv
    MS.csv
    MSCL.csv
    MSFT.csv
    MSI.csv
    MTB.csv
    MTCH.csv
    MTD.csv
    MU.csv
    NCLH.csv
    NDAQ.csv
    NDSN.csv
    NEE.csv
    NEM.csv
    NFIX.csv
    NL.csv
    NKE.csv
    NOC.csv
    NOW.csv
    """,
    """
    NIRG.csv  
    NSC.csv  
    NTAP.csv  
    NTRS.csv  
    NUE.csv  
    NVDA.csv  
    NVR.csv  
    NWS.csv  
    NWSA.csv  
    NXP1.csv  
    O.csv  
    ODFL.csv  
    OGN.csv  
    OKL.csv  
    OMC.csv  
    ON.csv  
    ORCL.csv  
    ORLY.csv  
    OTIS.csv  
    OXY.csv  
    PANW.csv  
    PARA.csv  
    PAYC.csv  
    PAYX.csv  
    PCAR.csv  
    PCG.csv  
    PEAK.csv  
    PEG.csv  
    """,
    """
    PEP.csv
    PFECsv
    PFG.csv
    PG.csv
    PGR.csv
    PH.csv
    PHM.csv
    PKG.csv
    PLD.csv
    PM.csv
    PNC.csv
    PNR.csv
    PNW.csv
    PODD.csv
    POOL.csv
    PPG.csv
    PPL.csv
    PRU.csv
    PSA.csv
    PSX.csv
    PTC.csv
    PWR.csv
    PXD.csv
    PVPL.csv
    OCOM.csv
    QRVO.csv
    RCL.csv
    REG.csv
    """,
    """
    STLCsv
    STLD.csv
    STT.csv
    STX.csv
    STZ.csv
    SWK.csv
    SWKS.csv
    SVF.csv
    SVK.csv
    SYY.csv
    T.csv
    TAP.csv
    TDG.csv
    TDY.csv
    TECH.csv
    TELL.csv
    TER.csv
    TFC.csv
    TFX.csv
    TGT.csv
    TJX.csv
    TMOCsv
    TMUS.csv
    TPR.csv
    TRGP.csv
    TRMB.csv
    TROW.csv
    TRV.csv
    TSCO.csv
    """,
    """
    TSLA.csv  
    TSN.csv  
    TT.csv  
    TTWO.csv  
    TXN.csv  
    TXT.csv  
    TYL.csv  
    UAL.csv  
    UDR.csv  
    UHS.csv  
    ULTA.csv  
    UNH.csv  
    UNP.csv  
    UPS.csv  
    URI.csv  
    USB.csv  
    V.csv  
    VFC.csv  
    VICI.csv  
    VLO.csv  
    VMC.csv  
    VRSK.csv  
    VRSN.csv  
    VRTX.csv  
    VTR.csv  
    VTRS.csv  
    VZ.csv  
    WAB.csv  
    """
]


def extract_symbols(content):
    symbols = []
    for line in content.strip().split('\n'):
        symbol = line.strip().split('.')[0].upper()  # Handle .csv, .CSV, typos
        if symbol:
            symbols.append(symbol)
    return symbols

# Collect all symbols from new file contents
all_symbols = []
for content in file_contents:
    symbols = extract_symbols(content)
    all_symbols.extend(symbols)
unique_new_symbols = list(set(all_symbols))
unique_new_symbols.sort()

# Load existing data (if any)
existing_df = pd.DataFrame()
if os.path.exists('stock_names.csv'):
    existing_df = pd.read_csv('stock_names.csv')
    existing_symbols = existing_df['Symbol'].tolist()
else:
    existing_symbols = []

# Filter out symbols already in the existing CSV
new_symbols = [sym for sym in unique_new_symbols if sym not in existing_symbols]

# Fetch company names for new symbols
data = []
for symbol in new_symbols:
    try:
        ticker = yf.Ticker(symbol)
        name = ticker.info.get('longName', 'Not Found')
    except:
        name = 'Not Found'
    data.append({'Symbol': symbol, 'Company Name': name})

# Append new data to existing CSV
if data:
    new_df = pd.DataFrame(data)
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    updated_df.to_csv('stock_names.csv', index=False)
    print(f"Added {len(new_df)} new entries to stock_names.csv")
else:
    print("No new symbols to add.")
