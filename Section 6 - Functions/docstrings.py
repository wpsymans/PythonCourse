#Banner Text formats banner text for display

def center_text(line_width: int, payload):
    """Blah Blah Blah!"""
    
    payload.center(line_width)


def format_banner_text(line_width , payload):

    test = center_text("test","test2")

    little_line = int(line_width) - 4

    if payload == "*":
        payload = "* {} *".format(" " * little_line)
        print(payload)
    else:
        center_text = payload.center(line_width - 2 )
        print("*{}*".format(center_text))


format_banner_text(80,"*")
format_banner_text(80,"sample text")