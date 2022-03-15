import asyncio
import platform
from core.logger import Logger

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def run_async(func, *args, executor=None):
    """Runs an action in an asyncronous executor"""

    return await asyncio.get_event_loop().run_in_executor(executor, func, *args)


async def run_safe(func, *args, **kwargs):
    """Run an async function in safe mode"""

    try:
        result = await func(*args, **kwargs)
        return {
            'content': result,
            'success': True
        }
    except Exception as ex:
        return {
            'content': ex.message if 'message' in ex.__dict__ else ex.__str__(),
            'success': False
        }
