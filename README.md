# Mars Rock Classification using SVM
This project is a Mars Rock Image Classification tool built with Streamlit. It allows users to upload images of Mars rocks and predicts the rock type using a pre-trained Support Vector Machine (SVM) model.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Project-Altair-IUT/Mars-Rock-Classification-using-SVM.git
cd Mars-Rock-Classification-using-SVM
```
Install the required packages. Make sure you have Python 3.6 or later installed:

```bashpip install gdown
pip install scikit-learn==1.0.2 streamlit==1.26.0 pillow==7.1.0 numpy==1.24.3 opencv-python==4.7.0.72 pandas==2.0.2 matplotlib==3.1.2 gdown
```
## Additional Files
Download the pre-trained model file "img_model.pkl" from this [link](https://drive.google.com/drive/folders/1UISX9LN31V_-EP5-vEWz48oMj631595J?usp=sharing) . Save the downloaded file in the project's root directory.
alternate shell command to download the img_model.pkl file directly:
```
gdown 1s8MvLxAgUlOyIwryHdRq2AuBO4rgS9ce
```
## Usage
After installing the required packages and downloading the model file, run the Streamlit app with the following command:
```bash
streamlit run app.py
```
This will start a local server and launch the Mars Rock Image Classification web app in your default web browser.

## How to Use
1. Access the web app using the provided URL.
2. Click on the "Upload the Rock Image (Keep this in Rocks)" button.
3. Select an image of a Mars rock from your local machine.
4. The app will display the uploaded image.
5. Click on the "Predict Rock Type" button to classify the rock type.
6. The app will display the probabilities of the image belonging to different rock types in both tabular and chart form.

## Contributing
We welcome contributions to improve this project. If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.
