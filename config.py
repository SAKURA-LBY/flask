from datetime import timedelta


class BaseConfig:
    """配置基类  可以将相同的配置抽取到基类中, 减少重复代码"""

    # 定义和配置同名的类属性
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


class DevelopmentConfig(BaseConfig):
    """开发环境"""
    SQL_URL = '127.0.0.1:3306/test1'  # 数据库地址


class ProductionConfig(BaseConfig):
    """生产环境"""
    SQL_URL = '222.10.15:3306/users'  # 数据库地址
config_dict={'dev':DevelopmentConfig,'pro':ProductionConfig}