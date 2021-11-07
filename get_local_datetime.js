
const update_local_time = () => {
	const now = new Date();
	now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
	const datestr = now.toISOString().slice(0, 10);
	const timestr = now.toISOString().slice(11, 16);
	console.log(datestr);
	console.log(timestr);
	return {
		datestr,
		timestr
	};
};


const send_local_time = () => {
	const local_time = {
		date : now_date.value,
		time : now_time.value
	};

	fetch("set_time", {
		method: "POST",
		headers: {
			"Content-Type" : "application/json"
		},
		body: JSON.stringify(local_time)
	})
	.then(response => response.json())
	.then(data => {
		console.log("Success");
	})
	.catch((error) => {
		console.error("Error", error);
	});
};


const send_next_pattern = () => {
	fetch("next_pattern", {
		method : "POST",
		headers : {
			"Content-Type" : "application/json"
		},
		body: JSON.stringify("{}")
	})
	.then(response => response.json())
	.then(data => {
		console.log("Success");
	})
	.catch((error) => {
		console.error("Error", error);
	});
};


window.addEventListener('load', () => {
	local_time = update_local_time();
	now_date.value = local_time.datestr;
	now_time.value = local_time.timestr;
});


setInterval(() => {
	fetch("device_time").then((response) => {
		response.text().then((text) => {
			console.log(text);
			current_time_from_device.textContent = text;
		});
	});
//	local_time = update_local_time();
//	now_date.value = local_time.datestr;
//	now_time.value = local_time.timestr;
}, 1000);

