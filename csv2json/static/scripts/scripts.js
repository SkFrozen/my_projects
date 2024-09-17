const csv = document.getElementById("input_csv");
const btn = document.getElementById("btn_csv");
const link = document.getElementById("json_download")

btn.addEventListener("click", () => {
	const form_data = new FormData();
	form_data.append("file", csv.files[0])
	response = fetch("/convert", {
		method: "POST",
		body: form_data,
	})
		.then(response => (response.json()))
		.then(result => {
			if (result.error) {
				alert(result.error)
			} else {
				link.setAttribute('href', `/${result.file}`)
				alert("JSON file is ready to upload ->")
			}
		})
});
