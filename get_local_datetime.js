
window.addEventListener('load', () => {
	const now = new Date();
	now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
	now.setMilliseconds(null);
	console.log(now.toISOString().slice(0, 10));
	console.log(now.toISOString().slice(11, 16));
	const datestr = now.toISOString().slice(0, 10);
	const timestr = now.toISOString().slice(11, 16);
	document.getElementById('now_date').value = datestr;
	document.getElementById('now_time').value = timestr;
});

setInterval(() => {
	fetch("device_time").then((response) => {
		response.text().then((text) => {
			console.log(text);
			current_time_from_device.textContent = text;
		});
	});
}, 1000);

