from django.http import HttpResponse, HttpRequest


class SkinsListView:
    def get(self, request: HttpRequest):
        template = "<html>" "Full list of Fortnite skins in 2023" "</html>"

        return HttpResponse(content=template)
