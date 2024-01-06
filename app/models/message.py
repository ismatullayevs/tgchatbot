from tortoise import fields
from tortoise.models import Model


class Chat(Model):
    id = fields.BigIntField(pk=True)

class Message(Model):
    ROLE_CHOICES = ['user', 'assistant', 'system']

    id = fields.UUIDField(pk=True)
    message_id = fields.BigIntField(index=True)
    chat = fields.ForeignKeyField("models.Chat", related_name='messages')
    text = fields.TextField()
    role = fields.CharField(max_length=10, choices=ROLE_CHOICES)
    replied_to = fields.ForeignKeyField("models.Message", null=True, related_name='replies')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.text
