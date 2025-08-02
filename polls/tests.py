import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions with a future pub_date.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Future question", pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(question_text="Old question", pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(question_text="Recent question", pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_no_questions(self):
        """
        Index view should display appropriate message if no questions exist.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the index page.
        """
        question = Question.objects.create(
            question_text="Past question.", pub_date=timezone.now() - datetime.timedelta(days=30)
        )
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        """
        Questions with a future pub_date should not be displayed on the index page.
        """
        Question.objects.create(
            question_text="Future question.", pub_date=timezone.now() + datetime.timedelta(days=30)
        )
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_and_past_question(self):
        """
        Even if both future and past questions exist, only past should be shown.
        """
        past_question = Question.objects.create(
            question_text="Past question.", pub_date=timezone.now() - datetime.timedelta(days=30)
        )
        Question.objects.create(
            question_text="Future question.", pub_date=timezone.now() + datetime.timedelta(days=30)
        )
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [past_question])

    def test_two_past_questions(self):
        """
        The questions index page should display multiple past questions in reverse chronological order.
        """
        question1 = Question.objects.create(
            question_text="Past question 1.", pub_date=timezone.now() - datetime.timedelta(days=30)
        )
        question2 = Question.objects.create(
            question_text="Past question 2.", pub_date=timezone.now() - datetime.timedelta(days=5)
        )
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],  # Newer question2 should come first
        )
