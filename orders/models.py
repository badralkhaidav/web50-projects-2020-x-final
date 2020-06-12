from django.db import models

import django.utils.timezone
# Create your models here.

from django.db import models
import django.utils.timezone

# Create your models here.

class Order(models.Model):
    TAG = (
            ('Хүсэлт илгээсэн','Хүсэлт илгээсэн'),
            ('Хариу ирсэн',' Хариу ирсэн'),
            ('Бараа захиалга хийгдсэн', 'Бараа захиалга хийгдсэн'),
            ('Бараа худалдан авалт хийгдсэн','Бараа худалдан авалт хийгдсэн'),
            ('Бараа Англи дахь хаягт ирсэн','Бараа Англи дахь хаягт ирсэн'),
            ('Бараа Англиас илгээгдсэн','Бараа Англиас илгээгдсэн'),
            ('Замдаа','Замдаа'),
            ('Бараа гааль дээр','Бараа гааль дээр'),
            ('Бараа авахад бэлэн','Бараа авахад бэлэн'),
            ('Хүлээлгэн өгсөн','Хүлээлгэн өгсөн')
            )

    is_active=models.BooleanField(default=True)
    date_created=models.DateTimeField(default=django.utils.timezone.now)
    product_link=models.CharField(max_length=254,default="")
    price = models.CharField(max_length=64,default="")
    type = models.CharField(max_length=64,default="")
    amount = models.IntegerField(null=True, default=1)
    colour= models.CharField(max_length=64,default="")
    size_description = models.CharField(max_length=64,default="")
    name=models.CharField(max_length=64,default="")
    telephone=models.CharField(max_length=64,default="")
    email=models.CharField(max_length=64,default="")
    additional_info=models.CharField(max_length=254,default="")
    ip=models.CharField(max_length=64,default="")
    internal_comment=models.CharField(max_length=254,default="")
    order_id=models.IntegerField(null=True, default=1)
    status=models.CharField(default='Хүсэлт илгээсэн',choices=TAG,max_length=64)




def __str__(self):
    return f"{self.product_link} {self.price} {self.type} {self.amount} {self.colour} {self.size_description} "

class Transfer_Order(models.Model):
    TAGS = (
            ('Хүсэлт илгээсэн','Хүсэлт илгээсэн'),
            ('Хариу ирсэн',' Хариу ирсэн'),
            ('Шилжүүлэгч шилжүүлсэн', 'Шилжүүлэгч шилжүүлсэн'),
            ('Систем шалгаж байна','Систем шалгаж байна'),
            ('Хүлээн авагч руу шилжүүлсэн','Хүлээн авагч руу шилжүүлсэн'),
            ('Хүлээн авагчийн мэдээллийг шалгаж байна','Хүлээн авагчийн мэдээллийг шалгаж байна'),
            ('Хүлээгдэж байна','Хүлээгдэж байна'),
            )

    is_active=models.BooleanField(default=True)
    date_created=models.DateTimeField(default=django.utils.timezone.now)
    gbp_amount=models.CharField(max_length=254,null=False,default=1)
    gbpToMntDailyRate = models.CharField(max_length=64, null=False, default="1")
    mnt_amount=models.CharField(max_length=254,null=False,default=1)
    reference_id=models.IntegerField(null=False,default=1)
    fee= models.CharField(max_length=254,null=False,default=1)

    direction = models.CharField(max_length=64,default="")
    directionName = models.CharField(max_length=64,default="")
    reciever_name = models.CharField(max_length=64,default="")
    reciever_telephone = models.CharField(max_length=64,default="")
    reciever_email = models.CharField(max_length=64,default="")
    reciever_register = models.CharField(max_length=64,default="")
    reciever_bank = models.CharField(max_length=64,default="")
    reciever_account = models.CharField(max_length=64,default="")

    sender_name = models.CharField(max_length=64,default="")
    sender_telephone=models.CharField(max_length=64,default="")
    sender_email=models.CharField(max_length=64,default="")
    sender_postcode=models.CharField(max_length=64,default="")
    sender_ip=models.CharField(max_length=64,default="")

    additional_info=models.CharField(max_length=254,default="")
    ip=models.CharField(max_length=64,default="")
    internal_comment=models.CharField(max_length=254,default="")
    order_id=models.IntegerField(null=True, default=1)
    status=models.CharField(default='Хүсэлт илгээсэн',choices=TAGS,max_length=64)




def __str__(self):
    return f"{self.product_link} {self.price} {self.type} {self.amount} {self.colour} {self.size_description} "
