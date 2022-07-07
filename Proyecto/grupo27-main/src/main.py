'''Inicializa la ejecución de la aplicación y configura todo lo necesario.'''
from . import constants, controllers as ctr
from .assets import app_icon
from .handlers import window


def main() -> None:
    '''Crea la aplicación.

    - Setear todo lo necesario.
    - Inicializarlo.
    - Ejecuta el bucle de eventos..'''

    window_ctr = window.WindowController(constants.PATH_SCREENS)

    window_ctr.init(
        ctr.settings.starting_page,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )

    window_ctr.loop()


def main_dev(args: list[str]) -> None:
    '''Crea la aplicación en modo desarrollador.

    - Setea todo lo necesario.
    - Inicializarlo.
    - Ejecuta el bucle de eventos.

    Argumentos:
        args: lista de argumentos de desarrollador pasados a través de la línea de comando'''

    HELP_MESSAGE = '''Argumento disponibles:
    --to=<seconds> : define la duración en segundos de inactividad hasta que se cierra la aplicación, por defecto 5 segundos
    --is=<screen name> : define la pantalla de inicio de la aplicación, por defecto -SELECT-PROFILE-
    --el=<true | false> : Habilita el registro de eventos, predeterminado falso'''

    duration = 5 * 1000
    initial_screen = '-SELECT-USER-'
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

