
window.addEventListener('load', () => {
	const now = new Date();
	now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
	now.setMilliseconds(null);
	console.log(now.toISOString().slice(0,-8))
	document.getElementById('now').value =
		now.toISOString().slice(0, -8);
});
