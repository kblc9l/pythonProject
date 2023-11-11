COLOR = {
    'orange': {
        'background1000': '#1b1b1b',
        'background500': '#292929',
        'background250': '#808080',
        'background-dominant1': '#ffa31a',
        'background-dominant2': '#ffffff',
        'warning': '#c71700',
        'background400': '#8080807a'

    }
}


def rewrite_qss(name_file, color):
    with open(name_file, 'r') as style_file:
        style_file = style_file.read()
        style_file = style_file.replace('background1000', COLOR[color]['background1000'])
        style_file = style_file.replace('background500', COLOR[color]['background500'])
        style_file = style_file.replace('background250', COLOR[color]['background250'])
        style_file = style_file.replace('background-dominant1', COLOR[color]['background-dominant1'])
        style_file = style_file.replace('background-dominant2', COLOR[color]['background-dominant2'])
        style_file = style_file.replace('warning', COLOR[color]['warning'])
        style_file = style_file.replace('background400', COLOR[color]['background400'])
        return style_file


def rewrite_qss_for_widget(style_file, color):
    style_file = style_file.replace('background1000', COLOR[color]['background1000'])
    style_file = style_file.replace('background500', COLOR[color]['background500'])
    style_file = style_file.replace('background250', COLOR[color]['background250'])
    style_file = style_file.replace('background-dominant1', COLOR[color]['background-dominant1'])
    style_file = style_file.replace('background-dominant2', COLOR[color]['background-dominant2'])
    style_file = style_file.replace('warning', COLOR[color]['warning'])
    style_file = style_file.replace('background400', COLOR[color]['background400'])
    return style_file
