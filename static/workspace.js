Vue.component('mount_disk', {
	props: {id:'id'},
	template: `
<td>
	<button type="button" name="umount_disk {{id}}" class="btn btn-warning btn-sm">Отмонтировать</button>
	<button type="button" name="format_disk {{id}}" class="btn btn-danger btn-sm">Форматировать</button>
</td>
`
})

Vue.component('system_disk', {
})

Vue.component('umount_disk', {
	props: {id:'id'},
		template:`
<td>
	<button type="button" name="mount_disk {{id}}" class="btn btn-success btn-sm">Примонтировать</button>
	<input type="file" class="form-control-file" id="exampleFormControlFile1" webkitdirectory/>
</td>
`
})

let all_input_disks_names =  document.getElementsById("input_disks_names").value;
let all_input_disks_types =  document.getElementsById("input_disks_sizes").value;
let all_input_disks_sizes =  document.getElementsById("input_disks_types").value;
let all_input_disks_mountpoints =  document.getElementsById("input_disks_mountpoints").value;
let all_input_disks_priorities =  document.getElementsById("input_disks_priorities").value;



let id=0;
let disks_names = ['sda','sdb','sdc','sdd'];
let disks_sizes = ['20gb','1gb','50gb','100gb'];
let disks_mountpoints = ['/','','/home/desktop',''];
let disks_types = ['disk','part','disk','disk'];
let disks_priority = ['system','system','common','common'];

var app = new Vue({
	el:'#app',

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
//<mount_disk v-if="array_disks.priority[index] === 'common' && array_disks.mountpoint[index] !== ''" ></mount_disk>
//<umount_disk v-else-if="array_disks.type[index] === 'disk' && array_disks.mountpoint[index] === ''"></umount_disk>