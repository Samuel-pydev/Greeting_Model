# Dataset of grettings and non grettings

sentences = [
    # 100 greetings (label = 1)
    "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "Howdy", "Greetings",
    "What’s up", "How are you", "How’s it going", "Nice to meet you", "Pleasure to meet you",
    "Long time no see", "Hey there", "Hiya", "Yo", "Sup", "Welcome", "Good to see you",
    "How have you been", "How do you do", "Warm greetings", "Salutations", "Peace", "Hello friend",
    "Hi everyone", "Hey buddy", "Good day", "Top of the morning", "Lovely to see you", "Hey folks",
    "Hi there", "How’s everything", "Great to see you", "Morning", "Evening", "Afternoon",
    "Hey you", "Hi friend", "What's up",

    "Hello there", "Hi buddy", "Hey friend", "Good to meet you", "Nice seeing you", "Glad to see you",
    "Hey everyone", "Hi folks", "Hello everyone", "Hey mate", "Hi mate", "Hey pal", "Hi pal",
    "Greetings friend", "Warm hello", "A warm welcome", "Hey champ", "Hi champ", "Hello dear",
    "Hi dear", "Hey dear", "Hi all", "Hello all", "Hey all", "Good to have you here",
    "Nice to see you again", "Great seeing you", "Hi again", "Hello again", "Hey again",
    "Hey stranger", "Hi stranger", "Hello stranger", "Howdy partner", "Greetings everyone",
    
    

    # 100 non-greetings (label = 0)
    "table", "mountain", "engine", "notebook", "galaxy", "pepper", "ocean", "ladder", "cloud",
    "hammer", "forest", "keyboard", "diamond", "pillow", "river", "compass", "bicycle",
    "curtain", "volcano", "mirror", "lantern", "suitcase", "candle", "desert", "camera",
    "jacket", "satellite", "bottle", "painting", "thunder", "bridge", "feather", "wallet",
    "island", "clock", "shovel", "rocket", "marble", "tunnel", "umbrella",

    "phone", "tablet", "charger", "speaker", "microphone", "headphones", "monitor", "printer",
    "router", "modem", "cable", "switch", "server", "database", "algorithm", "function",
    "variable", "loop", "array", "string", "integer", "boolean", "object", "class", "method",
    "compile", "execute", "debug", "deploy", "commit", "branch", "merge", "repository",
    "framework", "library", "package", "module", "script", "terminal", "console",

    "apple", "banana", "orange", "grape", "mango", "pineapple", "strawberry", "blueberry",
    "watermelon", "kiwi", "peach", "pear", "plum", "cherry", "apricot", "coconut",
    "car", "bus", "train", "airplane", "bicycle ride", "motorcycle", "truck",
    "road", "highway", "traffic", "signal", "engine oil", "fuel tank", "brake",
    "school", "teacher", "student", "classroom", "homework", "exam", "lesson",
    "book", "pen", "pencil", "eraser", "desk", "chair", "board"
]

# labels
labels = [1]*100 + [0]*100