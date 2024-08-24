from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from .models import University, Lead

def generate_pdf(file_path):
    document = SimpleDocTemplate(file_path, pagesize=letter)
    elements = []

    # Fetch data from University model
    university_data = [["ID", "University Name", "Name Field", "Email Field", "Phone Field"]]
    for university in University.objects.all():
        university_data.append([
            university.id,
            university.university_name,
            university.name_field,
            university.email_field,
            university.phone_field,
        ])
    
    # Create table for University data
    university_table = Table(university_data)
    university_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(university_table)

    elements.append(Spacer(1, 20))

    # Fetch data from Lead model
    lead_data = [["ID", "University", "Name", "Email", "Phone", "Country", "State", "City"]]
    for lead in Lead.objects.all():
        lead_data.append([
            lead.id,
            lead.university.university_name,
            lead.name,
            lead.email,
            lead.phone,
            lead.country,
            lead.state,
            lead.city,
        ])
    
    # Create table for Lead data
    lead_table = Table(lead_data)
    lead_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(lead_table)

    document.build(elements)
