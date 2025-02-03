from fastapi_jwt_auth import AuthJWT
from fastapi import Depends
from my_project.blogs.models import Blog
from http import HTTPStatus
from my_project import language as common_language
from my_project import constants
from my_project.users import language as user_language


# Blog CREATE, UPDATE, READ and DELETE
class BlogCRUD:

    @staticmethod
    def get_blog(blog_id: int, ):
        """
        This method taken blog id and send the blog details.
        :param blog_id: blog id
        :return:tuple of Response components, For success or Error
        """
        if not (blog := Blog.get_blog(blog_id)):
            response = common_language.Response(status_code=HTTPStatus.NOT_FOUND,
                                                message=constants.ERR_BLOG_NOT_EXISTS.format(blog_id))
            return response.send_error_response()
        return blog

    @staticmethod
    def create_blog(request, authorize: AuthJWT = Depends()):
        """
        This method takes all required parameters and create blog.
        :param request: schema object of blog data.
        :param authorize:
        :return: tuple of Response components, For success or Error
        """
        req_data = user_language.convert_data_into_json(request)
        current_user = authorize.get_jwt_subject()
        req_data["owner_id"] = current_user
        if not (Blog.save_blog(req_data)):
            return common_language.Response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                            message=constants.ERR_SQL_ALCHEMY_ERROR).send_error_response()
        success_msg = constants.MSG_REGISTER_BLOG_SUCCESSFULLY.format(current_user)
        return common_language.Response(status_code=HTTPStatus.CREATED, message=success_msg).send_success_response()

    @staticmethod
    def update_blog(blog_id, request, authorize: AuthJWT = Depends()):
        """
        This method is used to update the current user blog.
        :param blog_id: id of blog.
        :param request: schema request data
        :param authorize:
        :return: tuple of Response components, For success or Error
        """
        req_data = user_language.convert_data_into_json(request)
        current_user = authorize.get_jwt_subject()
        if not (Blog.check_current_user_blog(blog_id, current_user)):
            return common_language.Response(status_code=HTTPStatus.BAD_REQUEST,
                                            message=constants.ERR_BLOG_NOT_EXISTS.format(
                                                blog_id)).send_error_response()

        if not (Blog.update_blog_in_db(blog_id, req_data, current_user)):
            return common_language.Response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                            message=constants.ERR_SQL_ALCHEMY_ERROR).send_error_response()
        return common_language.Response(status_code=HTTPStatus.OK,
                                        message=constants.MSG_UPDATE_BLOG).send_success_response()

    @staticmethod
    def delete_blog(blog_id, authorize: AuthJWT = Depends()):
        """
        This method is used to delete the current user blog.
        :param blog_id: id of blog.
        :param authorize:
        :return: tuple of Response components, For success or Error.
        """
        current_user = authorize.get_jwt_subject()

        if not (Blog.check_current_user_blog(blog_id, current_user)):
            return common_language.Response(status_code=HTTPStatus.BAD_REQUEST,
                                            message=constants.ERR_BLOG_NOT_EXISTS.format(
                                                blog_id)).send_error_response()

        if not (Blog.delete_blog(blog_id, current_user)):
            return common_language.Response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                            message=constants.ERR_SQL_ALCHEMY_ERROR).send_error_response()
        return common_language.Response(status_code=HTTPStatus.NO_CONTENT,
                                        message=constants.MSG_DELETED_BLOG).send_success_response()
