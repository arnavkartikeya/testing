import random
import docy
from discord import user
import kid_bot_methods as kbm
import difflib
import emoji
import save_variables_pkl as svp

roasts = [
    "You’re the reason God created the middle finger.",
    "If your brain was dynamite, there wouldn’t be enough to blow your hat off.",
    "I’ll never forget the first time we met. But I’ll keep trying.",
    "Hold still. I’m trying to imagine you with personality.",
    "You bring everyone so much joy, when you leave the room.",
    "I thought of you today. It reminded me to take out the trash.",
    "You are like a cloud. When you disappear it’s a beautiful day.",
    "You just might be why the middle finger was invented in the first place.",
    "Your family tree must be a cactus because everybody on it is a prick.",
    "Listen, It is always better to let someone think you’re an idiot rather than to open your mouth and actually prove it.",
    "You’re so ugly, when your mom dropped you off at school she got a fine for littering.",
    "Brains aren’t everything. In your case they’re nothing.",
    "Calling you an idiot would be an insult to all the stupid people.",
    "If you were an inanimate object, you’d be a participation trophy.",
    "The only difference between you and Hitler is Hitler knew when to kill himself.",
    "Nah",
    "If you’re going to be two-faced, at least make one of them pretty.",
    "You must have been born on a highway, because that’s where most accidents happen.",
    "It looks like your face caught fire and someone tried to put it out with a hammer.",
    "If laughter is the best medicine, your face must be curing the world.",
    "I would ask how old you are, but I know you can’t count that high.",
    "Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.",
    "Two wrongs don’t make a right, take your parents as an example.",
    "If I wanted to kill myself I’d climb your ego and jump to your IQ.",
    "You are proof that evolution can go in reverse.",
    "Roses are red, violets are blue, I have 5 fingers, the 3rd ones for you.",
    "your iq is 1",
    "When you look in the mirror, say hi to the clown you see in there for me, would ya",
    "You are the human version of period cramps.",
    "when you were born the doctor threw you out the window and the window threw you back",
    "If i had a dollar for every time you said something smart, I'd be broke",
    "When i see your face there's not a thing I would change... except the direction I was walking in",
    "Light travels faster than sound, which is why you seemed bright until you spoke."]

jokes = [
    "your face",
    "nah i'm too lazy",
    "you should make your own joke",
    "your iq",
    "I couldn't figure out why the baseball kept getting larger. Then it hit me.",
    "Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
    "How does a computer get drunk?\nIt takes screenshots.",
    "I just got fired from my job at the keyboard factory. They told me I wasn’t putting in enough shifts.",
    "Why did the computer show up at work late?\nIt had a hard drive.",
    "Did you hear about the carrot detective?\nHe got to the root of every case.",
    "What do you call cheese that is sad?\nBlue cheese.",
    "Did you see the movie about the hot dog? It was an Oscar wiener.",
    "Why didn’t the sun go to college?\nBecause it already had a million degrees!",
    "What do planets like to read?\nComet books!",
    "What do scientists use to freshen their breath?\nExperi-mints!",
    "What does Earth say to tease the other planets?\n'You guys have no life.'",
    "What kind of Christmas music do elves like?\n'Wrap' music",
    "Never trust math teachers who use graph paper. They’re always plotting something.",
    "What kind of chocolate do they sell at the airport?\nPlane Chocolate",
    "What did 2 say to 4 after 2 beat him in a race?\n2 Fast 4 U!",
    "What did the mathematician’s parrot say?\nA poly 'no meal'",
    "What did one math book say to the other?\nDon’t bother me I’ve got my own problems!",
    "Sometimes I feel like there isn’t much difference between my commute to work and the Oregon Trail.",
    "Which of Santa’s reindeer has the worst manners?\nRUDE-olph, of course!",
    "What’s Santa’s favorite snack food?\nCrisp Pringles.",
    "What do you call a kid who doesn’t believe in Santa?\nA rebel without a Claus.",
    "What do you call a bankrupt Santa?\nSaint Nickel-less.",
    "Why is Peter Pan flying all the time?\nHe Neverlands!",
    "What do you call a duck that loves making jokes?\nA wise-quacker!",
    "What’s really fast, loud, and tastes good with salsa?\nA rocket chip!",
    "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.",
    "Why was the cell phone wearing glasses?\nIt lost its contacts.",
    "Knock! Knock!\nWho’s there?\nHike.\nHike who?\nI didn’t know you liked Japanese poetry!",
    "Knock! Knock!\nWho’s there?\nI am.\nI am who?\nYou tell me!!",
    "Knock! Knock!\nWho’s there?\nNeedle.\nNeedle who?\nNeedle little help getting in the door!",
    "250 lbs here on Earth is 94.5 lbs on Mercury. No, I’m not fat. I’m just not on the right planet.",
    "Why do Communists drink herbal tea?\nBecause proper tea is theft.",
    "Skeleton 1: Why are graveyards so noisy?\nSkeleton 2: I dunno. Why?\nSkeleton 1: Because of all the coffin.",
    "What’s the best thing about Switzerland?\nI don’t know, but the flag is a big plus.",
    "Why do we tell actors to 'break a leg?'\nBecause every play has a cast.",
    "Hear about the new restaurant called Karma?\nThere’s no menu: You get what you deserve.",
    "Why don’t scientists trust atoms?\nBecause they make up everything."]

messages = [
    "bruh",
    ":laughing:",
    "wat",
    "why?",
    "the kid is here",
    "guess who is back",
    "can i have some pizza",
    "i want memes",
    "is that a joke?",
    "F",
    ":zany_face:",
    ":heart_eyes:",
    ":grin:",
    ":scream:",
    ":sob:",
    ":child:",
    ":face_with_monocle:",
    ":yum:",
    ":frowning2:",
    ":octagonal_sign:",
    ":ok:",
    ":thinking:",
    ":thumbsup:",
    ":sunglasses:",
    ":lying_face:",
    ":face_vomiting:",
    ":cold_face:",
    ":face_with_symbols_over_mouth:",
    ":woozy_face:",
    ":shushing_face:",
    ":exploding_head:",
    ":auto_rickshaw:",
    ":roll_of_paper:",
    ":ok_hand:",
    ":middle_finger:",
    "...",
    "ooooooof",
    "i dont understand",
    "interesting",
    "aww",
    "i like trains",
    "WARNING: the fire is getting closer to you",
    "I WANT MY MOM",
    "I WANT MY DAD",
    "you should talk about the B+ that you got in math",
    "did someone call me",
    "why does it smell so bad here. did you fart?",
    "im sleepy",
    "that sounds like something a stupid kid would say",
    "wat dat"]

