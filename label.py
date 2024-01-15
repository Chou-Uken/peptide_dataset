from biofkit.proteinKit import pdbKit
import os
from tqdm import tqdm


pdbFileList = os.listdir('./pdbFile/')

with tqdm(total=10259) as pbar:
    with open('label.csv', mode='w') as label:  
        for pdbFileName in pdbFileList:
            pdbFilePath = os.path.join('./pdbFile/', pdbFileName)
            chainId = pdbFileName.split('.')[0].split('_')[-1]        
            seq = pdbKit.pdb2Seq(pdbFilePath=pdbFilePath)[chainId]
            label.write(pdbFileName + ', ' + seq + '\n')
            pbar.update()    
