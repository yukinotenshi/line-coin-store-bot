import peewee as pw
from datetime import datetime
from playhouse.shortcuts import model_to_dict


db = pw.SqliteDatabase("data.db")


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.now)
    updated_at = pw.DateTimeField(default=datetime.now)

    def to_dict(self):
        return model_to_dict(self, recurse=False)

    def save(self, force_insert=False, only=None):
        self.updated_at = datetime.now()
        super().save(force_insert, only)

    class Meta:
        database = db


class Order(BaseModel):
    order_id = pw.IntegerField()
    items = pw.CharField()
    target_id = pw.CharField()
    status = pw.CharField()
    is_processing = pw.BooleanField(default=False)
