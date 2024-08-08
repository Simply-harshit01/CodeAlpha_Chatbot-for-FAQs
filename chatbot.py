import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def setup_nltk():
    nltk.download('punkt')
    nltk.download('stopwords')

# Preprocessing with NLTK
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

# Entity Recognition and Dependency Parsing with SpaCy
nlp = spacy.load('en_core_web_sm')

def analyze_text(text):
    doc = nlp(text)
    for entity in doc.ents:
        print(f"Entity: {entity.text}, Label: {entity.label_}")

    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Dependency: {token.dep_}")

# Define FAQs and Use Cosine Similarity for Matching
faqs = [
    {"question": "What are some common mental health issues among youth?", "answer": "Common issues include anxiety, depression, and stress."},
    {"question": "How can I manage academic stress?", "answer": "Try setting realistic goals and taking regular breaks."},
{"question": "What is mental health?", "answer": "Mental health refers to our emotional, psychological, and social well-being, affecting how we think, feel, and act."},

{"question": "Why is mental health important for young people?", "answer": "Good mental health is crucial for young people as it affects their development, relationships, academic performance, and overall quality of life."},

{"question": "What are common mental health issues faced by young people?", "answer": "Common mental health issues include anxiety, depression, ADHD, eating disorders, and substance abuse."},

{"question": "How can I tell if I or someone else is experiencing a mental health problem?", "answer": "Signs of mental health problems can include persistent sadness, withdrawal from activities, changes in eating or sleeping habits, and difficulty concentrating."},

{"question": "What causes mental health issues in young people?", "answer": "Factors can include genetics, brain chemistry, trauma, life experiences, and family history of mental health issues."},

{"question": "How does social media affect mental health?", "answer": "Social media can impact mental health positively by providing community and support, but it can also cause stress, anxiety, and low self-esteem due to comparison and cyberbullying."},

{"question": "What is anxiety?", "answer": "Anxiety is a feeling of worry or fear that is strong enough to interfere with one's daily activities."},

{"question": "How can I manage anxiety?", "answer": "Techniques such as deep breathing, mindfulness, regular exercise, and talking to a counselor can help manage anxiety."},

{"question": "What is depression?", "answer": "Depression is a mood disorder characterized by persistent sadness, loss of interest in activities, and various physical and emotional problems."},

{"question": "How can I help a friend who is depressed?", "answer": "Listen without judgment, offer support, encourage them to seek professional help, and check in regularly."},

{"question": "What is stress?", "answer": "Stress is the body's reaction to any change that requires an adjustment or response, which can be physical, mental, or emotional."},
{"question": "How can I reduce stress?", "answer": "Practice relaxation techniques, stay organized, set realistic goals, and make time for hobbies and activities you enjoy."},

{"question": "What is ADHD?", "answer": "Attention-Deficit/Hyperactivity Disorder (ADHD) is a condition marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development."},

{"question": "How is ADHD treated?", "answer": "ADHD can be treated with behavioral therapy, medication, or a combination of both, depending on individual needs."},

{"question": "What are eating disorders?", "answer": "Eating disorders are serious mental health conditions involving abnormal eating habits that negatively affect a person's physical and mental health."},

{"question": "How can I support someone with an eating disorder?", "answer": "Encourage them to seek professional help, offer emotional support, and avoid commenting on their appearance or eating habits."},

{"question": "What is self-harm?", "answer": "Self-harm refers to intentionally causing harm to oneself as a way to cope with emotional pain, anger, or frustration."},

{"question": "What should I do if I know someone who is self-harming?", "answer": "Encourage them to talk to a trusted adult or mental health professional and offer your support without judgment."},

{"question": "How can I improve my self-esteem?", "answer": "Focus on your strengths, practice self-compassion, set achievable goals, and surround yourself with supportive people."},

{"question": "What is mindfulness?", "answer": "Mindfulness is the practice of being present and fully engaged in the moment without judgment, often used to reduce stress and improve mental health."},

{"question": "How can I practice mindfulness?", "answer": "You can practice mindfulness through meditation, deep breathing exercises, and focusing on the present moment in daily activities."},

{"question": "What is resilience?", "answer": "Resilience is the ability to adapt and recover from adversity, trauma, or stress."},
{"question": "How can I build resilience?", "answer": "Building resilience involves developing a strong support network, maintaining a positive outlook, and learning from experiences."},

{"question": "What is the role of exercise in mental health?", "answer": "Regular exercise can boost mood, reduce stress and anxiety, and improve overall mental health."},

{"question": "What are some relaxation techniques?", "answer": "Relaxation techniques include deep breathing, progressive muscle relaxation, guided imagery, and yoga."},

{"question": "How can sleep affect mental health?", "answer": "Poor sleep can contribute to mental health issues like anxiety and depression, while good sleep supports emotional and psychological well-being."},

{"question": "How can I improve my sleep hygiene?", "answer": "Maintain a regular sleep schedule, create a comfortable sleep environment, limit screen time before bed, and avoid caffeine in the evening."},

{"question": "What is cognitive-behavioral therapy (CBT)?", "answer": "CBT is a type of psychotherapy that helps people identify and change negative thought patterns and behaviors."},

{"question": "How can I access mental health services?", "answer": "You can access mental health services through school counselors, community health centers, or by contacting mental health professionals directly."},

{"question": "What is the role of family in supporting mental health?", "answer": "Family can provide emotional support, encouragement, and a sense of stability, which are important for mental health."},

{"question": "How can I talk to my parents about my mental health?", "answer": "Choose a good time, be honest about your feelings, and ask for their support in finding help if needed."},

{"question": "What is peer pressure?", "answer": "Peer pressure is the influence exerted by a peer group to encourage someone to change their attitudes, values, or behaviors to conform to group norms."},

{"question": "How can I resist peer pressure?", "answer": "Trust your instincts, practice saying no, surround yourself with supportive friends, and make decisions based on your values."},

{"question": "What is social anxiety?", "answer": "Social anxiety is the fear of being judged or negatively evaluated in social situations, leading to avoidance and distress."},

{"question": "How can I cope with social anxiety?", "answer": "Gradually face social situations, practice deep breathing, challenge negative thoughts, and seek support from a therapist if needed."},

{"question": "What is the impact of bullying on mental health?", "answer": "Bullying can lead to anxiety, depression, low self-esteem, and even suicidal thoughts."},

{"question": "What should I do if I am being bullied?", "answer": "Speak to a trusted adult, keep a record of incidents, and seek support from friends, family, or a counselor."},

{"question": "How does substance abuse affect mental health?", "answer": "Substance abuse can lead to addiction, worsen mental health conditions, and increase the risk of developing new mental health issues."},

{"question": "How can I help a friend with substance abuse issues?", "answer": "Express your concern, encourage them to seek professional help, and offer your support throughout their recovery."},

{"question": "What is the importance of a healthy diet for mental health?", "answer": "A balanced diet can improve mood, increase energy levels, and support brain function, contributing to better mental health."},

{"question": "How can I maintain a balanced diet?", "answer": "Eat a variety of foods, including fruits, vegetables, lean proteins, and whole grains, and limit processed foods and sugars."},

{"question": "What is the impact of loneliness on mental health?", "answer": "Loneliness can lead to depression, anxiety, and a decrease in overall well-being."},

{"question": "How can I combat loneliness?", "answer": "Reach out to friends and family, join clubs or groups with similar interests, and engage in community activities."},

{"question": "What is the role of hobbies in mental health?", "answer": "Hobbies provide a sense of purpose, reduce stress, and improve overall mental well-being by allowing creative expression and relaxation."},

{"question": "How can I find a hobby that interests me?", "answer": "Explore different activities, such as art, sports, music, or volunteering, and see what brings you joy and fulfillment."},

{"question": "What is the connection between mental health and academic performance?", "answer": "Poor mental health can negatively impact concentration, motivation, and performance in school, while good mental health supports academic success."},

{"question": "How can I manage academic stress?", "answer": "Prioritize tasks, set realistic goals, take breaks, and seek support from teachers or counselors if needed."},

{"question": "What is PTSD?", "answer": "Post-Traumatic Stress Disorder (PTSD) is a mental health condition triggered by experiencing or witnessing a traumatic event, leading to symptoms such as flashbacks and anxiety."},

{"question": "How is PTSD treated?", "answer": "PTSD can be treated with therapy, medication, or a combination of both, often involving techniques like cognitive-behavioral therapy or EMDR."},

{"question": "What is bipolar disorder?", "answer": "Bipolar disorder is a mental health condition characterized by extreme mood swings, including emotional highs (mania) and lows (depression)."},

{"question": "How is bipolar disorder managed?", "answer": "Bipolar disorder is managed with medication, therapy, lifestyle changes, and regular monitoring by a healthcare professional."},

{"question": "What are panic attacks?", "answer": "Panic attacks are sudden episodes of intense fear or discomfort that peak within minutes, accompanied by physical symptoms like a racing heart and shortness of breath."},

{"question": "How can I cope with panic attacks?", "answer": "Practice deep breathing, use grounding techniques, and seek professional help if panic attacks are frequent."},

{"question": "What is OCD?", "answer": "Obsessive-Compulsive Disorder (OCD) is a mental health condition characterized by unwanted, intrusive thoughts (obsessions) and repetitive behaviors (compulsions)."},

{"question": "How is OCD treated?", "answer": "OCD is treated with therapy, particularly cognitive-behavioral therapy, and sometimes medication."},
{"question": "What is the impact of family dynamics on mental health?", "answer": "Positive family dynamics can provide support and stability, while negative dynamics can contribute to stress and mental health issues."},

{"question": "How can I improve family relationships?", "answer": "Communicate openly, practice empathy, set boundaries, and seek family therapy if needed."},

{"question": "What is grief?", "answer": "Grief is the emotional response to loss, which can involve feelings of sadness, anger, and confusion."},

{"question": "How can I cope with grief?", "answer": "Allow yourself to feel emotions, seek support from loved ones, and consider talking to a counselor or joining a support group."},

{"question": "What is self-care?", "answer": "Self-care involves taking actions to preserve or improve one's physical, mental, and emotional health."},

{"question": "How can I practice self-care?", "answer": "Make time for activities you enjoy, prioritize rest and relaxation, and maintain a balanced lifestyle."},

{"question": "What is emotional intelligence?", "answer": "Emotional intelligence is the ability to understand, manage, and express emotions effectively, both personally and in relationships."},

{"question": "How can I improve my emotional intelligence?", "answer": "Practice self-awareness, empathy, and effective communication, and seek feedback from others."},

{"question": "What is the importance of communication in mental health?", "answer": "Effective communication can help express feelings, resolve conflicts, and build supportive relationships, contributing to better mental health."},

{"question": "How can I improve my communication skills?", "answer": "Listen actively, express yourself clearly, practice empathy, and be open to feedback."},

{"question": "What is the role of humor in mental health?", "answer": "Humor can reduce stress, improve mood, and enhance relationships, contributing to better mental health."},

{"question": "How can I incorporate humor into my life?", "answer": "Spend time with funny friends, watch comedy shows, and try to find humor in everyday situations."},

{"question": "What is seasonal affective disorder (SAD)?", "answer": "SAD is a type of depression that occurs at a specific time of year, usually in winter, due to changes in light exposure."},
{"question": "How is SAD treated?", "answer": "SAD can be treated with light therapy, medication, and lifestyle changes like exercise and exposure to natural light."},

{"question": "What is the importance of creativity in mental health?", "answer": "Engaging in creative activities can reduce stress, boost mood, and provide an outlet for self-expression."},

{"question": "How can I explore my creativity?", "answer": "Try activities like painting, writing, music, or dance, and allow yourself to experiment without judgment."},

{"question": "What is the impact of trauma on mental health?", "answer": "Trauma can lead to long-term mental health issues like PTSD, anxiety, and depression, affecting a person's well-being."},

{"question": "How can I heal from trauma?", "answer": "Seek professional support, practice self-care, and consider therapies like EMDR or trauma-focused cognitive-behavioral therapy."},

{"question": "What is the role of nature in mental health?", "answer": "Spending time in nature can reduce stress, improve mood, and enhance overall mental well-being."},

{"question": "How can I incorporate nature into my life?", "answer": "Take walks outside, spend time in parks or gardens, and engage in outdoor activities like hiking or cycling."},
{"question": "What is the importance of setting boundaries?", "answer": "Setting boundaries helps protect your mental health, maintain healthy relationships, and prevent burnout."},

{"question": "How can I set healthy boundaries?", "answer": "Communicate your needs clearly, say no when necessary, and prioritize self-care."},

{"question": "What is the role of spirituality in mental health?", "answer": "Spirituality can provide a sense of purpose, community, and comfort, contributing to overall mental well-being."},

{"question": "How can I explore my spirituality?", "answer": "Engage in practices like meditation, prayer, or reflection, and seek communities that align with your beliefs."},

{"question": "What is the impact of perfectionism on mental health?", "answer": "Perfectionism can lead to stress, anxiety, and low self-esteem, negatively affecting mental health."},

{"question": "How can I overcome perfectionism?", "answer": "Set realistic goals, practice self-compassion, and focus on progress rather than perfection."},

{"question": "What is the role of humor in coping with difficult situations?", "answer": "Humor can provide perspective, reduce tension, and foster resilience when facing challenges."},

{"question": "How can I find humor in difficult situations?", "answer": "Look for the lighter side, share funny experiences with others, and practice finding joy in everyday moments."},

{"question": "What is the impact of technology on mental health?", "answer": "Technology can offer support and resources but can also lead to stress and social isolation if overused."},

{"question": "How can I balance technology use and mental health?", "answer": "Set boundaries for screen time, prioritize in-person interactions, and engage in offline activities."},

{"question": "What is the role of gratitude in mental health?", "answer": "Practicing gratitude can improve mood, increase resilience, and enhance overall well-being."},

{"question": "How can I practice gratitude?", "answer": "Keep a gratitude journal, express appreciation to others, and focus on positive aspects of your life."},

{"question": "What is the impact of body image on mental health?", "answer": "Negative body image can lead to low self-esteem, eating disorders, and depression."},

{"question": "How can I improve my body image?", "answer": "Focus on health rather than appearance, practice self-compassion, and avoid comparing yourself to others."},

{"question": "What is the importance of laughter in mental health?", "answer": "Laughter can reduce stress, boost mood, and strengthen social connections, contributing to better mental health."},

{"question": "How can I bring more laughter into my life?", "answer": "Watch comedy shows, spend time with funny friends, and try to find humor in everyday situations."},

{"question": "What is the impact of music on mental health?", "answer": "Music can elevate mood, reduce stress, and provide an outlet for emotional expression."},

{"question": "How can I use music for mental health?", "answer": "Create playlists that match your mood, play an instrument, or attend live music events."},

{"question": "What is the role of community in mental health?", "answer": "Being part of a supportive community can provide a sense of belonging, reduce isolation, and improve mental health."},

{"question": "How can I find a supportive community?", "answer": "Join groups or clubs with shared interests, volunteer, and seek connections in your local area."},

{"question": "What is the importance of play in mental health?", "answer": "Engaging in playful activities can reduce stress, improve creativity, and enhance overall well-being."},

{"question": "How can I incorporate play into my life?", "answer": "Set aside time for fun activities, try new games, and allow yourself to be spontaneous."},

{"question": "What is the impact of meditation on mental health?", "answer": "Meditation can reduce stress, improve focus, and increase emotional resilience."},

{"question": "How can I start meditating?", "answer": "Begin with short sessions, use guided meditations, and find a quiet space to practice regularly."},

{"question": "What is the role of kindness in mental health?", "answer": "Acts of kindness can boost mood, reduce stress, and enhance social connections, benefiting mental health."}
    # Add more FAQs as needed
]

def get_response(user_query):
    questions = [faq['question'] for faq in faqs]
    tfidf_vectorizer = TfidfVectorizer().fit_transform(questions + [user_query])
    cosine_similarities = cosine_similarity(tfidf_vectorizer[-1], tfidf_vectorizer[:-1]).flatten()
    closest_question_idx = cosine_similarities.argmax()
    return faqs[closest_question_idx]['answer']

# Main Chatbot Interface
if __name__ == "__main__":
    setup_nltk()  # Ensure NLTK data is downloaded
    print("Chatbot: Hello! Ask me anything about mental health.")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_query)
        print(f"Chatbot: {response}")
