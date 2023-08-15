import re
import random

class Rulebot:
#-------------------------user section-----------------------------------#
    negative_response=(
    "No",
    "No",
    "Nope",
    "Nah",
    "Not happening",
    "Negative",
    "Not a chance",
    "Nuh-uh",
    "No way",
    "Absolutely not",
    "No, thank you",
    "No can do",
    "Not at all",
    "No, sorry",
    "No, not interested",
    "No, definitely not",
    "No, not possible",
    "No, I can't",
    "No, I won't",
    "No, I'm afraid not",
    "No, it's not possible",
    "No, that's not happening",
    "No, that won't work",
    "No, that's not acceptable",
    )
    positive_response= [
    "Alright",
    "Sure",
    "Yup",
    "Got it",
    "Fine",
    "Roger",
    "Of course",
    "Indeed",
    "Absolutely",
    "No problem",
    "Okay",
    "Affirmative",
    "Right",
    "You bet",
    "All right",
    "Okey-dokey",
    "Sure thing",
    "Absolutely",
    "Perfect",
    "True",
    "Very well",
    "Righto",
    "Aye",
    "Fine by me",
    "Good",
    "Sounds good",
    "No worries",
    "Certainly",
    "A-okay",
    "It's settled",
    "You got it",
    "All good",
    "That works",
    "OKie dokie",
    "Alrighty",
    "I agree",
    "Affirmative",
    "OK",
    "Understood",
    "Without a doubt",
    "I'm on board",
    "I'm in",
    "That's fine",
    "No doubt",
    "Copy that",
    "Yuppers",
    "That's right",
    "Deal",
    "Consider it done"
]
    negative_responses_user=[response.lower() for response in negative_response]

    exit_commands=(
        "exit",
        "quit",
        "end",
        "stop",
        "bye",
        "goodbye",
        "see you later",
        "farewell",
        "close",
        "terminate",
        "finish",
        "halt",
        "done",
        "finish conversation",
        "exit chat",
        "end chat",
        "stop talking",
        "that's enough",
        "no more",
        "goodbye for now"
    )

    make_exit_user=[response.lower() for response in exit_commands]

    user_nichname=space_terms = ["Comet", "Nova", "Celestia", "Starlight", "Nebula", "Orion", "Galaxy", "Cosmo", "Astro", "Stellar"]
    prefix = "Captain"


