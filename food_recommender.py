import pandas as pd
import ast
from textblob import TextBlob
import random

# Step 1: Load and preprocess the dataset
def load_and_prepare_data():
    df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/project2/datasets/RAW_recipes.csv", usecols=["name", "ingredients", "nutrition"])
    df.dropna(inplace=True)

    # Convert stringified lists to actual lists
    df["ingredients"] = df["ingredients"].apply(ast.literal_eval)
    df["nutrition"] = df["nutrition"].apply(ast.literal_eval)

    # Extract calories from nutrition
    df["calories"] = df["nutrition"].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else None)
    df.dropna(subset=["calories"], inplace=True)

    return df

# Step 2: Analyze mood from journal
def analyze_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Happy"
    elif polarity < -0.1:
        return "Sad"
    else:
        return "Neutral"

# Step 3: Recommend meals based on mood and goal
def recommend_meals(df, mood, goal):
    # Filter by goal
    if goal == "Lose Weight":
        df = df[df["calories"] < 400]
    elif goal == "Gain Weight":
        df = df[df["calories"] > 600]
    elif goal == "Stay Healthy":
        df = df[(df["calories"] >= 400) & (df["calories"] <= 600)]

    # Mood-based keyword filtering
    mood_keywords = {
        "Happy": ["salad", "grill", "bowl", "wrap", "smoothie"],
        "Sad": ["soup", "pasta", "stew", "casserole", "noodles"],
        "Neutral": ["rice", "lentil", "sandwich", "omelette", "vegetable"]
    }

    keywords = mood_keywords.get(mood, [])
    filtered = df[df["name"].str.contains('|'.join(keywords), case=False, na=False)]

    # If no match, fall back to goal-based only
    if filtered.empty:
        filtered = df

    return filtered["name"].drop_duplicates().sample(n=5, random_state=random.randint(1, 100)).tolist()

# Step 4: Main program
def main():
    try:
        print("🌿 Welcome to the Smart Diet Recommender 🌿\n")

        journal = input("📝 How are you feeling today? Write a short journal entry:\n> ").strip()
        if not journal:
            raise ValueError("Journal entry cannot be empty.")

        goal = input("\n🎯 What is your health goal? (Lose Weight / Gain Weight / Stay Healthy):\n> ").strip().title()
        if goal not in ["Lose Weight", "Gain Weight", "Stay Healthy"]:
            raise ValueError("Invalid goal. Please enter one of the suggested options.")

        print("\n🔍 Analyzing your mood...")
        mood = analyze_mood(journal)
        print(f"✅ Detected Mood: {mood}")

        print("\n📦 Loading recipes...")
        df = load_and_prepare_data()
        if df.empty:
            raise ValueError("The recipe dataset is empty or could not be loaded.")

        print("\n🍽 Generating your personalized meal plan...")
        meals = recommend_meals(df, mood, goal)
        if not meals:
            print("⚠ Sorry, no meals matched your preferences.")
        else:
            print("\n✨ Here are 5 meal suggestions for you:")
            for i, meal in enumerate(meals, 1):
                print(f"{i}. {meal}")

    except FileNotFoundError:
        print("❌ Could not find the dataset file. Please make sure 'RAW_recipes.csv' is in your folder.")

    except ValueError as ve:
        print(f"⚠ {ve}")

    except Exception as e:
        print(f"🔴 Unexpected error: {str(e)}")

    finally:
        print("\n✅ Thank you for using Smart Diet Recommender.")
if __name__=="__main__":
    main()