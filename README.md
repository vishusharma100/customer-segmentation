# Customer Segmentation using K-Means Clustering

## Project Overview
A machine learning project that segments customers according to income and purchasing behavior. The project uses K-Means clustering after feature scaling and evaluates candidate cluster counts with the Elbow Method and Silhouette Score.

## Objectives
- Clean and explore customer data
- Identify meaningful customer groups
- Select an appropriate number of clusters
- Build K-Means clustering model
- Visualize customer segments
- Prepare a Power BI-ready dataset
- Translate clusters into business-oriented customer segments

## Tech Stack
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Jupyter Notebook, Power BI

## Dataset
The project includes a synthetic dataset of 500 customers with:
- CustomerID
- Age
- Gender
- AnnualIncome_k
- PurchaseFrequency
- AvgOrderValue
- SpendingScore
- TotalSpend

The dataset is synthetic and created specifically for portfolio/learning purposes.

## Machine Learning Workflow
1. Load data
2. Check missing values and duplicates
3. Explore numerical features
4. Standardize clustering features
5. Test K values from 2 to 8
6. Compare inertia and silhouette score
7. Train K-Means
8. Profile each cluster
9. Export segmented customer data
10. Build Power BI dashboard

## Model
K-Means Clustering

Selected K from the highest silhouette score among K=2..8: **3**

## Graphs
- `graphs/elbow_method.png`
- `graphs/silhouette_score.png`
- `graphs/customer_clusters.png`
- `graphs/segment_distribution.png`
- `graphs/frequency_vs_aov.png`

## Power BI Dashboard
Import `powerbi/customer_segments_powerbi.csv`.

Recommended dashboard layout:
- KPI cards: Total Customers, Avg Income, Avg Spending Score, Total Spend
- Donut chart: Customers by Segment
- Scatter chart: Annual Income vs Spending Score
- Column chart: Avg Total Spend by Segment
- Bar chart: Avg Purchase Frequency by Segment
- Slicers: Gender, Age, Segment

## Business Interpretation
- Premium: relatively strong income and spending behavior; suitable for loyalty and retention programs.
- Potential High Value: good opportunity for upselling/cross-selling.
- Developing: customers who may respond to personalized promotions.
- Low Value: use cost-efficient engagement and retention campaigns.

## Run Locally
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Customer_Segmentation.ipynb
```

Or:
```bash
python customer_segmentation.py
```

## Repository Structure
```text
customer-segmentation/
├── dataset/
│   ├── customer_data.csv
│   └── customer_segments.csv
├── notebooks/
│   └── Customer_Segmentation.ipynb
├── graphs/
│   ├── elbow_method.png
│   ├── silhouette_score.png
│   ├── customer_clusters.png
│   ├── segment_distribution.png
│   └── frequency_vs_aov.png
├── powerbi/
│   ├── customer_segmentation_powerbi.csv
│   └── customer_segments_powerbi.csv
├── customer_segmentation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Resume Project Description
**Customer Segmentation using K-Means Clustering** — Built a machine learning solution using Python and Scikit-learn to segment 500 customers based on income and purchasing behavior. Applied data preprocessing, feature scaling, Elbow Method and Silhouette Score analysis, K-Means clustering, visualization, and Power BI-ready reporting to derive actionable customer insights.

## Disclaimer
This portfolio project uses synthetic data. Cluster labels are analytical groupings and should be validated against real customer behavior before business deployment.
