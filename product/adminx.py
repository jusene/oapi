import xadmin
from import_export import resources
from xadmin import views
from xadmin.layout import Main, Fieldset, Side

from product.models import ProductInfo

from django.apps import apps


# Register your models here.
class PoductInfoResource(resources.ModelResource):

    def __init__(self):
        super(PoductInfoResource, self).__init__()
        field_list = apps.get_model('product', 'ProductInfo')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = ProductInfo
        skip_unchanged = True
        # 导入数据时，如果该数据未修改，则忽略
        report_skipped = True
        # 再导入预览页面中显示跳过的记录

        import_id_fields = ('id', )
        # 在对象标识的默认字段是id

        fields = (
            'id',
            'product_name',
            'product_picture',
            'product_describe',
            'product_manager'
        )
        # 白名单

        exclude = (
            'product_detail'
            'create_time',
            'update_time'
        )


class ProductInfoAdmin:
    form_layout = (
        Main(
            Fieldset('产品部分',
                     'product_name', 'product_describe', 'product_manager',),
            Fieldset('图片部分',
                     'product_picture', 'product_detail',),
        ),
        Side(
            Fieldset('时间部分',
                     'create_time', 'upload_time',),
        )
    )

    list_display = [
        'id',
        'product_name',
        #'product_picture',
        'product_picture_preview',
        'product_describe',
        'product_manager',
        'product_detail',
        'create_time',
        'update_time',
    ]

    ordering = ['id']

    search_fields = ['product_name', 'product_manager']
    list_filter = ['product_name', 'create_time', 'update_time']
    show_detail_fields = ['product_name', 'product_picture', 'product_detail']

    list_editable = [
        'product_name',
        'product_picture',
        'product_describe',
        'product_manager'
    ]

    list_per_page = 10

    model_icon = 'fa fa-laptop'

    import_export_args = {
        'import_resource_class': PoductInfoResource,
    }


xadmin.site.register(ProductInfo, ProductInfoAdmin)