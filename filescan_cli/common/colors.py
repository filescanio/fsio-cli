import colorama


colors = {
    'malicious': colorama.Fore.RED,
    'likely_malicious': colorama.Fore.RED,
    'suspicious': colorama.Fore.YELLOW,
}


def get_verdict_color(verdict):
	verdict = verdict.lower()
	if verdict in colors:
		return colors[verdict]
	else:
		return colorama.Fore.GREEN


def colorize(text, color = colorama.Fore.GREEN):
	return color + text + colorama.Fore.WHITE
