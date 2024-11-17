import folium

# Define map center coordinates for Accra, Ghana
map_center = [5.6037, -0.1870]

# Create the map
map = folium.Map(location=map_center, zoom_start=12)

# Add a marker
folium.Marker(
    [5.6037, -0.1870],
    popup="Accra, Ghana",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(map)

# Save the map to an HTML file
map.save("map.html")
print("Map has been saved as 'map.html'. Open it in a browser to view.")

