from flask import Flask, render_template, request, redirect, url_for
import re
import markdown
import os
import numpy as np
import tensorflow as tf
import time
import requests
from keras.preprocessing import image
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
import json
from google.generativeai import GenerativeModel
import google.generativeai as genai
import google.ai.generativelanguage as types
app = Flask(__name__)

# Load Pretrained Keras Model for Ingredient Recognition
model = tf.keras.models.load_model("efficientnetv2_fast_food_classifier.keras")

# Load saved class indices
with open("class_indices.json", "r") as f:
    idx_to_class = json.load(f)
idx_to_class = {int(k): v for k, v in idx_to_class.items()}

print("✅ Loaded class indices:", idx_to_class)

# Google AI Studio API (Gemini API) for Recipe Generation
genai.configure(api_key="your api key")
#GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText?key={GOOGLE_API_KEY}"

# Function to Predict Ingredients from Image
def predict_ingredients(img_path):
    img = image.load_img(img_path, target_size=(96, 96))  # Resize to model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)  # Normalize
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)  # Get highest probability index
    predicted_class_label = idx_to_class.get(predicted_class_index, "Unknown Ingredient")  # Get class label
    print(predicted_class_label)

    return predicted_class_label

# Function to Generate AI-based Recipe Suggestions
# Function to Generate AI-based Recipe Suggestions with Images
def generate_recipes(ingredients):
    prompt = f"Suggest 3 different Indian recipes using these ingredients: {ingredients}. Provide only the names of the recipes in a numbered list."

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(prompt)
        
        if response and response.text:
            recipes = re.findall(r"\d+\.\s*(.*)", response.text)  # Extract recipe names

            if not recipes:  
                recipes = response.text.split("\n")[:3]

            recipe_names = [recipe.strip() for recipe in recipes]

            # Generate images for each recipe
            recipe_images = [generate_recipe_image(recipe) for recipe in recipe_names]

            return list(zip(recipe_names, recipe_images))  # Pair names with images

    except Exception as e:
        print(f"Error generating recipes: {e}")

    return [("Recipe not available.", "static/default.jpg")]


import requests

# Replace this with your actual Hugging Face API Token
 <your key>

def generate_recipe_image(recipe_name):
    """Generate an AI food image using Hugging Face's Stable Diffusion API."""
    image_path = f"static/{recipe_name.replace(' ', '_')}.png"
    if os.path.exists(image_path):  # If image exists, return it immediately
        return image_path
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

    prompt = f"A high-quality, well-plated, delicious image of {recipe_name}, realistic and vibrant."

    for attempt in range(3):  # Retry mechanism
        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            response.raise_for_status()  # Raise error if request fails
            
            if response.status_code == 200:
                image_data = response.content
                image_path = f"static/{recipe_name.replace(' ', '_')}.png"

                # Ensure the directory exists
                os.makedirs("static", exist_ok=True)

                with open(image_path, "wb") as file:
                    file.write(image_data)

                return image_path  # Return saved image path

        except requests.exceptions.RequestException as e:
            print(f"❌ Hugging Face API call failed (Attempt {attempt + 1}): {e}")
            time.sleep(2 ** attempt)  # Exponential backoff (1s, 2s, 4s)
    
    return "static/default.jpg"  #
def generate_recipe_instructions(recipe_name, ingredients):
    prompt = (
        f"Provide step-by-step cooking instructions for {recipe_name} using these ingredients: {ingredients}. "
        "If necessary, you can include up to 3-5 additional common ingredients, but do not ask any questions. " 
        "After the instructions, provide an estimated nutritional breakdown per serving, including calories, protein, fats, carbohydrates, and fiber. and the heading of nutritinal values should be only the Nutritinal"
        "Return only the final instructions and nutritional values in a structured format."
    )

    model = genai.GenerativeModel("gemini-1.5-flash")  # Using Gemini API
    try:
        response = model.generate_content(prompt)
        print("📖 Recipe Instructions Response:", response.text)

        if response and response.text:
            return response.text.strip()  # Clean the response
    except Exception as e:
        print(f"❌ Error generating recipe instructions: {e}")

    return "Instructions and nutritional values not available."

# Function to Generate Cooking Instructions for a Selected Recipe
# def generate_recipe_instructions(recipe_name, ingredients):
#     prompt = (
#         f"Provide step-by-step cooking instructions for {recipe_name} using these ingredients: {ingredients}. "
#         "If necessary, you can include up to 3-5 additional common ingredients, but do not ask any questions. "
#         "Return only the final instructions."
#     )
#     model = genai.GenerativeModel("gemini-1.5-flash")  # Use Gemini API
#     try:
#         response = model.generate_content(prompt)
#         print("📖 Recipe Instructions Response:", response.text)

#         if response and response.text:
#             return response.text.strip()  # Clean the response
#     except Exception as e:
#         print(f"❌ Error generating recipe instructions: {e}")

#     return "Instructions not available."

# Home Route - Display Top 3 Recipes
@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = []

    if request.method == 'POST':
        if 'ingredients' in request.form:
            ingredients = request.form['ingredients']
        elif 'image' in request.files:
            image_file = request.files['image']
            img_path = os.path.join("static/uploads", image_file.filename)
            image_file.save(img_path)
            ingredients = predict_ingredients(img_path)

        # Generate AI-based recipes with images
        recipes = generate_recipes(ingredients)

    return render_template('index.html', recipes=recipes)

# def index():
#     recipes = []

#     if request.method == 'POST':
#         if 'ingredients' in request.form:
#             ingredients = request.form['ingredients']
#         elif 'image' in request.files:
#             image_file = request.files['image']
#             img_path = os.path.join("static/uploads", image_file.filename)
#             image_file.save(img_path)
#             ingredients = predict_ingredients(img_path)

#         # Generate AI-based recipes
#         recipes = generate_recipes(ingredients)

#     return render_template('index.html', recipes=recipes)

# Recipe Details Route - Show Instructions

@app.route('/recipe/<recipe_name>')
def recipe_details(recipe_name):
    ingredients = request.args.get('ingredients', '')  
    instructions_with_nutrition = generate_recipe_instructions(recipe_name, ingredients)

    # Locate where nutrition info starts
    nutrition_start = None
    lines = instructions_with_nutrition.strip().split("\n")
    for i, line in enumerate(lines):
        if "**Nutritional Values" in line:
            nutrition_start = i
            break

    if nutrition_start is not None:
        instructions = "\n".join(lines[:nutrition_start]).strip()
        nutrition_info = "\n".join(lines[nutrition_start:]).strip()
    else:
        instructions = instructions_with_nutrition.strip()
        nutrition_info = "Nutritional values not available."

    # Convert Markdown to HTML
    instructions_html = markdown.markdown(instructions)
    nutrition_info_html = markdown.markdown(nutrition_info)

    return render_template('recipe.html', 
                           recipe_name=recipe_name, 
                           instructions=instructions_html, 
                           nutrition_info=nutrition_info_html)


if __name__== '__main__':
    app.run(debug=True) 