
import os
import matplotlib.pyplot as plt

input_dir = "/hhome/ps2g07/document_analysis/github/Project_Synthesis2-/Code/Denoise/MIRNetv2+DocTR/demo/degraded"
restored_dir = "/hhome/ps2g07/document_analysis/github/Project_Synthesis2-/Code/Denoise/MIRNetv2+DocTR/demo/restored"
gt_dir = "/hhome/ps2g07/document_analysis/github/Project_Synthesis2-/Sample documents - PNG"

out_dir = "/hhome/ps2g07/document_analysis/github/Project_Synthesis2-/Code/Denoise/MIRNetv2+DocTR/visualization/"

gt = False
for root, dir, files in os.walk(input_dir):
    for file in files:
        # try: 
        degraded_path = os.path.join(root, file)
        gt_path = os.path.join(root.replace(input_dir, gt_dir), file)
        restored_path = os.path.join(root.replace(input_dir, restored_dir), file)

        print(degraded_path)
        print(gt_path)
        print(restored_path)

        degraded = plt.imread(degraded_path)
        restored = plt.imread(restored_path)
        
        if gt:
            gt_img = plt.imread(gt_path)
            
            fig, ax = plt.subplots(1, 3, figsize=(40, 20))
            plt.subplots_adjust(wspace=0.1)
            plt.tight_layout()

            ax[2].imshow(gt_img)
            ax[2].set_title('Ground Truth', fontsize=30)
            ax[2].axis('off')
            
        else: 
            fig, ax = plt.subplots(1, 2, figsize=(27, 20))
            plt.subplots_adjust(wspace=0.1)
            plt.tight_layout()
        
        ax[0].imshow(degraded)
        ax[0].set_title('Degraded', fontsize=30)
        ax[0].axis('off')
            
        ax[1].imshow(restored)
        ax[1].set_title('Restored', fontsize=30)
        ax[1].axis('off')
        
        os.makedirs(os.path.join(root.replace(input_dir, out_dir)), exist_ok=True)
        plt.savefig(os.path.join(root.replace(input_dir, out_dir), file))
        plt.close()
        # break
        # except: 
        #     # print(f"Error processing {file}")
        #     continue