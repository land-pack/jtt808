# Blue color for tips information
def receiver_tips(host, port, time):
    print '\033[1;34;40m'
    print '*' * 50
    print '*HOST:\t', host
    print '*PORT:\t', port
    print '*TIME:\t', time
    print '*' * 50
    print '\033[0m'
