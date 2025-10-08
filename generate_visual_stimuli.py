from PIL import Image, ImageDraw


def create_circle_stimulus(filename, color, size=400, transparent_bg=True):
    """Create a circular visual stimulus with transparent background"""
    # Create image with RGBA mode for transparency support
    if transparent_bg:
        img = Image.new('RGBA', (size, size), color=(0, 0, 0, 0))
    else:
        # PsychoPy default gray is approximately (128, 128, 128)
        img = Image.new('RGB', (size, size), color=(128, 128, 128))
    
    draw = ImageDraw.Draw(img)
    
    # Draw circle in the center
    margin = size // 4
    
    if transparent_bg:
        # For transparent background, use RGBA color format
        if color == 'white':
            fill_color = (255, 255, 255, 255)
        elif color == 'black':
            fill_color = (0, 0, 0, 255)
        else:
            fill_color = color
    else:
        fill_color = color
    
    draw.ellipse([margin, margin, size-margin, size-margin],
                 fill=fill_color, outline=fill_color)
    
    # Save the image
    img.save(filename)
    print(f"Created {filename}")


# Generate stimuli with transparent background for PsychoPy
print("Generating visual stimuli with transparent backgrounds...")
print("These will work with any PsychoPy background color.\n")

create_circle_stimulus('white_visual.png', color='white', transparent_bg=True)
create_circle_stimulus('black_visual.png', color='black', transparent_bg=True)

print("\nVisual stimuli generated successfully!")
print("- white_visual.png (white circle, transparent background)")
print("- black_visual.png (black circle, transparent background)")
print("\nThese images will adapt to PsychoPy's gray background.")
