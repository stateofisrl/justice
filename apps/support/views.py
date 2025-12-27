from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings
from .models import SupportTicket, TicketReply
from .forms import TicketForm, TicketReplyForm


class TicketCreateView(View):
    def get(self, request):
        form = TicketForm()
        return render(request, 'support/ticket_form.html', {'form': form})

    def post(self, request):
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('support:ticket_detail', pk=ticket.pk)
        return render(request, 'support/ticket_form.html', {'form': form})


class TicketDetailView(View):
    def get(self, request, pk):
        ticket = get_object_or_404(SupportTicket, pk=pk)
        replies = ticket.replies.all()
        form = TicketReplyForm()
        
        context = {
            'ticket': ticket,
            'replies': replies,
            'form': form,
        }
        return render(request, 'support/ticket_detail.html', context)

    def post(self, request, pk):
        ticket = get_object_or_404(SupportTicket, pk=pk)
        reply_submitted = False
        
        if 'user_reply' in request.POST:
            form = TicketReplyForm(request.POST)
            if form.is_valid():
                reply = form.save(commit=False)
                reply.ticket = ticket
                reply.author_name = ticket.user_name
                reply.is_staff_reply = False
                reply.save()
                reply_submitted = True
                return redirect('support:ticket_detail', pk=ticket.pk)
        
        elif 'staff_reply' in request.POST and request.user.is_staff:
            message = request.POST.get('message')
            if message:
                reply = TicketReply.objects.create(
                    ticket=ticket,
                    author=request.user,
                    author_name=request.user.get_full_name() or request.user.username,
                    is_staff_reply=True,
                    message=message
                )
                # Send email notification
                send_notification_email(ticket, reply)
        
        elif 'status_update' in request.POST and request.user.is_staff:
            new_status = request.POST.get('status')
            ticket.status = new_status
            ticket.save()
        
        replies = ticket.replies.all()
        form = TicketReplyForm()
        
        context = {
            'ticket': ticket,
            'replies': replies,
            'form': form,
            'reply_submitted': True,
        }
        return render(request, 'support/ticket_detail.html', context)


def send_notification_email(ticket, reply):
    """Send email notification to user when staff replies"""
    subject = f"Re: {ticket.subject}"
    message = f"""
    Hello {ticket.user_name},
    
    There's a new response to your support ticket:
    
    {reply.message}
    
    View your ticket: http://127.0.0.1:8000/support/ticket/{ticket.pk}/
    
    Best regards,
    ScamResolvedCSI Support Team
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [ticket.user_email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email: {e}")