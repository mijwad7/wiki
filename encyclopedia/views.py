from django.shortcuts import render
import markdown2
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = converter(title)
    if content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "No entry found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })

def search(request):
    if request.method == "POST":
        search_term = request.POST['q']
        content = util.get_entry(search_term)
        if content is None:
            entries = util.list_entries() 
            matched_entries = []
            for entry in entries:
                if search_term.lower() in entry.lower():
                    matched_entries.append(entry)   
            return render(request, "encyclopedia/search.html", {
            "matched_entries": matched_entries,
            "search_term": search_term
            })
        else:
            content = converter(search_term)
            return render(request, "encyclopedia/entry.html", {
            "title": search_term,
            "content": content
        })


def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        exist = util.get_entry(title)
        if exist:
            return render(request, "encyclopedia/error.html",{
                "message": "Entry already exists"
            })
        else:
            util.save_entry(title, content)
            content = converter(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": content
                })


def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })


def save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        content = converter(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
            })


def rand(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    content = converter(random_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": random_entry,
        "content": content
        })


def converter(title):
    content = util.get_entry(title)
    content = markdown2.markdown(content)
    if content is None:
        return None
    else:
        return content
