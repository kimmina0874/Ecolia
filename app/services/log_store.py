logs = []

def add_log(msg):
	if len(logs) > 100:
		logs.pop(0)
	logs.append(msg)

def get_logs():
	return logs[::-1]
