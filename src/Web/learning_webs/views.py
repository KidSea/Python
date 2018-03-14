from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# 在这里创建视图

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_webs/index.html')

def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_webs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_webs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_webs:topics'))

    context = {'form': form}
    return  render(request, 'learning_webs/new_topic.html', context)

def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_webs:topic', args=[topic_id]))

    context = {'topic': topic,'form': form}
    return  render(request, 'learning_webs/new_entry.html', context)

def edit_entry(request, entry_id):
    """在特定的主题中添加新条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 未提交数据，创建一个表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_webs:topic', args=[topic.id]))

    context = {'entry': entry,'topic': topic,'form': form}
    return  render(request, 'learning_webs/edit_entry.html', context)