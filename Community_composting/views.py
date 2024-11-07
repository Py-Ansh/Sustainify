# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Discussion, Reply
from .forms import DiscussionForm, ReplyForm
from django.contrib.auth.decorators import login_required
from .models import CompostingPit

import json





def CC_Home(request):
    return render(request, "CC_main.html")




# View to display all discussions
def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'discussion_list.html', {'discussions': discussions})



# View to create a new discussion
@login_required
def create_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.created_by = request.user
            discussion.save()
            return redirect('discussion_list')
    else:
        form = DiscussionForm()
    return render(request, 'create_discussion.html', {'form': form})

# View to create a reply to a discussion
@login_required
def create_reply(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.discussion = discussion
            reply.created_by = request.user
            reply.save()
            return redirect('discussion_list')
    else:
        form = ReplyForm()
    return render(request, 'create_reply.html', {'form': form, 'discussion': discussion})




# View to delete a discussion (only by the owner)
@login_required
def delete_discussion(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if discussion.created_by == request.user:
        discussion.delete()
    return redirect('discussion_list')









@login_required
def find_composting_pits(request):
    composting_pits = CompostingPit.objects.all()
    composting_pits_json = json.dumps([
        {"id": pit.id, "name": pit.name, "location": pit.location, 
         "latitude": float(pit.latitude), "longitude": float(pit.longitude), 
         "owner_id": pit.owner.id} 
        for pit in composting_pits
    ])

    
    return render(request, 'Find_pits.html', {'composting_pits_json': composting_pits_json, 'composting_pits': composting_pits,})


@login_required
def add_composting_pit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Create a new composting pit
        CompostingPit.objects.create(
            name=name,
            location=location,
            latitude=latitude,
            longitude=longitude,
            owner=request.user  # Owner of the pit
        )

        
        return redirect('find_composting_pits')
    return redirect('find_composting_pits')


@login_required
def remove_composting_pit(request, pit_id):
    # Ensure the user is logged in and owns the pit
    if request.user.is_authenticated:
        pit = get_object_or_404(CompostingPit, id=pit_id)
        if pit.owner == request.user:
            pit.delete()  # Delete the pit
            return redirect('find_composting_pits')  # Redirect to the list of pits after removal
        else:
            return redirect('find_composting_pits')  # Redirect if the user is not the owner
    else:
        return redirect('login')  # Redirect to login if not authenticated
