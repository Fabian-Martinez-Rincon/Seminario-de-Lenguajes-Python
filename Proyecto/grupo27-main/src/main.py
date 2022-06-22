'''Initialize the execution of the application and configure everything necessary.'''
from . import constants, controllers as ctr
from .assets import app_icon
from .handlers import window


def main() -> None:
    '''Creates the application.

    - Set up everything necessary.
    - Initialize it.
    - Runs the event loop.'''

    window_ctr = window.WindowController(constants.PATH_SCREENS)

    window_ctr.init(
        ctr.settings.starting_page,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )

    window_ctr.loop()


def main_dev(args: list[str]) -> None:
    '''Creates the application on developer mode.

    - Set up everything necessary.
    - Initialize it.
    - Runs the event loop.

    Args:
        args: list of developer arguments passed through the command line.'''

    HELP_MESSAGE = '''Available arguments:
    --to=<seconds> : defines the duration in seconds of inactivity until application closes, default 5 seconds
    --is=<screen name> : defines the starting screen of the application, default -SELECT-PROFILE-
    --el=<true | false> : enables event loggin, default false'''

    duration = 5 * 1000
    initial_screen = '-SELECT-PROFILE-'
    event_logging = False
    for arg in args:
        match arg.split('='):
            case '--to', timeout:
                if not timeout.isdecimal():
                    print(
                        f'Argument error: value for --to must be an integer, invalid \'{timeout}\''
                    )
                    return
                timeout = int(timeout)
                if timeout == 0:
                    print(f'Argument error: value for --to must be greater than 0')
                    return
                duration = int(timeout) * 1000
            case '--is', screen:
                initial_screen = screen
            case '--el', state:
                if state not in ('true', 'false'):
                    print(
                        f'Argument error: value for --el must be \'true\' or \'false\', invalid \'{state}\''
                    )
                    return
                event_logging = state == 'true'
            case arg if arg[0].startswith('--help'):
                print(HELP_MESSAGE)
                return
            case any:
                print(
                    f'Argument warning: \'{"=".join(any)}\' is not valid,'
                    ' use --help to see available arguments'
                )

    window_ctr = window.WindowController(constants.PATH_SCREENS)

    if not window_ctr.screen_ctr.is_registered(initial_screen):
        print(
            f'Screen error: initial screen \'{initial_screen}\' is not registered'
        )
        return

    ctr.observer.enable_logging(event_logging)

    window_ctr.init(
        initial_screen,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )

    window_ctr.set_timeout(duration, constants.EXIT_APPLICATION)

    window_ctr.loop()
