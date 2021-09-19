from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, \
    StringRelatedField, PrimaryKeyRelatedField, HyperlinkedRelatedField, \
    HyperlinkedIdentityField, SerializerMethodField

from .models import Album, Track, Singer


class TrackListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['name', 'active', 'url']


class TrackDetailSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = ['name', 'active', 'singers']


class AlbumListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'url']
        # extra_kwargs = {
        #     'url': {'view_name': 'album-detail', 'lookup_url_kwarg': 'question_id'},
        # }

    def to_representation(self, instance):
        # print(instance)
        # print(type(instance))
        ret = super().to_representation(instance)
        ret['mohammad'] = 'ashkan'
        return ret

    def to_internal_value(self, data):
        data = data['time']['data']
        data_ret = super().to_internal_value(data)

        return data_ret


class AlbumDetailSerializer(ModelSerializer):
    track_set = TrackSerializer(many=True, read_only=True)
    field1 = SerializerMethodField(method_name='compute_field1')
    # tracks = StringRelatedField(source='track_set', many=True, read_only=True)
    # tracks = PrimaryKeyRelatedField(source='track_set', many=True, read_only=True)
    # tracks2 = HyperlinkedRelatedField(source='track_set', many=True, read_only=True,
    #                                  view_name='track-detail')
    # tracks1= HyperlinkedIdentityField(source='track_set', many=True, view_name='track-detail')

    class Meta:
        model = Album
        fields = ['name', 'is_active', 'track_set', 'field1']

    def compute_field1(self, obj):
        return obj.id