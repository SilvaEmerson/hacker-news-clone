import json

from graphene_django.utils.testing import GraphQLTestCase
from hackernewsclone.graphql_config import schema


QUERY = """
    query {
        allPosts {
            edges {
                node {
                    id
                    title
                }
            }
        }
    }"""

WRONG_QUERY = """
    query {
        allPosts {
            edges {
                node {
                    id
                    invalidField
                }
            }
        }
    }"""


ADD_WRITER_MUTATION = """
    mutation {
        addUser(input: {username: "Luis", email:"luis@example.com", password:"abc123"}) {
            user {
              id
            }
        }
  }"""


ADD_POST_MUTATION = """
mutation {
    addPost(input: {title: "101 Things You Shouldn't Know", author: "Louis", content: "Demo"}) {
        post {
          title
          author {
            username
          }
        }
    }
}
"""

ADD_WRITER_MUTATION_WRONG = """
    mutation {
        addUser(input: {username: "Luis", email:"luis@example.com", password:"abc123"}) {
            user {
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
        mutation {
            addUser(input: {username: "Louis", email:"luis@example.com", password:"abc123"}) {
                user {
                    id
                    username
                }
            }
        }
        """
        )
        self.assertResponseNoErrors(add_author_query)
        response = self.query(ADD_POST_MUTATION)
        content = json.loads(response.content)["data"]["addPost"]["post"]
        self.assertIsNotNone(content)
