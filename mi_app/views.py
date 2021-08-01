from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import locale

locale.setlocale(locale.LC_ALL, "es-CL")  # cambia el idioma a español de Chile

# ejemplos básicos
def index(request):
    return HttpResponse("probando mi 1er proyecto")


# fotos
def fotos(request):
    context = {
        "imgs": [
            "https://scontent.fscl22-1.fna.fbcdn.net/v/t1.6435-9/153563935_2860075567603087_660622751330902851_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=0debeb&_nc_eui2=AeGLz6DUYFubfMLKOin-48JG8zsuZgs6YUzzOy5mCzphTKSepd6gbvILiR7nE8Y4ve-dtOBoLcHXCcceJxnaVySr&_nc_ohc=XkgDoGKpnd0AX_qjP5T&_nc_ht=scontent.fscl22-1.fna&oh=6d915efaf6871aeff777a4665f51848f&oe=612B36F5",
            "https://scontent.fscl22-1.fna.fbcdn.net/v/t1.6435-9/66033113_2349755505301765_208223613692674048_n.jpg?_nc_cat=108&ccb=1-3&_nc_sid=0debeb&_nc_eui2=AeEL4fgx5PtwSIlZfbGT1R53Caih4PZGMvkJqKHg9kYy-aZ-0ojSY-U5COCpiLswf-Jj8jL9AjnfMoi8CbXYnDzZ&_nc_ohc=EDszgkTOqm8AX864Eq5&_nc_ht=scontent.fscl22-1.fna&oh=8bc920ad0684f5764448c3b9bb090426&oe=612BCA9A",
            "https://scontent.fscl22-1.fna.fbcdn.net/v/t1.6435-9/65544659_2349118662032116_2576049958834667520_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=0debeb&_nc_eui2=AeGdhl00G_lW4W2Ln_pXMeJirgdQqobp5KSuB1CqhunkpDN0TljM6zbpkmKLJtO_XRrIK3-wzJzJ8DfTw9rFLR5h&_nc_ohc=8NDhytv5FuAAX9FsbRt&tn=zAgiZXNiUkR5SYHl&_nc_ht=scontent.fscl22-1.fna&oh=5152587e954de853cb6d0e72438fa21e&oe=6128E063",
            "https://scontent.fscl22-1.fna.fbcdn.net/v/t1.18169-9/10247440_1397383060539019_4505889245860110122_n.jpg?_nc_cat=107&ccb=1-3&_nc_sid=cdbe9c&_nc_eui2=AeHe21svTiZX1cu2BlZ_Bccx2joH9iI4ieTaOgf2IjiJ5KlaW93zBs9OJJtFHRmhAnuFeZhumGT6CYibc-oDMAoP&_nc_ohc=0DLP8syfQQMAX_F-BuK&tn=zAgiZXNiUkR5SYHl&_nc_ht=scontent.fscl22-1.fna&oh=c5c4c13e4f0909b357ff1f9803e18916&oe=61293875",
        ]
    }
    return render(request, "fotos.html", context)


# app reloj
def time_display(request):
    context = {
        "dayw": strftime("%a", localtime()),
        "day": strftime("%d de %B", localtime()),
        "date": strftime("%d %B %Y", localtime()),
        "timeH": strftime("%H", localtime()),
        "timeM": strftime("%M", localtime()),
        "timeS": strftime("%S", localtime()),
    }
    return render(request, "time_display.html", context)


# login/logout sessions
def login(request, name):
    request.session["name"] = name
    return redirect("/time_display")


def logout(request):
    del request.session["name"]
    return redirect("/fotos")
