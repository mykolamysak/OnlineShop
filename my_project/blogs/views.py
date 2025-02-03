from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi_jwt_auth import AuthJWT
from my_project.blogs import services
from my_project.blogs.schemas import BlogCreateRequestSchema, BlogResponseSchema
from fastapi import status

router = InferringRouter(
    tags=["blogs"],
    prefix=""
)


@cbv(router)
class BlogResource:
    """
     https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/
    """
    Authorize: AuthJWT = Depends()
    blog_service = services.BlogCRUD()

    @router.get("/api/v1/{blog_id}/blog/", status_code=status.HTTP_200_OK, response_model=BlogResponseSchema)
    def get(self, blog_id: int):
        """
        This method is called when request method id get.
        :param blog_id: id of blog
        :return:
        """
        self.Authorize.jwt_required()
        return self.blog_service.get_blog(blog_id, )

    @router.post("/api/v1/blog/create/", status_code=status.HTTP_201_CREATED)
    def post(self, request: BlogCreateRequestSchema):
        """
        This method is called when request method is post.
        :param request: schema request data
        :return:
        """
        self.Authorize.jwt_required()
        return self.blog_service.create_blog(request, self.Authorize)

    @router.delete("/api/v1/{blog_id}/blog/", status_code=status.HTTP_204_NO_CONTENT)
    def delete(self, blog_id: int):
        """
        This method is called when request method is delete.
        :param blog_id: id of blog
        :return:
        """
        self.Authorize.jwt_required()
        return self.blog_service.delete_blog(blog_id, self.Authorize)

    @router.put("/api/v1/{blog_id}/blog/update/", )
    def put(self, blog_id: int, request: BlogCreateRequestSchema):
        """
        This method is called when request method is update.
        :param: id of blog.
        :param: schema request data.
        :return:
        """
        self.Authorize.jwt_required()
        return self.blog_service.update_blog(blog_id, request, self.Authorize)
