#!/usr/bin/env python3

from gimpformats.gimpXcfDocument import GimpDocument

def export_xcf_layers(xcf_path):
    """Export all layers from XCF file as PNG images"""
    
    # Load the XCF file
    project = GimpDocument(xcf_path)
    
    print(f"Image size: {project.width}x{project.height}")
    
    # Get raw layers
    if hasattr(project, 'raw_layers'):
        layers = project.raw_layers
        print(f"Found {len(layers)} raw layers")
        
        for i, layer in enumerate(layers):
            try:
                # Create a layer object
                layer_obj = project.getLayer(i)
                
                if layer_obj and hasattr(layer_obj, 'image'):
                    layer_image = layer_obj.image
                    
                    if layer_image is not None:
                        # Get layer name
                        layer_name = getattr(layer_obj, 'name', f'layer_{i}')
                        clean_name = str(layer_name).replace(' ', '_').replace('/', '_')

                        filename = f"{i:03d}_{clean_name}.png"
                        
                        # Save as PNG
                        layer_image.save(filename)
                        print(f"Saved: {filename}")
                    else:
                        print(f"No image data for layer {i}")
                else:
                    print(f"Could not get layer object for layer {i}")
                    
            except Exception as e:
                print(f"Error processing layer {i}: {e}")
    

if __name__ == "__main__":
    export_xcf_layers("open_chars.xcf")
