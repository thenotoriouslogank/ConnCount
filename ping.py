import ipaddress
import asyncio

async def ping(host):
    host = str(host)
    proc = await asyncio.create_subprocess_shell(
        f'ping {host} -c 1',
        stderr=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.DEVNULL
        )
    stdout,stderr = await proc.communicate()
    if proc.returncode == 0:
        f = open('ip', 'a')
        f.write(f'{host} \n')

loop = asyncio.get_event_loop()
tasks = []

mynet = ipaddress.ip_network('192.168.0.0/24')
for host in mynet.hosts():
    task = ping(host)
    tasks.append(task)

tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)