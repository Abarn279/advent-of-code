from file_importer import FileImporter

class Bot:
    def __init__(self, id, low_instr, high_instr):
        self.chips = []
        self.id = id
        self.low = low_instr
        self.high = high_instr

def get_bot(bots, id):
    return [i for i in bots if i.id == id][0]

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/10a.txt").split("\n")]

instructions = [i.split(" ") for i in inp if i.startswith("bot")]
values = [i.split(" ") for i in inp if i.startswith("value")]

# list of bot objects
bots = []

for instruction in instructions:
    bot = Bot(int(instruction[1]), (instruction[5], int(instruction[6])), (instruction[10], int(instruction[11])))
    bots.append(bot)

for value in values:
    get_bot(bots, int(value[5])).chips.append(int(value[1]))

def get_first_comparer(bots, val1, val2):
    queued_bots = [i for i in bots if len(i.chips) >= 2]
    while len(queued_bots) > 0:
        # Run instruction
        for bot in queued_bots:
            if val1 in bot.chips and val2 in bot.chips:
                return bot.id

            # run low instruction
            val = min(bot.chips)
            if (bot.low[0] == "bot"):
                get_bot(bots, bot.low[1]).chips.append(val)

            bot.chips.remove(val)

            # run high instruction
            val = min(bot.chips)
            if (bot.high[0] == "bot"):
                get_bot(bots, bot.high[1]).chips.append(val)

            bot.chips.remove(val)

        queued_bots = [i for i in bots if len(i.chips) >= 2]

print(get_first_comparer(bots, 17, 61))