import pandas as pd

def map_skus(filepath):
    xls = pd.ExcelFile(filepath)
    sheet_names = xls.sheet_names

    inv_sheet = next((s for s in sheet_names if "current" in s.lower()), None)
    map_sheet = next((s for s in sheet_names if "msku" in s.lower() and "with" in s.lower()), None)

    if not inv_sheet or not map_sheet:
        raise Exception(f"Required sheets not found. Found: {sheet_names}")

    inv = pd.read_excel(xls, sheet_name=inv_sheet, header=1)
    mapping = pd.read_excel(xls, sheet_name=map_sheet)

    inv.columns = [str(c).strip().lower() for c in inv.columns]
    mapping.columns = [str(c).strip().lower() for c in mapping.columns]

    if 'msku' not in inv.columns or 'sku' not in mapping.columns or 'msku' not in mapping.columns:
        raise Exception("Missing 'msku' or 'sku' columns.")

    merged = pd.merge(inv, mapping[['msku', 'sku']], on='msku', how='left')
    merged['Mapped SKU'] = merged['sku'].fillna("Not Mapped")

    return merged
