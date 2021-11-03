from django.shortcuts import render
from django.http import HttpResponse
import random

# from .forms import NewPostForm


# skats
def pirmais_skats(request):

	# ja submit, tad metode ir POST
	if request.method == 'POST':
								# input nosaukums
		full_name = request.POST['full_name']
		mathematics = int(request.POST['mathematics'])
		latvian = int(request.POST['latvian'])
		foreign = int(request.POST['foreign'])

		response = full_name + ' can apply to university.'
		if mathematics < 40 or latvian < 40 or foreign < 40:
			response = full_name + ' can not apply to university.'

		if mathematics not in range(101) or latvian not in range(101) or foreign not in range(101):
			response = 'Marks are out of range!'

		return HttpResponse(response)

	# šis parādās pie metodes GET (kad ievadam /show-name)

	return render(request, template_name='form.html',)


def motivate_view(request):
	x = random.randint(1,5)
	return HttpResponse(x)



def ierasanaas_skats(request):

	# ja submit, tad metode ir POST
	if request.method == 'POST':
								# input nosaukums

		full_name = request.POST['visitor_name']
		date = request.POST['date_time']
		reason = request.POST['reason_why']


		teksts = "<font style='font-family: Arial'><b>" + full_name + " will arive at " + date + "</b><br>Reason: " + reason + "</font>"

		return HttpResponse(teksts)

	return render(request, template_name='ierasanas_template.html', )

