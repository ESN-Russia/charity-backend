import random

ADJ_LIST = [
    "attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab",
    "elegant", "fancy", "fit", "flabby", "glamorous", "gorgeous", "handsome",
    "long", "magnificent", "muscular", "plain", "plump", "quaint", "scruffy",
    "shapely", "short", "skinny", "stocky", "ugly", "unkempt", "unsightly",
    "ashy", "black", "blue", "gray", "green", "icy", "lemon", "mango", "orange",
    "purple", "red", "salmon", "white", "yellow", "aggressive", "agreeable",
    "ambitious", "brave", "calm", "delightful", "eager", "faithful", "gentle",
    "happy", "jolly", "kind", "lively", "nice", "obedient", "polite", "proud",
    "silly", "thankful", "victorious", "witty", "wonderful", "zealous"
    ]

NOUN_LIST = [
    "alligator", "ant", "bear", "bee", "bird", "camel", "cat", "cheetah",
    "chicken", "chimpanzee", "cow", "crocodile", "deer", "dog", "dolphin",
    "duck", "eagle", "elephant", "fish", "fly", "fox", "frog", "giraffe",
    "goat", "goldfish", "hamster", "hippopotamus", "horse", "kangaroo",
    "kitten", "lion", "lobster", "monkey", "octopus", "owl", "panda", "pig",
    "puppy", "rabbit", "rat", "scorpion", "seal", "shark", "sheep", "snail",
    "snake", "spider", "squirrel", "tiger", "turtle", "wolf", "zebra",
    ]

VERB_LIST = [
    "accepts", "adds", "admits", "advertises", "advises", "affords", "approves",
    "authorizes", "avoids", "borrows", "builds", "buys", "calculates",
    "cancels", "changes", "charges", "checks", "chooses", "complains",
    "completes", "confirms", "considers", "convinces", "counts", "decides",
    "decreases", "delivers", "develops", "discounts", "dismisses", "dispatches",
    "distributes", "divides", "employs", "encourages", "establishes",
    "estimates", "exchanges", "extends", "fixes", "funds", "improves",
    "increases", "informs", "installs", "invests", "invoices", "joins", "lends",
    "lengthens", "lowers", "maintains", "manages", "measures", "mentions",
    "obtains", "orders", "organizes", "owes", "owns", "packs", "participates",
    "pays", "plans", "presents", "prevents", "processes", "produces",
    "promises", "promotes", "provides", "purchases", "raises", "reaches",
    "receives", "recruits", "reduces", "refuses", "rejects", "reminds",
    "removes", "replies", "resigns", "responds", "returns", "rises", "sells",
    "sends", "separates", "shortens", "splits", "structures", "succeeds",
    "suggests"
    ]

ADVERBS_LIST = [
    "accidentally", "angrily", "anxiously", "awkwardly", "badly", "blindly",
    "boastfully", "boldly", "bravely", "brightly", "cheerfully", "coyly",
    "crazily", "defiantly", "deftly", "deliberately", "devotedly", "doubtfully",
    "dramatically", "dutifully", "eagerly", "elegantly", "enormously", "evenly",
    "eventually", "exactly", "faithfully", "finally", "foolishly", "fortunately",
    "frequently", "gleefully", "gracefully", "happily", "hastily", "honestly",
    "hopelessly", "hourly", "hungrily", "innocently", "inquisitively", "irritably",
    "jealously", "justly", "kindly", "lazily", "loosely", "madly", "merrily",
    "mortally", "mysteriously", "nervously", "obediently", "obnoxiously",
    "occasionally", "often", "perfectly", "politely", "poorly", "powerfully",
    "promptly", "quickly", "rapidly", "rarely", "regularly", "rudely", "safely",
    "seldom", "selfishly", "seriously", "shakily", "sharply", "silently",
    "slowly", "solemnly", "sometimes", "speedily", "sternly", "technically",
    "tediously", "unexpectedly", "usually", "victoriously", "vivaciously",
    "warmly", "wearily", "weekly", "wildly", "yearly",
    ]

print("Adj {}, N {}, V {}, Adv {}, total options -- {}".format(
    len(ADJ_LIST), len(NOUN_LIST), len(VERB_LIST), len(ADVERBS_LIST),
    len(ADJ_LIST) * len(NOUN_LIST) * len(VERB_LIST) * len(ADVERBS_LIST),
    ))


def generate_password():
    adj = random.choice(ADJ_LIST)
    noun = random.choice(NOUN_LIST)
    verb = random.choice(VERB_LIST)
    adverb = random.choice(ADVERBS_LIST)

    return "_".join([adj, noun, verb, adverb])
