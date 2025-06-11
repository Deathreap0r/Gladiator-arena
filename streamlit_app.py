import streamlit as st
import random

# Gladiator Names & Titles
NAMES = ["Raxus", "Velgrim", "Drakmar", "Thorn", "Mordak", "Ironjaw", "Vexis", "Karn", "Brutus", "Skorn"]
TITLES = ["the Mauler", "of the Pit", "Doomfist", "the Cruel", "Warbeast", "the Untamed", "Bonecrusher", "Hellborn"]

def generate_name():
    return f"{random.choice(NAMES)} {random.choice(TITLES)}"

def create_gladiator():
    stats = sorted(random.sample(range(1, 30), 2))
    strength = stats[0]
    agility = stats[1] - stats[0]
    endurance = 30 - stats[1]
    return {
        "name": generate_name(),
        "strength": strength,
        "agility": agility,
        "endurance": endurance
    }

def fight(g1, g2):
    hp1 = g1['endurance']
    hp2 = g2['endurance']
    log = [f"⚔️ {g1['name']} VS {g2['name']}"]

    while hp1 > 0 and hp2 > 0:
        if random.random() < g1['strength'] / (g1['strength'] + g2['agility']):
            dmg = max(1, g1['strength'] // 2)
            hp2 -= dmg
            log.append(f"{g1['name']} hits for {dmg} damage!")
        else:
            log.append(f"{g1['name']} misses!")

        if hp2 <= 0:
            break

        if random.random() < g2['strength'] / (g2['strength'] + g1['agility']):
            dmg = max(1, g2['strength'] // 2)
            hp1 -= dmg
            log.append(f"{g2['name']} counters for {dmg} damage!")
        else:
            log.append(f"{g2['name']} misses!")

    winner = g1['name'] if hp1 > 0 else g2['name']
    log.append(f"🏆 {winner} is victorious!")
    return "\n".join(log), g1, g2

# --- Streamlit UI ---
st.title("⚔️ Gladiator Evolution Arena")

if st.button("Start Battle"):
    g1 = create_gladiator()
    g2 = create_gladiator()
    result, g1stats, g2stats = fight(g1, g2)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(g1stats['name'])
        st.text(f"STR: {g1stats['strength']}\nAGI: {g1stats['agility']}\nEND: {g1stats['endurance']}")
    with col2:
        st.subheader(g2stats['name'])
        st.text(f"STR: {g2stats['strength']}\nAGI: {g2stats['agility']}\nEND: {g2stats['endurance']}")

    st.code(result)
