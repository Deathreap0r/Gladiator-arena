# 🔹 FORGE OF FLESH AND FIRE - STREAMLIT APP
import streamlit as st
import random

st.set_page_config(page_title="Forge of Flesh and Fire", layout="centered")

# --- Data Structures ---
titles_by_level = {
    1: "Initiate",
    2: "Steelborn",
    3: "Blooded",
    4: "Prime",
    5: "Ascended"
}

arena_conditions = [
    "Warp Storm: Psychic surges disrupt all logic",
    "Grav Flux: Movement impaired by shifting weight",
    "Radiation Leak: Organic tissue weakens",
    "No-Reflex Protocol: Counterattacks disabled",
    "Spectator Bloodlust: Critical hits doubled"
]

classes = {
    "Reaper": {"Strength": 8, "Agility": 6, "Endurance": 5},
    "Scourge": {"Strength": 6, "Agility": 9, "Endurance": 4},
    "Ironhowl": {"Strength": 7, "Agility": 4, "Endurance": 9},
    "Apostle": {"Strength": 5, "Agility": 5, "Endurance": 7},
    "Burned": {"Strength": 6, "Agility": 7, "Endurance": 6},
}

leaderboard = []

# --- Helper Functions ---
def create_gladiator():
    name_prefixes = ["GORE", "XARN", "HEX", "KARN", "NUL"]
    name_suffixes = ["-77", "-RAGE", "-MKV", "-TERROR", "-X"]
    name = random.choice(name_prefixes) + random.choice(name_suffixes)
    class_name = random.choice(list(classes.keys()))
    level = 1
    xp = 0
    return {
        "name": name,
        "class": class_name,
        "level": level,
        "xp": xp
    }

def fight(g1, g2, mutator):
    g1_power = sum(classes[g1["class"]].values()) + g1["level"] + random.randint(0, 6)
    g2_power = sum(classes[g2["class"]].values()) + g2["level"] + random.randint(0, 6)

    if "Critical" in mutator and random.random() < 0.2:
        g1_power += 5
    if "Critical" in mutator and random.random() < 0.2:
        g2_power += 5

    if g1_power > g2_power:
        return g1
    else:
        return g2

def level_up(gladiator):
    gladiator["xp"] += 1
    if gladiator["xp"] >= gladiator["level"] and gladiator["level"] < 5:
        gladiator["level"] += 1
        gladiator["xp"] = 0

def get_title(gladiator):
    return titles_by_level[gladiator["level"]]

# --- UI Logic ---
st.title("🔥 FORGE OF FLESH AND FIRE 🔥")
st.markdown("A grimdark gladiator arena of biomechanical bloodsport. Tap 'Begin Tournament' to unleash the slaughter.")

if st.button("Begin Tournament"):
    condition = random.choice(arena_conditions)
    st.subheader(f"Arena Condition: {condition}")

    g1 = create_gladiator()
    g2 = create_gladiator()
    g3 = create_gladiator()
    g4 = create_gladiator()

    semifinal_1_winner = fight(g1, g2, condition)
    semifinal_2_winner = fight(g3, g4, condition)

    final_winner = fight(semifinal_1_winner, semifinal_2_winner, condition)
    level_up(final_winner)

    title = get_title(final_winner)
    st.success(f"🏆 Champion: {final_winner['name']} the {title} ({final_winner['class']})")

    leaderboard.append(f"{final_winner['name']} the {title} [{final_winner['class']}]")

if st.button("Show Ascended Ironbound Leaderboard"):
    st.subheader("📜 The Ascended Ironbound")
    if leaderboard:
        for champ in leaderboard[::-1]:
            st.markdown(f"- {champ}")
    else:
        st.info("No champions have ascended yet.")

