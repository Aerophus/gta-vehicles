import os
import json

# Folder containing your images
images_folder = 'images'
output_file = 'vehicles.json'

vehicle_names = set()

for filename in os.listdir(images_folder):
    if filename.endswith('.webp'):
        # Remove _D or _N and extension
        name = filename.rsplit('_', 1)[0]
        vehicle_names.add(name)

# Convert to sorted list
vehicle_list = sorted(list(vehicle_names))

# Save to JSON
with open(output_file, 'w') as f:
    json.dump(vehicle_list, f, indent=4)

print(f"Saved {len(vehicle_list)} vehicles to {output_file}")
