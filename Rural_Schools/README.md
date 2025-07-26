# Geospatial Diagnosis of Rural Public Schools in San Diego County

📍 **Project Title:** AI-Driven Energy Justice for Rural Schools: Wind Power and Digital Connectivity in San Diego and Surrounding Regions  
📁 **Repository Folder:** `Rural_Schools/diagnosis/`

---

## 🔍 Executive Summary

This repository presents a geospatial diagnosis of public schools in San Diego County—particularly those located in rural ZIP codes—aimed at identifying gaps in wind energy infrastructure and internet connectivity. These insights provide the foundation for designing AI-powered solutions that promote educational equity, clean energy access, and economic resilience in underserved communities.

---

## 📊 Methodology

The analysis combines cleaned educational datasets with national wind turbine infrastructure data and school district boundary files. The following components were developed using Python (Pandas, GeoPandas, Folium):

### 🗺️ 1. Interactive Map of Rural Public Schools  
- **Goal:** Visualize public schools located within rural ZIP codes in San Diego County.  
- **Method:** Filters a cleaned dataset of San Diego public schools by rural ZIP codes and maps them using Folium with custom markers.  
- **Output:** `map_schools_rural.html` (interactive HTML map)

### 🧭 2. School District Boundary Overlay  
- **Goal:** Associate each rural school with its corresponding school district.  
- **Method:** Spatial join between school locations and district polygons using GeoPandas. Result is plotted as a static PNG image.  
- **Output:** `school_districts_map.png` (static district map with school points)

### 🌬️ 3. Proximity Analysis to Wind Turbines  
- **Goal:** Calculate geodesic distances between each rural school and the nearest operational wind turbine.  
- **Method:**  
  - Loads the latest U.S. Wind Turbine Database (V8.1).  
  - Converts coordinates to shapely Points and computes distances (in km).  
  - Categorizes schools as:  
    - `Near` (<5 km)  
    - `Medium` (5–10 km)  
    - `Far` (>10 km)  
- **Output Summary:**  

Far (>10 km): 12,802 schools
Medium (5–10 km): 576 schools
Near (<5 km): 208 schools
---

## 🧠 Strategic Interpretation

- Over **12,000 rural schools** lack immediate proximity to wind turbines, exposing a vast infrastructure gap.
- Only **208 schools** are located within 5 km of existing turbines—potential early adopters for AI-driven microgrid pilot programs.
- Mapping districts alongside ZIP classifications enables **targeted clean energy and broadband initiatives**.
- The tools developed are scalable, transparent, and data-driven—empowering policy, engineering, and philanthropic collaboration.

---

## 🏛️ National Interest Justification

This work aligns with multiple national priorities:
- ⚡ Clean Energy & Grid Resilience (DOE)
- 🛰️ Broadband Access & Digital Equity (FCC & NTIA)
- 🏫 Educational Equity in Rural America (Department of Education)

The geospatial outputs support interventions that:
- Reduce rural-urban energy inequality,
- Enhance digital infrastructure in education,
- Advance the U.S. climate, education, and economic goals.

---

## 🌎 Regional Focus & Scalability

Although focused on San Diego County, this approach is easily adaptable to:
- Other rural California counties (e.g., Imperial, Kern, Humboldt),
- National scale applications in agricultural and tribal areas,
- Integration with AI/ML for predictive siting and optimization.

---

## 📁 Output Files

| File | Description |
|------|-------------|
| `map_schools_rural.html` | Interactive map of rural schools with ZIP code filter |
| `school_districts_map.png` | Static map overlay of school districts with rural school points |
| `schools_wind_distance_summary.txt` | Tabulated proximity results for wind turbine accessibility |

---

## ✅ Technologies Used

- `Python 3.11`
- `Pandas` / `GeoPandas` / `Folium`
- `Shapely` / `Geopy`
- `U.S. Wind Turbine Database (V8.1)`
- `California Department of Education (CDE)`

---

## 📬 Contact

For inquiries, contributions, or collaborations related to rural energy and AI-based infrastructure planning, please contact:

**Catalina Cifuentes**  
M.S. in Data Analytics | Energy & AI Researcher  
📍 San Diego, California  
✉️ catalina.data.ai@gmail.com *(replace with your actual email)*

