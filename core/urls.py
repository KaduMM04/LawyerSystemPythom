from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, AdvogadoViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet, basename="cliente")
router.register(r"advogados", AdvogadoViewSet, basename="advogado")

urlpatterns = router.urls
