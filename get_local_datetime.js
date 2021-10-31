
window.addEventListener('load', () => {
	const now = new Date();
	now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
	now.setMilliseconds(null);
	console.log(now.toISOString().slice(0, 10));
	console.log(now.toISOString().slice(11, 16));
	const datestr = now.toISOString().slice(0, 10);
	const timestr = now.toISOString().slice(11, 16);
	document.getElementById('nowDate').value = datestr;
	document.getElementById('nowTime').value = timestr;
});
