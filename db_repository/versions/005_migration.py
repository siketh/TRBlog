from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=10000)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
    Column('abstract', VARCHAR(length=1000)),
    Column('title', VARCHAR(length=100)),
    Column('repo_url', VARCHAR(length=200)),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('abstract', String(length=1000)),
    Column('body', String(length=10000)),
    Column('created', DateTime),
    Column('updated', DateTime),
    Column('repo_url', String(length=200)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['timestamp'].drop()
    post_meta.tables['post'].columns['created'].create()
    post_meta.tables['post'].columns['updated'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['timestamp'].create()
    post_meta.tables['post'].columns['created'].drop()
    post_meta.tables['post'].columns['updated'].drop()
