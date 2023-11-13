COLOR = {  # словарь оттенков
    'orange': {
        'background1000': '#1b1b1b',
        'background500': '#292929',
        'background250': '#808080',
        'background-dominant1': '#ffa31a',
        'background-dominant2': '#ffffff',
        'warning': '#c71700',
        'background400': '#8080807a',
        'active': '#ffffff',
        'inactive': '#808080'
    },
    'black_and_white': {
        'background1000': '#212529',
        'background500': '#282c31',
        'background250': '#6e767f',
        'background-dominant1': '#ced4da',
        'background-dominant2': '#ced4da',
        'warning': '#dc2f02',
        'background400': '#6e767f7a',
        'active': '#ced4da',
        'inactive': '#6e767f'
    },
    'native_dark': {
        'background1000': '#22272e',
        'background500': '#272e35',
        'background250': '#6d7887',
        'background-dominant1': '#4895ef',
        'background-dominant2': '#cbd0df',
        'warning': '#ef6c75',
        'background400': '#6d78877a',
        'active': '#cbd0df',
        'inactive': '#6d7887'
    },
    'redux_dark': {
        'background1000': '#242526',
        'background500': '#2F3031',
        'background250': '#737373',
        'background-dominant1': '#BC98EA',
        'background-dominant2': '#EBEDF0',
        'warning': '#BC3174',
        'background400': '#7373737a',
        'active': '#EBEDF0',
        'inactive': '#737373'
    },
    'vs_code': {
        'background1000': '#252526',
        'background500': '#333333',
        'background250': '#818181',
        'background-dominant1': '#6ebbeb',
        'background-dominant2': '#d7d7d7',
        'warning': '#f5b732',
        'background400': '#8181817a',
        'active': '#d7d7d7',
        'inactive': '#818181'
    },
}


def rewrite_qss(name_file, color):  # изменение qss-файла (замена ключевых слов на hex)
    with open(name_file, 'r') as style_file:
        style_file = style_file.read()
        style_file = style_file.replace('background1000', COLOR[color]['background1000'])
        style_file = style_file.replace('background500', COLOR[color]['background500'])
        style_file = style_file.replace('background250', COLOR[color]['background250'])
        style_file = style_file.replace('background-dominant1', COLOR[color]['background-dominant1'])
        style_file = style_file.replace('background-dominant2', COLOR[color]['background-dominant2'])
        style_file = style_file.replace('warning', COLOR[color]['warning'])
        style_file = style_file.replace('background400', COLOR[color]['background400'])
        style_file = style_file.replace('inactive', COLOR[color]['inactive'])
        style_file = style_file.replace('active', COLOR[color]['active'])

        return style_file


def rewrite_qss_for_widget(style_file, color): # изменение строки (замена ключевых слов на hex)
    style_file = style_file.replace('background1000', COLOR[color]['background1000'])
    style_file = style_file.replace('background500', COLOR[color]['background500'])
    style_file = style_file.replace('background250', COLOR[color]['background250'])
    style_file = style_file.replace('background-dominant1', COLOR[color]['background-dominant1'])
    style_file = style_file.replace('background-dominant2', COLOR[color]['background-dominant2'])
    style_file = style_file.replace('warning', COLOR[color]['warning'])
    style_file = style_file.replace('background400', COLOR[color]['background400'])
    style_file = style_file.replace('inactive', COLOR[color]['inactive'])
    style_file = style_file.replace('active', COLOR[color]['active'])

    return style_file
