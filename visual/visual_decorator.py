# Read color for error information!
def display_color(color_name='red'):
    color = {'red': '31', 'blue': '34', 'yellow': '33'}

    def _display_color(function_name):
        def __display_color(output_string):
            print '\033[1;%s;40m' % color[color_name]
            print '*' * 80
            function_name(output_string)
            print '*' * 80
            print '\033[0m'

        return __display_color

    return _display_color


@display_color('red')
def error(val):
    print '[Error]\t', val


@display_color('blue')
def info(val):
    print '[Info]\t', val


@display_color('yellow')
def warning(val):
    print '[Warn]\t', val


if __name__ == '__main__':
    error("The data format error")
    warning("The data is not complete")
    info('connect from 192.168.0.76')
