import langchain_helper as lch
import streamlit as st
import random

sad_list = ["sad", "Sad", "Upset", "upset", "anxious", "Anxious", "down", "Down", "angry", "Angry"]

# Sad
sad_activities = [
    #Level 1-4
    "Take 5 deep breaths and focus on the sensation of your breath.",
    "Take a relaxing bath or shower: Treat yourself to a warm bath or shower to help soothe your body and mind.",
    "Listen to a calming piece of music and focus on the melody and rhythm.", 
    "Practice gratitude by writing down three things you're thankful for.",
    "Do a quick body scan meditation, starting from your toes and moving up to your head.",
    "Take a drive and explore a new area: A change of scenery can help lift your spirits and provide a sense of adventure.",
    "Write in a journal or express your feelings through art: Writing down your thoughts and feelings or engaging in creative activities like drawing or painting can be therapeutic.", 
    "Read a book or listen to an audiobook: Escaping into a good book can provide a temporary escape and offer a new perspective.", 
    "Watch a funny movie or TV show: Laughter is a great way to relieve stress and improve your mood.", 
    "Write in a journal or express your feelings through art: Writing down your thoughts and feelings or engaging in creative activities like drawing or painting can be therapeutic.",
    "Do a puzzle or play a board game: Engaging in activities that challenge your mind can help take your focus away from negative thoughts.",
    "Volunteer at a local charity or organization: Helping others can give you a sense of purpose and fulfillment.",
    "Write a letter to someone you care about: Expressing gratitude or reaching out to someone you care about can strengthen your relationships and improve your mood.",
    #Level 5-7
    "Express Your Feelings: Take some time to acknowledge and express your emotions. You can write about how you're feeling in a journal or talk to someone you trust about what's on your mind.", 
    "Listen to uplifting music or your favorite playlist: Music has the power to uplift your spirits and boost your mood.",
    "Cry it out: you can ease your mind and release the tension in your body by allowing yourself to process your emotions.",
    "Engage in a Hobby: Spend time doing something you enjoy or exploring a new hobby. Engaging in activities that bring you pleasure and fulfillment can help distract you from negative thoughts and feelings.",
    "Engage in Creative Activities: Try engaging in creative activities like drawing, painting, writing poetry, or playing a musical instrument. These activities can help you express yourself and channel your emotions in a positive way.",
    "Practice Self-Compassion: Be kind to yourself and practice self-compassion. Treat yourself with the same kindness and understanding that you would offer to a friend in a similar situation.",
    "Practice Gratitude: Take a moment to focus on the things you're grateful for in your life. Practicing gratitude can help shift your perspective and remind you of the positive aspects of your life.",
    "Watch a funny movie or TV show: Laughter is a great way to relieve stress and improve your mood.",
    "Do a workout or yoga session: Exercise releases endorphins, which are natural mood boosters. Even a short workout or yoga session can help improve your mood.",
    #Level 8-9
    "Do a workout or yoga session: Exercise releases endorphins, which are natural mood boosters. Even a short workout or yoga session can help improve your mood.",
    "Practice Gratitude: Take a moment to focus on the things you're grateful for in your life. Practicing gratitude can help shift your perspective and remind you of the positive aspects of your life.",
    "Practice Self-Compassion: Be kind to yourself and practice self-compassion. Treat yourself with the same kindness and understanding that you would offer to a friend in a similar situation.",
    "Express Your Feelings: Take some time to acknowledge and express your emotions. You can write about how you're feeling in a journal or talk to someone you trust, or a professional about what's on your mind.", 
    "Seek Professional Help: If your sadness persists or becomes overwhelming, don't hesitate to reach out to a therapist or counselor for support. They can offer guidance and strategies to help you cope with your emotions.",
    #Level 10
    "Hotlines and Helplines: \nNational Suicide Prevention Lifeline: 1-800-273-TALK (1-800-273-8255) - A free, confidential 24/7 helpline providing support and resources for anyone in distress, including suicide prevention. \n Crisis Text Line: Text HELLO to 741741 - A free, confidential text-based crisis intervention service available 24/7.",
    "Therapist Directories: \n Websites like Psychology Today (https://www.psychologytoday.com/) and TherapyDen (https://www.therapyden.com/) allow you to search for therapists in your area, filtering by insurance, specialization, and other preferences.",
    "Support Groups: \nJoining a support group, either in-person or online, can provide a sense of community and understanding from others who may be experiencing similar struggles.", 
    "Online Therapy Platforms:\n Websites like BetterHelp (https://www.betterhelp.com/) and Talkspace (https://www.talkspace.com/) offer online therapy with licensed professionals. You can message your therapist anytime and have video or phone sessions based on your convenience.",
    "Emergency Services: \nIf you are in immediate danger or experiencing a mental health crisis, please seek help from emergency services or go to the nearest emergency room."
]

st.title("Speak to our chatbot, Moodie")

emotion = st.text_input(label="How are you feeling?", max_chars=10)

if emotion:
    scale = st.selectbox("On a scale of 1-10, to what extent do you feel so?", range(0, 11))
    if (emotion in sad_list) and scale in [1, 2, 3, 4]:
        activity = random.sample(sad_activities[:13], 5)
        for x in activity:
            st.write("- " + x)
    elif (emotion in sad_list) and scale in [5, 6, 7]:
        activity = random.sample(sad_activities[12:22], 5)
        for x in activity: 
            st.write("- " + x)
    elif (emotion in sad_list) and scale in [8,9]:
        activity = random.sample(sad_activities[22:27], 5)
        for x in activity: 
            st.write("- " + x)
    elif (emotion in sad_list) and scale == 10:
        activity = random.sample(sad_activities[-5:], 5)
        for x in activity: 
            st.write("- " + x)
    elif (emotion.lower() == "depressed" or emotion == "Depressed") and scale > 0:
        activity = random.sample(sad_activities[-5:], 5)
        for x in activity: 
            st.write("- " + x)
    elif scale == 0:
        st.subheader("How Moodie 1.0 works")
        st.write("1. Begin by sharing how you're feeling along with the intensity level, rated from 1 to 10. A higher number indicates a stronger emotional state.")
        st.write("2. Moodie will generate a list of activities tailored to your emotional state.") 
        st.write("3. Use these suggestions as inspiration for how to navigate your current emotional state. Each recommendation is intended to help you find moments of joy, peace, and relaxation.")
        st.write("By providing relevant activities, Moodie aims to encourage you to take steps towards improving your well-being. Feel free to explore the suggestions provided by Moodie and discover new ways to care for yourself.")
    else:
        response = lch.generate_result(emotion, scale)
        response_text = response.get('text', '')  # Extracting the 'text' value from the dictionary
        response_lines = [line.strip() for line in response_text.split('\n') if line.strip()]  # Splitting the text into lines and removing empty lines
        response_bullets = response_lines[:5]  # Taking the first 5 non-empty lines
        for bullet in response_bullets:
            st.write(" " + bullet)
else:
    st.subheader("How Moodie 1.0 works")
    st.write("1. Begin by sharing how you're feeling along with the intensity level, rated from 1 to 10. A higher number indicates a stronger emotional state.")
    st.write("2. Moodie will generate a list of activities tailored to your emotional state.") 
    st.write("3. Use these suggestions as inspiration for how to navigate your current emotional state. Each recommendation is intended to help you find moments of joy, peace, and relaxation.")
    st.write("By providing relevant activities, Moodie aims to encourage you to take steps towards improving your well-being. Feel free to explore the suggestions provided by Moodie and discover new ways to care for yourself.")

