import pandas as pd


input_file = 'rcsb_pdb_custom_report_20260421134636.csv'
output_file = 'chainlist.txt'


targets = [
    "1AAP_A",
    "1D0D_A",
    "1F5R_I",
    "1KNT_A",
    "1TFX_C",
    "1ZR0_B",
    "4ISN_B",
    "4U30_X",
    "4U32_X"
]


df = pd.read_csv(input_file)


df.iloc[:, 0] = df.iloc[:, 0].ffill()


with open(output_file, 'w') as f:
    
    for indice, riga in df.iterrows():
        
        
        pdb_id   = str(riga.iloc[0]).strip().replace('"', '')
        sequenza = str(riga.iloc[1]).strip().replace('"', '')
        catena   = str(riga.iloc[2]).strip().replace('"', '')
        
        
        if sequenza == "nan" or len(sequenza) < 5:
            continue

        
        match_id = f"{pdb_id}_{catena}"
        
        
        if match_id in targets:
            f.write(f"{pdb_id}:{catena}\n")
            print(f"Successfully extracted: {pdb_id}:{catena}")