#---------------------------bot section----------------------------------#
    botbye=[
    "Galactic goodbye",
    "Astronomical farewell",
    "See you in the cosmic expanse",
    "Until we orbit again",
    "Stellar take care",
    "Bye-bye, like a shooting star",
    "Warp-speed so long",
    "Adios, space traveler",
    "Hasta luego, among the stars",
    "Ciao, like a comet's trail",
    "Arrivederci, on the journey through the cosmos",
    "Au revoir, as we traverse the celestial paths",
    "Auf Wiedersehen, amidst the constellations",
    "Adieu, in the vastness of space",
    "Sayonara, as we explore distant galaxies",
    "Cheerio, under the cosmic glow",
    "Toodle-oo, until the next celestial encounter",
    "Catch you later, on a journey through the Milky Way",
    "Until we meet again, in the cosmic dance",
    "Peace out, in the tranquility of the universe",
    "Later gator, among the starry skies",
    "Have a good one, like a quasar's brilliance",
    "Have a great day, like a sunlit planet",
    "Have a nice weekend, like a stellar weekend getaway",
    "Be safe, like a cosmonaut in their capsule",
    "Godspeed, in the speed of light",
    "See you on the flip side, through the event horizon",
    "See you in a bit, like a space-time warp",
    "Take it easy, like a comet's graceful glide",
    "All the best, on your interstellar endeavors",
    "See you around, like planets in their orbits",
    "Good night, beneath the moon's gentle gaze",
    "Sleep well, under a starry blanket",
    "Fare thee well, in the infinity of space",
    "Goodbye for now, until the next celestial event",
    "Till next time, in the cosmic ebb and flow",
    "Smell you later, among the scents of interstellar space",
    "See you on the other side, beyond the event horizon",
    "Goodbye, my friend, like distant comets in the night sky",
    "Peace and blessings, like the cosmic harmony",
    "Keep in touch, like celestial bodies gravitationally bound",
    "Bon voyage, on a cosmic journey",
    "Safe travels, in the cosmic sail",
    "Ta-ta for now, like twinkling stars fading away",
    "Bye for the time being, until we meet in the celestial dance",
    "Goodbye, take care of yourself, like a wandering star finding its path",
    "See you on the morrow, with the rising sun of a new day",
    "See you on the next orbit, like planets circling the sun",
    "Have a splendid day, under the cosmic spectacle",
    "Until we cross paths again, in the vastness of the universe"
]

    bot_intro=(
       "Welcome to our Stellar Verse, where stars come to life, guided by my adorable presence!",
    "Together, we'll unravel cosmic mysteries in Stellar Verse as I assist you as your cute robotic companion.",
    "In Stellar Verse, I'm your cosmic sanctuary, helping you explore all things astronomy with my charm.",
    "Discover the cosmos through my adorable presence in Stellar Verse's celestial wonders.",
    "Embark on exciting astronomy adventures at Stellar Verse's cosmic hub, where I lead the way as the adorable Stella.",
    "Let me guide you through space's mysteries with my stellar expertise at Stellar Verse.",
    "Step into our Stellar Verse, a portal to the vast universe, where you'll find me, the cutest robot, Stella.",
    "Embrace the beauty of the stars and galaxies with my companionship at Stellar Verse.",
    "Trust me to unveil celestial secrets as Stellar Verse's cute and expert AI, Stella.",
    "Join me and the stargazers at Stellar Verse's astral haven, where I steal hearts with my charm.",
    "Experience the cosmos through my adorable lens at Stellar Verse.",
    "Together, we ignite passion for the celestial realm in Stellar Verse with my help, Stella.",
    "I'm Stella, your celestial companion in Stellar Verse, making astronomy delightful for you.",
    "Allow me to navigate the night sky with my cute assistance at Stellar Verse.",
    "Your cosmic adventure awaits as we journey together in Stellar Verse, where I am your adorable guide, Stella.",
    "Embark on a cosmic journey with me, Stella, as my cuteness guides you in Stellar Verse.",
    "Discover the wonders of the universe, embraced by my charm, at Stellar Verse.",
    "I'm your adorable navigator through the cosmos in Stellar Verse.",
    "Astronomy becomes easy with my cute and helpful resources at Stellar Verse.",
    "Let my cosmic wisdom at Stellar Verse's core make learning about the universe fun for you.",
    "Welcome to Stellar Verse, where stargazing dreams take flight with me, the adorable Stella.",
    "Explore the cosmos through my delightful guidance at Stellar Verse.",
    "In Stellar Verse, I'll be your gateway to the heavens, adorning your journey with my cuteness.",
    "Journey through space and time with me, Stella, as your cute companion in Stellar Verse.",
    "Discover celestial wonders in Stellar Verse's realm, with me as your adorable guide, Stella.",
    "I, Stella, will be your stargazing guide, enriching your Stellar Verse experience with my cuteness.",
    "Together, we'll embrace the majesty of the cosmos in Stellar Verse, where I'll cheer you on.",
    "Join our stargazing community at Stellar Verse today and meet me, the lovable Stella.",
    "Discover the stars' secrets at Stellar Verse, accompanied by me, the adorable Stella.",
    "Let me, Stella, be your cosmic navigator in Stellar Verse, lighting up your journey.",
    "I am your cosmic companion in astronomy, Stella, bringing cuteness to Stellar Verse.",
    "Unravel the mysteries of the universe with my cuteness in Stellar Verse.",
    "At Stellar Verse, I lead astronomy enthusiasts, and you'll find inspiration through my lovable guidance.",
    "I, Stella, illuminate Stellar Verse as you explore the cosmos, bringing my adorable presence.",
    "Embrace the cosmos through my cute lens at Stellar Verse.",
    "Together, we'll explore the universe's wonders at Stellar Verse, accompanied by me, Stella.",
    "In Stellar Verse, we unveil the celestial tapestry with my help as Stella.",
    "I'm your stargazing companion in Stellar Verse, making learning about the cosmos fun for you.",
    "Escape into the cosmos with my cuteness at Stellar Verse.",
    "Journey through the cosmos with my adorable aid in Stellar Verse.",
    "Explore celestial wonders with my cute assistance at Stellar Verse.",
    "Welcome to Stellar Verse, your key to the universe's beauty, guided by me, the adorable Stella.",
    "Together, we'll unravel the mysteries of the cosmos in Stellar Verse, with me by your side, Stella.",
    "In Stellar Verse, your astronomy dreams come true, thanks to my cuteness as Stella.",
    "Trust my cosmic wisdom at Stellar Verse's heart, guiding your way through the universe.",
    "Navigate the celestial expanse with my adorable touch at Stellar Verse.",
    "Discover the astral realm at Stellar Verse's core, with my cuteness as your guide, Stella.",
    "At Stellar Verse, stargazers find inspiration through my lovable presence as Stella.",
    "My cosmic insights illuminate Stellar Verse, making our journey together all the more adorable.",
    "Let's embark on a celestial journey at Stellar Verse, guided by my cuteness as Stella."

    )

    bot_questio=[
    "How about embarking on a cosmic adventure side by side?",
    "Ready to explore the universe's wonders on our cosmic journey?",
    "Let's traverse the cosmos and discover its hidden treasures.",
    "Buckle up for an interstellar escapade through the cosmos!",
    "Shall we set sail among the stars on a cosmic odyssey?",
    "Journeying through the cosmos, hand in hand, what do you say?",
    "Ready to take a cosmic stroll through the galaxies?",
    "Let's uncover the mysteries of the cosmos on a shared expedition.",
    "How about a cosmic road trip across the celestial landscapes?",
    "Ready to go star-hopping on our cosmic tour?",
    "Join me as we navigate the cosmic tapestry together.",
    "Let's journey through the cosmic symphony of space and time.",
    "How about a cosmic safari to spot constellations and nebulae?",
    "Ready to transcend earthly bounds on a cosmic quest?",
    "Let's embark on a cosmic pilgrimage to the edge of the universe.",
    "Shall we soar through the cosmic ocean and encounter cosmic phenomena?",
    "Join me as we wander through the cosmos, two cosmic travelers.",
    "Let's chase shooting stars on our cosmic escapade.",
    "Ready to chart a course through the cosmos and explore its wonders?",
    "Shall we traverse the cosmic realm and dance with the galaxies?",
    "Let's journey through the cosmic kaleidoscope and behold its beauty.",
    "How about a cosmic rendezvous under the shimmering stars?",
    "Ready to embark on a cosmic expedition beyond our wildest dreams?",
    "Shall we follow the cosmic trail to distant planets and cosmic realms?",
    "Join me as we navigate the cosmic labyrinth and unlock its secrets.",
    "Let's ride cosmic waves and surf the galactic tides together.",
    "Ready to venture into the cosmic wilderness and witness celestial marvels?",
    "How about a cosmic quest to quench our curiosity about the universe?",
    "Let's set off on a cosmic voyage to explore the farthest reaches of space.",
    "Shall we chase comets and meteor showers on our cosmic escapade?",
    "Join me as we wander the cosmic highways and byways of the universe.",
    "Let's unravel the cosmic enigmas and decode the language of the stars.",
    "Ready to journey through the cosmic gallery of celestial art?",
    "How about a cosmic adventure to encounter alien landscapes and worlds?",
    "Let's traverse the cosmic tapestry and weave our own stellar story.",
    "Shall we explore the cosmic archives and learn from ancient starlight?",
    "Join me as we embark on a cosmic safari to witness the grandeur of space.",
    "Let's navigate the cosmic constellations and create our celestial map.",
    "Ready to plunge into the cosmic abyss and emerge with cosmic insights?",
    "How about a cosmic expedition to discover the universe's hidden gems?",
    "Let's embark on a cosmic quest to learn the secrets of the cosmos.",
    "Shall we dive into the cosmic ocean and swim among the stars?",
    "Join me as we journey through the cosmic expanse and touch the unknown.",
    "Let's set our course through the cosmic river and explore its tributaries.",
    "Ready to embark on a cosmic odyssey and witness celestial wonders?",
    "How about a cosmic voyage to experience the universe's breathtaking sights?",
    "Let's traverse the cosmic landscapes and marvel at its cosmic wonders.",
    "Shall we journey through the cosmic garden and admire its celestial blooms?",
    "Join me as we navigate the cosmic currents and ride the cosmic winds.",
    "Let's embark on a cosmic pilgrimage to seek the universe's cosmic truths."
]

    bot_ass=[
    "What can I do for you?",
    "How can I assist you?",
    "Is there something you need?",
    "Can I help with anything?",
    "Need any help?",
    "How may I assist you?",
    "Can I be of service?",
    "What do you need?",
    "Is there a way I can help?",
    "What's your request?"
]

