import streamlit as st
import random

# Expanded word puzzles with 30+ entries (max 2 emojis each)
word_puzzles = [
    # Movies
    {"emojis": "👑🦁", "answer": "Lion King", "choices": ["Lion King", "Jungle Book", "Simba"], "level": 1, "points": 200},
    {"emojis": "🕷️🕸️", "answer": "Spider-Man", "choices": ["Spider-Man", "Spider", "Web"], "level": 1, "points": 200},
    {"emojis": "🧙⚡", "answer": "Harry Potter", "choices": ["Harry Potter", "Wizard", "Magic"], "level": 1, "points": 200},
    {"emojis": "🤖❤️", "answer": "Wall-E", "choices": ["Wall-E", "Robot Love", "AI"], "level": 1, "points": 200},
    {"emojis": "🐭🏰", "answer": "Mickey Mouse", "choices": ["Mickey Mouse", "Disney", "Cartoon"], "level": 1, "points": 200},
    
    # Technology
    {"emojis": "📱💵", "answer": "Mobile Payment", "choices": ["Mobile Payment", "Apple Pay", "Digital Wallet"], "level": 2, "points": 400},
    {"emojis": "🤖💬", "answer": "Chatbot", "choices": ["Chatbot", "AI Assistant", "Robot"], "level": 2, "points": 400},
    {"emojis": "🛰️🌐", "answer": "Satellite Internet", "choices": ["Satellite Internet", "Starlink", "Space Web"], "level": 2, "points": 400},
    {"emojis": "🔋🚗", "answer": "Electric Car", "choices": ["Electric Car", "Tesla", "EV"], "level": 2, "points": 400},
    {"emojis": "👁️🤖", "answer": "Face ID", "choices": ["Face ID", "Biometrics", "Recognition"], "level": 2, "points": 400},
    
    # Current Affairs
    {"emojis": "🌍🔥", "answer": "Global Warming", "choices": ["Global Warming", "Climate Change", "Hot Earth"], "level": 3, "points": 600},
    {"emojis": "💉🦠", "answer": "Vaccination", "choices": ["Vaccination", "COVID-19", "Pandemic"], "level": 3, "points": 600},
    {"emojis": "🚀🌕", "answer": "Moon Mission", "choices": ["Moon Mission", "Space Travel", "NASA"], "level": 3, "points": 600},
    {"emojis": "⚡🌪️", "answer": "Natural Disaster", "choices": ["Natural Disaster", "Hurricane", "Storm"], "level": 3, "points": 600},
    {"emojis": "💵🔄", "answer": "Digital Currency", "choices": ["Digital Currency", "Bitcoin", "Crypto"], "level": 3, "points": 600},
    
    # Food
    {"emojis": "🍕🇮🇹", "answer": "Pizza", "choices": ["Pizza", "Italian Food", "Cheese"], "level": 1, "points": 200},
    {"emojis": "🍣🇯🇵", "answer": "Sushi", "choices": ["Sushi", "Japanese Food", "Raw Fish"], "level": 1, "points": 200},
    {"emojis": "☕📖", "answer": "Coffee Break", "choices": ["Coffee Break", "Tea Time", "Reading"], "level": 1, "points": 200},
    {"emojis": "🍔🍟", "answer": "Fast Food", "choices": ["Fast Food", "Burger", "McDonalds"], "level": 1, "points": 200},
    {"emojis": "🍫🏭", "answer": "Chocolate Factory", "choices": ["Chocolate Factory", "Willy Wonka", "Candy"], "level": 1, "points": 200},
    
    # Sports
    {"emojis": "⚽🏆", "answer": "World Cup", "choices": ["World Cup", "Football", "Soccer"], "level": 2, "points": 400},
    {"emojis": "🏀🏀", "answer": "NBA", "choices": ["NBA", "Basketball", "Dunk"], "level": 2, "points": 400},
    {"emojis": "🎾🏅", "answer": "Wimbledon", "choices": ["Wimbledon", "Tennis", "Grand Slam"], "level": 2, "points": 400},
    {"emojis": "🏊⏱️", "answer": "Swimming Race", "choices": ["Swimming Race", "Olympics", "Pool"], "level": 2, "points": 400},
    {"emojis": "🚴🏔️", "answer": "Tour de France", "choices": ["Tour de France", "Cycling", "Bike Race"], "level": 2, "points": 400},
    
    # Science
    {"emojis": "🧬🔍", "answer": "DNA Research", "choices": ["DNA Research", "Genetics", "Biology"], "level": 3, "points": 600},
    {"emojis": "🪐🔭", "answer": "Space Telescope", "choices": ["Space Telescope", "Hubble", "NASA"], "level": 3, "points": 600},
    {"emojis": "🧪💥", "answer": "Chemical Reaction", "choices": ["Chemical Reaction", "Experiment", "Lab"], "level": 3, "points": 600},
    {"emojis": "🧠⚡", "answer": "Neuroscience", "choices": ["Neuroscience", "Brain Power", "Psychology"], "level": 3, "points": 600},
    {"emojis": "🌋🔥", "answer": "Volcano", "choices": ["Volcano", "Eruption", "Lava"], "level": 3, "points": 600},
    
    # Bonus Hard Questions
    {"emojis": "🎭🦇", "answer": "Phantom of the Opera", "choices": ["Phantom of the Opera", "Batman", "Theater"], "level": 3, "points": 800},
    {"emojis": "🧜♀️🔱", "answer": "Little Mermaid", "choices": ["Little Mermaid", "Ariel", "Underwater"], "level": 3, "points": 800},
    {"emojis": "🦸♀️💥", "answer": "Wonder Woman", "choices": ["Wonder Woman", "Superhero", "DC Comics"], "level": 3, "points": 800},
    {"emojis": "🧟♂️🏚️", "answer": "The Walking Dead", "choices": ["The Walking Dead", "Zombie", "Apocalypse"], "level": 3, "points": 800},
    {"emojis": "👽📞", "answer": "ET", "choices": ["ET", "Alien", "Phone Home"], "level": 3, "points": 800}
]

