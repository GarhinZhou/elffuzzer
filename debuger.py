#!/usr/bin/env python3
from pwn import *

context(arch='amd64', os='linux', log_level='debug')

payload=flat([
    read('./crashes/2026-03-30_12:40:58/default/crashes/id1')
])
p = process('./checkinbird')

gdb.attach(p)
pause()

p.sendline(payload)

p.interactive()