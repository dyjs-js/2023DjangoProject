from django.db import models

# Create your models here.


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # jango는 데이터 베이스에 저장하지 않게함 = reuse할 코드라고 말하는것
    # 그리고 rooms의 model에서 상속받게함
    class Meta:
        abstract = True
