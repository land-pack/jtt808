"""
If you want to send something to your terminal!
Your need it's name & it's socket descriptor!
so we have Dicts type below to make your have latest
socket descriptor at any time! It's empty at begin.
When a terminal connect server,we'll catch it's socket
descriptor and save it to our SOCKET_DESCRIPTOR Dicts!
"""

SOCKET_DESCRIPTOR = {}
