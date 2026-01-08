async function classifyText() {
  const text = document.getElementById("textInput").value;
  const resultDiv = document.getElementById("result");

  if (!text.trim()) {
    resultDiv.innerHTML = "<span class='error'>❌ Please enter some text</span>";
    return;
  }

  resultDiv.innerHTML = "<span class='loading'>⏳ Classifying...</span>";

  try {
    const response = await fetch("http://localhost:8000/classify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    const data = await response.json();

    let badgeClass = "badge-green";
    if (data.category === "Complaint") badgeClass = "badge-red";
    else if (data.category === "Query") badgeClass = "badge-blue";

    resultDiv.innerHTML = `
      <span class="badge ${badgeClass}">
        ${data.category} (${(data.confidence * 100).toFixed(1)}%)
      </span>
    `;
  } catch (err) {
    console.error(err);
    resultDiv.innerHTML = "<span class='error'>❌ Network error</span>";
  }
}
