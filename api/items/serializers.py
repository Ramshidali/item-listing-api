from rest_framework import serializers

from items.models import Item, ItemUnits


class ItemUnitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemUnits
        fields = ('UnitId','NoOfUnits','Rate')


class ItemSerializer(serializers.ModelSerializer):
    itemUnits = ItemUnitsSerializer(many=True)

    class Meta:
        model = Item
        fields = ['ItemName','MRP','itemUnits']

    def create(self, validated_data):
        print("create")
        data = validated_data.pop('itemUnits')
        ItemId = Item.objects.create(**validated_data)
        for i in data :
            ItemUnits.objects.create(ItemId=ItemId, **i)
        return ItemId


    def update(self, instance, validated_data):
        data = validated_data.pop('itemUnits')
        ItemId = Item.objects.filter(pk=instance.pk).update(**validated_data)
        return ItemId


class GetItemSerializer(serializers.ModelSerializer):
    itemUnits = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['ItemName','MRP','itemUnits']

    def get_itemUnits(self,instance) :
        units_serializer = []

        if ItemUnits.objects.filter(ItemId__pk = instance.pk).exists():
            units = ItemUnits.objects.filter(ItemId__pk = instance.pk)
            units_serializer = ItemUnitsSerializer(units,many=True).data

        return {
            "itemUnits" : units_serializer,
        }