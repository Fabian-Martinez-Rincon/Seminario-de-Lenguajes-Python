'''Contiene diccionarios con configuraciones predeterminadas.'''
SETTINGS = {
    'default': {
        'title': 'Figurace',
        'full_screen': True,
        'starting_page': '-INTRODUCTION-',
        'theme': 'Blue-Like',
        'default_user': ''
    },
}
DIFFICULTIES = {
    'easy': {
        'time_per_round': 60,
        'rounds_per_game': 10,
        'points_correct_answer': 10,
        'points_bad_answer': 0,
        'characteristics_shown': 4
    },
    'normal': {
        'time_per_round': 50,
        'rounds_per_game': 10,
        'points_correct_answer': 12,
        'points_bad_answer': -2,
        'characteristics_shown': 3
    },
    'hard': {
        'time_per_round': 40,
        'rounds_per_game': 10,
        'points_correct_answer': 15,
        'points_bad_answer': -5,
        'characteristics_shown': 2
    },
    'insane': {
        'time_per_round': 30,
        'rounds_per_game': 10,
        'points_correct_answer': 20,
        'points_bad_answer': -10,
        'characteristics_shown': 1
    },
    'custom': {
        'time_per_round': 50,
        'rounds_per_game': 10,
        'points_correct_answer': 12,
        'points_bad_answer': -2,
        'characteristics_shown': 3
    },
}
DIFFICULTY_NAME = 'normal'
THEMES = {
    'Blue-Like': {
        'BG_BASE': '#112B3C',
        'BG_PRIMARY': '#1A5276',
        'BG_SECONDARY': '#39769C',
        'F_C_ACCENT': '#F0F0F0',
        'F_C_PRIMARY': '#CCDAE3',
        'F_C_SECONDARY': '#B6C4CC',
        'F_F_UI': 'System',
        'F_F_CONTENT': 'Consolas',
        'F_SIZE_H1': 86,
        'F_SIZE_H2': 48,
        'F_SIZE_H3': 32,
        'F_SIZE_H4': 26,
        'F_SIZE_T1': 24,
        'F_SIZE_T2': 16,
        'F_SIZE_T3': 8,
        'BD_ACCENT': 16,
        'BD_PRIMARY': 12,
        'BD_SECONDARY': 6,
        'BD_DELIMITER': 2,
        'BG_BUTTON': '#6FC5FF',
        'BG_BUTTON_DISABLED': '#ADCFE6',
        'BG_BUTTON_HOVER': '#5A9ECC',
        'F_C_BUTTON': '#243F50',
        'F_C_BUTTON_DISABLED': '#4F616C',
        'F_C_BUTTON_HOVER': '#37576B',
        'BG_POPUP': '#178EBC',
        'ERROR_BG_ACCENT': '#EF190C',
        'ERROR_BG_NORMAL': '#E42A1F',
        'ERROR_BG_SOFT': '#CD4840'
    }
}
