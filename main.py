import requests
import os

# To run this script, replace 'YOUR_API_KEY' with your actual Stability AI key
# or set it as an environment variable.
API_KEY = os.getenv("STABILITY_API_KEY", "YOUR_API_KEY_HERE")

response = requests.post(
    "https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"Bearer {API_KEY}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Modern digital art visualization of n8n, a sprawling, glowing, interconnected workflow automation system. Landscape orientation (16:9 aspect ratio) for a desktop background. Abstract nodes like glowing geometric shapes (hexagons, spheres, cubes) are connected by bright energy lines forming branching pathways and loops, creating a futuristic neural network. Data streams visualized as light pulses moving rapidly along the connections. The scene is set in a deep cosmic or cybernetic void with gradient tones of sapphire blue, purple, and vibrant teal, contrasted by sharp orange and electric pink light glows from the nodes. Soft, volumetric lighting and bokeh effects. The overall style is clean, modern, high-tech, cinematic. Spacious composition with empty areas on the left and right, leaving room for desktop icons. Sharp focus on central elements.",
        "output_format": "webp",
        "aspect_ratio": "16:9"
    },
)

if response.status_code == 200:
    with open("./n8n_wallpaper.webp", 'wb') as file:
        file.write(response.content)
    print("Success! Image saved as n8n_wallpaper.webp")
else:
    raise Exception(str(response.json()))
