import settings


def parse_slack(input_lines):
    if input_lines and len(input_lines) > 0:
        for line in input_lines:
            print(line)
            if line and 'text' in line and line['text'].startswith(settings.BOT_NAME):
                return line['text'][len(settings.BOT_NAME):], line['channel']
    return None, None
