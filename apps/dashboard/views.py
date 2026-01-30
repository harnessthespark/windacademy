from datetime import date, timedelta
from django.db.models import Sum, Q, Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.accounts.permissions import IsStaffUser
from apps.contacts.models import Delegate
from apps.clients.models import Client
from apps.training.models import CourseInstance, Booking
from apps.recruitment.models import Job, Candidate, Placement
from apps.documents.models import Invoice


@api_view(["GET"])
@permission_classes([IsStaffUser])
def dashboard_stats(request):
    today = date.today()
    next_30 = today + timedelta(days=30)

    delegate_count = Delegate.objects.count()

    client_counts = dict(
        Client.objects.values_list("status").annotate(count=Count("id")).values_list("status", "count")
    )

    upcoming_instances = CourseInstance.objects.filter(
        start_date__gte=today, start_date__lte=next_30,
        status__in=["scheduled", "confirmed"],
    ).count()

    open_jobs = Job.objects.filter(status__in=["open", "interviewing", "offered"]).count()
    active_candidates = Candidate.objects.exclude(stage__in=["rejected", "withdrawn", "placed"]).count()
    placements_this_year = Placement.objects.filter(
        start_date__year=today.year, status__in=["started", "probation", "confirmed"]
    ).count()

    invoice_agg = Invoice.objects.exclude(status__in=["cancelled", "draft"]).aggregate(
        total_revenue=Sum("total", filter=Q(status="paid")),
        total_outstanding=Sum("total", filter=Q(status__in=["sent", "viewed", "overdue"])),
    )

    return Response({
        "delegates": delegate_count,
        "clients": client_counts,
        "upcoming_training_instances": upcoming_instances,
        "open_jobs": open_jobs,
        "active_candidates": active_candidates,
        "placements_this_year": placements_this_year,
        "revenue_paid": invoice_agg["total_revenue"] or 0,
        "invoices_outstanding": invoice_agg["total_outstanding"] or 0,
    })
