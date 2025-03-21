# 🌍 **Travel Destination Sentiment Analysis**

### 📊 **Project Description**
The **Travel Destination Sentiment Analysis** project aims to extract, process, and visualize customer reviews from multiple travel platforms. It utilizes **web scraping, sentiment analysis, and data visualization** techniques to gain insights into customer experiences, identify trends, and help travel companies make data-driven decisions.

---

### 🚀 **Tech Stack Used**
- **Python** → Data processing, cleaning, and sentiment analysis.  
- **Scrapy ** → Web scraping reviews from travel platforms.  
- **Scikit-Learn, VADER** → Sentiment classification.  
- **Power BI** → Data visualization and dashboard creation.  
- **Pandas & Seaborn** → Data wrangling and exploratory data analysis (EDA).  

---

### 🔥 **Project Workflow**

1. **Data Extraction:**
   - Used **Scrapy** and **Selenium** to scrape customer reviews, ratings, and metadata from platforms like Expedia, Booking.com, and Tours4Fun.  
   - Implemented **proxy rotation** and user-agent randomization to bypass bot detection.  

2. **Data Cleaning & Preprocessing:**
   - Removed null and duplicate values.  
   - Converted dates to the correct format.  
   - Standardized sentiment labels (`positive`, `negative`, `neutral`).  
   - Handled missing or inconsistent values.  

3. **Sentiment Analysis:**
   - **VADER & TextBlob** → Assigned sentiment scores to each review.  
   - Categorized reviews into `positive`, `negative`, or `neutral`.  
   - Calculated overall platform sentiment scores.  

4. **Visualization & Dashboard (Power BI):**
   - Created an **interactive Power BI dashboard** displaying:  
     - **Site-specific metrics**: Total reviews, average rating, and sentiment distribution.  
     - **Trends over time**: Review volume across different platforms.  
     - **Sentiment breakdown**: Pie and bar charts showing sentiment proportions.  
     - **Helpfulness score**: Average helpfulness by platform.  
     - **Dynamic filters and slicers** for single-site analysis.  

---

### 📊 **Power BI Dashboard Features**
- **Platform Selector:** Dropdown slicer to view details of one platform at a time.  
- **KPIs:**  
   - Total Reviews  
   - Average Rating  
   - Positive Review Percentage  
   - Average Helpfulness  
- **Visuals:**  
   - Line chart → Reviews over time.  
   - Pie chart → Sentiment distribution.  
   - Bar chart → Helpfulness by rating.  
   - Word cloud → Frequently mentioned review aspects.  
- **Dynamic Titles:** Graph titles change based on the selected platform.  

---

### 🔥 **Folder Structure**
``` plain text
📁 Travel_Sentiment_Analysis
├── 📂 data # Raw and cleaned datasets
│ ├── consumer_review.csv # Raw scraped review data
│ ├── sentiment_analysis_result.csv# Sentiment classification results
│
├── 📂 scripts # Python scripts
│ ├── scraper.py # Web scraping script
│ ├── sentiment_analysis.py# Sentiment analysis script
│ ├── data_cleaning.py # Data preprocessing and cleaning
│
├── 📂 dashboards # Power BI files
│ ├── Travel_Dashboard.pbix# Power BI dashboard file
│
├── README.md # Project documentation
└── requirements.txt # Python dependencies
```


---

### ⚙️ **Installation **

1. **Clone the Repository:**
```bash
git clone <repository_url>
cd Travel_Sentiment_Analysis
```
2. **Create and Activate a Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate the environment  
# Windows:
venv\Scripts\activate  
```
3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the Scraper**
```bash
   scrapy crawl consumeraffairs_spider -o consumer_reviews.csv
```
5. **Perform Sentiment Analysis**
```bash
python scripts/sentiment_analysis.py
```

### 📊 **Power BI Dashboard Execution**
1. **Open Power BI Desktop.**  
2. Click on **Open File** → Select the `Travel_Dashboard.pbix` file.  
3. Interact with the slicers to view **site-specific metrics**.  

---

### 📈 **Key Metrics & Insights**
- **Highest Reviewed Platforms:** Platforms with the largest number of reviews.  
- **Sentiment Distribution:** Breakdown of positive, negative, and neutral reviews by platform.  
- **Review Trends:** Volume of reviews over time.  
- **Top Aspects Mentioned:** Frequently praised or criticized services.  
- **Helpfulness Analysis:** Most helpful platforms based on review helpfulness scores.  


---

### 🛠️ **Dependencies**
- Python 3.9+  
- Scrapy  
- Selenium  
- Scikit-Learn  
- Pandas, NumPy  
- Power BI  



---


---

### 📧 **Contact Information**
- **Author:** Richa Kumari  
- **Email:** richasingh91725@gmail.com  
- **LinkedIn:** https://www.linkedin.com/in/richa-kumari-213891215