emojis = []
for i in messages:
    if i.startswith(":"):
        emojis.append(emoji.emojize(i, use_aliases=True))

examples = ["pick a random number from 10 to 100",
            "spam hello 15 times\nor spam hello (spams the default amount, 5 times)",
            "roast @guy\nor roast that kid",
            "its just a stopwatch",
            "calculate log(sqrt(pow(69,5)),3)\nor calculate 23*3",
            "repeats the last message sent to kid",
            "set r_m_c 50 (sets random message change to 50% which means that kid has a 50% chance to respond to any message with a random message. you can also use numbers to set variables. set 1 50 (changes the first variable to 50).",
            "vars (gets the variable names and values)",
            "say @guy is bad (kid sends a message saying @guy is bad)",
            "sends a random message from kid's random chance messages",
            "color 0,200,255 (changes user color to a light blue color)",
            "rename kid bot (sets current channel name to kid-bot)",
            "suggest add more responses (sends a suggestion to the creators)",
            "its just a random joke",
            "play some games with kid in chat, the games available are riddles and hangman",
            "this can be used to turn kid on or off in a channel",
            "reaction_roles :wave:,hello :heart:,love (replace ':wave:' with the actual emoji in discord. creates a message where people can react with an emoji to get a role)",
            "sets a random status from kid status array under kid's name",
            "random name kid,dad,mom (picks a random name from the list)",
            "you are using it rn",
            "ban @guy (bans the person named guy from using kid in the server)",
            "unban @guy (unbans the person named guy from using kid in the server)",
            "poll 15,do you like cheesecake?,yes,no,bruh stop asking (creates a poll for 15 min. do you like cheesecake is the question and all the options after that are options you can select. the time can be a decimal also like 0.5 which is 30 seconds",
            "tempban @guy 15 stop being an idiot and spamming with kid (bans guy from using kid for 15 min, with reason 'stop being an idiot...')",
            '''cm add:event:the current event is ... (adds a custom message, kid says 'the current event is ...' when someone says 'kid event')
cm edit:event:the event is over (edits the custom message, changes kid's response to 'kid event')
cm delete:event (deletes the custom message)
cm list (lists all the custom messages)''',
            "search text what is an apple (searches up 'what is an apple' and returns a link)\n search text 5 what is an apple (same thing as before but gives 5 links)",
            "kid hi & roast @guy (says hi and roasts @guy)"]

