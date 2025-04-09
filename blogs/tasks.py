# Test Sending message to RabbitMQ
from celery import shared_task

@shared_task
def test_task(name):
    print(f'Hello, {name}!')
    return f'Processed task for {name}'


""""
  # Use this to test sending messages in the terminal
    1. docker exec -it django_blogs python manage.py shell
    2. from blog.tasks import test_task
    3. test_task.delay("Eustace")

"""