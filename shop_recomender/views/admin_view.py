from django.template.response import TemplateResponse
from shop_recomender.models.user import User
class AdminView:
    @staticmethod
    def see_all_users(request):
        users = User.objects.all()
        context = {"users": users}
        # print(users.query)
        return TemplateResponse(request, "admin/all_users.html", context)