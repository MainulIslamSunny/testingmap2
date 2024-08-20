import folium
from folium.plugins import Draw

# Initialize the map
map = folium.Map(location=[23.7808405, 90.419689], zoom_start=10)

# Add drawing tools to the map
draw = Draw(
    draw_options={
        'polyline': False,
        'polygon': False,
        'circlemarker': False,
        'rectangle': True,  # Enable rectangle drawing
        'circle': True,      # Enable circle drawing
        'marker': False,
    },
    edit_options={
        'edit': True,
        'remove': True
    }
)
draw.add_to(map)

# Save the generated HTML to run.html
map.save('run.html')
