# -*- coding: utf-8 -*-

'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/users')
async def index1(request):
     users = await User.findAll()
     return {
         '__template__' : 'test.html',
        'users' : users
     }


@get('/blogs')
async def index(request):
    summary = '呵呵呵'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at')
    for u in users:
        u.password = '******'
    return dict(users=users)