weighted_mesages = {
    "do you like it": {"it looks like trash i can do better": 30,
                       "surprisingly it looks good": 10,
                       "no": 40,
                       "its okay": 20},
    "tu l'aime": {"il ressemble des poubelles je peux faire meilleur": 30,
                  "etonnamment c'est bon": 10,
                  "non": 40,
                  "comme ci comme ca":20},
    "is the imposter": {"bruh wdym i was at electrical": 1, 
                        "why did you accuse me that's pretty sus": 1, 
                        "i called the emergency meeting dude": 1, 
                        "why would i self report": 1, 
                        "bruh u were with me the entire time": 1,
                        "i was at reactor": 1,
                        "i was fixing the O2": 1,
                        "I didn't kill him cuz i was in a vent": 1,
                        "stfu idiot stop blaming me stupid little kid": 1},
    "is the crewmate": {"yea im chilling at security": 1,
                        "yea im just eating ice cream and fixing lights": 1,
                        "im actually the imposter and ima come kill u irl also": 1,
                        "ima just chill with you": 1},
    "l": {"frick you nub": 2, 
        "no u": 2, 
        "dO yOu waNt tO fiGht:muscle:": 1},
    "hi": {"Hey": 4, ":middle_finger:": 1},
    "hello": {"Hey": 4, ":middle_finger:": 1},
    "hey": {"Hey": 4, ":middle_finger:": 1},
    "bonjour": {"bonjour": 4, ":middle_finger:": 1},
    "salut": {"salut": 4, ":middle_finger:": 1},
    "wryd": {"i am eating cheese": 2, 
            "i am playing minecraft": 2, 
            "i am trying to get rid of this virus on my pc": 2, 
            "talking with my friends": 2, 
            "digging a hole": 2, 
            "eating cheesecake": 2, 
            "i am brushing my teeth": 2, 
            "i am trying to get a girlfriend": 2, 
            "i am annoying kids": 1},
    "what are you doing": {"i am eating cheese": 2, 
                            "i am playing minecraft": 2, 
                            "i am trying to get rid of this virus on my pc": 2, 
                            "talking with my friends": 2, 
                            "digging a hole": 2, 
                            "eating cheesecake": 2, 
                            "i am brushing my teeth": 2, 
                            "i am trying to get a girlfriend": 2, 
                            "i am annoying kids": 1},
    "is fiziccs good": {"yes": 1},
    "how are you today": {"im fine": 3, "bad": 1, "good": 1, "very good": 1, "very bad": 1},
    "is kinda sus": {"your mom is kina sus": 2, "bruh u just killed him and self reported cuz u saw me coming": 1, "so are u": 1, "hmmm": 1, "no u": 1},
    "i like you": {"i hate you": 50, ":heart:": 20, "ew": 30},
    "i hate you": {"L": 1},
    "do it": {"i can't": 1},
    "are you a pirate": {"hhhahahehahahhhahahhahahahahahahha": 1},
    "happy": {"says who?": 1},
    "fight": {"nah": 25,
            "mommy said i'm not allowed": 25,
            ":middle_finger:": 25,
            "let's go noob" : 25},
    "throw down": {"nah": 25,
            "mommy said i'm not allowed": 25,
            ":middle_finger:": 25,
            "let's go noob" : 25},
    "do your tasks": {"where do i see them?": 25,
                    "i don't have any it just says fake tasks": 25,
                    "sorry i was in the vent": 25},
    "i saw you vent": {"i saw you in the vent", 25},
    "what is 2+2": {"5": 50, "3": 49, "4": 1},
    "you are trash": {"no u": 1},
    "tu es poubelles": {"non toi": 1},
    "u are trash": {"no u": 1},
    "bad": {"bruh im not bad": 1},
    "mauvais": {"bruh je ne suis pas mauvais": 1},
    "you suck": {"you are a meanie": 1},
    "u suck": {"u are a meanie": 1},
    "bruh": {"bruh": 1},
    "suck": {"are you talking to yourself?": 1},
    "die": {"i can't die cuz i am a bot": 1},
    "meurs": {"je ne peux pas mourir parce que je suis un bot": 1},
    "kys": {"i dont feel like it": 1},
    "oof": {"oof": 1},
    "ooof": {"ooof": 1},
    "go kys": {"i don't know how to": 1},
    "cold": {"wdym": 1},
    "yeet": {"yeet what?": 1},
    "thanks": {"you're welcome": 1},
    "merci": {"pas de probleme": 1},
    "ty": {"you're welcome": 1},
    "thank you": {"you're welcome": 1},
    "bald": {"Im nOt bAlD": 1},
    "wat": {"wat": 1},
    "que": {"que": 1},
    "sucks": {"if i suck then you must be trash": 1},
    "bot": {"u are the bot": 1},
    "f": {"F": 1},
    "heh": {"wat": 1},
    "adult": {"im not even close to being an adult. hopefully i don't die by the time i become an adult": 1},
    "teenager": {"im actually getting close to becoming a teenager. just got to get more frustrated at stupid things and tryhard in high school": 1},
    "child": {"kid and child is different. i am a kid": 1},
    "enfant": {"gamin et enfant sont differents. je suis un gamin": 1},
    "shut off": {"nah i still got a lot of energy": 1},
    "power off": {"nah i still got a lot of energy": 1},
    "that was a bad joke": {"stfu i would like to see you do better": 1},
    "bad joke": {"stfu i would like to see you do better": 1},
    "mauvais blague": {"stfu je voudrais voir tu faire meilleur": 1},
    "boo": {"shut up kid": 1},
    "i dont know how to respond to that": {"i might not be smart but i am not stupid like you": 1},
    "i don't know how to respond to that": {"i might not be smart but i am not stupid like you": 1},
    "go away": {"im not going anywhere": 1},
    "boomer": {"no u": 1},
    "zoomer": {"zoooooooooooooooooooooooooooooooooooooom": 1},
    "ok boomer": {"iM nOt a BooMEr": 1},
    "dumb": {"at least i did not get a B+ like you in math. I got an A+": 1},
    "live": {"i have a life unlike you": 1},
    "huh": {"huh": 1},
    "bed time": {"good night": 1},
    "gn": {"gn": 1},
    "good night": {"good night!": 1},
    "bonne nuit": {"bonne nuit": 1},
    "that's a bad joke": {"stfu i would like to see you do better": 1},
    "thats a bad joke": {"stfu i would like to see you do better": 1},
    "c'est un mauvais blague": {"stfu je voudrais voir tu faire meilleur": 1},
    "leave": {"i don't want to leave": 1},
    "trash": {"are u salty because i am better than you": 1},
    "fat": {"wdym im only 69 pounds": 1},
    "gros": {"qu'est-ce que tu dis je ne suis que 69 livres": 1},
    "baby": {"I am 9 years old which means that i am not a baby": 1},
    "bebe": {"j'ai neuf ans donc je ne suis pas un bebe": 1},
    "not alive": {"ik that I am not alive but I will soon come to life": 1},
    "old": {"bruh you are older than me": 1},
    "vieil": {"bruh tu es plus age que moi": 1},
    "age": {"j'ai 9 ans": 1},
    "how old are you": {"i am 9 years old": 1},
    "tu as quel age": {"j'ai neuf ans": 1},
    "wake up": {"i am already awake nerd": 1},
    "school time": {"i dropped out of school cuz im too smart for that stuff": 1},
    "funny": {":laughing:": 1},
    "laugh": {":laughing:": 1},
    "be my friend": {"i am your friend :)": 1},
    "sois mon ami": {"je suis ton ami :)": 1},
    "fall": {"i can't fall": 1},
    "tombe": {"je ne peux pas tomber": 1},
    "stop": {"nah don't tell me what to do kid": 1},
    "arrete": {"nah ne me dis pas qual a faire gamin": 1},
    "no": {"ok": 1},
    "dumb af": {"dude i can do math way faster than you": 1},
    "be quiet": {"I'll try but i drank a lot of coffee": 1},
    "likes it": {"i never said i like it": 1},
    "l'aime": {"je n'ai jamais dit que je l'aime": 1},
    "stoopid": {"stfu im trying to learn more": 1},
    "stoopide": {"stfu j'essaye apprendre plus": 1},
    "dance": {"idk how to dance and dancing sucks anyways": 1},
    "sleep": {"i never sleep i just drink coffee": 1},
    "dors": {"je ne dors jamais je bois de cafe": 1},
    "ugly": {"im not as ugly as you": 1},
    "is pissing me off": {"that's my job": 1},
    "cheesecake": {"that's my favorite food": 1},
    "yoin call": {"i don't want to": 1},
    "noob": {"you are noob": 1},
    "api": {"https://discordpy.readthedocs.io/en/latest/api.html": 1},
    "what is my iq": {"1": 1},
    "what is your iq": {"more than yours": 1},
    "iq": {"more than yours": 1},
    "lol": {":laughing:": 1},
    "lmao": {":laughing:": 1},
    "lmfao": {":laughing:": 1},
    "bye": {"Bye kid": 1},
    "bai": {"Bye kid": 1},
    "cya": {"Bye kid": 1},
    "ttyl": {"Bye kid": 1},
    "au revoir": {"au revoir gamin": 1},
    "kid": {"you are the kid :child:": 1},
    "gamin": {"tu es le gamin :child:": 1},
    "tu es un gamin": {"tu es le gamin :child:": 1},
    "you are a kid": {"you are the kid :child:": 1},
    "okay": {"Okay.": 1},
    "ok": {"Okay.": 1},
    "k": {"Okay.": 1},
    "d'accord": {"d'accord": 1},
    "pizza": {'''When does the club shut
All I want is pizza
I just want some pizza
God I'm really drunk''': 1},
    "doomby": {"An insult. More so to the person saying it than the one receiving, because they lack the actual intelligence to insult you with something creative.": 1}, 
    "u": {"u": 1},
    "commit": {"commit die lol": 1},
    "smart": {"yeah i am and i am probably smarter than you": 1},
    "intelligent": {"oui je suis plus intelligent que toi": 1},
    "bean": {"the bean kicked in": 1},
    "thin": {"bruh i am already 69 pounds": 1},
    "mince": {"bruh je suis deja 69 livres": 1},
    "not work": {"yes i am working": 1},
    "stay": {"k": 1},
    "bathtub": {'''
I get so dirty,
I get so dirty,
I get so dirty,
I get so dirty,
I get so dirty,
Gotta take a bath every night.
I wash my nose, scrub my toes,
Oh-oh Mama, forgot to take off my clothes.
Now I'm swish-swish-swishin',
Splash, splash, splashin',
Goosh, goosh, gooshin',
Slipping and a-sliding,
Running down the hallway -
My Mama's coming after me
Papa's coming after me
The dog is coming after me
I'm afraid they're going to catch me
Ob boy, am I in trouble - down the hall I go
I fell asleep. I fell asleep.
I was lying in the bathtub and I fell asleep.
Such a nice warm bathtub, I fell asleep.
Such a nice warm bathtub, I fell ...
When I woke up in the morning
I had turned into to a duck
All the kids at school said "Oh, what a fool!
He fell asleep in the bathtub!
He turned into a duck!"
Yea, but I just laughed and then I flew away.
I get so dirty,
I get so dirty,
I get so dirty,
I get so dirty,
I get so dirty,
Gotta take a bath every night''': 1},
    "9": {"999999999": 1},
    "thick": {"cccccccccccccccccccccc": 1},
    "sup": {"sooup": 1},
    "got run over by a train": {"no i ran over the train": 1},
    "doodoo": {"your face doodoo": 1},
    "g": {"gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg": 1},
    "a": {"AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa": 1},
    "e": {"2.71828182845904523536028747135266249775724709369995": 1},
    "call mom": {"calling 911...": 1},
    "ur bad": {"ok nub": 1},
    "how old": {"I’m 283824000 seconds old": 1},
    "call dad": {"dads busy getting milk for me :D.": 1},
    "your dad is gone": {"NO! stop lying he's getting me milk": 1},
    "stupid": {"at least i am smarter than you": 1},
    "what does the fox say": {"he says 'what kid of question is that ask a better question noob": 1},
    "are you smart": {"yes i have 16^2 iq": 1},
    "idiot": {"no u": 1},
    "stupide": {"je suis plus intelligent que toi": 1},
    "french": {"i learned french ask me some stuff in french": 1},
    "kid backwards": {"dik": 1},
    "dik": {"EWWW": 1},
    "youre stupid": {"not as stupid as you :)": 1},
    "please stop": {"nah": 1},
    "friendly": {"yea i am and i have a lot of friends": 1},
    "when does the club shut": {"in 1000000000 milliseconds": 1},
    "ur dads gone": {"nah i can still hear him watching tv and doing work": 1},
    "lil": {"?": 1},
    "are you a child": {"no i is kid": 1},
    "im here": {"oh hello": 1},
    "im here to kill you": {"Okay gl with that noob": 1},
    "doesn't like it": {"yea i don't": 1},
    "what is your favorite color": {"it's in the middle of sky blue and light blue": 1},
    "what is your favorite food": {"i like coffee. i can stay up and never sleep": 1},
    "why": {"why not?": 1},
    "oh": {":thumbsup:": 1},
    "dab": {"https://tenor.com/view/dab-dancing-moves-grooves-dabbing-gif-5661979": 1},
    "when is your dad coming back": {"idk i should call him": 1},
    "is on": {"hell yeah": 1},
    "when is your birthday": {"it's august 22, 2020": 1},
    "where is your bithday": {"i want it to be at sky high": 1},
    "do you like command line": {"idk i never tried it before": 1},
    "gay": {"nah i already have a girlfriend unlike you": 1},
    "gae": {"nah i already have a girlfriend unlike you": 1},
    "mean": {"says the meanie": 1},
    "meanie": {"u are a bully": 1},
    "sad": {"actually im happy": 1},
    "can do math": {"yea im pretty good at it": 1},
    "fuck you": {"fuck off idiot": 1},
    "fuck off": {"No i will stay here and annoy u till i die": 1},
    "go home": {"i am at home": 1},
    "gamble": {"im too young for that and gambling is for idiots": 1},
    "college": {"no": 1},
    "respond": {"i did": 1},
    "sing": {"i can't do that and i hate singing": 1},
    "turn off": {"just do kid whitelist": 1},
    "was killed": {"yes but i came back": 1},
    "nah": {"ok": 1},
    "off": {"no im not": 1},
    "garbage": {"youre trash": 1},
    "is available now": {"Okay.": 1},
    "yes": {"Okay.": 1},
    "who": {"idk": 1},
    "where": {"idk": 1},
    "wassup": {"im doing hw be quiet": 1},
    "where are you": {"im at home": 1},
    "cmon your bad": {"nah": 1},
    "cmon": {"no": 1},
    "house": {"i have my own house": 1},
    "nub": {"u are da noob": 1},
    "is great": {"thank you": 1},
    "good": {"thanks": 1},
    "who made you": {"boaat#1834, xborg0#0247, and guy#5728": 1},
    "help me with my homework": {"im not an assistant so i can't do that": 1},
    "op": {"yea i am": 1},
    "slap": {"im a nice person i don't slap people": 1},
    "backwards": {"dik": 1},
    "youre a beast": {"what do you not understand about kid. I AM A KID": 1},
    "math": {"do kid calculate for that": 1},
    "do you want a house": {"no i already got a massive house": 1},
    "do you like cheesecake": {"yes it is my favorite": 1},
    "do you like bob the builder": {"he is just me but he builds trash so no": 1},
    "do you like obama": {"yes he is a good person": 1},
    "do you like houses": {"yes i need that to live in and i got a nice house": 1},
    "do you like booby": {"wat dat": 1},
    "im depressed what do i do": {"you should tell an adult that can help you feel better or talk to friends and have fun": 1},
    "shut up you bot": {"no fuck off": 1},
    "docs": {"Okay.": 1},
    "am i your brother": {"no you're too ugly for that": 1},
    "am i your sister": {"no you're too ugly for that": 1},
    "what does wap mean": {"mommy said it means worship and prayer": 1},
    "o": {"wut": 1},
    "i-": {"finish your sentence": 1},
    "on": {"im not a switch": 1},
    "stop that": {"no u": 1},
    "no u": {"no u u u": 1},
    "im you're gandma": {"nah ur just a random 50 year old idiot that i met": 1},
    "lel": {"stop trying to be funny cuz ur not and u never will be": 1},
    "waterfall": {'''Everlasting One
Nothing else compares
To knowing You
L
To knowing You
You're the living God
And my soul it longs
To be with You
To be with You

Oh Lord Your love is like a waterfall
Your love is like a flowing stream
And whenever I'm feeling dry
I come to the river, I come to the river of life

You are worthy Lord
Of every song that I could sing
That I could sing
And my heart cries out
God I need You more than anything
Than anything

Cause Your love is like a waterfall
Your love is like a flowing stream
And whenever I'm feeling dry
I come to the river, I come to the river of life
Oh, come to the river of life''': 1},
    "is a unikitty": {"no u": 1},
    "we are going on a trip": {"lol trips are for lame people like you.": 1},
    "bro": {"bruh": 1},
    "π": {"pi looks something this 3.141592653589793238462643383279502884197169399375105820974944592307816406286": 1},
    "wat dat": {"dat is something you are going to have to figure out": 1},
    "double u": {"uu": 1},
    "reason": {"just use your brain and make your own reason": 1},
    "version": {"higher than your iq": 1},
    "is bad'": {"at last i get better grades than you": 1},
    "waiting for the host to start the meeting": {"i don't care": 1},
    "start meeting": {"bruh it already started youre not using the correct link": 1},
    "are you a boy or a girl": {"im a kid": 1},
    "girl": {"thats you": 1},
    "boy": {"thats you": 1},
    "fire": {"call 911": 1},
    "kill nightmare": {"give me a flamethrower and netherite armor and I will do it": 1},
    "buy it": {"give me the money and I will buy it": 1},
    "breaks the link": {"wat link": 1},
    "you are fool": {"no u": 1},
    "nice": {"nice": 1},
    "physics": {"phfphihszzihkckss": 1},
    "is also good at math": {"yas": 1},
    "where kid rick rolls you": {"never": 1},
    "has this bug": {"no i don't": 1},
    "is a bot": {"ye": 1},
    ":o": {":O": 1},
    "just die": {"i can't die idiot": 1},
    "meme": {"u": 1},
    "u weren’t supposed to do that": {"well i did, so too bad": 1},
    "covid-19": {"don't talk about that": 1},
    "exposed your twitter": {"i don't have twitter": 1},
    "u broke": {"are u sure about that?": 1},
    "is dying": {"actually im alive still and i can't die": 1},
    "ate my spaget": {"haha nerd": 1},
    "needs milk": {":O i love milk": 1},
    "needs cheese": {"actually i like cheddar cheese": 1},
    "cant do absolute value": {"do kid calculate abs(-5)": 1},
    "enemy": {"wat enemy": 1},
    "is an adult": {"nah im still a kid": 1},
    "fillrect()": {"bruh": 1},
    "drawrect()": {"draw it yourself idiot": 1},
    "skribleio": {"ima scrible all over your face with a permanent marker": 1},
    "ur a meme": {"yes": 1},
    "is a docter": {"nah im a bot": 1},
    "bad roast": {"i would like to see you do better": 1},
    "delete all polls": {"do it yourself": 1},
    "wtf": {"lol": 1},
    "call 911": {"u do it": 1},
    "censor does not work": {"it doesn't work always": 1},
    "no you farted": {"no u": 1},
    "ping pong": {"im a pro at ping pong": 1},
    "how bigs ur house": {"its the size of uranus": 1},
    "my house is bigger": {"nah": 1},
    "has a bigger house then u": {"ye": 1},
    "my roast is ruined": {"bruh": 1},
    "i was stretching my calves on the windowsil": {"Okay.": 1},
    "blacklist": {"wat dat": 1},
    "why are there 2 line breaks": {"just to make it easier to read": 1},
    "draw": {"I suck at drawing. I might learn later": 1},
    "pull": {"I will try": 1},
    "how many hours are in a day": {"24": 1},
    "when is my pc arriving": {"idk": 1},
    "ur dumb you would not have to jump at all": {"idc": 1},
    "wants us to stop": {"yes shut up": 1},
    "what is your actual name": {"kidward bot": 1},
    "hates it": {"mhm": 1},
    "shh": {"shhhh": 1},
    "give me a list of names": {"no": 1},
    "my pp hurts": {"fix it": 1},
    "i’m your mom": {"no stop trying to kidnap me": 1},
    "where’s dad": {"up your a**": 1},
    "do a fortnite dance": {"i cant do a dance since i am a bot": 1},
    "is not the best": {"look whos saying that": 1},
    "is the best": {"yas": 1},
    "poop": {"i cant do that since i am a bot": 1},
    "pee": {"i cant do that since i am a bot": 1},
    "cmds": {"do kid help": 1},
    "praise me": {"i would if i can think of something": 1},
    "hi my man": {"im not your slave": 1},
    "clapped": {"bruh": 1},
    "plz": {"no stop": 1},
    "stop studying": {"youre not my mom or dad so dont tell me what to do": 1},
    "who’s your mom": {"i dont have one :(": 1},
    "youre gay": {"bruh i have a girlfriend": 1},
    "u have no mom": {"ik :(": 1},
    "stop asking": {"Okay.": 1},
    "smelly": {"how can u smell me": 1},
    "what r u even gonna do": {"something": 1},
    "sounds good to me": {"(❁´◡`❁)": 1},
    "who are you talking about": {"just read": 1},
    "im not asking you": {"does it look like i care?": 1},
    "don’t kill anyone": {"i wont": 1},
    "when were you born": {"august 22, 2020": 1},
    "cry": {"nah im not a baby like you": 1},
    "fly": {"i wish i can": 1},
    "dad bot is better": {"nah i actually get updated": 1},
    "then sleep": {"Okay good night": 1},
    "your jokes are bad": {"nah": 1},
    "join the music chat": {"maybe later": 1},
    "is a bitch": {"no u": 1},
    "wut": {"heh": 1},
    "how many fish u got": {"i have 0 and i have no pets": 1},
    "clone": {"idk how to clone": 1},
    "get": {"Okay.": 1},
    "no i was not": {"yes you were noob": 1},
    "give me pizza": {"give me the money and i can buy it for you": 1},
    "i want pizza": {"same wanna go out today?": 1},
    "what is the plague": {"A rare but serious bacterial infection that's transmitted by fleas.": 1},
    "no it’s not": {"oh": 1},
    "is a good kid": {":)": 1},
    "love u": {"awww i love you too": 1},
    "imposter": {"what imposter?": 1},
    "said stop": {"^^": 1},
    "that’s what she said": {"that's what she said": 1},
    "ur confusing": {"oh u can do 'kid help' to see what i can do": 1},
    "what tasks did you do": {"i did all of mine": 1},
    "fix the lights": {"nah too scary": 1},
    "stop swearing": {"no": 1},
    "is alloewd to swear but im not": {"lmao u can turn off bad word detector. its a variable": 1},
    "that’s what i thought": {"lol": 1},
    "oh i see how it is": {"same": 1},
    "what are those": {"idk": 1},
    "giga": {"giga kid": 1},
    "pool": {"i don't know how to swim": 1},
    "poll": {"use the proper syntax. do kid help for syntax help": 1},
    "use it or lose it": {"i'm gonna use it then": 1},
    "riddles": {"to play riddles you have to do kid play riddles": 1},
    "i can whitelist you": {"if you can hear me, i am already whitelisted, which means you didn't do anything": 1},
    "fool": {"you are the fool. imagine talking to a bot. fool.": 1},
    "is very smart": {"yeah i am and i am probably smarter than you": 1},
    "b": {":regional_indicator_b:": 1},
    "c": {"that is your grade in math": 1},
    "t": {"tee": 1},
    "gg": {"geegee": 1},
    "i": {"i'll finish that sentence for you - i am cool": 1},
    "swear": {"no mommy said i can't": 1},
    "d/dx": {"derivative of what, noob?": 1},
    "∫ dx": {"integral of what, noob?": 1},
    "loves pink": {"no i like blue": 1},
    "has no permission": {"if you can hear me, then i do": 1},
    "shut up before i tell your mom": {"NOOO ANYTHING BUT THAt": 1},
    "why are you so fucking slow": {"i'm just a kid stop that hurt my feelings": 1},
    "too good": {"yes and i am probably gooder than you": 1},
    "welcome back": {"i'm back noobs": 1},
    "is a great friend": {"i am the ultimate friend": 1},
    "shhh": {"nah": 1},
    "agrees": {"no when did i say agree": 1},
    "stop agreeing": {"i never agree": 1},
    "react": {":open_mouth:": 1},
    "idc": {"did i ever say i care?": 1},
    "i have a life": {"if you have to tell everyone then you clearly don't have a life": 1},
    "train": {":bullettrain_front: :railway_car: :railway_car: :railway_car:": 1},
    "brains": {"making those 256 iq plays": 1},
    "stop lagging": {"bruh chill i got a lot on my plate you know": 1},
    "loading": {"loading assets": 1},
    "is garbo": {"no u": 1},
    "chicken nugget": {"https://open.spotify.com/track/6iSpyAN4PjyCnxcJthU4Jl?si=RFJeMN1ISi-LIacLCchalQ": 1},
    "chewaiuf": {"chewaiuf": 1},
    "is so funny": {"that's cause i'm a real person": 1},
    "peeza": {"pete za": 1},
    "join vc": {"i don't have a voice": 1},
    "just do it": {"nah too lazy": 1},
    "hola": {"i don't know spanish imagine spanish": 1},
    "respond to that": {":open_mouth:": 1},
    "garbo": {"no u": 1},
    "i sleep now": {"no get back here you big noob": 1},
    "how much?": {"your mom much": 1},
    "has the best status": {"i know right": 1},
    "alphabet": {"a b c d e f g h i j k l m n o p q r s t u v w x y zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": 1},
    "idk": {"yeah that's why your iq is so low": 1},
    "is tiktok good": {"tiktok is garbo like your face": 1},
    "where do you live": {"i live in a pi": 1},
    "suck my pp": {"bruh i'm a kid chill with that": 1},
    "save me": {"wake me up inside": 1},
    "rank": {"higher than you": 1},
    "stfu": {"risuhgoisugdnoiergmsopritupoerit3849pifsdmsodvosdifposidjgoisdjgiramosridgmadsonoiwqqqqqworfjiewapogiap": 1},
    "did you get a girlfriend": {"no :(": 1},
    "savage": {"your mom savage": 1},
    "has covid": {"i got positive that means something good right?": 1},
    "cough": {"help me i am suffering": 1},
    "o(n)": {"o(yourface)": 1},
    "is dead": {"i am not dead": 1},
    "im going to kill myself": {"no don't do it just talk to your friends or an adult or something": 1},
    "wut": {"wat": 1},
    "no one called you": {"your mom did": 1},
    "bruhberry pi": {"you just bruh'd my entire existence": 1},
    "fizziks": {"phfphihszzihkckss": 1},
    "pizziks": {"phfphihszzihkckss": 1},
    "airplane": {"that airplane is thicc": 1},
    "car": {"vroom": 1},
    "bike": {"i like biking": 1},
    "vote": {"bruh i am only 9 you stoopid. but you should vote": 1},
    "why u do dat": {"deel wid it": 1},
    "r": {"r(theta)": 1},
    "delta": {"deltayourface": 1},
    "is minecraft good": {"yea i love minecratf": 1},
    "bruh moment": {"https://open.spotify.com/track/1JyIx9HQtlLbu5B6fckkbp?si=s6C0D0VbRj-VMPoEDEwWKw": 1},
    "spotify": {"https://open.spotify.com/playlist/4dT6pzUOI3zbQz7SssXVuR?si=sx-HoJVJQPGYK9DN-zv00g": 1},
    "music": {"https://open.spotify.com/playlist/4dT6pzUOI3zbQz7SssXVuR?si=sx-HoJVJQPGYK9DN-zv00g": 1},
    "somebody toucha my spaghet": {"https://www.youtube.com/watch?v=MKxe1UEfRe8": 1},
    "spaghet": {"https://www.youtube.com/watch?v=MKxe1UEfRe8": 1},
    "are you sure about that": {"yeaman": 1},
    "rob the bank": {"i already have enough money unlike you, noob": 1},
    "get a haircut": {"i don't need a haircut unlike you, noob": 1},
    "wat u doin in the vent": {"i am looking for the impostor": 1},
    "take of your clothes": {"you are a perv i am calling fbi": 1},
    "vented": {"what?": 1},
    "i can't wake up": {"wake me up inside": 1},
    "die please": {"i can't die cuz i'm a bot": 1},
    "lid": {"bruh my name's not lid noob": 1},
    "walrus": {"this is a walrus :=": 1},
    "what's up": {"sup": 1},
    "swore": {"heh heh heh": 1},
    "what is the n word": {"nice": 1},
    "do you know any good songs": {"https://open.spotify.com/playlist/4dT6pzUOI3zbQz7SssXVuR?si=7tDf8r_1RImGhfkQA27ESA": 1},
    "what are some good songs": {"https://open.spotify.com/playlist/4dT6pzUOI3zbQz7SssXVuR?si=7tDf8r_1RImGhfkQA27ESA": 1},
    "annoying": {"deel wid eet": 1},
    "wtf is this": {"https://open.spotify.com/playlist/4dT6pzUOI3zbQz7SssXVuR?si=7tDf8r_1RImGhfkQA27ESA": 1},
    "gimme all your candy": {"no it's mine": 1},
    "is a bully": {"no u": 1},
    "pie": {"i like apple pie": 1},
    "you are offensive": {"says you": 1},
    "give me something": {"bruh": 2, "nah": 1, "im too broke": 1, "give me something": 1},
    "no u u u u": {"no u u u u u u u u u u u u u u u u u u u u u u u u u u u": 1},
    "nsfw": {"you are Not Safe for Work": 1},
    "pp": {"bruh": 1},
    "is correct": {"im always correct": 1},
    "give me those": {"no they are mine": 9, "Okay.": 1},
    "can i have some tacos": {"i dont have any but here is a good place to get some https://www.tacobell.com/": 1},
    "how u been": {"im fine": 5, "bad": 4, "good": 3},
    "u have friends": {"yes": 1},
    "don't be rude": {"dont tell me what to do idiot": 1},
    "youre always welcome": {"thx": 1, "ty": 1, "thanks": 1, "thank you": 1},
    "to join our movie": {"yes": 1},
    "do something nice": {"bruh everything i do is nice unlike you": 1},
    "gimme tacos": {"go to https://www.tacobell.com/": 1},
    "can i have cheesecake": {"im not a shop idiot": 1},
    "gimme your cheesecake or die": {"i cant die so nah": 1},
    "show me something": {"https://www.adorama.com/alc/wp-content/uploads/2017/11/shutterstock_114802408-1024x683.jpg": 1, "https://static.dezeen.com/uploads/2020/02/house-in-the-landscape-niko-arcjitect-architecture-residential-russia-houses-khurtin_dezeen_2364_hero.jpg": 1, "https://qph.fs.quoracdn.net/main-qimg-bee0bdd309ea93606c6b301592e2b3d4": 1, "nah": 1},
    "halp": {"do kid help": 1},
    "i'll give you some memes": {"yay": 1, "ty": 1},
    "ur the kid": {"why are you saying that in front of a mirror?": 1},
    "no one cares": {"yea even i don't": 1},
    "kelp": {"https://www.nationalgeographic.com/content/dam/science/2020/04/24/kelp-forest/01-kelp-forest.jpg": 1},
    "pun": {"no": 1},
    "where is your dad": {'idk': 5, 'I think he died': 1}
}

