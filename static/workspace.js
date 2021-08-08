Vue.component('mount_disk', {
	props: {id:'id'},
	template: `
<td>
	<input type="submit" name="umount_disk" class="btn btn-warning btn-sm" value="Отмонтировать">
	<input type="submit" name="format_disk" class="btn btn-danger btn-sm" value="Форматировать">
</td>
`
})

Vue.component('system_disk', {
})

Vue.component('umount_disk', {
	props: {id:'id'},
		template:`
<td>
	<input type="submit" name="mount_disk" class="btn btn-success btn-sm" value="Примонтировать">
	<input type="file" class="form-control-file" id="exampleFormControlFile1" webkitdirectory/>
	<input type="text" name="path_to_mount" placeholder="Введите дирректорию !">
</td>
`
})

let all_input_disks_names =  document.getElementById("input_disks_names").value;//  getElementsByName("input_disks_names")[0].valueOf();
let all_input_disks_sizes =  document.getElementById("input_disks_sizes").value;//document.getElementsByName("input_disks_types").values().toString();
let all_input_disks_mountpoints = document.getElementById("input_disks_mountpoints").value; //document.getElementsByName("input_disks_mountpoints").values().toString();
let all_input_disks_types =  document.getElementById("input_disks_types").value;//document.getElementsByName("input_disks_sizes").values().toString();
let all_input_disks_priorities =  document.getElementById("input_disks_priorities").value;//document.getElementsByName("input_disks_priorities").values().toString();

//alert(all_input_disks_mountpoints)

let id=0;
let disks_names = all_input_disks_names.split(' ');//['sda','sdb','sdc','sdd'];
let disks_sizes = all_input_disks_sizes.split(' ');//['20gb','1gb','50gb','100gb'];
let disks_mountpoints = all_input_disks_mountpoints.split(' ');//['/','','/home/desktop',''];
let disks_types = all_input_disks_types.split(' ');//['disk','part','disk','disk'];
let disks_priority = all_input_disks_priorities.split(' ');//['system','system','common','common'];

//alert(disks_mountpoints)

var app = new Vue({
	el:'#app',
	delimiters:['{[', ']}'],
	data: {
		array_disks:
			{name:disks_names, size: disks_sizes, mountpoint: disks_mountpoints,type: disks_types, priority: disks_priority},

	},

	isMountDisk: false,
	isUmountDisk: false,

methods: {
	set_disk_status: function (index ){
		console.log('Hi!'+ index)

		this.isMountDisk = false;
		this.isUmountDisk= false;

			if (disks_priority[index] === 'system') {
				return;
			}

			if (disks_priority[index] === 'common' && disks_mountpoints[index] !== '') {
				this.isMountDisk = true
			}

			if (disks_types[index] === 'disk' && disks_mountpoints[index] === '') {
				this.isUmountDisk = true
			}
		}
	}
});



//alert(disks_names + " " + disks_sizes + " " + disks_mountpoints + " " + disks_types + " " +disks_priority);