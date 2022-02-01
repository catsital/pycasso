document.getElementById("submit").addEventListener("click", showSpinner);

document.querySelector("input[type=file]").onchange = ({
  target: { value },
}) => {
  document.querySelector("input[type=submit]").disabled = !value;
};

var loading = document.getElementById('loading');

function showSpinner() {
  loading.style.visibility = 'visible';
}

function hideSpinner() {
  loading.style.visibility = 'hidden';
}