def initialize_game():
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_points' not in st.session_state:
        st.session_state.total_points = 0
    if 'current_quiz_index' not in st.session_state:
        st.session_state.current_quiz_index = 0
    if 'quizzes_order' not in st.session_state:
        st.session_state.quizzes_order = random.sample(range(len(word_puzzles)), len(word_puzzles))
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False
    if 'user_guess' not in st.session_state:
        st.session_state.user_guess = ""
    if 'free_coins' not in st.session_state:
        st.session_state.free_coins = 3
    if 'game_history' not in st.session_state:
        st.session_state.game_history = []

def next_quiz():
    st.session_state.current_quiz_index += 1
    st.session_state.show_answer = False
    st.session_state.user_guess = ""

def check_answer(selected_choice):
    current_puzzle = word_puzzles[st.session_state.quizzes_order[st.session_state.current_quiz_index]]
    is_correct = selected_choice == current_puzzle["answer"]
    
    if is_correct:
        st.session_state.score += 1
        st.session_state.total_points += current_puzzle["points"]
        st.session_state.game_history.append({
            "emojis": current_puzzle["emojis"],
            "answer": current_puzzle["answer"],
            "user_answer": selected_choice,
            "correct": True,
            "points": current_puzzle["points"]
        })
        st.success("Correct! 🎉")
    else:
        st.session_state.game_history.append({
            "emojis": current_puzzle["emojis"],
            "answer": current_puzzle["answer"],
            "user_answer": selected_choice,
            "correct": False,
            "points": 0
        })
        st.error(f"Wrong! The correct answer was: {current_puzzle['answer']} 😔")
    
    st.session_state.show_answer = True

def get_hint():
    current_puzzle = word_puzzles[st.session_state.quizzes_order[st.session_state.current_quiz_index]]
    answer = current_puzzle["answer"]
    
    # Deduct a free coin for hint
    if st.session_state.free_coins > 0:
        st.session_state.free_coins -= 1
        # More detailed hint based on answer length
        if len(answer) <= 5:
            hint = f"First letter: {answer[0]}, Last letter: {answer[-1]}"
        else:
            hint = f"First letter: {answer[0]}, Length: {len(answer)}, Category: {get_category(current_puzzle)}"
        return hint
    else:
        return "No free coins left for hints!"

def get_category(puzzle):
    # Determine category based on level (simplified for this example)
    if puzzle['level'] == 1:
        return "Easy"
    elif puzzle['level'] == 2:
        return "Medium"
    else:
        return "Hard"

def reset_game():
    st.session_state.clear()
    initialize_game()
    st.experimental_rerun()

# Initialize game state
initialize_game()

st.title("BrainGlyph Arena")
st.write("Guess the word/phrase from the emojis!")

if st.session_state.current_quiz_index < len(word_puzzles):
    current_puzzle = word_puzzles[st.session_state.quizzes_order[st.session_state.current_quiz_index]]

    # Header with level and points
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(f"Level {current_puzzle['level']}")
    with col2:
        st.subheader(f"Points: {current_puzzle['points']}")
    with col3:
        st.subheader(f"Total: {st.session_state.total_points}")

    # Puzzle display
    st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current_puzzle['emojis']}</h1>", unsafe_allow_html=True)
    
    # Hint system
    hint = None
    hint_col, coin_col = st.columns(2)
    with hint_col:
        if st.button("Get Hint", disabled=st.session_state.show_answer or st.session_state.free_coins <= 0):
            hint = get_hint()
    with coin_col:
        st.write(f"💎 Free Hints: {st.session_state.free_coins}")
    
    if hint:
        st.info(f"💡 Hint: {hint}")
    
    # Shuffle choices
    choices = random.sample(current_puzzle["choices"], len(current_puzzle["choices"]))
    
    # Display choices as buttons with better styling
    for choice in choices:
        if st.button(
            choice, 
            key=choice, 
            disabled=st.session_state.show_answer,
            use_container_width=True
        ):
            check_answer(choice)
    
    if st.session_state.show_answer:
        st.button("Next Puzzle →", on_click=next_quiz, use_container_width=True)

else:
    st.balloons()
    st.header("🎯 Game Over!")
    st.markdown(f"<h2 style='text-align: center;'>🏆 Final Score: {st.session_state.score}/{len(word_puzzles)}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>💰 Total Points: {st.session_state.total_points}</h2>", unsafe_allow_html=True)
    
    # Display game history
    st.subheader("📊 Your Game History")
    for i, result in enumerate(st.session_state.game_history, 1):
        emoji = "✅" if result["correct"] else "❌"
        st.write(f"{emoji} Puzzle {i}: {result['emojis']}")
        st.write(f"   Your answer: {result['user_answer']}")
        st.write(f"   Correct answer: {result['answer']}")
        st.write(f"   Points earned: {result['points']}")
        st.write("---")
    
    # Play Again button with better styling
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button(
            "🔄 Play Again", 
            on_click=reset_game,
            use_container_width=True,
            type="primary"
        ):
            pass
