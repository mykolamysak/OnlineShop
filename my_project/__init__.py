import config
from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from my_project import exceptions
from my_project import constants


@AuthJWT.load_config
def get_config():
    return config.Settings()


def create_app():
    """
    Construct the core application.
    The whole function can be divided in 3 steps below

        >> Create a fast api app object, which derives configuration values
        (either from a Python class, a config file, or environment variables).
        >> Import the logic which makes up our app (such as routes).
        >> Register routers   .

    """
    # callback to get your configuration

    app = FastAPI(title="fast-api-project", description=constants.DESCRIPTION, version="1.0.1", exception_handlers={
        AuthJWTException: exceptions.authjwt_exception_handler}, )

    from my_project.users.views import router as user_router
    from my_project.blogs.views import router as blog_router
    # register router
    app.include_router(user_router)
    app.include_router(blog_router)

    return app
