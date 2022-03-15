import asyncio
import platform
from core.logger import Logger

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logger = Logger()

async def run_async(func, *args, executor=None):
    """Runs an action in an asyncronous executor"""

    return await asyncio.get_event_loop().run_in_executor(executor, func, *args)


async def run_safe(func, *args, **kwargs):
    """Run an async function in safe mode"""

    try:
        return await func(*args, **kwargs)
    except Exception as ex:
        logger.exception(ex)
        return ''
