from celery import task
from django.conf import settings
from PIL import Image
from os import path, remove
from .models import Profile


@task
def resize_avatar(path_to_file, id):
    try:
        absolute_path_to_file = path.join(settings.MEDIA_ROOT, path_to_file)

        image = Image.open(absolute_path_to_file)

        path_dir, name_file = path.split(path_to_file)
        name, ext = path.splitext(name_file)
        new_name_with_ext = name + '_res_400x400' + ext

        # path to file for update DB
        path_for_db = path.join(path_dir, new_name_with_ext)

        # path for save
        new_save_path = path.join(settings.MEDIA_ROOT, path_dir, new_name_with_ext)

        (width, height) = image.size

        # crop:
        if width > height:
            crop_box = (int(round(width-height)/2), 0, width - int(round(width-height)/2), height)
        else:
            crop_box = (0, int(round(height-width)*0.33), width, height - int(round(height-width)*0.67))

        print(crop_box)
        image = image.crop(crop_box)

        # resize:
        size = (400, 400)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(new_save_path)

        # update db:
        print('~~~~id~~~', id)
        prof_instance = Profile.objects.get(id=id)
        prof_instance.avatar_image = path_for_db
        prof_instance.save()

        # delete user upload file
        remove(absolute_path_to_file)

        return True

    except Exception as err:
        print(err)

        return False


