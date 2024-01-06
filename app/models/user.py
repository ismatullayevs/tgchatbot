from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.BigIntField(pk=True)
    first_name = fields.CharField(max_length=255, blank=True)
    last_name = fields.CharField(max_length=255, blank=True)
    # TODO: add phone number validation
    phone_number = fields.CharField(max_length=255, blank=True, null=True)
    is_premium = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    is_active = fields.BooleanField(default=True)
    #TODO: move this to chat model
    last_message = fields.OneToOneField('models.Message', related_name='user', null=True, on_delete=fields.SET_NULL)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
