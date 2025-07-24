async function upload() {
  const file = document.getElementById("fileInput").files[0];
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:5000/upload", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();
  document.getElementById("output").innerText = JSON.stringify(result, null, 2);
}
