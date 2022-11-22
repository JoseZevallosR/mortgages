from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import tablesForm

import json

import pandas as pd
# Create your views here.
#https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/

#https://stackoverflow.com/questions/72561111/send-post-from-js-to-django
#https://ridwanray.medium.com/django-and-fetch-api-form-submissions-without-page-reloading-dc5106598005
#how to sent a json object with javascript back to django post method

def home(request):
	return render(request,'home.html')


class MyView(View):
	form_class = tablesForm
	template_name = 'editable/tables_form.html'

	def get(self,request,*args, **kwargs):
		form = self.form_class()
		ctx ={'form':form}
		return render(request,self.template_name,ctx)

	def post(self,request,*args, **kwargs):
		form = self.form_class(request.POST,request.FILES)
		ctx={'form': form}
		if form.is_valid():
			bc_data = request.FILES['file_upload']
			tables = pd.read_excel(bc_data,sheet_name='tdis').to_html(classes=["table", "table-hover"],justify='center',index=False,table_id='time_dis')#, justify='center'
			tables = tables.replace('<td>', '<td class="editable" align="center">')
			ctx['tables'] = tables
			return render(request,self.template_name,ctx)

		return render(request, self.template_name, ctx)


class MyEdit(View):
	
	template_name = 'editable/edit_table.html'

	def get(self,request,*args, **kwargs):
		bc_data = '/home/wk-gida1/Documentos/Jose/mortgages/mortages/Transient_boundary_conditions.xlsx'
		ctx={}
		tables = pd.read_excel(bc_data,sheet_name='tdis').to_html(classes=["table", "table-hover"],justify='center',index=False,table_id='time_dis')#, justify='center'
		tables = tables.replace('<td>', '<td class="editable" align="center">')
		ctx['tables'] = tables

		return render(request,self.template_name,ctx)

	def post(self,request,*args, **kwargs):
		
		ctx = {}
		print(self.request.POST)
		
		return render(request, self.template_name, ctx)