from visual_decorator import display_color


@display_color('cyan')
def load_data(new_data, bar_word="Bytes"):
    total = new_data
    print '\r%d Bytes' % (total),
    os.write(1, '|')
    sys.stdout.flush()
