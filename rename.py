import os

dirr = "/hhome/ps2g07/document_analysis/github/Project_Synthesis2-/Code/Denoise/MIRNetv2/visualization_comparison"

"""
change from 

Folder1
    - 0.png
    - 1.png
Folder2
    - 0.png
    - 1.png
    
To 
Folder1_0.png
Folder1_1.png
Folder2_0.png
Folder2_1.png
"""

for root, dir, files in os.walk(dirr):
    for file in files:
        # new_name = root.split("/")[-1] + "_" + file
        print(os.path.join(root, file), os.path.join(dirr, root.split("/")[-1] + "_" + file))
        # print(root)
        os.rename(os.path.join(root, file), os.path.join(dirr, root.split("/")[-1] + "_" + file))
        
        # os.rename(os.path.join(dirr, file), os.path.join(dirr, "_".join(file.split("_")[1:])))