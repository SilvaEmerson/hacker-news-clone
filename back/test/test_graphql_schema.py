import json

from graphene_django.utils.testing import GraphQLTestCase
from hackernewsclone.graphql_config import schema


QUERY = """
    query {
        allPosts {
            id
            title
        }
    }"""

WRONG_QUERY = """
    query {
        allPosts {
            id
            content
        }
    }"""


ADD_WRITER_MUTATION = """
    mutation {
        addWriter(input: {name: "Luis"}){
            writer{
                name
                id
            }
        }
  }"""


ADD_POST_MUTATION = """
mutation {
    addPost(input: {title: "101 Things You Shouldn't Know", author: "Louis"}){
        post{
            title
                author{
                    name
                }
            }
    }
}
"""

ADD_WRITER_MUTATION_WRONG = """
    mutation {
        addWriter(input: {age: 18}){
            writer{
                name
                id
            }
        }
  }"""


class MainTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_allPosts_query_should_return_no_errors(self):
        response = self.query(QUERY)
        self.assertResponseNoErrors(response)

    def test_allPosts_query_should_return_errors(self):
        response = self.query(WRONG_QUERY)
        self.assertResponseHasErrors(response)

    def test_addWriter_mutation_should_return_no_errors(self):
        response = self.query(ADD_WRITER_MUTATION)
        self.assertResponseNoErrors(response)

    def test_addWriter_mutation_should_return_errors(self):
        response = self.query(ADD_WRITER_MUTATION_WRONG)
        self.assertResponseHasErrors(response)

    def test_addPost_mutation_should_return_no_errors(self):
        response = self.query(ADD_POST_MUTATION)
        self.assertResponseNoErrors(response)

    def test_addPost_mutation_should_return_None(self):
        response = self.query(ADD_POST_MUTATION)
        content = json.loads(response.content)["data"]["addPost"]["post"]
        self.assertIsNone(content)

    def test_addPost_mutation_should_not_return_None(self):
        add_author_query = self.query(
            """
        mutation{
            addWriter(input: {name: "Louis"}){
                writer{
                    id
                    name
                }
            }
        }
        """
        )
        self.assertResponseNoErrors(add_author_query)
        response = self.query(ADD_POST_MUTATION)
        content = json.loads(response.content)["data"]["addPost"]["post"]
        self.assertIsNotNone(content)
