import os

def handle_upload_file(author, f):
    if not os.path.exists(f'main/static/uploads/users/{author}/'):
        os.mkdir(f'main/static/uploads/users/{author}/')

    with open(f'main/static/uploads/users/{author}/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)