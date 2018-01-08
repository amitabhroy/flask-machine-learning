class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production environment
    """
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

