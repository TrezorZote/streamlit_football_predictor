import streamlit as st
# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier
#from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import football_data 

# Sample dataset with match outcomes based on past matches outcomes
# outcomes both_teams_to_score = 3, home_to_score0 = 1, away_to_score = 2

data = {
                             'Outcome': [3,     3,     3,     3,    3,   3,    3,     3,    1,    2,      2,    1,    1,    1,     1 ],
   'home_goalscoredhome_pergame_ratio': [1.8,  1.6,  2.1,   1.8,  2.6,   1.6,  1.6,  2.4,  1.6,  1.4,    1.0,  2.0,  3.5,   2.4,   2.6], 
   'away_goalscoredaway_pergame_ratio': [1.6,  1.9,  2.4,   1.9,  2.8,   1.5,  1.9,  3.0,  1.5,  2.0,    1.7,  1.1,  1.8,   1.1,   1.2],
    'home_goalconceeded_pergame_ratio': [1.1,  2.2,  1.9,   1.7,  0.5,   1.9,  1.1,  1.3,  0.4,  1.0,    1.3,  0.8,  1.4,   1.3,   0.6],
    'away_goalconceeded_pergame_ratio': [1.4,  1.1,  0.6,   1.9,  1.0,   1.4,  1.2,  1.1,  1.9,  1.0,    0.8,  1.3,  1.6,   1.8,   1.7],
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[[ 'home_goalscoredhome_pergame_ratio', 
         'away_goalscoredaway_pergame_ratio',
         'home_goalconceeded_pergame_ratio',  'away_goalconceeded_pergame_ratio']]

y = df['Outcome']

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the  model
model =  DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict the results on the test set
# Evaluate the model
#print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
y_pred = model.predict(X_test)

league_chosen = any
leagues = [football_data.pl_team_stats,football_data.championship_team_stats,
           football_data.la_liga_team_stats,football_data.spanish_segunda_team_stats,
           football_data.ligue1_team_stats,football_data.serie_a_team_stats,
           football_data.bundesliga_team_stats,football_data.bundesliga2_team_stats,
           football_data.eredivisie_team_stats,football_data.danish_superliga_stats,
           football_data.saudi_pro_league_stats,football_data.swiss_league_stats,
           football_data.primeira_liga_team_stats,football_data.turkish_super_lig_stats]
 

def set_league(league_number: int):
  global league_chosen
  league_chosen = leagues[league_number]

def get_league_number(league_name: str) -> int:
    """
    Returns an integer corresponding to the league based on its name.

    Mapping:
    0  -> Premier League
    1  -> England Championship
    2  -> La Liga
    3  -> Spain Segunda
    4  -> Ligue 1
    5  -> Serie A
    6  -> Bundesliga
    7  -> Bundesliga 2
    8  -> Eredivisie
    9  -> Danish Superliga
    10 -> Saudi Pro League
    11 -> Swiss League
    12 -> Portugal Primeira Liga
    13 -> Turkish Super Lig
    """

    # Convert to lowercase to make matching case-insensitive
    league_lower = league_name.lower()

    # Mapping from substring to league number
    league_mapping = {
        "premier": 0,
        "championship": 1,
        "la liga": 2,
        "segunda": 3,
        "ligue 1": 4,
        "serie a": 5,
        "bundesliga 2": 7,
        "bundesliga": 6,
        "eredivisie": 8,
        "superliga": 9,
        "saudi": 10,
        "swiss": 11,
        "primeira": 12,
        "turkish": 13
    }

    # Check if any key is present in the league_name
    for key, number in league_mapping.items():
        if key in league_lower:
            return number

    # Default if no match
    return -1
   
# ------------------------------
# prediction function
# ------------------------------
def predict_outcome(league: str, home_team: str, away_team: str) -> str:
    league_number = get_league_number(league)
    set_league(league_number)
    # ------------------------------
    # Validate team names
    # ------------------------------
    if home_team not in league_chosen or away_team not in league_chosen:
        return "Invalid team name or league chosen enter correct full names"

    # ------------------------------
    # Extract features
    # ------------------------------
    home_goals_scored_per_game = league_chosen[home_team][0]
    home_goals_conceded_per_game = league_chosen[home_team][2]
    away_goals_scored_per_game = league_chosen[away_team][1]
    away_goals_conceded_per_game = league_chosen[away_team][3]

    game_features = [[
        home_goals_scored_per_game,
        away_goals_scored_per_game,
        home_goals_conceded_per_game,
        away_goals_conceded_per_game
    ]]  # ← 2D shape for sklearn

    # ------------------------------
    # Make prediction
    # ------------------------------
    prediction = model.predict(game_features)[0]

    # ------------------------------
    # Map prediction to text
    # (adjust labels to match training data!)
    # ------------------------------
    if prediction == 0:
        return "Home team to score"
    elif prediction == 1:
        return "Away team to score"
    else:
        return "Both teams to score"

import streamlit as st

# ------------------------------
# Session state initialization
# ------------------------------
#this checks if prediction and history variables were already initialised in the session 
if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------
# UI Title
# ------------------------------
st.title("⚽ Football Goal Outcome Predictor")
st.write("Enter the home and away teams, then click **Predict**.")

# ------------------------------
# Input fields
# ------------------------------
home_team = st.text_input("Home Team")
away_team = st.text_input("Away Team")
# League selection
available_leagues = [
    "Premier League",
    "England Championship",
    "La Liga",
    "Spain Segunda",
    "Ligue 1",
    "Serie A",
    "Bundesliga",
    "Bundesliga 2",
    "Eredivisie",
    "Danish Superliga",
    "Saudi Pro League",
    "Swiss League",
    "Portugal Primeira Liga",
    "Turkish Super Lig"
]

selected_league = st.selectbox("Select League", available_leagues)

# ------------------------------
# Buttons Layout
# ------------------------------
col1, col2, col3 = st.columns(3)

show_history = False  # whether to show the history of past predictions

# Predict Button
with col1:
    if st.button("Predict"):
        result = predict_outcome(selected_league,home_team, away_team)
        st.session_state.prediction = result

        if result != "Invalid input":
            st.session_state.history.append(
                f"{home_team} vs {away_team} → {result}"
            )

# Reset Button (keeps history)
with col2:
    if st.button("Reset"):
        st.session_state.prediction = None
        st.session_state.history.clear
        st.rerun()

# Show History Button
with col3:
    show_history = st.button("Show History")

# ------------------------------
# Display prediction
# ------------------------------
if st.session_state.prediction:
    st.success(f"Prediction: {st.session_state.prediction}")

# ------------------------------
# Display history
# ------------------------------
if show_history and st.session_state.history:
    st.subheader("Prediction History")
    for item in st.session_state.history:
        st.write(f"• {item}")
elif show_history:
    st.info("No predictions made yet.")
