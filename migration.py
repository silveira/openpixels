#!/usr/bin/env python3

from PIL import Image
import os

# Folder paths
input_folder = "layers"
output_folder = "layers_output"
os.makedirs(output_folder, exist_ok=True)

# Define vertical cut regions (x_start, x_end)
cuts = [
    (32, 36),   # remove x=32–35 (4 pixels wide) 
    (68, 73)    # remove x=68–72 (5 pixels wide)
]

def remove_vertical_sections(img, cuts):
    # Sort cuts by x_start
    cuts = sorted(cuts, key=lambda c: c[0])
    
    width, height = img.size
    
    # Build list of kept regions
    kept_regions = []
    current_x = 0
    
    for x_start, x_end in cuts:
        # Add region before this cut
        if x_start > current_x:
            kept_regions.append(img.crop((current_x, 0, x_start, height)))
        current_x = x_end  # skip this region
    
    # Add final region after last cut
    if current_x < width:
        kept_regions.append(img.crop((current_x, 0, width, height)))
    
    # Concatenate horizontally
    new_width = sum(region.width for region in kept_regions)
    new_img = Image.new("RGBA", (new_width, height))
    
    x_offset = 0
    for region in kept_regions:
        new_img.paste(region, (x_offset, 0))
        x_offset += region.width
    
    return new_img

# Process all PNGs
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        new_img = remove_vertical_sections(img, cuts)
        
        save_path = os.path.join(output_folder, filename)
        new_img.save(save_path)

        print(f"Processed {filename} → new size {new_img.size}")

