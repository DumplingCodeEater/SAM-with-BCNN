

## Setup Instructions
### 1. **Install Dependencies**
   - Install all required packages listed in `requirements.txt`:

### 2. **Running the Notebooks**

- **Google Colab Version:**  
Run the cells in the `SAM2_with_BCNN.ipynb` notebook in order on Google Colab.

- **Local Version:**  
Run the cells in the `SAM2_with_BCNN_Local.ipynb` notebook in order on your local machine.

**Note:** Ensure CUDA is installed and set up correctly on your local machine to run the code on GPU. If CUDA is not set up, the code will run on CPU, but may be slower.

---

## Notes

- Due to the large size of the medical dataset, a few were picked to be used in the notebook for a rough draft of how the code works.
- Removed the data .gz file from this folder since it might be too large to upload (was ~3GB for a single one).
- `create_subdatasets.py` was used to create a smaller dataset for testing purposes

---

## Presentation and Paper
 - [Presentation of this code's purpose and potential implementations](https://youtu.be/DYssfQb-crA)
 - Paper can be found in the `Integrating_SAM2_with_Bayesian_Convolutional_Neural_Networks.pdf`
