# WIND Toolkit Data Exploration - Wind Speed Visualizations

This project performs exploratory data analysis and visualization of the **WIND Toolkit Site Metadata** dataset from NREL, focusing on wind speed distribution and geographic patterns.

---

## 📁 Project Structure


---

## 📊 Visualizations Generated

1. **Wind Speed Histogram**  
   Displays the distribution of wind speeds (in m/s) across different sites.

2. **Scatter Plot: Latitude vs Wind Speed**  
   Shows how wind speed varies with geographic latitude.

3. **Boxplot: Wind Speed by State**  
   Compares wind speed distributions across different states.

4. **Geospatial Map of Wind Speed**  
   Geographic locations of sites colored by wind speed, providing spatial insight.

---

## 📦 Requirements

Make sure to install the following Python libraries before running the script:

```bash
pip install pandas matplotlib geopandas
▶️ How to Run
Place the wtk_site_metadata.csv file in the project root directory.

Run the script main.py in your Python environment:

bash
Copy
Edit
python main.py
The script will automatically create a folder called winddata_visualizations_NREL containing the generated image files.
📌 Data Source
The data comes from the WIND Toolkit Site Metadata by NREL, containing geospatial and wind speed information for multiple sites across the U.S.

👩‍💻 About the Author
Catalina Cifuentes — Data Analyst and Master’s student in Data Science, focused on AI projects applied to renewable energy and energy justice in San Diego, California.pandas
matplotlib
geopandas
