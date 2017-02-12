import asyncio, sys
import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()
async def test():
    await orm.crate_pool(loop=loop, host='localhost', port=3306, user='root', password='root', db='test')
    u = User(name='hehe', email='a@example.com', passwd='123456', image='about:blank')
    await u.save()
    # print(u)
    r = await User.findAll()
    print(1, r)
    await orm.destroy_pool()
loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)
