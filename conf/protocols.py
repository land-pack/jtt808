"""
0x
"""
from core.urls import pattern

JTT808 = pattern(
        ('register', 0x8100),
        ('unregister', 0x8200)
)

if __name__ == '__main__':
    print JTT808
