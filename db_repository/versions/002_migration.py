from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('abstract', String(length=1000)),
    Column('body', String(length=10000)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=64)),
    Column('last_name', String(length=64)),
    Column('full_name', String(length=64)),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['abstract'].create()
    post_meta.tables['post'].columns['title'].create()
    post_meta.tables['user'].columns['first_name'].create()
    post_meta.tables['user'].columns['full_name'].create()
    post_meta.tables['user'].columns['last_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['abstract'].drop()
    post_meta.tables['post'].columns['title'].drop()
    post_meta.tables['user'].columns['first_name'].drop()
    post_meta.tables['user'].columns['full_name'].drop()
    post_meta.tables['user'].columns['last_name'].drop()
