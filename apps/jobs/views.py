from django.shortcuts import render
from apps.index.models import Settings
from apps.jobs.models import Jobs
# Create your views here.

#JOB
def listing_single(request):
    return render(request, 'jobs/listing_single.html', locals())
def company_listing(request):
    return render(request, "jobs/company_listing.html", locals())

def company_listing_single(request):
    return render(request, 'jobs/company_listing_single.html', locals())


# CV
def cv(request):
    return render(request, "jobs/cv.html", locals())
def cv_add(request):
    return render(request, "jobs/add_cv.html", locals())
from django.http import HttpResponse

def cv_download(request):
    if request.method == 'POST':
        if request.FILES:
            # Если форма содержит файл
            uploaded_file = request.FILES['your_file_input_name']  # Замените 'your_file_input_name' на имя вашего поля для загрузки файла
            # Обработка файла, например, сохранение на сервере
            with open('путь_к_папке/имя_файла.docx', 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Здесь можете добавить дополнительную логику или обработку файла, если это необходимо

            # Возврат ответа о успешной загрузке
            return HttpResponse('Файл успешно загружен!')
        else:
            # Обработка, если файл отсутствует
            return HttpResponse('Файл не был загружен. Пожалуйста, выберите файл для загрузки.')
    else:
        # В случае, если это не POST-запрос, отображаем шаблон
        return render(request, "jobs/cv_download.html")


def about(request):
    return render(request, "base/about.html", locals())

def contact(request):
    return render(request, "base/contact.html", locals())