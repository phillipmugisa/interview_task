from django.shortcuts import render
from django.views import View
from openpyxl import load_workbook
from django.conf import settings
import os

def search_excel(name, filepath):
    results = []

    workbook = load_workbook(filename=filepath)
    sheet = workbook.active
    # loop through name column(A)
    for cell in sheet["A"]:
        print(cell)

    return results

class HomeView(View):
    template_name = "manager/index.html"
    context_data = {
        "page_name": "Home View"
    }

    def get(self, request):
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        name = request.POST.get("name")

        filepath = os.path.join(settings.BASE_DIR, "static/excel_files/sample.xlsx")
        results = search_excel(name, filepath)
        self.context_data["results"] = results
        return render(request, template_name=self.template_name, context=self.context_data)