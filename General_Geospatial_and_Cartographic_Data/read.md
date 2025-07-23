# School Accessibility & Wind Turbine Proximity Analysis

## Project Overview

This project analyzes the accessibility of public schools in California relative to existing wind turbines. The goal is to:

- Calculate the distance from each school to the nearest wind turbine.
- Categorize schools based on proximity into near, medium, and far distance groups.
- Identify schools potentially underserved by wind energy infrastructure.
- Create an interactive map to visualize schools and their distance categories.

This analysis supports decision-making for renewable energy deployment and digital infrastructure planning in education.

---

## Data Sources

- **Public Schools Data:** California Department of Education public schools dataset (`pubschls.csv`).
- **Wind Turbines Data:** United States Wind Turbine Database (`uswtdb_V8_1_20250522.csv`).

---

## Setup Instructions

1. Clone or download this repository.

2. Install required Python packages:

    ```bash
    pip install pandas geopandas shapely folium
    ```

3. Place the data files (`pubschls.csv` and `uswtdb_V8_1_20250522.csv`) in a folder on your machine.

4. Update file paths in the scripts (`distance_analysis.py` and `map_visualization.py`) to match your data file locations.

---

## Usage

### Distance Analysis

Run `distance_analysis.py` to:

- Load and clean school and turbine data.
- Calculate distances from schools to nearest turbines (in kilometers).
- Categorize schools by distance.
- Save results to a CSV file (`schools_with_distances.csv`).

```bash
python distance_analysis.py

Visualization
Run map_visualization.py to:

Load the processed CSV.

Generate an interactive HTML map showing schools color-coded by distance category.

Save the map as schools_wind_turbines_map.html.
python map_visualization.py

Notes
The distance calculations use the California Albers projection (EPSG:3310) for accurate measurements.

The map uses Folium with color-coded circle markers.

Schools within 5 km of a turbine are green; 5-10 km are orange; more than 10 km are red.

Contact
For questions or support, please reach out to:

Catalina Cifuentes
Email: catacift@gmail.com