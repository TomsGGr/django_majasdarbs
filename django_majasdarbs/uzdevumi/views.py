from django.shortcuts import render
from django.http import HttpResponse




#skats
def pirmais_skats(request):

	# ja submit, tad metode ir POST
	if request.method == 'POST':
								# input nosaukums
		full_name = request.POST['full_name']
		mathematics = int(request.POST['mathematics'])
		latvian = int(request.POST['latvian'])
		foreign = int(request.POST['foreign'])


		response = full_name +' can apply to university.'
		if mathematics < 40 or latvian < 40 or foreign < 40:
			response = full_name +' can not apply to university.'

		if mathematics not in range(101) or latvian not in range(101) or foreign not in range(101):
			response = 'Marks are out of range!'

		return HttpResponse(response)

	# šis parādās pie metodes GET (kad ievadam /show-name)

	return render(request, template_name='form.html',)



