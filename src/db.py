from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Session = sessionmaker()
Base = declarative_base()

# haroでModelを追加した場合、
# alembicでimportしているBaseに紐付けるためModelをimportしてください
# [例]:from haro.plugins.user_models import User # noqa
from haro.plugins.water_models import WaterHistory  # noqa
from haro.plugins.redbull_models import RedbullHistory  # noqa
from haro.plugins.kintai_models import KintaiHistory  # noqa
from haro.plugins.alias_models import UserAliasName  # noqa
from haro.plugins.cleaning_models import Cleaning  # noqa
from haro.plugins.create_models import CreateCommand, Term  # noqa
from haro.plugins.kudo_models import KudoHistory  # noqa
from haro.plugins.thx_models import ThxHistory  # noqa
from haro.plugins.redmine_models import RedmineUser, ProjectChannel  # noqa


def init_dbsession(config, prefix='sqlalchemy.'):
    """configに設定した値でDBの設定情報を初期化

    :param dict config: configから生成したdictの設定値
    :param str prefix: configのoption名から取り除く接頭辞
    :return: `~sqlalchemy.orm.session.Session` インスタンス
    """
    options = dict((key[len(prefix):], config[key])
                   for key in config
                   if key.startswith(prefix))
    options['_coerce_config'] = True
    url = options.pop('url')
    try:
        engine = create_engine(url, pool_size=20, **options)
    except TypeError:
        # SQLiteの場合pool_sizeは指定できないので暫定対応
        engine = create_engine(url, **options)
    Session.configure(bind=engine)
    Base.metadata.bind = engine
    return Session
