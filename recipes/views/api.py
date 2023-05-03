from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
<<<<<<< HEAD
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
=======
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
>>>>>>> 4082e4074467ec78e20c991b392ca5bf96ad582e
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tag.models import Tag

from ..models import Recipe
from ..permissions import IsOwner
from ..serializers import RecipeSerializer, TagSerializer


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 1


<<<<<<< HEAD
class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    # def get(self, request):
    #     recipes = Recipe.objects.get_published()[:10]

    #     serializer = RecipeSerializer(
    #         instance=recipes,
    #         many=True,
    #         context={
    #             'request': request
    #         },)

    #     return Response(serializer.data)

    # def post(self, request):

    #     serializer = RecipeSerializer(
    #         data=request.data,
    #         context={'request': request}
    #     )

    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(
    #         author_id=1,
    #         category_id=1,
    #         tags=[1]
    #     )

    #     return Response(serializer.data, status=status.HTTP_200_OK)


class RecipeAPIv2Detail(APIView):
    def get_recipe(self, pk):
        recipe = get_object_or_404(
            Recipe.objects.get_published(),
            pk=pk
        )
        return recipe

    def get(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(
            instance=recipe,
            many=False,
            context={
                'request': request
            }
        )
        return Response(serializer.data)

    def patch(self, request, pk):
        recipe = self.get_recipe(pk)
=======
class RecipeAPIv2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Novo Contexto"] = 1234
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        category_id = self.request.query_params.get('category_id', '')

        if category_id != '' and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)

        return qs

    def get_object(self):
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(self.get_queryset(), pk=pk)

        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsOwner(), ]

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        print('RESQUEST', request.user)
        print(request.user.is_authenticated)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def partial_update(self, request, *args, **kwargs):

        recipe = self.get_object()
>>>>>>> 4082e4074467ec78e20c991b392ca5bf96ad582e
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={
                'request': request
            },
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@api_view()
def tag_api_detail(request, pk):

    tag = get_object_or_404(
        Tag.objects.filter(pk=pk))

    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={
            'request': request
        },)

    serializer = TagSerializer(instance=tag, many=False)

    return Response(serializer.data)
