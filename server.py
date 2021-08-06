from flask import Flask, request, render_template, flash, redirect, Markup
import subprocess
# from flask_login import LoginManager, login_user, login_required, UserMixin

from Scripts.authentication import authentication_user
from Scripts import get_all_about_disks

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'jijwiajdiwaj9ji2j2hhnwa989jkmxzlpppwq2'

all_disks_name_array = []
all_disks_size_array = []
all_disks_type_array = []
all_disks_mountpoint_array = []
all_disks_priority_array = []


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
@app.route('/authentication.html', methods=['POST', 'GET'])
def authentication():
    if request.method == "POST":
        try:
            if authentication_user(request.form['login_input'], request.form['password_input']):
                all_disks_name_array = get_all_about_disks.all_disks_name_array
                all_disks_size_array = get_all_about_disks.all_disks_size_array
                all_disks_type_array = get_all_about_disks.all_disks_type_array
                all_disks_mountpoint_array = get_all_about_disks.all_disks_mountpoint_array
                all_disks_priority_array = get_all_about_disks.all_disks_priority_array
                return redirect('workspace.html')
            else:
                flash('Неккоректные данные !', category='error')
                return render_template('authentication.html')

        except Exception:
            return render_template('authentication.html')
    else:
        return render_template('authentication.html')


def mount_disk(disk_name, mountpoint):
    mount_cmd = f'sudo mount -v {disk_name} {mountpoint}'
    subprocess.run(mount_cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    pass


def umount_disk(mountpoint):
    umount_cmd = 'sudo umount ' + mountpoint
    subprocess.run(umount_cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    pass


def format_disk(mountpoint):
    format_cmd = 'scrub ' + mountpoint
    subprocess.run(format_cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    pass


def return_workspace_template():
    return render_template('workspace.html', all_disks_name_array=all_disks_name_array,
                           all_disks_size_array=all_disks_size_array,
                           all_disks_mountpoint_array=all_disks_mountpoint_array,
                           all_disks_type_array=all_disks_type_array,
                           all_disks_priority_array=all_disks_priority_array)


@app.route('/workspace.html', methods=['POST', 'GET'])
def workspace():
    if request.method == "POST":
        try:
            if request.form['umount_disk']:
                umount_disk()
                return_workspace_template()

            if request.form['mount_disk']:
                mount_disk()
                return_workspace_template()

            if request.form['format_disk']:
                format_disk()
                return_workspace_template()

        except Exception:
            return_workspace_template()

    else:
        return_workspace_template()


if __name__ == '__server__':
    app.run(debug=True)
