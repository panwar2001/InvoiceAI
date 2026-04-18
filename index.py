from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config

model_path = "./models/glm-ocr-6bit"
model, processor = load(model_path)
config = load_config(model_path)

# List of image paths from RAPIDO_1
image_paths = ["./RAPIDO_1/0.png", "./RAPIDO_1/1.png", "./RAPIDO_1/2.png"]

for i, img_path in enumerate(image_paths):
    print(f"\n--- Processing Rapido Receipt {i} ---")
    
    # Using the most reliable trigger for GLM-OCR models
    prompt_text = (
        "Text Recognition: Extract the following into JSON:\n"
        "- amount: Total ride amount\n"
        "- date: Time of ride\n"
        "- pickup: Pickup location address\n"
        "- drop: Drop location address\n"
        "- distance: Trip distance. Usually appears with units like km, kilometer, mi, or miles."
    )
    
    formatted_prompt = apply_chat_template(processor, config, prompt_text, num_images=1)
    
    # Pass path directly for better preprocessing
    output = generate(model, processor, prompt=formatted_prompt, image=img_path, max_tokens=1024, temp=0.0)
    print(f"EXTRACTION RESULT:\n{output.text}")