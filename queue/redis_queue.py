import redis
import json

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

def publish_task(task):

    redis_client.publish(
        "agent_tasks",
        json.dumps(task)
    )

def consume_task():

    pubsub = redis_client.pubsub()

    pubsub.subscribe("agent_tasks")

    for message in pubsub.listen():

        if message["type"] == "message":

            print("Received:", message["data"])