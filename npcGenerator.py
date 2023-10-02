import os
import random

# Define some names and personality traits
firstNames = [
    "Alice", "Bob", "Catherine", "David", "Eleanor", "Frank", "Grace", "Henry", "Isabella", "Jack",
    "Katherine", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rebecca", "Samuel", "Tiffany",
    "Ulysses", "Vera", "William", "Xander", "Yasmine", "Zachary", "Ava", "Benjamin", "Charlotte", "Daniel",
    "Emma", "Felix", "Gabriella", "Hannah", "Isaac", "Joseph", "Kaitlyn", "Lucas", "Madison", "Natalie",
    "Oliver", "Penelope", "Quincy", "Rachel", "Sophia", "Thomas", "Uma", "Vincent", "Wendy", "Xavier",
    "Yara", "Zoe", "Arthur", "Brianna", "Caleb", "Diana", "Ella", "Finn", "Gemma", "Harper",
    "Ian", "Julia", "Kaden", "Lily", "Mason", "Nora", "Oscar", "Piper", "Quinn", "Ruby",
    "Seth", "Tessa", "Ulysses", "Violet", "Wesley", "Xander", "Yasmine", "Zachary", "Amelia", "Benjamin",
    "Chloe", "Daniel", "Emily", "Finn", "Grace", "Hannah", "Isaac", "Jacob", "Katherine", "Liam",
    "Mia", "Natalie", "Oliver", "Penelope", "Quincy", "Rachel", "Sophia", "Thomas", "Uma", "Vincent",
    "Wendy", "Xavier", "Yara", "Zoe", "Alice", "Bennett", "Clara", "Dexter", "Ella", "Fiona",
    "George", "Hazel", "Isaiah", "Josie", "Kai", "Lila", "Max", "Nora", "Olive", "Peter",
    "Quinn", "Riley", "Sam", "Tessa", "Ulysses", "Vera", "William", "Xander", "Yasmine", "Zachary",
    "Aria", "Beckett", "Cora", "Dylan", "Elena", "Finn", "Georgia", "Hudson", "Ivy", "Jasper",
    "Kylie", "Liam", "Mila", "Nathan", "Olivia", "Parker", "Quinn", "Rebecca", "Samuel", "Tiffany",
    "Ulysses", "Vera", "William", "Xander", "Yasmine", "Zachary"
]
middleNames = [
    "Alexander", "Belle", "Carter", "Daisy", "Elias", "Faith", "George", "Hope", "Isaac", "Jane",
    "Kai", "Lily", "Mason", "Nora", "Oliver", "Penny", "Quinn", "Rose", "Samuel", "Theodore",
    "Ulysses", "Violet", "William", "Xavier", "Yara", "Zane", "Amelia", "Benjamin", "Cora", "Dylan",
    "Ella", "Finn", "Grace", "Henry", "Ivy", "James", "Katherine", "Liam", "Mia", "Nathan",
    "Olivia", "Paul", "Quinn", "Rebecca", "Samuel", "Tiffany", "Ulysses", "Vera", "William", "Xander",
    "Yasmine", "Zachary", "Ava", "Blake", "Catherine", "David", "Eleanor", "Felix", "Gemma", "Henry",
    "Isabella", "Jack", "Katherine", "Liam", "Mia", "Nora", "Oliver", "Penelope", "Quincy", "Rachel",
    "Sophia", "Thomas", "Uma", "Vincent", "Wendy", "Xavier", "Yara", "Zoe", "Arthur", "Brianna",
    "Caleb", "Diana", "Ella", "Finn", "Gemma", "Harper", "Isaiah", "Julia", "Kaden", "Lily",
    "Mason", "Nora", "Oscar", "Piper", "Quinn", "Ruby", "Seth", "Tessa", "Ulysses", "Violet",
    "Wesley", "Xander", "Yasmine", "Zachary", "Amelia", "Bennett", "Clara", "Dexter", "Ella", "Fiona",
    "George", "Hazel", "Isaiah", "Josie", "Kai", "Lila", "Max", "Nora", "Olive", "Peter",
    "Quinn", "Riley", "Sam", "Tessa", "Ulysses", "Vera", "William", "Xander", "Yasmine", "Zachary",
    "Aria", "Beckett", "Cora", "Dylan", "Elena", "Finn", "Georgia", "Hudson", "Ivy", "Jasper",
    "Kylie", "Liam", "Mila", "Nathan", "Olivia", "Parker", "Quinn", "Rebecca", "Samuel", "Tiffany",
    "Ulysses", "Vera", "William", "Xander", "Yasmine", "Zachary"
]
lastNames = [
    "Anderson", "Brown", "Clark", "Davis", "Evans", "Foster", "Garcia", "Harris", "Jackson", "Kim",
    "Lee", "Martinez", "Nguyen", "O'Connor", "Patel", "Roberts", "Smith", "Taylor", "Wilson", "Zhang",
    "Adams", "Baker", "Carter", "Diaz", "Edwards", "Flores", "Gonzalez", "Hernandez", "Johnson", "King",
    "Lopez", "Miller", "Nelson", "Ortiz", "Perez", "Rodriguez", "Sanchez", "Thomas", "Walker", "Young",
    "Adams", "Allen", "Baker", "Campbell", "Cooper", "Davis", "Edwards", "Fisher", "Gonzales", "Harris",
    "Jackson", "Johnson", "King", "Lewis", "Martin", "Mitchell", "Parker", "Roberts", "Smith", "Taylor",
    "Wilson", "Young", "Bennett", "Brown", "Carter", "Clark", "Davis", "Evans", "Foster", "Garcia",
    "Harrison", "Hernandez", "James", "Jones", "Kim", "Lee", "Martinez", "Nelson", "O'Connor", "Patel",
    "Quinn", "Reed", "Sanchez", "Taylor", "Upton", "Vargas", "Williams", "Xu", "Young", "Zhang",
    "Allen", "Anderson", "Baker", "Carter", "Davis", "Evans", "Foster", "Gonzalez", "Harris", "Jackson",
    "Kim", "Lee", "Martinez", "Nelson", "O'Connor", "Patel", "Roberts", "Smith", "Taylor", "Wilson",
    "Zhang", "Adams", "Brown", "Clark", "Davis", "Evans", "Foster", "Garcia", "Harris", "Jackson",
    "Kim", "Lee", "Martinez", "Nguyen", "O'Connor", "Patel", "Roberts", "Smith", "Taylor", "Wilson",
    "Zhang", "Adams", "Baker", "Carter", "Diaz", "Edwards", "Flores", "Gonzalez", "Hernandez", "Johnson",
    "King", "Lopez", "Miller", "Nelson", "Ortiz", "Perez", "Rodriguez", "Sanchez", "Thomas", "Walker",
    "Young", "Adams", "Allen", "Baker", "Campbell", "Cooper", "Davis", "Edwards", "Fisher", "Gonzales",
    "Harris", "Jackson", "Johnson", "King", "Lewis", "Martin", "Mitchell", "Parker", "Roberts", "Smith",
    "Taylor", "Wilson", "Young", "Bennett", "Brown", "Carter", "Clark", "Davis", "Evans", "Foster",
    "Garcia", "Harrison", "Hernandez", "James", "Jones", "Kim", "Lee", "Martinez", "Nelson", "O'Connor",
    "Patel", "Quinn", "Reed", "Sanchez", "Taylor", "Upton", "Vargas", "Williams", "Xu", "Young",
    "Zhang"
]
personalities = [
    "Adventurous", "Agreeable", "Ambitious", "Analytical", "Artistic", "Assertive", "Attentive", "Authentic", "Calm", "Charismatic",
    "Charming", "Cheerful", "Clever", "Compassionate", "Confident", "Cooperative", "Courageous", "Creative", "Curious", "Dedicated",
    "Dependable", "Determined", "Diplomatic", "Disciplined", "Easygoing", "Energetic", "Enthusiastic", "Flexible", "Friendly", "Generous",
    "Gentle", "Graceful", "Grateful", "Hardworking", "Honest", "Humorous", "Imaginative", "Independent", "Innovative", "Intelligent",
    "Intuitive", "Kind", "Loyal", "Modest", "Optimistic", "Organized", "Passionate", "Patient", "Persistent", "Playful",
    "Polite", "Practical", "Proactive", "Reliable", "Resilient", "Resourceful", "Sincere", "Sociable", "Spontaneous", "Studious",
    "Sympathetic", "Talented", "Thoughtful", "Trustworthy", "Understanding", "Versatile", "Warmhearted", "Witty", "Youthful", "Zestful",
    "Adaptable", "Adventurous", "Affectionate", "Ambitious", "Amiable", "Analytical", "Artistic", "Assertive", "Attentive", "Authentic",
    "Brave", "Calm", "Capable", "Caring", "Charismatic", "Charming", "Cheerful", "Clever", "Compassionate", "Confident",
    "Cooperative", "Courageous", "Creative", "Curious", "Daring", "Dependable", "Determined", "Diplomatic", "Disciplined", "Easygoing",
    "Energetic", "Enthusiastic", "Flexible", "Friendly", "Generous", "Gentle", "Grateful", "Hardworking", "Helpful", "Honest",
    "Humble", "Imaginative", "Independent", "Innovative", "Intelligent", "Intuitive", "Joyful", "Kind", "Loyal", "Modest",
    "Optimistic", "Passionate", "Patient", "Persistent", "Playful", "Polite", "Practical", "Proactive", "Reliable", "Resilient",
    "Resourceful", "Sincere", "Sociable", "Spontaneous", "Studious", "Sympathetic", "Talented", "Thoughtful", "Trustworthy", "Understanding",
    "Versatile", "Warmhearted", "Witty", "Youthful", "Zestful", "Adaptable", "Adventurous", "Affectionate", "Ambitious", "Amiable",
    "Analytical", "Artistic", "Assertive", "Attentive", "Authentic", "Brave", "Calm", "Capable", "Caring", "Charismatic",
    "Charming", "Cheerful", "Clever", "Compassionate", "Confident", "Cooperative", "Courageous", "Creative", "Curious", "Daring",
    "Dependable", "Determined", "Diplomatic", "Disciplined", "Easygoing", "Energetic", "Enthusiastic", "Flexible", "Friendly", "Generous",
    "Gentle", "Grateful", "Hardworking", "Helpful", "Honest", "Humble", "Imaginative", "Independent", "Innovative", "Intelligent",
    "Intuitive", "Joyful", "Kind", "Loyal", "Modest", "Optimistic", "Passionate", "Patient", "Persistent", "Playful",
    "Polite", "Practical", "Proactive", "Reliable", "Resilient", "Resourceful", "Sincere", "Sociable", "Spontaneous", "Studious",
    "Sympathetic", "Talented", "Thoughtful", "Trustworthy", "Understanding", "Versatile", "Warmhearted", "Witty", "Youthful", "Zestful"
]

