import xadmin
from xadmin import views
from product.models import ProductInfo


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSetting:
    global_search_model = [ProductInfo]
    site_title = '运维平台'
    site_footer = '技术保障部'

    menu_style = 'accordion'

    apps_icon = {
        "product": "fa fa-music"
    }

    global_model_icon = {
        ProductInfo: "fa fa-film"
    }


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)