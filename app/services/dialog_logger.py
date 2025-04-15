dialogs = {
	"international": [],
	"national": [],
	"city": [],
	"village": [],
	"personal": []
}

def add_dialog(level, message):
	if level not in dialogs:
		level = "personal"
	dialogs[level].append(message)
	if len(dialogs[level]) > 100:
		dialogs[level].pop(0)

def get_dialogs(level="all"):
	if level == "all":
		return sum(dialogs.values(), [])
	return dialogs.get(level, [])
