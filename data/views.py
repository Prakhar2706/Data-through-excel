from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
import requests
from .models import Lead, University
from .serializers import LeadSerializer, UniversitySerializer
from django.http import HttpResponse
from .utils import generate_pdf
import os

# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([AllowAny])
def list_universities(request):
    universities = University.objects.all().values('id', 'university_name')
    return Response(universities)

@api_view(['POST'])
@permission_classes([AllowAny])
def receive_lead(request):
    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
        lead = serializer.save()
        university = lead.university
        # Check if the university needs to be wrapped in an array
        if(university.wrap_in_array):
            data = [{
                university.name_field: lead.name,
                university.email_field: lead.email,
                university.phone_field: lead.phone,
                university.country_field: lead.country,
                university.state_field: lead.state,
                university.city_field: lead.city,
                university.district_field: lead.district,
                university.program_field: lead.program,
                university.course_field: lead.course,
                university.source_field: lead.source,
            }]
        else:
            data = {
                university.name_field: lead.name,
                university.email_field: lead.email,
                university.phone_field: lead.phone,
                university.country_field: lead.country,
                university.state_field: lead.state,
                university.city_field: lead.city,
                university.district_field: lead.district,
                university.program_field: lead.program,
                university.course_field: lead.course,
                university.source_field: lead.source,
            }
        try:
            response = requests.post(university.api_url, json=data)
            if response.status_code == 200:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Failed to post data to university API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def upload_leads(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        df = pd.read_excel(file)

        # Ensure phone numbers are treated as strings
        df['phone'] = df['phone'].astype(str)
        
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    errors = []
    for index, row in df.iterrows():
        university_id = row.get('university_id')
        try:
            university = University.objects.get(id=university_id)
        except University.DoesNotExist:
            errors.append({"row": index + 1, "error": "University not found"})
            continue


        phone = str(row.get(university.phone_field))
        if len(phone) > 15:
            errors.append({"row": index + 1, "error": "Phone number exceeds 15 characters"})
            continue
        
        lead_data = {
            'university': university.id,
            'name': row.get(university.name_field),
            'email': row.get(university.email_field),
            # 'phone': str(row.get(university.phone_field)),
            'phone': phone,
            'country': row.get(university.country_field),
            'state': row.get(university.state_field),
            'city': row.get(university.city_field),
            'district': row.get(university.district_field),
            'program': row.get(university.program_field),
            'course': row.get(university.course_field),
            'source': row.get(university.source_field),
        }

        serializer = LeadSerializer(data=lead_data)
        if serializer.is_valid():
            lead = serializer.save()
            # Prepare data to send to university
            if university.wrap_in_array:
                data = [{
                    university.name_field: lead.name,
                    university.email_field: lead.email,
                    university.phone_field: lead.phone,
                    university.country_field: lead.country,
                    university.state_field: lead.state,
                    university.city_field: lead.city,
                    university.district_field: lead.district,
                    university.program_field: lead.program,
                    university.course_field: lead.course,
                    university.source_field: lead.source,
                }]
            else:
                data = {
                    university.name_field: lead.name,
                    university.email_field: lead.email,
                    university.phone_field: lead.phone,
                    university.country_field: lead.country,
                    university.state_field: lead.state,
                    university.city_field: lead.city,
                    university.district_field: lead.district,
                    university.program_field: lead.program,
                    university.course_field: lead.course,
                    university.source_field: lead.source,
                }

            try:
                response = requests.post(university.api_url, json=data)
                if response.status_code != 200:
                    errors.append({"row": index + 1, "error": "Failed to post data to university API"})
            except requests.exceptions.RequestException as e:
                errors.append({"row": index + 1, "error": str(e)})
        else:
            errors.append({"row": index + 1, "error": serializer.errors})

    if errors:
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Leads processed successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def download_pdf(request):
    file_path = 'Data.pdf'
    generate_pdf(file_path)

    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
        return response