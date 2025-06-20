from django.http import HttpResponse

def address(request):
    return HttpResponse("Saya tinggal di Sukabumi.")

def phone(request):
    return HttpResponse("Nomor telepon saya: 0838-0604-5235")
