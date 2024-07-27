from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from characteristic.models import CharacteristicGroup, Characteristic, Combination, ExecutionTime


class CharacteristicGroupSerializer(serializers.ModelSerializer):
    """
    Сериализация `CharacteristicGroup`
    """

    class Meta:
        model = CharacteristicGroup
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    """
    Сериализация `Characteristic`
    """
    characteristicGroup = serializers.SerializerMethodField()

    class Meta:
        model = Characteristic
        fields = ['id', 'title', 'description', 'characteristicGroup']

    def get_characteristicGroup(self, instance: Characteristic):
        return CharacteristicGroupSerializer(instance.characteristic_group).data


class CombinationSerializer(serializers.ModelSerializer):
    """
    Сериализация `Combination`
    """
    characteristic_group = CharacteristicGroupSerializer()
    characteristic = CharacteristicSerializer()
    children = RecursiveField(many=True)

    class Meta:
        model = Combination
        fields = ['id', 'characteristic_group', 'characteristic', 'children']


class ExecutionTimeSerializer(serializers.ModelSerializer):
    """
    Сериализация `ExecutionTime`
    """

    class Meta:
        model = ExecutionTime
        fields = '__all__'
