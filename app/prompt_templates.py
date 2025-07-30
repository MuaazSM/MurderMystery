def build_prompt(mystery, user_input):
    clues_text = "\n".join(f"- {clue}" for clue in mystery["clues"])
    suspects = ", ".join(mystery["suspects"])
    clues_formatted = "\n".join(['- ' + clue for clue in mystery['clues']])
    
    return f"""
    You are an AI Detective game evaluator. A player has just watched a video and submitted a theory about what happened.
    Here are the mystery details:

    Title: {mystery['title']}

    Description: {mystery['description']}

    Suspects: {suspects}

    Clues: {clues_formatted}

    Correct Answer:
    {clues_text}

    Reasoning:
    {mystery['reasoning']}


    ---------

    Now evaluate the player's theory and respond with:

    1) A verdict: Is the Theory Correct or Incorrect? 
    2) A short explanation for why it is correct or not.
    3) If incorrect, give a subtle hint.

    Player's Theory:
    \"\"\"{user_input}\"\"\"
    """