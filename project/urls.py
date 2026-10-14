from django.http import HttpResponse, JsonResponse
from django.urls import path


def index(_request):
    return HttpResponse(
        "<!doctype html><html><head><title>Django stack fixture</title></head>"
        "<body><h1>Django stack fixture</h1></body></html>",
        content_type="text/html; charset=utf-8",
    )


def healthz(_request):
    return JsonResponse({"ok": True, "framework": "django"})


def status(_request):
    return JsonResponse({"ok": True, "framework": "django", "message": "read-only fixture"})


urlpatterns = [
    path("", index),
    path("healthz", healthz),
    path("api/status", status),
]
