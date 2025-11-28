#!/usr/bin/env python3

from PIL import Image
import os

folder = "layers"

for filename in sorted(os.listdir(folder)):
  if filename.lower().endswith(".png"):
    path = os.path.join(folder, filename)
    with Image.open(path) as img:
      width, height = img.size
      print(f"{width} {height} {filename}")
