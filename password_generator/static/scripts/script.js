const answer_button = document.getElementById("answerButton")
const option_span = document.getElementById("optionSpan")
const option_select = document.getElementById("optionSelect")
const answer_input = document.getElementById("answerInput");

function send_request() {
	const error_head = document.querySelector(".header-error__text")
	const password_len = document.getElementById("optionLength")
	const score = document.querySelector(".answer-item__p")

	score.textContent = "Score: "
	// Sets empty string in the h2
	error_head.textContent = ""
	// Creates options array from the select
	selected_values = Array.from(option_select.selectedOptions).map(option => option.value)
	// Creates settings for the password generator
	let settings = {
		"length": password_len.value,
		"options": selected_values
	}

	request = fetch('/generator', {
		method: "POST",
		headers: {
			"Content-Type": "application/json;charset=utf-8"
		},
		body: JSON.stringify(settings)
	})
		.then(response => (response.json()))
		.then(result => {
			if (result.error) {
				error_head.textContent = result.error
			} else {
				answer_input.value = result.password
				switch (result.score) {
					case 4:
						score.insertAdjacentHTML(
							'beforeend',
							"<span style='color: green;'>great</span>"
						)
						break
					case 3:
						score.insertAdjacentHTML(
							"beforeend",
							"<span style='color: rgb(255, 242, 0);'>good</span>"
						)
						break
					case 2:
						score.insertAdjacentHTML(
							'beforeend',
							"<span style='color: orange;'>middle</span>"
						)
						break
					case 1:
						score.insertAdjacentHTML(
							'beforeend',
							"<span style='color: red;'>weak</span>"
						)
				}
			}
		})
};

answer_button.addEventListener("mouseleave", () => {
	// Updates tooltip text
	document.getElementById("answerTooltip").textContent = "Copy to clipboard"
})

option_span.addEventListener("click", () => {
	option_select.classList.toggle("active")
});

function show_tooltip() {
	const span = document.getElementById("answerTooltip")
	answer_input.select();
	navigator.clipboard.writeText(answer_input.value);
	span.textContent = "Copied:" + answer_input.value
};

