import asyncio
import sys

import httpx




SCRIPTS = [
    'RealTimeBot\Inst\SOL.py',
    'RealTimeBot\Inst\ADA.py',
    'RealTimeBot\Inst\XRP.py'
]

async def waiter(sc, p):
    await p.wait()
    return sc, p


async def main():
    waiters  = []
    
    
    for sc in SCRIPTS:
        p = await asyncio.create_subprocess_exec(sys.executable, sc)
        print('Started', sc)
        waiters.append(asyncio.create_task(waiter(sc, p)))

   
    while waiters:
        done, waiters = await asyncio.wait(waiters, return_when=asyncio.FIRST_COMPLETED)
        for w in done:
            sc,p = await w
            print('Done', sc)
        
      
if __name__ == "__main__":
    asyncio.run(main())
    