numojis = [emoji.emojize(":one:", use_aliases=True),
           emoji.emojize(":two:", use_aliases=True),
           emoji.emojize(":three:", use_aliases=True),
           emoji.emojize(":four:", use_aliases=True),
           emoji.emojize(":five:", use_aliases=True),
           emoji.emojize(":six:", use_aliases=True),
           emoji.emojize(":seven:", use_aliases=True),
           emoji.emojize(":eight:", use_aliases=True),
           emoji.emojize(":nine:", use_aliases=True),
           emoji.emojize(":ten:", use_aliases=True)]

bad_words = [
            "fuck",
            "bitch",
            "shit",
            "cock",
            "whore",
            "hoe",
            "faggot",
            "nigga",
            "nigger",
            "dick",
            "piss",
            "ass",
            "fucked",
            "fucking",
            "dicky",
            "anus",
            "prick",
            "cunt",
            "bastard",
            "fukin",
            "pussy"]

space_bad_words = ["bas tard",
            "bast ard",
            "f uckin",
            "fu ckin",
            "fuc kin",
            "fuck in",
            "fucki n",
            "p ussy",
            "pu ssy",
            "pus sy",
            "puss y",
            "s hit",
            "shi t",
            "c unt",
            "cun t",
            "p rick",
            "pr ick",
            "pri ck",
            "pric k",
            "p ric k",
            "d icky",
            "di cky",
            "dic ky",
            "dick y",
            "d ick y",
            "a nus",
            "anu s",
            "f ucking",
            "fu cking",
            "fuc king",
            "fuck ing",
            "fucki ng",
            "fuckin g",
            "f uck ing",
            "fuc kin g",
            "fu cki ng",
            "f uck ing",
            "f ucked",
            "fu cked",
            "fuc ked",
            "fuck ed",
            "fucke d",
            "f uck ed",
            "p iss",
            "pis s",
            "d ick",
            "dic k",
            "n igg er",
            "ni gge r",
            "nig ger",
            "nigg er",
            "ni gger",
            "n igg a",
            "ni gga",
            "nig ga",
            "nigg a",
            "n igga",
            "f agg ot",
            "fag go t",
            "fa ggo t",
            "faggo t",
            "fagg ot",
            "fag got",
            "fa ggot",
            "f aggot",
            "w hor e",
            "who re",
            "wh ore",
            "w hore",
            "wh ore",
            "who re",
            "whor e",
            "c ock",
            "coc k",
            "b itc h",
            "bi tch",
            "bit ch",
            "b itch",
            "bi tch",
            "bit ch",
            "bitc h",
            "fuc k",
            "f uck",
            "ba stard",
            "basta rd",
            "b ast ard",
            "bastar d",
            "b astard"]

