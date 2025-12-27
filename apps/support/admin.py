from django.contrib import admin
from django.utils.html import format_html
from .models import SupportTicket, TicketReply


class TicketReplyInline(admin.TabularInline):
    model = TicketReply
    fields = ['author_name', 'message', 'is_staff_reply', 'created_at']
    readonly_fields = ['created_at']
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        base_fields = formset.form.base_fields
        if 'author_name' in base_fields:
            display_name = request.user.get_full_name() or request.user.get_username()
            base_fields['author_name'].initial = display_name
        if 'is_staff_reply' in base_fields:
            base_fields['is_staff_reply'].initial = True
        return formset


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_id', 'subject_preview', 'user_email', 'priority_badge', 'status_badge', 'created_at']
    list_filter = ['priority', 'status', 'created_at']
    search_fields = ['subject', 'user_name', 'user_email', 'message']
    readonly_fields = ['created_at', 'updated_at', 'message_display']
    ordering = ['-created_at']
    inlines = [TicketReplyInline]
    actions = ['mark_open', 'mark_in_progress', 'mark_resolved', 'mark_closed']
    
    fieldsets = (
        ('Ticket Information', {
            'fields': ('subject', 'user_name', 'user_email')
        }),
        ('Message', {
            'fields': ('message_display',)
        }),
        ('Status', {
            'fields': ('priority', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def ticket_id(self, obj):
        return f"#{obj.id}"
    ticket_id.short_description = "ID"
    
    def subject_preview(self, obj):
        return obj.subject[:50] + "..." if len(obj.subject) > 50 else obj.subject
    subject_preview.short_description = "Subject"
    
    def priority_badge(self, obj):
        colors = {
            'low': '#10b981',
            'medium': '#f59e0b',
            'high': '#ef4444',
            'critical': '#991b1b'
        }
        color = colors.get(obj.priority, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{}</span>',
            color,
            obj.get_priority_display()
        )
    priority_badge.short_description = "Priority"
    
    def status_badge(self, obj):
        colors = {
            'open': '#3b82f6',
            'in_progress': '#a855f7',
            'resolved': '#10b981',
            'closed': '#6b7280'
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = "Status"
    
    def message_display(self, obj):
        return obj.message
    message_display.short_description = "Message"

    # Admin actions for quick status updates
    def mark_open(self, request, queryset):
        updated = queryset.update(status='open')
        self.message_user(request, f"{updated} ticket(s) marked Open.")
    mark_open.short_description = "Mark selected tickets as Open"

    def mark_in_progress(self, request, queryset):
        updated = queryset.update(status='in_progress')
        self.message_user(request, f"{updated} ticket(s) marked In Progress.")
    mark_in_progress.short_description = "Mark selected tickets as In Progress"

    def mark_resolved(self, request, queryset):
        updated = queryset.update(status='resolved')
        self.message_user(request, f"{updated} ticket(s) marked Resolved.")
    mark_resolved.short_description = "Mark selected tickets as Resolved"

    def mark_closed(self, request, queryset):
        updated = queryset.update(status='closed')
        self.message_user(request, f"{updated} ticket(s) marked Closed.")
    mark_closed.short_description = "Mark selected tickets as Closed"


@admin.register(TicketReply)
class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ['get_ticket_id', 'ticket_subject', 'author_name', 'staff_badge', 'created_at']
    list_filter = ['is_staff_reply', 'created_at']
    search_fields = ['author_name', 'message', 'ticket__subject']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Reply Information', {
            'fields': ('ticket', 'author_name', 'is_staff_reply')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_ticket_id(self, obj):
        return f"#{obj.ticket.id}"
    get_ticket_id.short_description = "Ticket"
    
    def ticket_subject(self, obj):
        subject = obj.ticket.subject
        return subject[:40] + "..." if len(subject) > 40 else subject
    ticket_subject.short_description = "Subject"
    
    def staff_badge(self, obj):
        if obj.is_staff_reply:
            return format_html(
                '<span style="background-color: #06b6d4; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{}</span>',
                'Staff'
            )
        else:
            return format_html(
                '<span style="background-color: #6b7280; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{}</span>',
                'User'
            )
    staff_badge.short_description = "Type"
