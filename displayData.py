import json
import re
import os

json_file_path = os.path.join(os.path.dirname(__file__), 'products.json')

with open(json_file_path, 'r') as f:
    products = json.load(f)

value_unit_pattern = re.compile(r"([\d.]+)\s*(\w*)")

def extract_value_unit(spec):
    match = value_unit_pattern.match(spec)
    if match:
        value, unit = match.groups()
        return value, unit
    return spec, "" 


print(f"{'Product Code':<20} {'Name':<70} {'Weight (kg)':<15} {'Focal Length (mm)':<20} {'Design Wavelength (nm)':<25} {'Refractive Index':<15}")

for product in products:
    for code, specs in product.items():
        
        name = specs.get("Name", "N/A")
        weight, _ = extract_value_unit(specs.get("Weight"))
        focal_length, _ = extract_value_unit(specs.get("Focal length f"))
        design_wl, _ = extract_value_unit(specs.get("Design Wavelength"))
        refractive_index = specs.get("Refractive index   n<sub>e</sub>")

        print(f"{code:<20} {name:<70} {weight:<15} {focal_length:<20} {design_wl:<25} {refractive_index:<15}")
