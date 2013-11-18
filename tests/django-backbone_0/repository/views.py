from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from bbx.settings import DEFAULT_MUCUA, DEFAULT_REPOSITORY
from repository.models import Repository,getAvaliableRepositories,getDefaultRepository
from repository.serializers import RepositorySerializer

@api_view(['GET'])
def repository_list(request):
    """
    List all repositories
    """    
    repositories = getAvaliableRepositories()
    repositories_list = []
    for repo in repositories:
        repoName = repo[0]
        
        try:
            repository = Repository.objects.get(name = repoName)
            
        except Repository.DoesNotExist:
            print "not found: ", repoName
            repository = False
        
        if repository:
            repositories_list.append(repository)
    
    serializer = RepositorySerializer(repositories_list, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def repository_get_default(request):
    
    repositories_list = []
    repositories_list.append(getDefaultRepository())
    serializer = RepositorySerializer(repositories_list, many=True)
    
    return Response(serializer.data)
