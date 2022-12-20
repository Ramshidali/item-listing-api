import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.items.serializers import GetItemSerializer, ItemSerializer
from items.models import Item,ItemUnits

# items get and ceate view
@api_view(['GET', 'POST'])
def items(request):
    """
    List all items, or create a new item.
    """
    if request.method == 'GET':
        if Item.objects.filter().exists():
            instances = Item.objects.all()
            serializer = GetItemSerializer(instances, many=True)

            response_data = {
                "StatusCode": 200,
                "message" : "Success",
                "success" : True,
                "data" : serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)
        else :
            response_data = {
                "StatusCode": 200,
                "message" : "items not found",
                "success" : False,
                "data" : []
                }
            return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        items_serializer = ItemSerializer(data=request.data)

        if items_serializer.is_valid():
            items_serializer.save()

            response_data = {
                "StatusCode": 200,
                "message" : "item created successfully",
                "success" : True,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else :
            response_data = {
                "StatusCode": 400,
                "message" : items_serializer.errors,
                "success" : False,
            }
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def edit_item(request):
    print("edit")
    """
    Retrieve, update, delete or single view of a code items.
    params : itemid
    """
    if request.GET.get("itemid") :
        itemid = request.GET.get("itemid")
        print(itemid)

        try:
            print("try")
            item = Item.objects.get(pk=itemid)
        except Item.DoesNotExist:
            print("hi")

            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = GetItemSerializer(item)

            response_data = {
                "StatusCode": 200,
                "message" : "item details found",
                "success" : True,
                "item" : serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            item = Item.objects.get(ItemId=itemid)
            serializer = ItemSerializer(item, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                response_data = {
                    "StatusCode": 200,
                    "message" : "Item Updated successfully",
                    "success" : True,
                }

                return Response(response_data, status=status.HTTP_200_OK)
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            if Item.objects.filter(ItemId=itemid).exists():
                Item.objects.filter(ItemId=itemid).delete()
                ItemUnits.objects.filter(ItemId=itemid).delete()

                response_data = {
                    "StatusCode": 200,
                    "message" : "item deleted successfully",
                    "success" : True,
                }

                return Response(response_data, status=status.HTTP_200_OK)
            else :
                response_data = {
                    "StatusCode": 200,
                    "message" : "no item found with this itemid",
                    "success" : False,
                }

                return Response(response_data, status=status.HTTP_200_OK)
    else :
        response_data = {
            "StatusCode": 400,
            "message" : "invalid body request",
            "success" : False,
        }

        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
