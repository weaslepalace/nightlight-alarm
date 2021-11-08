
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


const make_set_alarm_form = () => {
	local_time = update_local_time();
	console.log("+");

	const row = document.createElement("tr");

	const col_0 = document.createElement("td");
	const t = document.createElement("input");
	t.setAttribute("type", "time");
	t.setAttribute("value", local_time.timestr);
	t.setAttribute("required", "");


	const col_1 = document.createElement("td");
	const a = document.createElement("select");
	a.setAttribute("name", "action");
	a.setAttribute("id", "action");
	const ao_none = document.createElement("option");
	ao_none.setAttribute("value", "NONE");
	ao_none.textContent = "Select an Action";
	const ao_0 = document.createElement("option");
	ao_0.setAttribute("value", "OFF");
	ao_0.textContent = "Off";
	const ao_1 = document.createElement("option");
	ao_1.setAttribute("value", "ALL_SOLID");
	ao_1.textContent = "All Solid";
	const ao_2 = document.createElement("option");
	ao_2.setAttribute("value", "BREATHING_RAINBOW_1");
	ao_2.textContent = "Breathing Rainbow 1";
	const ao_3 = document.createElement("option");
	ao_3.setAttribute("value", "BREATHING_RAINBOW_2");
	ao_3.textContent = "Breathing Rainbow 2";
	const ao_4 = document.createElement("option");
	ao_4.setAttribute("value", "FAST_RAINBOW");
	ao_4.textContent = "Fast Rainbow";
	const ao_5 = document.createElement("option");
	ao_5.setAttribute("value", "SOLID_RED");
	ao_5.textContent = "Solid Red";
	const ao_6 = document.createElement("option");
	ao_6.setAttribute("value", "SOLID_GREEN");
	ao_6.textContent = "Solid Green";
	const ao_7 = document.createElement("option");
	ao_7.setAttribute("value", "SOLID_BLUE");
	ao_7.textContent = "Solid Blue";
	const ao_8 = document.createElement("option");
	ao_8.setAttribute("value", "BREATHING_RAINBOW_3");
	ao_8.textContent = "Breathing Rainbow 3"
	a.appendChild(ao_none);
	a.appendChild(ao_0);
	a.appendChild(ao_1);
	a.appendChild(ao_2);
	a.appendChild(ao_3);
	a.appendChild(ao_4);
	a.appendChild(ao_5);
	a.appendChild(ao_6);
	a.appendChild(ao_7);
	a.appendChild(ao_8);

	const col_2 = document.createElement("td");
	const r = document.createElement("input");
	r.setAttribute("type", "checkbox");
	r.setAttribute("value", "reoccuring");
	r.setAttribute("id", "reoccuring");
	const rl = document.createElement("label");
	rl.setAttribute("for", "reoccuring");
	rl.textContent = "Reoccuring";

	const col_3 = document.createElement("td");
	const w = document.createElement("input");
	w.setAttribute("type", "checkbox");
	w.setAttribute("value", "weekends");
	w.setAttribute("is", "weekends");
	const wl = document.createElement("label");
	wl.setAttribute("for", "reoccuring");
	wl.textContent = "Weekends";

	col_0.appendChild(t);
	col_1.appendChild(a);
	col_2.appendChild(r);
	col_2.appendChild(rl);
	col_3.appendChild(w);
	col_3.appendChild(wl);
	row.appendChild(col_0);
	row.appendChild(col_1);
	row.appendChild(col_2);
	row.appendChild(col_3);
	set_alarm_forms.appendChild(row);
};


window.addEventListener('load', () => {
	local_time = update_local_time();
	now_date.value = local_time.datestr;
	now_time.value = local_time.timestr;
});


setInterval(() => {
	fetch("device_time").then((response) => {
		if(!response.ok) {
			throw new Error("Bad response");
		}
		response.text().then((text) => {
			console.log(text);
			current_time_from_device.textContent = text;
		});
	})
	.catch((error) => {
		current_time_from_device.textContent = "... unknown?"
	});
}, 1000);

