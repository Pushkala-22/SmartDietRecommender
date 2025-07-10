# 🥗 Smart Diet Recommender

This AI-powered project analyzes your mood from free-text journal entries and recommends nutritious meals based on how you feel and your health goals.

---

## 💡 Features

- 🌈 **Mood Detection**: Uses TextBlob sentiment analysis to detect if you're feeling Happy, Sad, or Neutral
- 🥦 **Goal-Based Meal Recommendations**: Filters meals based on your health goals: *Lose Weight*, *Gain Weight*, or *Stay Healthy*
- 📊 **gives some food recomendations
- 📚 **Real Dataset**: Based on the [RAW_recipes.csv](https://www.kaggle.com/datasets/schemersays/food-recommendation-system) dataset containing 230,000+ real recipes
- 🧠 **No Training Required**: Uses pre-trained NLP techniques and data science logic—no model training needed!

---

## 🛠️ Requirements
Install required packages with:

```bash
pip install pandas textblob
python -m textblob.download_corpora

📂 Project Files
File	Purpose
food_recommender.py	Main script to run your app
RAW_recipes.csv:	Dataset for meal information
                   # You can download it from here :
                    //https://drive.google.com/file/d/1kVJKDUUUlyCswM_0a1u22O3m4nc8B8ml/view?usp=sharing
                    
Smart_Diet_Project.ipynb	Notebook version with step-by-step explanation
README.md	This file!
requirements.txt (optional)	List of required libraries

▶️ How to Run the Project
Ensure RAW_recipes.csv is in the same folder as diet_recommender_final.py

Run the script:

bash
python diet_recommender_final.py


**Follow the prompts in your terminal:
Write a mood journal

Enter a health goal

Receive 5 meals with full nutrition info!

💬 Sample Output:
////
🌿 Welcome to the Smart Diet Recommender 🌿

📝 How are you feeling today? Write a short journal entry:
>  not ok

🎯 What is your health goal? (Lose Weight / Gain Weight / Stay Healthy):
>  stay healthy

🔍 Analyzing your mood...
✅ Detected Mood: Sad

📦 Loading recipes...

🍽 Generating your personalized meal plan...

✨ Here are 5 meal suggestions for you:
1. teriyaki chicken   noodles  21 day wonder diet  day 20
2. pork and green chili casserole
3. tasty cheesy scalloped potato casserole
4. ground turkey and eggplant casserole
5. pork chops   fried rice casserole

✅ Thank you for using Smart Diet Recommender.
////
📎 Credits
Dataset: Food.com recipes

NLP Toolkit: TextBlob

🙋‍♀️ Created By
 Pushkala AI/ML Internship  Project 
✨ Future dietetics meets intelligent decision-making ✨
