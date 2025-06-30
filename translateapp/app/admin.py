from django.contrib import admin
from .models import Account,Job,Bid,Dispute,Message,Rating

# Register your models here.
admin.site.register(Account)
admin.site.register(Job)
admin.site.register(Bid)
admin.site.register(Dispute)
admin.site.register(Message)
admin.site.register(Rating)