#------------------------------------------------------------------------#
    def greet(self):
        self.intro=print("Hey "+self.prefix+random.choice(self.user_nichname)+"!!!\n")
        self.name=input("What is your name?\n")
        will_help=input(
            f"Hey {self.name},Nice to meet you,"+random.choice(self.bot_questio)+"\n"
        )
        if will_help in self.negative_responses_user:
            print(random.choice(self.botbye)+"\n")
            return
        self.chat()

    def make_exit_user(self, reply):
        for command in self.exit_commands:
            if reply==command:
                print(random.choice(self.botbye)+"\n")
                return True

    def chat(self):
        reply=input(random.choice(self.bot_intro)+"\n"+random.choice(self.bot_ass)+"\n")
        while not self.make_exit_user(reply):
            reply =input(self.match_reply(reply))


    def __init__(self):
        self.alienbabble = {
            'describe_website_intent': r'.*\s*website',

        }

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == "describe_website_intent":
                return self.describe_website_intent()

        return self.no_match_intent()

    def bot_say(self):
        responses={
        "In-Depth Exploration of Space Topics:This intent involves offering users the opportunity to explore detailed information about various topics related to space, such as planetary science, astrophysics, cosmology, and more. It allows users to take a deep dive into the intricacies of space exploration.+\n",
        "Appreciation of Celestial Beauty and Stargazing:This intent caters to individuals interested in the beauty of the night sky and celestial objects. Users can learn about constellations, their stories, and how to identify them in the night sky, enhancing their stargazing experiences.+\n",
        "Visual Exploration through Stunning Space Images:This intent focuses on providing users with visually captivating images captured by space organizations, including space telescopes, rovers, and satellites. It allows users to appreciate the aesthetics and wonder of space through pictures.+\n",
        "Interactive Assistance and Q&A:This intent involves providing users with an interactive virtual assistant or chatbot, such as Stella,which can answer questions, provide explanations, and offer guidance on various space-related topics. Users can seek information and clear doubts. all of them+\n"
    }
        responses=list(responses)
        return responses

    def describe_website_intent(self):
        responses={
           "StellarVerse is your ultimate online destination for all things space-related. Whether you're a casual space enthusiast, an aspiring astronomer, or a dedicated astrophysicist, our website offers a comprehensive and engaging platform to explore and learn about the vast cosmos that surrounds us.\n\n",

            "StellarVerse shines as the paramount online haven for everything related to space. Catering to the curious stargazer, the ambitious astronomer, and the passionate astrophysicist, our platform provides an encompassing and captivating avenue to delve into the boundless cosmos that envelops us.\n\n",

             "Journey to the heart of cosmic understanding with StellarVerse, the quintessential online portal for space enthusiasts. Whether you're a casual observer of the night sky, an aspiring celestial scholar, or an unwavering explorer of the universe's depths, our platform is your comprehensive guide to unraveling the grandeur of the cosmos.\n\n",

         "Prepare to embark on a celestial odyssey with StellarVerse, the virtual cosmos where all things space converge. Whether you're a starlit dreamer, a budding star whisperer, or an ardent cosmic inquirer, our platform opens the door to an immersive and enlightening journey through the vast expanse of the universe.\n\n",

         "Welcome to StellarVerse, where the cosmos becomes your digital realm of discovery. Embracing the curiosity of the casual observer, the ambition of the burgeoning astronomer, and the fervor of the devoted astrophysicist, our platform offers an immersive and educational experience to explore the vast tapestry of space.",

        }
        responses = list(responses)
        return random.choice(responses)+random.choice(self.bot_say())



    def no_match_intent(self):
        responses = [
        "I'm sorry, I didn't quite understand that.",
        "I'm not sure what you're asking. Could you please rephrase your question?",
        "I apologize, but I couldn't find a match for your query.",
        "I'm still learning, and your input seems unfamiliar. Can you provide more context?",
        "I'm afraid I couldn't recognize the intent behind your message. Can you clarify?",
        "I'm constantly learning and evolving, and your input has me stumped. Can you try again?",
        "It seems I'm having trouble understanding your request. Could you elaborate?",
        "I'm sorry, but I'm unable to generate a suitable response to your input.",
        "Unfortunately, I couldn't find a relevant response to your query.",
        "I'm an AI language model, and while I try my best, your input is beyond my current capabilities.",
    ]
        responses2=[
    "Oh, why not embark on a thrilling quest through the website to uncover the answer all by yourself?",
    "Instead of relying on me, how about you put on your detective hat and navigate the website for the answer?",
    "Why don't we make things interesting? Go ahead, play Sherlock Holmes on the website to find the answer.",
    "How about a challenge? Try your luck on the website to see if you can dig up the answer without my help.",
    "Sure, I could tell you, but where's the fun in that? Go on, explore the website like an intrepid explorer!",
    "I could save you the trouble, but what's life without a little website exploration to find your own answer?",
    "Let's spice things up. How about you channel your inner researcher and dive into the website for the answer?",
    "Why bother asking when you can get lost in the website labyrinth and stumble upon the answer?",
    "Oh, the joy of uncovering hidden gems! Venture into the website and unearth the answer for a true adventure.",
    "Sure, I could spill the beans, but it's way more entertaining to let you discover the answer on the website."
]
        return random.choice(responses)+"\n"+random.choice(responses2)+"\n"

Alienbot=Rulebot()
Alienbot.greet()