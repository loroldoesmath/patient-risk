# Sample Final Project: Python

## Project Overview
This is a sample final project created for TEDA 1031 - Data Science with Python. Recall that the guiding question for this project is: *"How can I use Python to gain insight into a dataset?"* Feel free to use this README as a template for your own project. 

## Table of Contents
- [Dataset](#dataset)
- [Data Cleaning](#data-cleaning)
- [Data Manipulation](#data-manipulation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Statistical Analysis](#statistical-analysis)
- [Conclusions](#conclusions)
- [How to Run the Code](#how-to-run-the-code)

## Dataset
**Source**: [Brain Stroke Dataset on Kaggle](https://www.kaggle.com/datasets/jillanisofttech/brain-stroke-dataset)

**Dataset Description**: This dataset contains demographic data on 4982 patients, in addition to uninvasive medical statistics, and whether or not they've had a stroke.

**Motivating Questions**: 
Is there a correlation between stroke risk and: 
- Gender?
- Age?
- Hypertension?
- Marriage?
- Residence Type?
- Average Glucose Level?
- BMI?
- Whether or not a patient smokes or used to smoke?

## Data Cleaning
- Missing or duplicate values: I wrote a function called check_data_clean to check for missing values, check for duplicates, and print the data types.
- Outlier detection: Z-Score?
- Data consistency: Since there are multiple columns containing values such as 'Yes/No', 'Rural/Urban', 'Govt_job/children/Private/Self-employed', etc., we need to encode the data in a manner that makes it more suitable for correlation analysis. I used the .get_dummies() function to create True/False columns for each of the categorical variables. 

*Note: Refer to code comments for specific loading & cleaning operations, such as data consistency checks and data type conversions.*

## Data Manipulation
- **Sorting**: 
- **Filtering**: 
- **Grouping**: I created stroke_counts to count strokes by gender. 
- **Merging**: 
- **Reshaping**:

## Exploratory Data Analysis (EDA)
Descriptive Statistics by Potential Indicator: 

**Gender:** <br>
Percent of women: 58.36% <br>
Percent of men: 41.64% 
![Strokes by Gender](gender-stroke-stacked.png)
**Age:**  
- mean = 43.42
- std = 22.66
- range = 81.92

**Glucose Level:**
- mean = 105.94
- std = 45.08
- range = 216.62

Percent of respondents with **hypertension**:  9.62% <br>
Percent of respondents with **heart disease**:  5.52% <br>
Percent of respondents that have been **married**:  65.85% <br>
Percent of respondents that **have never smoked**:  36.90% <br>
Percent of respondents that **formerly smoked**:  17.41% <br>
Percent of respondents that **currently smoke**:  15.58% <br>
Percent of respondents that have had a **stroke**:  4.98% <br>

Within this dataset, we can see that women constitute a slight majority (58.36%) of the respondents. The average age is 43.42 years, with a wide age range (0 to about 82 years) and a high standard deviation, indicating a diverse age distribution. Glucose levels also show significant variability, with an average of 105.94 and a large standard deviation (45.08). While the percentages of respondents with hypertension (9.62%), heart disease (5.52%), and a history of strokes (4.98%) are relatively low, these conditions might correlate with certain demographics like age or smoking habits. Most respondents have been married (65.85%). Smoking habits reveal that a majority either have never smoked (36.90%) or formerly smoked (17.41%), while only 15.58% are current smokers. 

## Statistical Analysis

**Correlation analysis:**

The following figure shows the Pearson correlation coefficients between each of the variables. 

![Correlation Heatmap](correlation_heatmap.png)

## Conclusions

We can see from our statistical analysis that the patient's age has the greatest positive correlation with stroke out of all of the variables, with a Pearson correlation coefficient of 0.25. Age also seems to be positively correlated to heart disease and BMI. 

I was particularly curious about the effect smoking has on hypertension, heart disease, BMI, and stoke. Interestingly, current and former smokers don't seem to be at significant increased risk of any of the health conditions studied in this dataset. It is worth noting that respondents who had never smoked had a (near negligible) negative correlation with heart_disease while current and former smokers had a mild positive correlation with heart disease. 

Something else we can see is that marriage is positively correlated with increased BMI (though both marriage and BMI are positively correlated with age, so this apparent relationship could likely be due solely to the fact that people are more likely to have been married if they're older, and they're also more likely to have an increased BMI as they get older).

## How to Run the Code
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/loroldoesmath/patient-risk.git
   cd final-project
   ```

2. **Install Required Libraries**:  
   Make sure to install all necessary packages. Run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis Script**:  
   Execute the main Python script to reproduce the analysis:
   ```bash
   python analysis.py
   ```
