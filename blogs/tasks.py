from celery import shared_task

@shared_task
def test_task(name):
    print(f'Hello, {name}!')
    return f'Processed task for {name}'
