from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()

        teams_dict = [model_to_dict(Team) for Team in teams]
        return Response(teams_dict)


    def post(self, request):
        teams = Team.objects.create(**request.data)
        teams_dict = model_to_dict(teams)

        return Response(teams_dict, status.HTTP_201_CREATED)



class TeamViewId(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            teams = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({
                "message": "Team not found"
            }, status.HTTP_404_NOT_FOUND)

        teams_dict = model_to_dict(teams)

        return Response(teams_dict)



    def patch(self, request: Request, team_id: int) -> Response:
        try:
            teams = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({
                "message": "Team not found"
            }, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(teams, key, value)

        teams.save()
        teams_dict = model_to_dict(teams)

        return Response(teams_dict, status.HTTP_200_OK)


    def delete(self, request: Request, team_id: int) -> Response:
        try:
            teams = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({
                "message": "Team not found"
            }, status.HTTP_404_NOT_FOUND)

        teams.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

