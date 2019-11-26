from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from stdimage import StdImageField


# Create your models here.
class ProductInfo(models.Model):
    # 业务线表
    product_name = models.CharField(max_length=32, verbose_name='业务线名称')
    product_picture = StdImageField(
        upload_to='pictures/%Y%m%d',
        blank=True,
        null=True,
        variations={
            'large': (600, 400),
            'thumbnail': (100, 100, True),
            'medium': (300, 200),
        },
        delete_orphans=True,
        verbose_name="产品图片"
    )
    product_describe = models.CharField(max_length=255, verbose_name='业务线描述')
    product_manager = models.CharField(max_length=15, verbose_name='业务线负责人')
    product_detail = RichTextUploadingField(verbose_name='业务线详情', default='')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间', blank=True, null=True)

    class Meta:
        db_table = 'product_info'
        verbose_name = '业务线'
        verbose_name_plural = verbose_name

    def product_picture_preview(self):
        return '<img src="%s" />' % self.product_picture.thumbnail.url

    product_picture_preview.short_description = "产品图片"
    product_picture_preview.allow_tags = True

    def __str__(self):
        return self.product_name