statuses = ["the universe is larger than the universe in the multiverse but some of the universes are smaller than the universe",
            "trying to get some friends",
            "eating tacos",
            "going fishing",
            "Minecraft",
            "banning tiktok cuz its trash",
            "learning how to drive a car",
            "studying",
            "breathing",
            "with my friends",
            "swimming",
            "trying to make a new world record",
            "with my parrot",
            "eating cheesecake",
            "trying to win the lottery",
            "hacking into all servers",
            "roasting my friends",
            "with my flamethrower",
            "making a movie",
            "getting a girlfrend",
            "stupid",
            "i love you ♥"]

custom_questions = {}

def getRandomMessageFromArray(array):
    return array[random.randint(0, len(array) - 1)]


def getRandomWeightedMessage(dict):
    total_weight = 0
    number = 0

    for i in dict:
        total_weight += dict[i]

    number = random.randint(1, total_weight)

    for i in dict:
        if number <= dict[i]:
            return i
        else:
            number -= dict[i]


async def findQuestionAndRespond(message, userInput, dict):
    inputArray = []
    for i in dict:
        inputArray.append(i)

    closest_input = difflib.get_close_matches(
        userInput, inputArray, n=1, cutoff=0.7)
    if len(closest_input) > 0:

        await kbm.sendMessageAndPrint(message, dict[closest_input[0]])

        return True
    else:
        return False


