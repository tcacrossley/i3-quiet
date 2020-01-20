#!/usr/bin/env python3

from subprocess import run, check_output
from i3ipc.aio import Connection
from i3ipc import Event
import asyncio

async def main():
    def on_event(self, e):
        ws = 99
        if instance == 'polybar':
            if e.current.num == ws:
                run(['polybar-msg', 'cmd', 'hide'])
            elif e.old and e.old.num == ws:
                run(['polybar-msg', 'cmd', 'show'])
        elif instance == 'i3bar':
            if e.current.num == ws:
                run(['i3-msg', 'bar mode', 'invisible'])
            elif e.old and e.old.num == ws:
                run(['i3-msg', 'bar mode', 'dock'])

    if 'i3bar' in str(check_output('ps -A | grep i3bar', shell=True)):
        instance = 'i3bar'
    elif 'process' in str(check_output('ps -A | grep process', shell=True)):
        instance = 'polybar'
    c = await Connection(auto_reconnect=True).connect()
    workspaces = await c.get_workspaces()
    c.on(Event.WORKSPACE_FOCUS, on_event)
    await c.main()

asyncio.get_event_loop().run_until_complete(main())
