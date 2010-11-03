from django import test
from django.core.urlresolvers import reverse
from microblog.models import Microblog

class MicroblogTests(test.TestCase):

    def should_allow_posting_of_messages(self):
        Microblog.add_message('x')
        self.assertEqual(1, Microblog.objects.count())

    def should_return_most_recent_messages_first(self):
        Microblog.add_message("first")
        Microblog.add_message("second")
        timeline = Microblog.timeline()
        self.assertEqual('second', timeline[0].message)
        self.assertEqual('first', timeline[1].message)

    def should_not_allow_more_than_160_chars_in_a_message(self):
        self.assertRaises(ValueError, Microblog.add_message, 'x' * 161)


class MicroblogPageTests(test.TestCase):

    def should_allow_user_to_post_messages(self):
        client = test.Client()
        response = client.post(reverse('microblog:save'),
                                       {'message':'hi'}, follow=True)
        self.assertEqual(1, len(response.context['messages']))

    def should_show_list_of_messages(self):
        Microblog.add_message('asdfHIasdf')
        client = test.Client()
        response = client.get(reverse('microblog:index'))
        self.assertContains(text='<li>asdfHIasdf</li>', response=response)
