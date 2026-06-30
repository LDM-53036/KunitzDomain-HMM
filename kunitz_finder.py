import pandas as pd
import sys

pdb = sys.argv[1]

df = pd.read_csv(pdb) 


df.iloc[:, 0] = df.iloc[:, 0].ffill()

def e_un_kunitz(sequenza):
    
    s = str(sequenza).upper().strip()
    lunghezza = len(s)
    n_cisteine = s.count('C')
    
    if 45 <= lunghezza <= 75 and n_cisteine == 6:
        return True
    return False


with open('mmseq2_kunitzfasta', 'w') as fasta_file:
    

    for indice, dati_riga in df.iterrows():
        
        
        pdb_id   = str(dati_riga.iloc[0]).strip() 
        sequenza = str(dati_riga.iloc[1]).strip() 
        catena   = str(dati_riga.iloc[2]).strip() 

        
        if e_un_kunitz(sequenza):
            
            header = f">{pdb_id}_{catena}"
            
            
            fasta_file.write(f"{header}\n{sequenza}\n")

print(f"Processo completato!")
print(df)