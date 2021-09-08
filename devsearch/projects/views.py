from django.shortcuts import render
from django.http import HttpResponse

projectslist=[
    {
        'id': '1',
        'title': 'ecommerce website',
        'description': 'fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'portfolio website',
        'description': 'fully functional portfolio website'
    },
    {
        'id': '3',
        'title': 'social Network',
        'description': 'fully functional social Network website'
    }
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectslist}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectslist:
        if i['id'] ==pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})