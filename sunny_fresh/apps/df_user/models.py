from django.db import models

from datetime import datetime

from df_goods.models import GoodsInfo


class UserInfo(models.Model):

    uname = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    upwd = models.CharField(max_length=40, verbose_name="用户密码", blank=False)
    uemail = models.EmailField(verbose_name="邮箱")
    ushou = models.CharField(max_length=20, default="", verbose_name="收货地址")
    uaddress = models.CharField(max_length=100, default="", verbose_name="地址")
    uyoubian = models.CharField(max_length=6, default="", verbose_name="邮编")
    uphone = models.CharField(max_length=11, default="", verbose_name="手机号")
    uconsumed=models.IntegerField(default=0, verbose_name="已消费金额")
    u10coupon=models.IntegerField(default=0, verbose_name="十元优惠券")
    u20coupon = models.IntegerField(default=0, verbose_name="二十元优惠券")
    u30coupon = models.IntegerField(default=0, verbose_name="三十元优惠券")
    ulotterycount = models.IntegerField(default=1, verbose_name="用户剩余抽奖次数")
    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname


class GoodsBrowser(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="浏览时间")

    class Meta:
        verbose_name = "用户浏览记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}浏览记录{1}".format(self.user.uname, self.good.gtitle)

class GoodsComment(models.Model):
    
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")
    description = models.TextField(max_length=200, verbose_name="评论内容",)
    class Meta:
        verbose_name = "商品评论"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{0}对商品{1}的评论{2}".format(self.user.uname, self.good.gtitle,self.create_time)

