# Milk Quality Classifier

This code predicts the quality of milk based on the fat and SNF percentages. The code first reads the data from an Excel file and then creates two separate dataframes for the good and bad milk samples. The code then calculates the distance between each sample and the input parameters (ip1 and ip2). The samples with the shortest distances are considered to be the best matches. The code then prints the results of the prediction.

How to use the code
Download the code and save it to your computer.
Open a command prompt and navigate to the directory where you saved the code.
Run the code by typing the following command:
python milk_quality_prediction.py


4. The code will prompt you to enter the fat and SNF percentages of the new data.
5. The code will then print the results of the prediction.

## Requirements

The code requires the following Python libraries:

* pandas
* matplotlib.pyplot
* math
