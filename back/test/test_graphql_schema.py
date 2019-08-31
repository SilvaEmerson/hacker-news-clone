import json

from graphene_django.utils.testing import GraphQLTestCase
from hackernewsclone.graphql_config import schema


QUERY = """
            query {
                allPosts {
                    id
                    title
                }
            }
            """

WRONG_QUERY = """
            query {
                allPosts {
                    id
                    content
                }
            }
            """

class MainTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_allPosts_query_should_return_no_errors(self):
        response = self.query(QUERY)
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_allPosts_query_should_return_no_error(self):
        response = self.query(WRONG_QUERY)
        content = json.loads(response.content)
        self.assertResponseHasErrors(response)

