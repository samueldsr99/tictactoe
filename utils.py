from os import system, name
import sys


# colors
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def has_color(stream):
    if not (hasattr(stream, "isatty") and stream.isatty):
        return False
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False


has_color = has_color(sys.stdout)


def cprint(text, colour=WHITE):
    if has_color:
        seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
        sys.stdout.write(seq)
    else:
        sys.stdout.write(text)


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
