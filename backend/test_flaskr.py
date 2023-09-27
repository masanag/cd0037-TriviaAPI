import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(len(data['categories']), 6)
        self.assertEqual(data['categories']['1'], 'Science')

    def test_retrieve_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 10)
        self.assertEqual(data['total_questions'], 19)
        self.assertEqual(len(data['categories']), 6)

    def test_retrieve_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 3)

    def test_search_questions(self):
        res = self.client().post('/questions', json={'searchTerm': 'title'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 2)

    # def test_create_question(self):
    #     res = self.client().post('/questions', json={
    #         'question': 'What is the capital of the USA?',
    #         'answer': 'Washington DC',
    #         'category': 3,
    #         'difficulty': 1
    #     })
    #     data = json.loads(res.data)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/1')
    #     data = json.loads(res.data)
    #     self.assertEqual(data['success'], True)

    # Create a POST endpoint to get questions to play the quiz.
    # This endpoint should take category and previous question parameters
    # and return a random questions within the given category,
    # if provided, and that is not one of the previous questions.
    # TEST: In the "Play" tab, after a user selects "All" or a category,
    # one question at a time is displayed, the user is allowed to answer
    # and shown whether they were correct or not.
    def test_play_quize(self):
        res = self.client().post('/quizzes', json={
            'previous_question': [1, 2, 3],
            'quiz_category': {'type': 'Science', 'id': 1}
        })
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertEqual(data['question']['category'], 1)
        self.assertNotIn(data['question']['id'], [1, 2, 3])


    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)

    def test_422_create_question(self):
        res = self.client().post('/questions', json={
            'question': 'What is the capital of the USA?',
            'answer': 'Washington DC',
            'category': 'Art',
            'difficulty': 1
        })
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertEqual(data['error'], 422)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()