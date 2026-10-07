import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import Point

# Create Spatial Data for Candidate Locations
np.random.seed(101)
lats = np.random.uniform(33.40, 33.45, 10)
lons = np.random.uniform(-111.95, -111.90, 10)

gdf = gpd.GeoDataFrame({
    'site_id': [f"Site_{i+1}" for i in range(10)],
    'demographic_density': np.random.randint(1000, 5000, 10),
    'competitor_distance_km': np.random.uniform(0.2, 5.0, 10),
    'geometry': [Point(xy) for xy in zip(lons, lats)]
}, crs="EPSG:4326")

# Calculate Location Score (Multi-Criteria Decision Analysis)
gdf['location_score'] = (
    (gdf['demographic_density'] / gdf['demographic_density'].max()) * 0.6 +
    (gdf['competitor_distance_km'] / gdf['competitor_distance_km'].max()) * 0.4
) * 100

print(gdf[['site_id', 'demographic_density', 'competitor_distance_km', 'location_score']].sort_values(by='location_score', ascending=False))
