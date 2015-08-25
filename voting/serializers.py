# quickstart guide: http://www.django-rest-framework.org/tutorial/quickstart/
#>> Serializers define the API representation.

from voting.models import Choice
from rest_framework import serializers

# One serializer for each Model
# with HyperlinkedModelSerializer we can also use primary key and various other relationships (hyperlinking is good RESTful design)
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('name', 'votes')

