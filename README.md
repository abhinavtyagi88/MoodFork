# **MoodFork**  
### **Empower Your Mood with Flavorful Recipes**

---

## **🌟 Problem Statement**  
In our fast-paced lives, mood swings and stress are common. Food often serves as a source of comfort, but it can do more—specific flavors actively influence our emotions. Unfortunately, identifying recipes that align with our mood requires time, knowledge, and resources.  

**MoodFork** bridges this gap, offering a unique platform that connects your emotional state to recipes designed to enhance your well-being.

---

## **💡 Proposed Solution**  
MoodFork introduces a mood-based recipe recommendation tool. Users can:  
1. Select their **current mood** or the mood they **want to achieve**.  
2. Get recipes tailored to these emotional goals using **FlavorDB API**, which maps flavors and molecules to their mood-altering properties.  

### **Key Examples**  
- **Citrus Flavors**: Energizing and uplifting.  
- **Vanilla or Chamomile**: Calming and soothing.  

MoodFork creates a mindful, flavor-driven culinary experience to help users balance their emotions through food.  

---

## **⚙️ Features**
- Mood detection using AI (via **FER Library**) and user input.  
- Dynamic recipe recommendations based on the **FlavorDB API**.  
- Integration of **OpenCV** for mood analysis.  

---

## **🚀 How to Run**  
### Step 1: Install Required Libraries
Run the following commands to install dependencies:
```bash
pip install flask
pip install opencv-python
pip install opencv-python-headless
pip install fer
```

### Step 2: Start the Application
Use the command below in your terminal (preferably in **VS Code**):  
```bash
python app.py
```

### Step 3: Access the Application
Open your browser and navigate to:  
**http://127.0.0.1:5000**

---

## **🔗 API Integration**
### **FlavorDB API**  
The app integrates with **FlavorDB API** to map specific flavors to mood-altering properties, ensuring recipe suggestions that match your emotional needs.  

---

## **📂 Project Structure**
```
MoodFork/
│
├── __pycache__/          # Compiled Python bytecode (automatically generated, can be ignored)
├── scss/                 # SCSS (Sassy CSS) files for styling (optional)
├── static/               # Static assets like CSS, JavaScript, and images
├── templates/            # HTML templates for the Flask application
├── emotions_food.json    # JSON file mapping emotions to foods or ingredients
├── README.md             # Project documentation
└── app.py                # Main Flask application

```

---

## **🎨 UI Highlights**
- **Simple Mood Selection**: Users can easily select their emotional state.  
- **AI-Powered Detection**: The app can analyze facial expressions to suggest recipes.  
- **Recipe Recommendations**: Tailored suggestions based on mood and flavor science.  

---

## **📷 Screenshots**  
*Coming Soon!*  

---

## **💻 Technologies Used**
- **Python** (Flask Framework)  
- **OpenCV** (Mood Detection)  
- **FER Library** (Facial Expression Analysis)  
- **FlavorDB API** (Mood-Flavor Mapping)  

---

## **📌 Future Enhancements**
- Advanced **AI-based mood prediction** using facial expressions and text sentiment.  
- Mobile-friendly version.  
- User preferences and history-based recommendations.  

---

## **📧 Contact**
Feel free to reach out if you have questions or suggestions:  
- **Email**: [abhinavtyagi0502@gmail.com](mailto:abhinavtyagi0502@gmail.com)  
- **LinkedIn**: [Abhinav Tyagi](https://www.linkedin.com/in/abhinavtyagi88/)  

---

**Made with ❤️ by [Ctrl Freaks / Abhinav Tyagi]**  

---
