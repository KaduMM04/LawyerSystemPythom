from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, AdvogadoViewSet, ProcessoViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet, basename="cliente")
router.register(r"advogados", AdvogadoViewSet, basename="advogado")
router.register(r"processos", ProcessoViewSet, basename="processo")

urlpatterns = router.urls
