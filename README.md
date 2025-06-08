---

# 🍳 Smart Recipe Generator

The **Smart Recipe Generator** is an AI-powered web application that transforms meal planning by providing intelligent, real-time recipe suggestions. Built using a combination of **Machine Learning (ML)**, **Computer Vision**, and **Natural Language Processing (NLP)**, the system allows users to generate recipes either by **manually entering ingredients** or by **uploading an image** of the ingredients they have.

---

## 🧠 Key Features

* 🥦 **Ingredient Detection via Image Upload**
  Utilizes a **pretrained EfficientNetV2 model** to identify ingredients from uploaded images.

* ✍️ **Manual Ingredient Entry**
  Users can type ingredients to receive AI-generated recipes.

* 🪄 **AI-Powered Recipe Generation**
  Uses **Google AI Studio’s Gemini API** for dynamic, personalized recipe creation.

* 🖼️ **Recipe Image Generation**
  Leverages **Hugging Face API** to produce realistic recipe images based on the recipe name or description.

* 📋 **Step-by-Step Instructions**
  Each recipe comes with detailed, easy-to-follow directions.

* 🍽️ **Dynamic & Adaptive**
  Unlike static recipe databases, suggestions are based on real-time inputs—reducing food waste and enhancing usability.

---

## 🛠️ Tech Stack

| Component               | Technology Used                             |
| ----------------------- | ------------------------------------------- |
| Frontend                | HTML, CSS, JavaScript                       |
| Backend                 | Flask (Python)                              |
| ML Model                | EfficientNetV2 (for ingredient recognition) |
| NLP                     | Gemini API (Google AI Studio)               |
| Image Generation        | Hugging Face API                            |

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/navaneeth91/smart-recipe-generator.git
cd smart-recipe-generator
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Access the app locally at:
`http://127.0.0.1:5000/`

---

## 🧪 System Design Overview

* 📸 **Input Image** → Ingredient Detection via EfficientNetV2
* 📥 **Text Input** → Direct Ingredient Entry
* 🤖 **Processing** → Gemini API generates recipes with NLP
* 🖼️ **Output** → Recipe + Image + Instructions
* 🖥️ **Interface** → Interactive Flask web UI

---

## 📈 Use Case Benefits

* ✅ Minimizes **food waste** by recommending dishes using what users already have.
* ✅ Promotes **healthy home cooking**.
* ✅ Reduces the decision fatigue of “What to cook today?”
* ✅ Enhances user experience through **AI personalization**.

---

## 📸 Screenshots

*(Add screenshots of the UI, input form, recipe output with images)*
![WhatsApp Image 2025-06-05 at 18 04 37_68828a63](https://github.com/user-attachments/assets/8ebdeb6c-fc8a-4b04-9c4e-3841b59309e7)
![WhatsApp Image 2025-06-05 at 18 04 38_017babf7](https://github.com/user-attachments/assets/73430abf-f911-484f-9a9f-55f2beb52fe6)

![WhatsApp Image 2025-06-05 at 18 04 37_deac4883](https://github.com/user-attachments/assets/fe1a84c9-b5c5-443b-9035-70b31b66717c)
![WhatsApp Image 2025-06-05 at 18 04 38_54de45cd](https://github.com/user-attachments/assets/73573590-452b-4c4f-8c6c-818882b1b325)





---

## 🔮 Future Improvements

* 🧑‍🍳 User login with saved recipe history
* 🛒 Auto-generated grocery lists
* 🌐 Multi-language support

---

## 🧑‍💻 Team

* **Navaneeth Siliveri** – Vardhaman College of Engineering
 Feel free to connect on [LinkedIn](https://www.linkedin.com/in/navaneeth-siliveri-99b1392a9/) or explore more projects on [GitHub](https://github.com/navaneeth91).
* **Pragathi Vaddireddy** – Vardhaman College of Engineering
  Feel free to connect on [LinkedIn](https://www.linkedin.com/in/pragathi-reddy-491a39255) or explore more projects on [GitHub](https://github.com/pragathi2005).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

