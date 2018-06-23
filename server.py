#!/usr/bin/python3
#coding=utf-8

from socket import *
import sys
import os

#µÇÂ¼
def do_login(s,H,msg,clientaddr):
    msg = msg.split(' ')
    msg[2] = "%s login..."%msg[1]
    for conn in H:
        s.sendto(msg[2].encode(),conn)

    H.append(clientaddr)

    return

#ÍË³ö
def do_quit(s,H,msg,clientaddr):
    msg = "%s log out..."%msg.split(' ')[1]
    H.remove(clientaddr)
    for conn in H:
        s.sendto(msg.encode(),conn)

    return
    

def do_chat(s,H,msg,clientaddr):

    #'B xiangzhang "miss you"'
    buf = "%s say %s"\
    %(msg.split(' ')[1],msg.split(' ')[2])
    for conn in H:
        if conn != clientaddr:
            s.sendto(buf.encode(),conn)
    return

def do_parent(s,addr):
    #msg = type + name + text
    msg = "B server "

    while True:
        print("system message >>")
        text = sys.stdin.readline()
        msg = msg + text
        s.sendto(msg.encode(),addr)
    s.close()

def do_child(s):
    H = []

    while True:
        msg,clientaddr = s.recvfrom(4096)
        msg = msg.decode()
        tmp = msg.split(' ')
    
    #'L xiaozhang '
        if tmp[0] == 'L':
            do_login(s,H,msg,clientaddr)
    #'B xiangzhang "miss you"'
        if tmp[0] == 'B':
            do_chat(s,H,msg,clientaddr)
    #'Q xiangzhang '
        if tmp[0] == 'Q':
            do_quit(s,H,msg,clientaddr)

    return

def main():
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket(AF_INET,SOCK_DGRAM,0)
    s.bind(ADDR)

    pid = os.fork()

    if pid < 0:
        print("fail to create process")
        return
    elif pid == 0:
        do_child(s)
    else:
        do_parent(s,ADDR)


if __name__ == "__main__":
    main()
