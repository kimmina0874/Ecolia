logs = []

def add_log(message):
	if len(logs) >= 100:
		logs.pop(0)
	logs.append(message)

def get_logs():
	return logs[::-1]
