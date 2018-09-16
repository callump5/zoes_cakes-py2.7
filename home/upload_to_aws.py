import os
from django.utils.timezone import now

def upload_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'staff/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )