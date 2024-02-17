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
        val = cell.value
        if "name" not in val.lower() and name.lower() == val.lower():
            results.append(val)

    return results

class HomeView(View):
    template_name = "manager/index.html"
    excel_filename = "excel_files/sample.xlsx"
    context_data = {
        "page_name": "Home View"
    }

    def get(self, request):
        self.context_data["file_name"] = self.excel_filename
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        name = request.POST.get("name")

        filepath = os.path.join(settings.BASE_DIR, "static", self.excel_filename)
        results = search_excel(name, filepath)
        self.context_data["results"] = results
        self.context_data["file_name"] = self.excel_filename

        return render(request, template_name=self.template_name, context=self.context_data)