
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


const send_new_alarm = (alarm_params) => {
	clear_table(add_alarm);
	clear_table(add_alarm_header);
	console.log(alarm_params.name_input.value);
	const add_alarm_button = document.createElement("button");
	add_alarm_button.textContent = "+";
	add_alarm_button.addEventListener("click", make_set_alarm_form);
	add_alarm.appendChild(add_alarm_button);
};

const remove_alarm = (name) => {
	fetch("remove_alarm", {
		method : "POST",
		headers : {
			"Content-Type" : "application/json"
		},
		body: `["${name}"]`
	})
	.then(response => response.json())
	.then(data => {
			console.log("Success");
	})
	.catch((error) => {
		console.error("Error", error);
	});
};


const clear_table = (table) => {
	while(table.firstChild) {
		table.removeChild(table.firstChild);
	}	
};


const append_text_to_table = (row, text) => {
	const d = document.createElement("div");
	d.textContent = text
	const col = document.createElement("td");
	col.appendChild(d);
	row.appendChild(col)
};


const append_check_box_to_table = (row, checked, label, disable) => {
	const box = document.createElement("input");
	box.setAttribute("type", "checkbox");
	if(disable) {
		box.setAttribute("disable", "");
	}
	if(checked) {
		box.setAttribute("checked", "");
	}
	const col = document.createElement("td");
	const labl = document.createElement("label");
	if(label) {
		labl.textContent = label;
		col.appendChild(labl);
	}
	col.appendChild(box);
	row.appendChild(col);
};


const append_button_to_table = (row, text, value, onclick) => {
	const butt = document.createElement("button");
	butt.textContent = text;
	butt.addEventListener("click", () => {
		onclick(value);	
	});
	const col = document.createElement("td");
	col.appendChild(butt);
	row.appendChild(col);
}


const append_element_to_table = (row, element) => {
	const col = document.createElement("td");
	col.appendChild(element);
	row.appendChild(col);
}


const make_time_string = (t) => {
	const hh = t[3].toString().padStart(2, "0");
	const mm = t[4].toString().padStart(2, "0");
	const YYYY = t[0].toString().padStart(4, "0");
	const MM = t[1].toString().padStart(2, "0");
	const DD = t[2].toString().padStart(2, "0");
	const time_string = `${hh}:${mm} ${YYYY}-${MM}-${DD}`;
	return time_string;
};


const populate_alarm_display = (alarms) => {
	clear_table(display_alarms);
	clear_table(display_alarms_header);
	if(0 !== alarms.length) {
		const row = document.createElement("tr");
		append_text_to_table(row, "Name");
		append_text_to_table(row, "Time");
		append_text_to_table(row, "Pattern");
		append_text_to_table(row, "Repeat");
		append_text_to_table(row, "Weekends");
		display_alarms_header.appendChild(row);		
	}
	alarms.forEach((alarm) => {
		const row = document.createElement("tr");
		append_text_to_table(row, alarm["name"])
		append_text_to_table(row, make_time_string(alarm["time"]));
		append_text_to_table(row, alarm["pattern"]);
		append_check_box_to_table(row, alarm["daily"], "", true);
		append_check_box_to_table(row, alarm["weekends"], "", true);
		append_button_to_table(row, "-", alarm["name"], remove_alarm);
		display_alarms.appendChild(row);
	});
};


const get_alarms = () => {
	let alarms = {};
	fetch("get_alarms")
	.then((response) => {
		if(!response.ok) {
			throw new Error("Bad response");
		}
		console.log(response)
		response.json().then((json) => {
			populate_alarm_display(json);
		})
	})
	.catch((error) => {
		console.error("Error", error);
	});
	return alarms;
};


const make_dropdown = (name, values) => {
	const menu = document.createElement("select");
	menu.setAttribute("name", name);
	for(const [option, description] of Object.entries(values)) {
		opt = document.createElement("option");
		opt.setAttribute("value", option);
		opt.textContent = description;
		menu.appendChild(opt);
	}

	return menu;
};


const make_set_alarm_form = () => {
	clear_table(add_alarm);

	const row = document.createElement("tr");
	const label_row = document.createElement("tr");

	const name_input = document.createElement("input");
	name_input.setAttribute("type", "text");
	name_input.setAttribute("placeholder", "Alarm name");	
	append_element_to_table(row, name_input);

	const name_input_label = document.createElement("label");
	name_input_label.setAttribute("for", "name_input");
	name_input_label.textContent = "Name";
	append_element_to_table(label_row, name_input_label);
	
	const local_time = update_local_time();
	const time_input = document.createElement("input");
	time_input.setAttribute("type", "time");
	time_input.setAttribute("value", local_time.timestr);
	append_element_to_table(row, time_input);
	
	const time_input_label = document.createElement("label");
	time_input_label.setAttribute("for", "time_input");
	time_input_label.textContent = "Time";
	append_element_to_table(label_row, time_input_label);

	const pattern_options = {
		"NONE" : "Select a Light Pattern",
		"ALL_SOLID" : "All Solid",
		"BREATHING_RAINBOW_1" : "Breathing Rainbow 1",
		"BREATHING_RAINBOW_2" : "Breathing Rainbow 2",
		"FAST_RAINBOW" : "Fast Rainbow",
		"SOLID_RED" : "Solid Red",
		"SOLID_GREEN" : "Solid Green",
		"SOLID_BLUE" : "Solid Blue",
		"BREATHING_RAINBOW_3" : "Breathing Rainbow 3"
	};
	const pattern_menu = make_dropdown("pattern", pattern_options);
	append_element_to_table(row, pattern_menu);

	const pattern_menu_label = document.createElement("label");
	pattern_menu_label.setAttribute("for", "pattern_menu");
	pattern_menu_label.textContent = "Pattern";
	append_element_to_table(label_row, pattern_menu_label);

	const repeat_input = document.createElement("input");
	repeat_input.setAttribute("type", "checkbox");
	repeat_input.setAttribute("value", "repeat");
	append_element_to_table(row, repeat_input);

	const repeat_input_label = document.createElement("label");
	repeat_input_label.setAttribute("for", "repeat_input");
	repeat_input_label.textContent = "Repeat";
	append_element_to_table(label_row, repeat_input_label);

	const weekend_input = document.createElement("input");
	weekend_input.setAttribute("type", "checkbox");
	weekend_input.setAttribute("value", "weekends");
	append_element_to_table(row, weekend_input);

	const weekend_input_label = document.createElement("label");
	weekend_input_label.setAttribute("for", "weekend_input");
	weekend_input_label.textContent = "Weekends";
	append_element_to_table(label_row, weekend_input_label);
	
	const alarm_params = {
		name_input,
		time_input,
		pattern_options,
		repeat_input,
		weekend_input
	};
	append_button_to_table(row, "Make", alarm_params, send_new_alarm);
	add_alarm.appendChild(row);
	add_alarm_header.appendChild(label_row);
};


window.addEventListener('load', () => {
	local_time = update_local_time();
	now_date.value = local_time.datestr;
	now_time.value = local_time.timestr;
	
	const add_alarm_button = document.createElement("button");
	add_alarm_button.textContent = "+";
	add_alarm_button.addEventListener("click", make_set_alarm_form);
	add_alarm.appendChild(add_alarm_button);	
	get_alarms();		
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
	get_alarms();
}, 1000);