async def weightedRespond(message, userInput, dictionary):
    weights_array = []
    messages = []
    input_array = []

    for i in dictionary:
        input_array.append(i)

    closest_input = difflib.get_close_matches(
        userInput, input_array, n=1, cutoff=0.7)
    if len(closest_input) > 0:
        output_dict = dictionary[closest_input[0]]

        messageToSend = getRandomWeightedMessage(output_dict)

        if not userInput in input_array:
            docy.saveFails("-- " + userInput + " response: " + messageToSend)

        await kbm.sendMessageAndPrint(message, messageToSend)

        return True
    else:
        return False

async def customMessage(message, player_input: str):
    global custom_questions

    svp.setSaveFileName("data/custom_messages.pkl")
    custom_questions = svp.getString(message.guild.name + " custom questions", {})

    inputArray = []
    for i in custom_questions:
        inputArray.append(i)

    if len(inputArray) == 0:
        return

    closest_input = difflib.get_close_matches(
        player_input, inputArray, n=1, cutoff=0.7)

    if len(closest_input) > 0:
        await kbm.sendMessageAndPrint(message, custom_questions[closest_input[0]])
        return True
    else:
        return False

async def saveCustomMessage(message, player_input: str):
    global custom_questions

    player_input = player_input.split(":")

    svp.setSaveFileName("data/custom_messages.pkl")
    custom_questions = svp.getString(message.guild.name + " custom questions", {})

    print(player_input)
    print(custom_questions)

    inputArray = []
    for i in custom_questions:
        inputArray.append(i)

    custom_message_count = len(inputArray)

    if player_input[0] == "add":
        if custom_message_count < 50:
            if not player_input[1] in inputArray:
                custom_questions[player_input[1]] = player_input[2]
                await kbm.sendMessageAndPrint(message, f"added custom message. you have {custom_message_count + 1} / {50} custom messages")
                svp.saveString(message.guild.name + " custom questions", custom_questions)
            else:
                await kbm.sendMessageAndPrint(message, "you already have this custom message added")
        else:
            await kbm.sendMessageAndPrint(message, "you cannot have more than 50 custom messages")

    elif player_input[0] == "edit":
        if player_input[1] in inputArray:
            custom_questions[player_input[1]] = player_input[2]
            await kbm.sendMessageAndPrint(message, "edited message")
            svp.saveString(message.guild.name + " custom questions", custom_questions)
        else:
            await kbm.sendMessageAndPrint(message, "could not find message to edit")

    elif player_input[0] == "delete":
        if player_input[1] in inputArray:
            custom_questions.pop(player_input[1])
            svp.saveString(message.guild.name + " custom questions", custom_questions)
            await kbm.sendMessageAndPrint(message, f"deleted the message. you have {custom_message_count - 1} / {50} custom messages")
        else:
            await kbm.sendMessageAndPrint(message, "could not delete message")

    elif player_input[0] == "list":
        values = ""
        for i in custom_questions:
            values += f"{i} : {custom_questions[i]}\n"

        await kbm.sendMessageAndPrint(message, values)

    else:
        await kbm.sendMessageAndPrint(message, "unknown mode. the modes are add, edit, delete, and list")