# Define life events for different age ranges
lifeEvents = {
    0: [
    "Birth", "Learning to walk", "Learning to talk", "First tooth", "First birthday", "First haircut", "First words", "Starting daycare", "First steps", "Learning to feed themselves",
    "First playdate", "First trip to the zoo", "First time riding a bike", "First visit to the dentist", "Starting preschool", "First day of school", "Learning to read", "First pet", "Losing a baby tooth", "Learning to tie shoelaces",
    "Making their first friend", "First time swimming", "First family vacation", "First time camping", "Learning to ride a scooter", "First time playing a sport", "First time going to a theme park", "Learning to use the potty", "Starting kindergarten", "First time going to the movies",
    "First school performance", "First sleepover at a friend's house", "First visit from the Tooth Fairy", "Learning to ride a skateboard", "First science project", "First time losing something important", "First time going to a museum", "Learning to share", "Starting first grade", "First time making a sandcastle",
    "First dance recital", "First time learning to tell time", "First trip to the beach", "Learning to write their name", "First time going to a birthday party", "Starting second grade", "First time cooking with a parent", "First time visiting a farm", "Learning to ride a roller coaster", "First school field trip"
    ],
    10: [
    "Starting middle school", "First crush", "First part-time job", "First school dance", "Getting braces", "First school trip without parents", "First time using public transportation", "First cellphone", "Starting high school", "First romantic relationship",
    "First school sports team", "First time volunteering", "First time staying home alone", "First driver's permit", "First time going to a concert", "First job interview", "First time traveling abroad", "First major school project", "First school dance", "First date",
    "First car", "First heartbreak", "First school play or musical", "First time voting", "First time doing community service", "First big test or exam", "First time getting grounded", "First time getting a part-time job", "First time going to a music festival", "First time traveling with friends",
    "First serious relationship", "First time living away from home (e.g., college)", "First time getting a credit card", "First time moving to a new city", "First time experiencing a major life milestone (e.g., graduation)", "First time dealing with a significant loss", "First time managing finances independently", "First time dealing with a major health issue", "First time starting a long-term project or career", "First time learning to cook for themselves",
    "First time buying a car or property", "First time experiencing a natural disaster", "First time making a major life decision (e.g., choosing a career path)", "First time experiencing a major cultural event or festival", "First time becoming a mentor or role model", "First time traveling internationally on their own", "First time starting a family (e.g., getting married or having children)", "First time becoming financially independent", "First time facing a significant personal challenge or adversity", "First time achieving a long-term goal"
    ],
    20: [
    "Completing college education", "Starting first job", "Moving out of parents' home", "First serious relationship", "First apartment", "Traveling abroad for an extended period", "Getting engaged", "Starting graduate school", "Living in a different city or country", "First significant career advancement",
    "Getting married", "Becoming financially independent", "First time buying a house or property", "Starting a family (e.g., having children)", "Achieving career goals", "First major international trip", "Changing careers", "Experiencing personal growth and self-discovery", "Navigating long-term relationships", "Investing in retirement savings",
    "Exploring entrepreneurship", "Adopting a pet", "Graduating from professional or trade school", "Moving in with a partner", "Becoming an aunt or uncle", "Buying a car", "Experiencing a life-changing trip", "Volunteering for a cause", "Attending a life-changing seminar or workshop", "Starting a blog or personal project",
    "Navigating long-distance relationships", "Creating a financial plan", "Taking on a leadership role at work", "Starting a new hobby or interest", "Experiencing a personal transformation", "Becoming a mentor to others", "Learning a new language", "Meeting lifelong friends", "Discovering a passion for a new sport or activity", "Purchasing a valuable possession or collectible",
    "Experiencing a major cultural event or festival", "Becoming a godparent", "Overcoming a significant challenge or obstacle", "Adopting a healthy lifestyle", "Celebrating personal achievements and milestones", "Participating in a meaningful volunteer project", "Attending a life-changing concert or event", "Rekindling old friendships", "Experiencing a breakthrough in personal or professional life", "Achieving a significant personal goal"
    ],
    30: [
    "Celebrating milestone birthdays", "Raising children through their early years", "Buying a larger home", "Reaching career milestones", "Celebrating wedding anniversaries", "Becoming a parent to teenagers", "Children leaving for college", "Starting a new business venture", "Reconnecting with personal interests and hobbies", "Caring for aging parents",
    "Experiencing mid-life crisis", "Reevaluating life goals and priorities", "Traveling more for leisure", "Getting involved in community or charity work", "Experiencing major life changes (e.g., divorce)", "Purchasing a family vehicle", "Managing family finances", "Transitioning into leadership roles at work", "Planning for retirement", "Experiencing health-related challenges",
    "Investing in long-term financial stability", "Becoming a soccer parent", "Taking family vacations", "Becoming a scout leader", "Starting a significant home improvement project", "Buying a vacation property", "Caring for elderly relatives", "Getting involved in local politics", "Starting a new hobby or craft", "Celebrating a decade of marriage",
    "Navigating career changes", "Experiencing personal growth through therapy or self-help", "Getting involved in school PTA", "Experiencing a significant family reunion", "Starting a new chapter after a major life event", "Planning for children's college education", "Pursuing a lifelong dream or passion project", "Experiencing a significant personal achievement", "Starting a family tradition", "Achieving a financial milestone",
    "Supporting children's extracurricular activities", "Exploring new fitness routines", "Celebrating career promotions", "Experiencing significant travel adventures", "Celebrating milestone moments with friends", "Taking on leadership roles in community organizations", "Experiencing significant family celebrations", "Creating a family time capsule", "Experiencing personal breakthroughs", "Reconnecting with extended family"
    ],
    40: [
    "Children reaching adulthood", "Empty nesting", "Reevaluating personal and career goals", "Becoming grandparents", "Planning for retirement", "Celebrating milestone wedding anniversaries", "Exploring new hobbies and interests", "Traveling extensively", "Investing in personal health and fitness", "Navigating aging parents' needs",
    "Experiencing the joys of grandparenthood", "Managing finances for retirement", "Continuing professional growth", "Focusing on personal well-being", "Reconnecting with old friends", "Exploring a new phase of life", "Adjusting to adult children's independence", "Investing in leisure activities", "Preparing for retirement lifestyle", "Reflecting on life's accomplishments",
    "Experiencing career changes or transitions", "Celebrating family reunions", "Pursuing lifelong learning and education", "Taking on new hobbies and passions", "Traveling with adult children", "Experiencing milestone moments with grandchildren", "Exploring travel adventures with friends", "Purchasing a retirement home", "Celebrating children's achievements", "Planning for legacy and inheritance",
    "Reconnecting with nature and outdoor activities", "Attending reunions with schoolmates", "Experiencing the joys of family vacations", "Investing in personal growth and self-discovery", "Experiencing personal health transformations", "Celebrating children's weddings", "Embracing a slower pace of life", "Exploring creative pursuits and artistic endeavors", "Taking on volunteer roles in the community", "Continuing to cherish family bonds",
    "Celebrating milestone birthdays with loved ones", "Creating lasting memories with adult children", "Planning for retirement travel adventures", "Experiencing personal achievements and milestones", "Taking on leadership roles in social organizations", "Embracing a sense of fulfillment", "Supporting adult children's career aspirations", "Investing in lifelong friendships", "Celebrating personal passions and hobbies", "Experiencing the joys of retirement leisure"
    ],
    50: [
    "Retirement", "Enjoying leisure activities and travel", "Pursuing lifelong dreams and goals", "Continuing family traditions", "Celebrating milestones with grandchildren", "Investing in personal health and wellness", "Exploring new hobbies and interests", "Spending quality time with family and friends", "Reflecting on life's journey", "Engaging in volunteer and community work",
    "Maintaining financial stability in retirement", "Experiencing the joys of retirement", "Navigating health and medical considerations", "Traveling to new destinations", "Adjusting to an empty nest", "Savoring quiet moments", "Planning for legacy and inheritance", "Embracing a slower pace of life", "Reconnecting with old passions", "Living life to the fullest",
    "Celebrating milestone wedding anniversaries with family", "Continuing to explore personal interests and hobbies", "Enjoying retirement years", "Traveling with loved ones", "Becoming great-grandparents", "Investing in lifelong learning", "Embracing a slower pace of life", "Reconnecting with old friends and memories", "Sharing wisdom and experiences", "Maintaining health and well-being",
    "Enjoying family gatherings and celebrations", "Celebrating long-lasting relationships", "Planning for future generations", "Savoring the joys of grandparenthood", "Embracing the beauty of aging", "Creating lasting memories", "Investing in leisurely pursuits", "Finding contentment in everyday moments", "Continuing to give back to the community", "Living life with gratitude",
    "Reconnecting with extended family for special occasions", "Experiencing the beauty of grandparenthood", "Living life with a sense of purpose", "Celebrating milestones with adult children", "Pursuing artistic and creative passions", "Creating lasting memories with grandchildren", "Savoring the joys of friendship", "Investing in personal wellness and self-care", "Taking on new hobbies and interests", "Continuing to explore the world through travel"
    ],
    60: [
    "Celebrating milestone birthdays", "Continuing to explore hobbies and interests", "Enjoying retirement years", "Traveling with loved ones", "Becoming great-grandparents", "Investing in lifelong learning", "Embracing a slower pace of life", "Reconnecting with old friends and memories", "Sharing wisdom and experiences", "Maintaining health and well-being",
    "Enjoying family gatherings and celebrations", "Celebrating long-lasting relationships", "Planning for future generations", "Savoring the joys of grandparenthood", "Embracing the beauty of aging", "Creating lasting memories", "Investing in leisurely pursuits", "Finding contentment in everyday moments", "Continuing to give back to the community", "Living life with gratitude",
    "Reconnecting with extended family for special occasions", "Experiencing the beauty of grandparenthood", "Living life with a sense of purpose", "Celebrating milestones with adult children", "Pursuing artistic and creative passions", "Creating lasting memories with grandchildren", "Savoring the joys of friendship", "Investing in personal wellness and self-care", "Taking on new hobbies and interests", "Continuing to explore the world through travel",
    "Exploring new cuisines and culinary experiences", "Sharing stories and anecdotes with younger generations", "Participating in intergenerational activities", "Celebrating significant wedding anniversaries with loved ones", "Taking on leadership roles in community organizations", "Creating a family legacy", "Enjoying the beauty of nature and outdoor activities", "Supporting adult children's life journeys", "Experiencing the joys of lifelong friendships", "Traveling to bucket list destinations"
    ],
    70: [
    "Celebrating milestone anniversaries", "Enjoying quality time with family", "Reflecting on a lifetime of experiences", "Sharing wisdom with younger generations", "Continuing to explore personal interests", "Savoring cherished memories", "Embracing retirement with grace", "Investing in well-being and health", "Living a life of contentment", "Finding joy in simple pleasures",
    "Maintaining close relationships", "Celebrating family traditions", "Experiencing the beauty of aging", "Remaining active and engaged in life", "Continuing to learn and grow", "Expressing love and appreciation", "Celebrating the legacy created", "Living life with serenity", "Treasuring moments with loved ones", "Living life to the fullest",
    "Embracing the joys of great-grandparenthood", "Continuing to attend family gatherings and celebrations", "Sharing life lessons and stories", "Supporting adult children's dreams and endeavors", "Engaging in creative pursuits and hobbies", "Creating a family history or memoir", "Living with a sense of gratitude", "Celebrating milestones with extended family", "Investing in lifelong friendships", "Finding happiness in everyday moments",
    "Sharing life's treasures with loved ones", "Living a life filled with laughter", "Savoring the joys of relaxation and leisure", "Experiencing the beauty of generational bonds", "Creating a family scrapbook or photo album", "Living with an attitude of gratitude", "Embracing the beauty of lifelong love", "Celebrating life's blessings", "Taking on mentorship roles for younger generations", "Living life with a sense of fulfillment"
    ],
    80: [
    "Celebrating milestone birthdays", "Enjoying time with great-grandchildren", "Reflecting on a lifetime of accomplishments", "Sharing stories and wisdom", "Embracing the beauty of a long life", "Continuing to cherish family bonds", "Living with grace and gratitude", "Maintaining a sense of purpose", "Investing in health and well-being", "Finding joy in everyday moments",
    "Embracing a slower pace of life", "Remaining active and engaged", "Continuing to learn and grow", "Expressing love and appreciation", "Celebrating the legacy created", "Living life with serenity", "Treasuring the support of loved ones", "Creating lasting memories with family", "Finding fulfillment in simple pleasures", "Leaving a legacy of love and kindness",
    "Sharing life's stories with younger generations", "Celebrating milestone anniversaries with extended family", "Enjoying life's simple pleasures", "Supporting the dreams and aspirations of grandchildren", "Living with an attitude of gratitude", "Embracing the beauty of lifelong friendships", "Living with a sense of contentment", "Sharing life's joys with great-grandchildren", "Investing in lifelong bonds", "Celebrating life's treasures",
    "Embracing the wisdom of age", "Celebrating life's milestones with loved ones", "Continuing to make new memories", "Living a life filled with love", "Expressing gratitude for life's journey", "Treasuring the moments that matter most", "Living life with a sense of peace", "Celebrating a life well-lived", "Leaving a legacy of love and wisdom", "Embracing the beauty of generational love"
    ],
    90: [
    "Celebrating milestone birthdays", "Reflecting on a century of life", "Sharing stories with generations", "Embracing the beauty of a long and fulfilling life", "Living with grace and gratitude", "Maintaining a sense of purpose", "Investing in health and well-being", "Finding joy in everyday moments", "Treasuring the support of loved ones", "Creating lasting memories with family",
    "Finding fulfillment in simple pleasures", "Leaving a legacy of love and kindness", "Sharing life's stories with younger generations", "Celebrating milestone anniversaries with extended family", "Enjoying life's simple pleasures", "Supporting the dreams and aspirations of grandchildren", "Living with an attitude of gratitude", "Embracing the beauty of lifelong friendships", "Living with a sense of contentment", "Sharing life's joys with great-grandchildren", "Investing in lifelong bonds",
    "Celebrating life's treasures", "Embracing the wisdom of age", "Celebrating life's milestones with loved ones", "Continuing to make new memories", "Living a life filled with love", "Expressing gratitude for life's journey", "Treasuring the moments that matter most", "Living life with a sense of peace", "Celebrating a life well-lived", "Leaving a legacy of love and wisdom", "Embracing the beauty of generational love",
    "Celebrating a century of memories", "Sharing the wisdom of a long life", "Embracing the joys of family gatherings", "Living with gratitude for each day", "Reflecting on a lifetime of experiences", "Expressing love and appreciation", "Treasuring the blessings of a long life", "Investing in the happiness of generations", "Celebrating life's enduring love", "Leaving a lasting impact on the world"
    ],
    100: [
    "Celebrating a century of life", "Reflecting on a lifetime of memories", "Sharing stories with generations", "Embracing the beauty of a long and fulfilling life", "Living with grace and gratitude", "Maintaining a sense of purpose", "Investing in health and well-being", "Finding joy in everyday moments", "Treasuring the support of loved ones", "Creating lasting memories with family",
    "Finding fulfillment in simple pleasures", "Leaving a legacy of love and kindness", "Sharing life's stories with younger generations", "Celebrating milestone anniversaries with extended family", "Enjoying life's simple pleasures", "Supporting the dreams and aspirations of grandchildren", "Living with an attitude of gratitude", "Embracing the beauty of lifelong friendships", "Living with a sense of contentment", "Sharing life's joys with great-grandchildren", "Investing in lifelong bonds",
    "Celebrating life's treasures", "Embracing the wisdom of age", "Celebrating life's milestones with loved ones", "Continuing to make new memories", "Living a life filled with love", "Expressing gratitude for life's journey", "Treasuring the moments that matter most", "Living life with a sense of peace", "Celebrating a life well-lived", "Leaving a legacy of love and wisdom", "Embracing the beauty of generational love",
    "Celebrating a century of memories", "Sharing the wisdom of a long life", "Embracing the joys of family gatherings", "Living with gratitude for each day", "Reflecting on a lifetime of experiences", "Expressing love and appreciation", "Treasuring the blessings of a long life", "Investing in the happiness of generations", "Celebrating life's enduring love", "Leaving a lasting impact on the world", "Becoming a living legend"
    ]
}

# Function to generate NPC
def generate_npc():
    newNPC = []
    firstName = random.choice(firstNames)
    middleName = random.choice(middleNames)
    lastName = random.choice(lastNames)
    personality = random.choice(personalities)
    age = choose_age()

    newNPC.append(f"Name: {firstName} {middleName} {lastName}")
    newNPC.append(f"Personality: {personality}")
    newNPC.append(f"Age: {age} years")
    
    events = life_events(age)
    newNPC.extend(events)

    write_to_file(firstName, middleName, lastName, newNPC)

# Function to choose an age between 10-100
def choose_age():
    return random.randint(10, 100)

# Function to select life events based on age
def life_events(age):
    events = []
    for year in range(5, age + 1, 5):
        if year in lifeEvents:
            event = random.choice(lifeEvents[year])
            events.append(f"{year} years: {event}")
    return events

# Function to write NPC to a file
def write_to_file(firstName, middleName, lastName, npc_data):
    folder_path = "NPC"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_name = f"{firstName}_{middleName}_{lastName}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        for line in npc_data:
            file.write(f"{line}\n")

# Main program
generate_npc()
